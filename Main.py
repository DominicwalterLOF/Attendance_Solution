from tkinter import *
def Main(i):
    a = set()
    l = []
    #Nameset contains the name of the potential participants
    Nameset = {'Sample Person 1','Sample Person 2'}
    i = i.split("<span class=\"ZjFb7c\">")
    for j in i:
        j = j.split("</span>")[0]
        if not "<div" in j:
            a.add(j)

    for k in Nameset.difference(a) :
        l.append(k)
    return l
master = Tk()
master.geometry("260x400")
master.maxsize(260,400)
master.minsize(260,400)
p1 = PhotoImage(file='logo2.png')
master.iconphoto(False, p1)
background_image=PhotoImage(file='logo.png')
background_label = Label(master, image=background_image)
background_label.place(x=-600, y=-4, relwidth=5, relheight=1.5)
master.title("LOF Labs")
Label(master,text="Attendance Solution - AUTCS23").grid(row=0,column=1)
Label(master, text='').grid(row=1)
Label(master, text='Paste Here',).grid(row=2,column=1)
#Label(master, text='').grid(row=3)
Label(master, text='').grid(row=4)
Label(master, text='').grid(row=4)
Label(master, text='').grid(row=6)
Label(master, text='').grid(row=5)
Label(master, text='Absentees').grid(row=8, column=1)
e1 = Entry(master)
e2 = Text(master, width=30, height=2 ,relief=SUNKEN)
e3 = Text(master, width=30, height=10 , relief=SUNKEN, fg='red')
e2.grid(row=3, column=1)
e3.grid(row=9, column=1)
def submit():
    a = Main(e2.get("1.0",END))
    e2.delete(1.0,'end')
    for i in a:
        e3.insert(END,i + "\n")


sub_btn=Button(master,text = 'Fetch', command = submit)
sub_btn.grid(row=5,column=1)
x = e1.get()
print(x)
mainloop()