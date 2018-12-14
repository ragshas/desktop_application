from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=listbox1.curselection()[0]
        selected_tuple=listbox1.get(index)
        e_title.delete(0,END)
        e_title.insert(END,selected_tuple[1])
        e_author.delete(0,END)
        e_author.insert(END,selected_tuple[2])
        e_year.delete(0,END)
        e_year.insert(END,selected_tuple[3])
        e_isbn.delete(0,END)
        e_isbn.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    listbox1.delete(0,END)
    for row in backend.view():
        listbox1.insert(END,row)

def search_command():
    listbox1.delete(0,END)
    for row in backend.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()):
        listbox1.insert(END,row)

def add_command():
    backend.insert(title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
    listbox1.delete(0,END)
    listbox1.insert(END,(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_value.get(),author_value.get(),year_value.get(),isbn_value.get())

window = Tk()
window.wm_title("Book Store")

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

listbox1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window,text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b1=Button(window,text="Search entry", width=12, command=search_command)
b1.grid(row=3, column=3)

b1=Button(window,text="Add entry", width=12, command=add_command)
b1.grid(row=4, column=3)

b1=Button(window,text="Update", width=12, command=update_command)
b1.grid(row=5, column=3)

b1=Button(window,text="Delete", width=12, command=delete_command)
b1.grid(row=6, column=3)

b1=Button(window,text="Close", width=12, command=window.destroy)
b1.grid(row=7, column=3)


window.mainloop()
