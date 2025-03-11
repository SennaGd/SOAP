import tkinter as tk
from customtkinter import *
import win32gui
import win32con

# Window dimensions
Width = 500
Height = 800

# Create the main window
root = CTk()
root.geometry(f'{Width}x{Height}')
root.resizable(False, False)

# Remove the default title bar (frameless window)
root.overrideredirect(True)

# Set window icon (this will show in the taskbar)
root.iconbitmap("icon.ico")  # Replace with the path to your own .ico file

# Make the window always stay on top
root.attributes("-topmost", True)

# Custom title bar (this is a frameless window)
title_bar = CTkFrame(root, width=Width, height=40, fg_color="#34495e", corner_radius=10)
title_bar.place(x=0, y=0)

# Add a label to the window
label = CTkLabel(root, text="This is a frameless window", font=("Helvetica", 14, "bold"), text_color="white")
label.place(x=100, y=100)

# Button to close the application
close_button = CTkButton(title_bar, text="X", width=40, height=30, command=root.quit,
                         fg_color="#E74C3C", hover_color="#C0392B", corner_radius=15, border_width=0, text_color="white")
close_button.place(x=Width - 50, y=5)

# Custom minimize functionality
def minimize():
    root.withdraw()  # Hide the window (similar to minimizing)

minimize_button = CTkButton(title_bar, text="-", width=40, height=30, command=minimize,
                            fg_color="#F39C12", hover_color="#E67E22", corner_radius=15, border_width=0, text_color="white")
minimize_button.place(x=Width - 100, y=5)

# Function to drag the window around
def on_press(event):
    global x, y
    x = event.x
    y = event.y

def on_drag(event):
    dx = event.x - x
    dy = event.y
    root.geometry(f'+{root.winfo_x() + dx}+{root.winfo_y() + dy}')

# Bind mouse events for the title bar to make the window draggable
title_bar.bind("<Button-1>", on_press)
title_bar.bind("<B1-Motion>", on_drag)

# Background frame behind everything
background_frame = CTkFrame(root, width=Width, height=Height, fg_color="#3498db")
background_frame.place(x=0, y=40)

# Function to ensure the window shows up in the taskbar (Windows)
def set_taskbar():
    hwnd = win32gui.GetForegroundWindow()  # Get the window handle of the application
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)  # Ensure the window is shown
    win32gui.SetForegroundWindow(hwnd)  # Bring the window to the foreground
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)  # Ensure it stays on top

# Call the function to make sure the window is visible in the taskbar
root.after(100, set_taskbar)  # Call this after the window has been created

# Show the window again if hidden (simulate "restore" functionality)
def restore_window():
    root.deiconify()  # Restore the window when needed

# Main loop to run the application
root.mainloop()
