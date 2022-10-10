from cProfile import label
import string
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from matplotlib.pyplot import text

frm = Tk()           
fnt = 'None 20 bold' 
bg = '#AFEEEE'       
bgtxt = '#ffffff'    
fgtxt = '#000000'    
fg = '#191970'       
fw = 900             
fh = 700  

x = ( frm.winfo_screenwidth() - fw ) / 2
y = ( frm.winfo_screenheight() - fh) / 2 - 50

pad = 10
frm.geometry( '%dx%d+%d+%d' % ( fw, fh, x, y ))  
frm.title('Student File Data')
frm.config(bg=bg)

Label  ( frm, text='Student Data', bg='navy', fg='lightblue', font=fnt ).pack(pady=pad) 
frame = Frame(frm, bg=bg)
frame.pack(pady=pad)
Label( frame, text='ID', bg=bg, fg=fg, font=fnt ).grid(row=0, column=0)
Label( frame, text='Firstname', bg=bg, fg=fg, font=fnt ).grid(row=1, column=0)
Label( frame, text='Lastname', bg=bg, fg=fg, font=fnt ).grid(row=2, column=0)
Label( frame, text='Phone', bg=bg, fg=fg, font=fnt ).grid(row=3, column=0)
Label( frame, text='Address', bg=bg, fg=fg, font=fnt ).grid(row=4, column=0)
Label( frame, text='Email', bg=bg, fg=fg, font=fnt ).grid(row=5, column=0)
Label( frame, text='Grade', bg=bg, fg=fg, font=fnt ).grid(row=6, column=0)

svid = StringVar()
svfname = StringVar()
svlname = StringVar()
svphone = StringVar()
svaddress = StringVar()
svemail = StringVar()
svgrade = StringVar()
txtid      = Entry( frame, bg=bgtxt,fg=fgtxt, font=fnt, textvariable=svid )
txtfname   = Entry( frame, bg=bgtxt, fg=fgtxt, font=fnt, textvariable=svfname )
txtlname   = Entry( frame, bg=bgtxt, fg=fgtxt, font=fnt, textvariable=svlname )
txtphone   = Entry( frame, bg=bgtxt, fg=fgtxt, font=fnt, textvariable=svphone )
txtaddress = Entry( frame, bg=bgtxt, fg=fgtxt, font=fnt, textvariable=svaddress )
txtemail   = Entry( frame, bg=bgtxt, fg=fgtxt, font=fnt, textvariable=svemail )
txtgrade   = Entry( frame, bg=bgtxt, fg=fgtxt, font=fnt, textvariable=svgrade )

txtid.grid( row=0, column=1, pady=pad )
txtfname.grid( row=1, column=1, pady=pad )
txtlname.grid( row=2, column=1, pady=pad )
txtphone.grid( row=3, column=1, pady=pad )
txtaddress.grid( row=4, column=1, pady=pad )
txtemail.grid( row=5, column=1, pady=pad )
txtgrade.grid( row=6, column=1, pady=pad )

def create():
    if svid.get().strip()=='':
        messagebox.showinfo('', 'ID field is empty..')
        txtid.focus()
    elif svfname.get().strip()=='':
        messagebox.showinfo('','Firstname field is empty..') 
        txtfname.focus()
    elif svlname.get().strip()=='':
        messagebox.showinfo('','Lastname field is empty..') 
        txtlname.focus()
    elif svphone.get().strip()=='':
        messagebox.showinfo('','Phone field is empty..') 
        txtphone.focus()
    elif svaddress.get().strip()=='':
        messagebox.showinfo('','Address field is empty..') 
        txtaddress.focus()   
    elif svemail.get().strip()=='':
        messagebox.showinfo('','Email field is emty..') 
        txtemail.focus()
    elif svgrade.get().strip()=='':
        messagebox.showinfo('','Grade field is emty..') 
        txtgrade.focus()   
    else: 
        filename = svid.get() + '_' + svfname.get() + '.txt'
        f = open(filename, 'w+')
        f.write('Student ID       :' + svid.get() + '\n')
        f.write('Student Firstname:' + svfname.get() + '\n')
        f.write('Student Lastname :' + svlname.get()  +'\n') 
        f.write('Student Phone    :' + svphone.get() + '\n') 
        f.write('Student Address  :' + svaddress.get() + '\n')
        f.write('Student Email    :' + svemail.get() + '\n')
        f.write('Student Grade    :' + svgrade.get() + '\n')  
        f.close() 
        svid.set('')
        svfname.set('')
        svlname.set('')
        svphone.set('')
        svaddress.set('')
        svemail.set('')
        svgrade.set('')
        messagebox.showinfo('','Done')
        txtid.focus()

ttk.Button( frm, text='Create new student file', command=create ).pack(pady=pad)
ttk.Button( frm, text='Exit', command=frm.destroy ).pack(pady=pad)

ButtonStyle = ttk.Style()
ButtonStyle.configure('TButton', font=fnt, pady=pad, padding=pad)

frm.mainloop() 