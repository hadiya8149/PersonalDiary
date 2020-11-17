
from tkinter import *
from datetime import date

root = Tk()
root.title('Personal Diary')
canvas = Canvas(root)
canvas.pack(side=LEFT, fill = BOTH,expand =True)
canvas['bg'] = 'light blue'
canvas.configure(canvas, bd=0, width=500, height=500)

Label(canvas, height=5, text='Hi sweetheart How was your day?', background='light blue', foreground='black').place(x=150, y=1)
yCordinate = 150

for i in range(0, 5): 
    Label(canvas, height =0, text='________________________________________________________', background='light blue', foreground = 'blue').place(x=50, y= yCordinate)
    yCordinate+=50


lbl_1 =  Entry(canvas, width = 65, bd=0, font="Saira 8 ", relief = "groove",highlightcolor = 'light blue', highlightbackground= 'light blue', background = 'light blue')
lbl_2 =  Entry(canvas, width = 65, bd=0, font="Saira 8 ", relief = "groove",highlightcolor = 'light blue', highlightbackground= 'light blue', background = 'light blue')
lbl_3 =  Entry(canvas, width = 65, bd=0, font="Saira 8 ", relief = "groove",highlightcolor = 'light blue', highlightbackground= 'light blue', background = 'light blue')
lbl_4 =  Entry(canvas, width = 65, bd=0, font="Saira 8 ", relief = "groove",highlightcolor = 'light blue', highlightbackground= 'light blue', background = 'light blue')
lbl_5 =  Entry(canvas, width = 65, bd=0, font="Saira 8 ", relief = "groove",highlightcolor = 'light blue', highlightbackground= 'light blue', background = 'light blue')
lbl_1.place(x=50, y=147)
lbl_2.place(x=50, y=197)
lbl_3.place(x=50, y=247)
lbl_4.place(x=50, y=297)
lbl_5.place(x=50, y=347)
diary_notes = {}

date = date.today()
def save_note():
    text = lbl_1.get() + '\n' + lbl_2.get() + '\n' + lbl_3.get() + '\n' + lbl_4.get() + '\n' + lbl_5.get()
    diary_notes.update({date.isoformat(): text})
    print(diary_notes)
    diarytext = open('diary.txt', 'a')
    with diarytext as f:
        f.write(str(diary_notes))
        f.write('\n ')
        f.close()
    return text

save = Button(canvas, text="Save", command=save_note)
save.place(x=309, y=391)
popup = Label(canvas, background='light blue', foreground = 'white', height = 0, text= 'Note saved',font = 'Arial 24')


def show_history():
    history_window = Toplevel(root)
    history_window.title('All notes')
    history_window['bg'] = 'light blue'
    diary_text = open('diary.txt', 'r')
    with diary_text as f:
        data = f.read()
    txt = Label(history_window, text=data , background = 'light blue', foreground ='black')
    txt.pack()

history = Button(canvas, text="History", command=show_history)
history.place(x=10, y=10)

def callback(event):

    def hide():
        popup.place_forget()
    def display():
        popup.place(x=250, y= 391)
        save.after(500, hide)
    save.after(250, display)


save.bind('<Button-1>', callback)
canvas.mainloop()