from 
root=Tk()
root.("my calculator")
#label=label(root,font=("ariel",16),text="entry your name,bg="pink",fg="blue")
#label.pack()
root.geomentry("361*381+500-20")
VAL=""
data=StringVar()
display= Entry(root,textvariable=data,bd=29,justify="right",bg="powder blue",font=("ariel",20))
display.grid(row=0,column=2)
btn7=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6)
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("ariel",12,"bold"),bd=12,height=2,width=6)
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("ariel",12,"bold"),bd=12,height=2,width=6)
btn9.grid(row=1,column=2)
btn_add=Button(root,text="+",font=("ariel",12,"bold"),bd=12,height=2,width=6)
btn_add.grid(row=1,column=3)
root.mainloop()
# #rooot.resizable(0,0)
# btn4=Button(root,text="4",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(4))
# btn4.grid(row=2,column=0)
# btn5=Button(root,text="5",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(5))           
# btn5.grid(row=2,column=1)
# btn6=Button(root,text="6",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(6))
# btn6.grid(row=2,column=2)
# btn_sub=Button(root,text="-",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick("-"))
# btn_sub.grid(row=2,column=3)


# btn1=Button(root,text="1",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(1))                       
# btn6.grid(row=3,column=0)
# btn2=Button(root,text="2",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(2))
# btn2.grid(row=3,column=1)
# btn3=Button(root,text="3",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(3))
# btn3.grid(row=3,column=2)
# btn_mul=Button(root,text="*",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick("*"))
# btn_mul.grid(row=3,column=3)


# btnc=Button(root,text="c",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick("c"))    
# btnc.grid(row=4,column=0)
# btn0=Button(root,text="0",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick("0"))
# btn0.grid(row=4,column=1)
# btn_div=Button(root,text="/",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick("/"))
# btn_div.grid(row=4,column=2)
# btn_equal=Button(root,text="=",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick("="))
# btn_equal.grid(row=4,column=3)
# root.mainloop()





