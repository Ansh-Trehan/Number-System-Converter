from tkinter import *

def convert():
    try:
        s1=system1.get()
        s2=system2.get()
        dec=int(n.get(), s1)
        num1=n.get()
        num2=IntVar()
        st=StringVar()
        if(s2==2):
            num2=bin(dec).replace("0b","")
            st="Binary"
        elif(s2==8):
            num2=oct(dec).replace("0o","")
            st="Octal"
        elif(s2==10):
            num2=dec
            st="Decimal"
        elif(s2==16):
            num2=hex(dec).replace("0x","")
            st="Hexadecimal"
        out.config(text = "After converting " + str(num1) + " to " + str(st) + " is " + str(num2))
        explain.config(state=NORMAL)
    except:
        error

def explaination():
    try:
        ex=Toplevel()
        s1=system1.get()
        s2=system2.get()
        if(not s1==10):
            Label(ex, text="Convert Number to Decimal", font=("Helvetica",14,"bold")).grid(row=0, column=0)
            numb=str(n.get())
            i=len(numb)
            j=1
            s=s1
            select=""
            while (not i==0):
                select=numb[i-1]+ " * " + str(s) + "^" + str(j)+"\t"+select
                i-=1
                j+=1
            select+=" = "+str(int(n.get(),s1))
            Label(ex, text=select, font=("Helvetica",14,"italic")).grid(row=1, column=1)
        dec=int(n.get(),s1)
        if(not s2==10):
            Label(ex, text="Convert Number from Decimal to your system", font=("Helvetica",14,"bold")).grid(row=2, column=0)
            Label(ex, text="\t Step \t Operation \t Remainder", font=("Helvetica",14,"bold italic")).grid(row=3, column=1)
            i=1
            while(1==1):
                r=3+i
                select=str(i)+"\t"+str(int(dec))+"/"+str(s2)+"="+str(int(dec/s2))+"\t\t"+str(int(dec%s2))
                Label(ex, text=select, font=("Helvetica",14,"italic")).grid(row=r, column=1)
                dec=dec/s2
                i+=1
                if(dec<1):
                    break
            num=int(n.get(), s1)
            if(s2==2):
                num=bin(num).replace("0b","")
            elif(s2==8):
                num=oct(num).replace("0o","")
            elif(s2==10):
                num=num
            elif(s2==16):
                num=hex(num).replace("0x","")
            Label(ex, text="Getting last Quotient and Remainders from bottom to top, number = "+str(num), font=("Helvetica",14,"italic")).grid(row=r, column=1)
        ex.mainloop()
    except:
        error

def error():
    messagebox.showerror("ERROR", "Invalid Input")

win=Tk()
win.title("Number System Converter")
win.iconbitmap('26287.ico')
menu = Menu(win)
developed_by = Menu(menu, tearoff=0)
developed_by.add_command(label="Developed By")
developed_by.add_separator()
developed_by.add_command(label="Ansh Trehan")
developed_by.add_command(label="Ayush Singh")
developed_by.add_command(label="Ritanjay Rana")
menu.add_cascade(label='About Us',menu=developed_by)
win.config(menu=menu)
Label(win, text="Number System Converter",fg="red", font=("Helvetica",16,"bold italic"), justify=CENTER, relief=RAISED, anchor=CENTER).grid()
frame1 = Frame(win)
frame1.grid()
Label(frame1, text="Enter Number", font=("Helvetica",12,"italic")).grid(row=1, column=1)

n=StringVar()
Entry(frame1, textvariable=n, font=("Helvetica",12,"italic"), bd=5).grid(row=1, column=2)

frame2 = Frame(win)
frame2.grid()

system1 = IntVar()
system2 = IntVar()
syst1=IntVar()
syst2=IntVar()
Label(frame2, text="Select number system of entered number", font=("Helvetica",12,"bold")).grid(row=1, column=0)
Radiobutton(frame2, text="Binary", variable=system1, indicatoron=0, value=2, font=("Helvetica",12,"italic")).grid(row=2, column=0)
Radiobutton(frame2, text="Octal", variable=system1, indicatoron=0, value=8, font=("Helvetica",12,"italic")).grid(row=3, column=0)
Radiobutton(frame2, text="Decimal", variable=system1, indicatoron=0, value=10, font=("Helvetica",12,"italic")).grid(row=4, column=0)
Radiobutton(frame2, text="Hexadecimal", variable=system1, indicatoron=0, value=16, font=("Helvetica",12,"italic")).grid(row=5, column=0)

Label(frame2, text="Number to be converted in", font=("Helvetica",12,"bold"), padx=50).grid(row=1, column=3)
Radiobutton(frame2, text="Binary", variable=system2, indicatoron=0, value=2, font=("Helvetica",12,"italic")).grid(row=2, column=3)
Radiobutton(frame2, text="Octal", variable=system2, indicatoron=0, value=8, font=("Helvetica",12,"italic")).grid(row=3, column=3)
Radiobutton(frame2, text="Decimal", variable=system2, indicatoron=0, value=10, font=("Helvetica",12,"italic")).grid(row=4, column=3)
Radiobutton(frame2, text="Hexadecimal", variable=system2, indicatoron=0, value=16, font=("Helvetica",12,"italic")).grid(row=5, column=3)

Button(frame2, text="Convert", bd=5, pady=5, command= convert, font=("Helvetica",12,"bold"), justify=CENTER).grid(row=8, column=2)
frame3 = Frame(win)
frame3.grid()
out=Label(frame3, font=("Helvetica",12,"italic"))
out.grid(row=1, column=0)
explain=Button(frame3, text="Explanation", command=explaination, font=("Helvetica",12,"bold"), state=DISABLED, bd=5, justify=CENTER)
explain.grid(row=5,column=0)

win.mainloop()

