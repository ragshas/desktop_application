from tkinter import *
import backend

window = Tk()

ltitle=Label(window, text="Title")
ltitle.grid(row=0,column=0)

lauthor=Label(window, text="Author")
lauthor.grid(row=0, column=2)

lyear=Label(window,text="Year")
lyear.grid(row=1, column=0)

lisbn= Label(window, text="ISBN")
lisbn.grid(row=1,column=2)

title_value=StringVar()
e_title=Entry(window, textvariable=title_value)
e_title.grid(row=0,column=1)

author_value=StringVar()
e_author=Entry(window, textvariable=author_value)
e_author.grid(row=0,column=3)

year_value=StringVar()
e_year=Entry(window, textvariable=year_value)
e_year.grid(row=1,column=1)

isbn_value=StringVar()
e_isbn=Entry(window, textvariable=isbn_value)
e_isbn.grid(row=1,column=3)

listbox1=Listbox(window, height=6, width=35)
listbox1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

listbox1.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox1.yview)

b1=Button(window,text="View all", width=12)
b1.grid(row=2, column=3)

b1=Button(window,text="Search entry", width=12)
b1.grid(row=3, column=3)

b1=Button(window,text="Add entry", width=12)
b1.grid(row=4, column=3)

b1=Button(window,text="Update", width=12)
b1.grid(row=5, column=3)

b1=Button(window,text="Delete", width=12)
b1.grid(row=6, column=3)

b1=Button(window,text="Close", width=12)
b1.grid(row=7, column=3)


window.mainloop()
