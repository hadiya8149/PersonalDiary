
from tkinter import *
from datetime import date
date = date.today()


def unlock_app():
    usrname = username.get()
    passcode = password.get()
    if  (usrname == 'hadiya' ) and (passcode== 'abcd')  :
        root.destroy()
        import homepage
    else:
        print(usrname)
        print(passcode)
        username.delete('0', 'end')
        password.delete('0', 'end')
    
    
root = Tk()
root.title('Personal Diary -login page')
root.geometry('200x200')
log_page = Canvas(root)
log_page['bg'] = 'light blue'
log_page.pack(side=LEFT, fill=BOTH, expand=True)

log_page.config(log_page, height=500, width=500, bd=0)

Label(log_page,height = 3, text="Username", background='light blue', foreground='black').grid(row=0, column=0)

username = Entry(log_page, width = 10)
username.grid(row=0, column =1)
Label(log_page, height=3, text="Password", background ='light blue', foreground='black').grid(row=1, column=0)
password = Entry(log_page, width=10, show='*')
password.grid(row=1, column=1)

login = Button(log_page, text="Login", command=unlock_app)
login.grid(row=2, column=0)

log_page.mainloop()

