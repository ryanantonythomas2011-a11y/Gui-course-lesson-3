from tkinter import*
import calendar 

screen = Tk()
screen.geometry("700x700")



Calendar_label = Label(screen,text="Calendar",font=("Sans Serif",45)).place(x=250,y=50)
Enter = Label(screen,text="Enter the year").place(x=300,y=150)
enter_box = Entry(screen,width=15)
enter_box.place(x=300,y=200)
def showcalendar():
    screen2 = Tk()
    screen2.geometry("350x350")
    year = int(enter_box.get())
    content = calendar.calendar(year)
    calendar_content = Label(screen2,text=content)
    calendar_content.place(x=10,y=10)

show_calendar = Button(screen,command=showcalendar,text="Show Calendar").place(x=300,y=300)
exit_button = Button(screen,command=exit,text="Exit").place(x=320,y=400)
mainloop()


