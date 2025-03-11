from Constants import * 
from customtkinter import *
from Functions import *
from Tweaks import *
import win32gui
import win32con

root = CTk()
root.geometry(f'{Width}x{Height}')
root.resizable(False, False)
root.overrideredirect(True)
root.attributes("-topmost", 1)



top_bar = CTkFrame(root, width=Width, height=50, fg_color=background_color, corner_radius=5)
top_bar.place(x=0, y=0)


title_label = CTkLabel(top_bar, text="SOAP V5.23 | SOAP TWEAKS", font=("Slikscreen", 14, "bold"), text_color="white")
title_label.place(x=10, y=1)

quit_button = CTkButton(top_bar, text=" ", width=20, height=12, command=root.quit,
                        fg_color=quit_button_color, hover_color=quit_button_hover_color, 
                        corner_radius=15)
quit_button.place(x=Width - 25, y=5)


def on_press(event):
    global x, y
    x = event.x
    y = event.y

def on_drag(event):
    dx = event.x - x
    dy = event.y - y
    root.geometry(f'+{root.winfo_x() + dx}+{root.winfo_y() + dy}')

top_bar.bind("<Button-1>", on_press)
top_bar.bind("<B1-Motion>", on_drag)

title_label.bind("<Button-1>", on_press)
title_label.bind("<B1-Motion>", on_drag)

scroll_frame = CTkScrollableFrame(root,Width*0.97,Height)
scroll_frame.place(x=0,y=30)
scroll_frame.configure(fg_color=background_color,
                       corner_radius=0,
                       scrollbar_button_color=scrollbar_color,
                       scrollbar_button_hover_color=scrollbar_color_hover,)


class tweak_panel:
    def __init__(self,title,description,filepath_apply,filepath_revert,filetype_apply,filetype_revert):
        self.is_enabled = False
        self.EnableDisable = 'Apply'  

        Tweak_frame = CTkFrame(scroll_frame,Width-50,200,fg_color=tweak_frame_color,corner_radius=tweak_frame_radius)
        Tweak_frame.pack(pady=10)
        
        Title = CTkLabel(Tweak_frame,text=f"{title}",font=("Slikscreen", title_size, "bold"))
        Title.place(x=20,y=20)
        
        Description = CTkLabel(Tweak_frame,text=f"{description}",font=("Helvetica", description_size, "italic"))
        Description.configure(Tweak_frame,
                                text=f"{description}",
                                font=("Helvetica", description_size, "italic"),
                                anchor="w",
                                wraplength=Width - 200)
        Description.place(x=25,y=70)
        
        Tweak_button = CTkButton(Tweak_frame,Width*0.2,50,
                                 fg_color=tweak_button_color,
                                 hover_color=tweak_button_hovor_color,
                                 text=self.EnableDisable,
                                 corner_radius=corner_rad_btn
                                 )
        
        Tweak_button.place(x=Width-160,y=10)
        
        Tweak_button.configure(command=lambda:switch_enabled(Tweak_button,
                                                             self,
                                                             filetype_apply,
                                                             filetype_revert,
                                                             filepath_apply,
                                                             filepath_revert))

# loop to get all tweaks
i = 0
for tweak in tweaks:
    tweak_panel(
        tweak['title'],
        tweak['description'],
        tweak['filepath_apply'],
        tweak['filepath_revert'],
        tweak['filetype_apply'],
        tweak['filetype_revert'],
    )
    i += 1
    
# print(f"Amount of tweaks:{i}")
bottom_border = CTkFrame(root,width=Width,height=30,fg_color=background_color,corner_radius=0)
bottom_border.place(y=Height-20)
root.mainloop()
