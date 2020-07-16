from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import font, colorchooser, messagebox, filedialog
from tkinter import Menu
from tkinter import Menubutton
import os
import cv2
import random
import sys
 


front_page = tkinter.Tk()
front_page.title("Om Nama Sivay")
front_page.geometry("345x582")
front_page.resizable(0,0)

search_img = tkinter.PhotoImage(file = "img/src.png")
dot_img = tkinter.PhotoImage(file = "img/dot.png")
cam_img = tkinter.PhotoImage(file = "img/camera.png")
sts_img = tkinter.PhotoImage(file = "img/sts.png")
usr_1 = tkinter.PhotoImage(file = "img/user3.png")
save_img = tkinter.PhotoImage(file = "img/save.png")

def search():
    find = tkinter.Toplevel()
    find.title("Find")
    find.geometry("330x150")
    find.resizable(0,0)

    find_frame = tkinter.LabelFrame(find, text = "Search")
    find_frame.pack(pady = 20)

    text_find_lbl = ttk.Label(find_frame, text = "Find :")
    find_input = ttk.Entry(find_frame, width = 30)
    find_btn = ttk.Button(find_frame, text = "Find")

    text_find_lbl.grid(row = 0, column = 0, padx = 4, pady = 4 )
    find_input.grid(row = 0, column = 1, padx = 4, pady = 4)
    find_btn.grid(row = 1, column = 2, padx = 4, pady = 4)


def show():
	list1 = ["red","yellow","blue","orange"]
	list2 = ["helvetica","time","courier","verdana","georgia","palatino","bookman"]
	whatsApp_text_on_upper_frame.config(background = random.choice(list1), font = (random.choice(list2)))
	whatsApp_text_on_upper_frame.after(400,show)

def theme():
    top = tkinter.Tk()
    top.title("Color Theme")
    top.geometry("200x200")
    top.resizable(0,0)

    colors_menu = tkinter.Menu(top)

    red_clr = tkinter.PhotoImage(file = "img/red.png")
    light_plus_clr = tkinter.PhotoImage(file = "img/light_plus.png")
    night_clr = tkinter.PhotoImage(file = "img/night_blue.png")
    dark_clr = tkinter.PhotoImage(file = "img/dark.png")
    monokai_clr = tkinter.PhotoImage(file = "img/monokai.png")
    
    color_theme = tkinter.Menu(colors_menu, tearoff = False)
    
    theme_choice = tkinter.StringVar()
    colors_icons = (red_clr, light_plus_clr, night_clr, dark_clr, monokai_clr)
    top.config(menu=colors_menu)
 
    color_dict = {
        'Light Defaul' : ("#000000","#ffffff"),
        "Light Plus" : ("#474747","#e0e0e0"),
        "Dark" : ("#c4c4c4", "#2d2d2d"),
        "Red" : ("#2d2d2d","#ffe8e8"),
        "Monokai" : ("#d3b774", "#474747"),
        "Night Blue" : ("#ededed","#6b9dc2")
        }
    colors_menu.add_cascade(label = "Color Them", menu = color_theme)

    def change_theme():
        chose_theme = theme_choice.get()
        colour_tuple = color_dict.get(chose_theme)
        fg_color, bg_color = colour_tuple[0], colour_tuple[1]
        front_page.config(bg = bg_color, fg = fg_color)
    count = 0
    for i in color_dict:
        color_theme.add_radiobutton(label = i, image = colors_icons[count], variable = theme_choice, compound = LEFT, command = change_theme)
        count = count+1
    top.mainloop() 

def save_file():
    url = ""
    url = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = "Save File", filetypes = (("Text File","*.txt"),("All files","*.*")))
    try:
        with open (url,"r") as fr:
            text_editor.delete(1.0, tkinter.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return

def open_camera():
    vid = cv2.VideoCapture(0)

    while(True):
        ret, frame = vid.read()
        cv2.imshow("frmae",frame)
        if cv2.waitkey(1) & 0xFF == ord("q"):
            break
    vid.release()
    cv2.destroyWindow()

upper_frame =tkinter.Label(front_page)
upper_frame.pack(side = TOP,fill = X)

whatsApp_text_on_upper_frame = Button(upper_frame,text = "Lets Chat", border= 3,font = (18),relief = FLAT, command = show)
whatsApp_text_on_upper_frame.pack(side = LEFT, pady =1)

dot_btn = Button(upper_frame, image = dot_img,relief = FLAT,border = 0,bg = "black", command = theme)
dot_btn.pack(side = RIGHT, fill = X, pady = 1)


search_btn = Button(upper_frame, image = search_img, relief = FLAT, border = 0,bg = "black", command = search)
search_btn.pack(side = RIGHT, padx = 8, pady = 1)

cam_btn = Button(front_page, image = cam_img, relief = FLAT, border = 0, bg = "Black", command = open_camera )
cam_btn.place(x=5,y= 55)

cht_btn = Button(front_page,text = "Chats", relief = FLAT, border = 0, font = ("Times",17))
cht_btn.place(x = 44, y = 62)

status_btn = Button(front_page, text = "Status", relief = FLAT, border = 0, font = ("Times",17))
status_btn.place(x = 140, y = 62)

sts_lbl = Label(image= sts_img )
sts_lbl.place(x = 208, y= 75)

calls_btn = Button(front_page, text = "Calls", relief = FLAT, border = 0, font = ("Times",17))
calls_btn.place(x = 265, y = 62)

fst_line = Label(front_page, text = "------------------------------------------------------------------")
fst_line.place(x = 0, y = 90)

usr1_lbl = Button(front_page, image = usr_1, relief = FLAT, border = 0)
usr1_lbl.place(x =5, y = 110)

user1_name = Label(front_page, text = "User 1 Name", font = ("Bahnschrift",15))
user1_name.place(x = 90, y=130)

user2_lbl = Button(front_page, image = usr_1, relief = FLAT, border = 0)
user2_lbl.place(x = 5, y = 180 )

user2_name = Label(front_page, text = "User 2 Name", font = ("Bahnschrift",15))
user2_name.place(x = 90, y=200)

user3_lbl = Button(front_page, image = usr_1, relief = FLAT, border = 0)
user3_lbl.place(x = 5, y = 250 )

user3_name = Label(front_page, text = "User 3 Name", font = ("Bahnschrift",15))
user3_name.place(x = 90, y=270)

text_notePad = Label(front_page,text = "Use Note Pad For write Somthing", justify = "center",fg = "yellow", bg = "black" ,font = ("Consolas",14))
text_notePad.place(x = 14,y = 330)

text_editor = tkinter.Text(front_page)
text_editor.config(wrap = "word", relief = tkinter.FLAT)
text_editor.focus_set()
text_editor.place(x  = 5, y= 365)

save_btn = Button(front_page,image = save_img, command = save_file)
save_btn.place(x = 295, y = 370)


front_page.mainloop()