import json
import re

from PySide6.QtWidgets import QApplication, QComboBox, QFrame, QLabel, QLineEdit, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.i = 0
		self.filepath: None | str = None
		self.applyFilepath = None
		self.revertFilepath = None 
		self.setWindowTitle("Tweak Config")

		menubar = self.menuBar()

		tweaksMenu = menubar.addMenu("Settings")
		tweakViewAction = menubar.addAction("Show Tweaks")
		addTweakActionMenu = menubar.addAction("Add Tweak")
		openJsonAction = tweaksMenu.addAction("Open File")	
		addTweakAction= tweaksMenu.addAction("Add Tweak")	

		openJsonAction.triggered.connect(self.parseFile)
		addTweakAction.triggered.connect(self.showAddPage)	
		tweakViewAction.triggered.connect(self.parseFile)	
		addTweakActionMenu.triggered.connect(self.showAddPage)
		pageContents= QWidget()
		self.setCentralWidget(pageContents)

		self.pageLayout = QVBoxLayout()
		self.pageLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
		self.pageLayout
		pageContents.setLayout(self.pageLayout)
		label = QLabel("hi")
		self.pageLayout.addWidget(label)
		pageContents.setStyleSheet("background-color: hsl(0,0%, 30%); color: white;")

		self.show()
		

	def openFile(self) -> None:
		"""
		Assigns self.filepath whenever a '.json' file is selected.
		"""

		openedFile: tuple[str, str] = QFileDialog.getOpenFileName(self)
		self.filepath = openedFile[0]
		print(self.filepath)

		if not "json" in self.filepath[len(self.filepath)-4: len(self.filepath)]:
			self.filepath = None
		else:
			self.parseFile()
		return None

	def parseFile(self) -> None:
		"""
		Reads the assigned '.json' file,
		Generates frames containing all tweaks currently inside the file.
		"""
		self.clearLayout()
		# Return instantly whenever filepath not defined
		while self.filepath == None:
			self.openFile()
			return None

		with open(self.filepath, "r") as f:
			self.file = json.load(f)
		print(self.file)
		self.i=0
		for key in self.file:
			self.i+=1
			self.key = key
			tweakName = key 
			tweakCategory = self.file[key]['category']

			tweakFrame = QWidget()
			tweakLayout = QVBoxLayout()
			tweakFrame.setStyleSheet("background-color:hsl(0,0%,50%); color:white;")
			
			tweakNameLabel = QLabel("Title: "+ str(tweakName))
			tweakCategoryLabel = QLabel("Category: "+ str(tweakCategory))

			tweakDeleteButton = QPushButton("del")
			tweakDeleteButton.clicked.connect(lambda checked, k=str(key), f=tweakFrame: self.deleteTweak(k, f,))

			tweakLayout.addWidget(tweakNameLabel)
			tweakLayout.addWidget(tweakCategoryLabel)
			tweakLayout.addWidget(tweakDeleteButton)

			tweakFrame.setLayout(tweakLayout)
			self.pageLayout.addWidget(tweakFrame)
		

	def deleteTweak(self, key, frame: QWidget) -> None:
		if self.filepath == None:
			return None 

		self.pageLayout.removeWidget(frame)
		frame.deleteLater()

		self.file.pop(key, None)
		
		# TODO: REMOVE THESE COMMENTS WHEN ALL IS DONE | THIS DELETES THE TWEAKS 
		formattedJson= json.dumps(self.file, indent=4)
		with open(self.filepath, "w") as f:
			f.write(formattedJson)

	
	def showAddPage(self) -> None:
		self.clearLayout()
		self.title= QLabel()
		titleForm = QLineEdit("title")
		titleForm.textChanged.connect(self.title.setText)
		
		self.description = QLabel()
		descriptionForm = QLineEdit("description")
		descriptionForm.textChanged.connect(self.description.setText)

		self.category = QLabel()
		categoryForm = QComboBox()
		categoryForm.addItems(["input", "cpu", "gpu", "kernel", "network", "audio"])
		categoryForm.currentTextChanged.connect(self.category.setText)
		
		applyFileButton = QPushButton("Select: Apply File")
		applyFileButton.clicked.connect(self.applyFile)

		revertFileButton = QPushButton("Select: Revert File")
		revertFileButton.clicked.connect(self.revertFile)

		submitButton = QPushButton("Add")
		submitButton.clicked.connect(self.readForm)

		self.pageLayout.addWidget(titleForm)
		self.pageLayout.addWidget(descriptionForm)
		self.pageLayout.addWidget(categoryForm)

		self.pageLayout.addWidget(applyFileButton)
		self.pageLayout.addWidget(revertFileButton)

		self.pageLayout.addWidget(submitButton)
	
	
	def readForm(self) :
		print("Title: ",self.title.text())
		print("Category: ",self.category.text())
		print("Apply Path: ",self.applyFilepath)
		print("Revert Path: ",self.revertFilepath)  

		if self.applyFilepath == None or self.revertFilepath == None:
			return None

		# here starts tweak parsing | reading ".red" or ".bat" file
		applyContents = self.get_file_contents(self.applyFilepath)
		revertContents = self.get_file_contents(self.revertFilepath)
		
		applyTweak = self.parse_tweak_contents(self.applyFilepath, applyContents)
		revertTweak = self.parse_tweak_contents(self.revertFilepath, revertContents)

		tweakSet = {self.title.text(): {"category": self.category.text(),"apply": applyTweak, "revert": revertTweak}}	
		tweakSet = json.dumps(tweakSet, indent=4)		
		
		if self.filepath is not None:
			with open(self.filepath, "r") as f:
				file = json.load(f)
			file[self.title.text()] = {"name":self.title.text(), "description":self.description.text(), "category": self.category.text(), "toggled":0,"apply": applyTweak, "revert": revertTweak}
			print(file)
			formatted = json.dumps(file, indent=4)

			with open(self.filepath, "w") as f:
				f.write(formatted)

		
	def applyFile(self) -> None:
		filepath = QFileDialog.getOpenFileName(self)
		self.applyFilepath = filepath[0]

	def revertFile(self) -> None:
		filepath = QFileDialog.getOpenFileName(self)
		self.revertFilepath = filepath[0]

	def parse_tweak_contents(self,filepath: str, tweakContents):
		if ".reg" in filepath:
			print('reg')
			pattern = re.compile(
				r'\[(HKEY_[A-Z_]+)\\([^\]]+)\][\s\S]*?"([^"]+)"=(dword|hex|hex\(2\)):(\w+)',
				re.IGNORECASE
			)
			tweak = []
			regexSearch = re.search(pattern, tweakContents)
			if regexSearch:
				tweak.append({
					"function": "add",
					"hive": regexSearch.group(1),
					"path": regexSearch.group(2),
					"name": regexSearch.group(3),
					"value": regexSearch.group(5)
				})
			else:
				print("not found")
				
		else:
			pattern = re.compile(
				r'^reg(?:\.exe)?\s+'
				r'(add|delete)\s+'
				r'"(HKLM|HKCU|HKCR|HKU|HKCC|HKEY_LOCAL_MACHINE|HKEY_CURRENT_USER|HKEY_CLASSES_ROOT|HKEY_USERS|HKEY_CURRENT_CONFIG)\\([^"]+)"'
				r'(?:\s+/v\s+"?([^"\s]+)"?)?'
				r'(?:\s+/t\s+(REG_\w+))?'
				r'(?:\s+/d\s+(?:"([^"]+)"|([^\s/]+)))?'
				r'(?:\s+/f)?\s*$',
				re.IGNORECASE
			)
			tweak = []

			for line in tweakContents:
				regexSearch = re.match(pattern, line)

				if regexSearch:
					tweak.append({
						'function': regexSearch.group(1),
						'hive': regexSearch.group(2),
						'path': regexSearch.group(3),
						'name': regexSearch.group(4),
						'value': regexSearch.group(6) or regexSearch.group(7)
					})

		return tweak

	def get_file_contents(self, filepath: str):
		try:
			if '.reg' in filepath:
				try:
					with open(filepath, "r", encoding="utf-8") as file:
						return file.read()
				except UnicodeDecodeError:
					print("UTF-8 Failed")

				try:
					with open(filepath, "r", encoding="utf-16") as file:
						return file.read()
				except UnicodeDecodeError:
					print("UTF-16 Failed")

			elif '.bat' in filepath:
				with open(filepath, "r", encoding="utf-8") as file:
					return file.readlines()
		except AttributeError as e:
			raise e
	
	def clearLayout(self) -> None:
		self.pageLayout.removeWidget
		for i in reversed(range(self.pageLayout.count())):
			widget = self.pageLayout.itemAt(i)
			if widget and widget.widget() :
				widget.widget().deleteLater()
		

app = QApplication()

window = MainWindow()
window.show()
app.exec()
