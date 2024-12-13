from tkinter import *
win = Tk()
#============VAR
position = False
en1 = ""
en2 = ""
################Zaher BG
win.geometry("250x400")
win.resizable(0,0)
win.title("Calculator")
###############amaliat
def min(x):
    global position
    if x[-1] == " ":
        g = len(x)-3
    elif x[-1] == "|":
        g = len(x)-1
        position = True
    else:
        g = len(x)-1
    return x[0:g]
def power():
    global en1
    global en2
    lst = en1.split()
    c = 0
    g = []
    for i in lst:
        try:
            if i != "+"and i !="*"and i !="/"and i !="-" and i != "**":
                float(i)
        except:
            if float(str(eval(i[1:-1])))<0:
                g.append(str(float(str(eval(i[1:-1])))*-1))
            else : g.append(str(eval(i[1:-1])))
        else: g.append(i)
       
    en1 = ""
    en1 = str(eval("".join(g)))
    en2 = en1
    lbl_tv.config(text=en2)
def insert(x,y):
    global position
    global en1
    global en2
    if x == "C":
        en1 = f""
        en2 = f""
        position = False
        lbl_tv.config(text=en2)
        return
    if x == "OC":
        en1 = min(en1)
        en2 = min(en2)
        lbl_tv.config(text=en2)
        return
    if x == "|" and position == False:
        position = True
    elif x == "|" and position == True:
        position = False
        en1 += f"{x}"
        en2 += f"{y}"
        lbl_tv.config(text=en2)
        return
    if x in "/*-+**" and position == False:
        en1 += f" {x} "
        en2 += f" {y} "
        lbl_tv.config(text=en2)
    elif position == False:
        en1 += f"{x}"
        en2 += f"{y}"
        lbl_tv.config(text=en2)
    elif position == True:
        en1 += f"{x}"
        en2 += f"{y}"
        lbl_tv.config(text=en2)
 
##################Object BTN
btn_E = Button(text="=",width=8,height=1,bg = "green",command=power)
btn_E.place(x=40,y=220)
btn_Pluse = Button(text="+",width=3,height=3,bg = "green",command=lambda:insert("+","+"))
btn_Pluse.place(x=40,y=250)
btn_minus = Button(text="-",width=3,height=1,bg = "green",command=lambda:insert("-","-"))
btn_minus.place(x=75,y=250)
btn_X = Button(text="x",width=3,height=1,bg = "green",command=lambda:insert("*","x"))
btn_X.place(x=75,y=280)
btn_division = Button(text="÷",width=3,height=1,bg = "green",command=lambda:insert("/","÷"))
btn_division.place(x=40,y=310)
btn_power = Button(text="xY",width=3,height=1,bg = "green",command=lambda:insert("**","xY"))
btn_power.place(x=75,y=310)
btn_seven = Button(text="7",width=3,height=1,bg = "green",command=lambda:insert("7","7"))
btn_seven.place(x=110,y=250)
btn_eight = Button(text="8",width=3,height=1,bg = "green",command=lambda:insert("8","8"))
btn_eight.place(x=145,y=250)
btn_nine = Button(text="9",width=3,height=1,bg = "green",command=lambda:insert("9","9"))
btn_nine.place(x=180,y=250)
btn_four = Button(text="4",width=3,height=1,bg = "green",command=lambda:insert("4","4"))
btn_four.place(x=110,y=280)
btn_five = Button(text="5",width=3,height=1,bg = "green",command=lambda:insert("5","5"))
btn_five.place(x=145,y=280)
btn_six = Button(text="6",width=3,height=1,bg = "green",command=lambda:insert("6","6"))
btn_six.place(x=180,y=280)
btn_one = Button(text="1",width=3,height=1,bg = "green",command=lambda:insert("1","1"))
btn_one.place(x=110,y=310)
btn_two = Button(text="2",width=3,height=1,bg = "green",command=lambda:insert("2","2"))
btn_two.place(x=145,y=310)
btn_three = Button(text="3",width=3,height=1,bg = "green",command=lambda:insert("3","3"))
btn_three.place(x=180,y=310)
btn_dote = Button(text=".",width=3,height=1,bg = "green",command=lambda:insert(".","."))
btn_dote.place(x=110,y=340)
btn_zero = Button(text="0",width=3,height=1,bg = "green",command=lambda:insert("0","0"))
btn_zero.place(x=145,y=340)
btn_I = Button(text="|",width=3,height=1,bg = "green",command=lambda:insert("|","|"))
btn_I.place(x=180,y=340)
btn_Clear = Button(text="C",width=3,height=1,bg = "green",command=lambda:insert("C","C"))
btn_Clear.place(x=40,y=340)
btn_O_clear = Button(text="<-",width=3,height=1,bg = "green",command=lambda:insert("OC","OC"))
btn_O_clear.place(x=75,y=340)
###################Zaher FG
lbl_tv = Label(win,text="",font="arial 13 bold")
lbl_tv.place(x=40,y=55)

win.mainloop()