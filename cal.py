import tkinter
window=tkinter.tk()
window.titleka ('edure !')

top_frame=tkinter.frame(window).pack()
botton_frame=tkinter.frame(window).pack(side='botton')

btn1 = tkinter.Button(top_frame,text='Button 1',fg= "red").pack()=#'fg-foreground'is used to color the contents
btn2 = tkinter.Button(top_frame,text='Button 2',fg= "green").pack()=#'text'is used to write the text on the text on the Butyon
btn3 = tkinter.Button(top_frame,text='Button 3',fg="purple").pack(side= "left")
btn4 = tkinter.Button(top_frame,text='Button 4',fg="orange").pack(side="left")

import tkinter

window=tkinter.TK()
window.title("EDUREKA !")

# creating 2 text lables and input labels

tkinter.Label1(window,text = "username").grid(row=0)#this is placed in 0.0
