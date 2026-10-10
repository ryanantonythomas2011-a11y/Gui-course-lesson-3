from tkinter import*
screen = Tk()
screen.geometry("500x500")
screen.title("Adder")

label1 = Label(screen,text="Enter The Numbers")
label1.place(x=200,y=50)

entry1 = Entry(screen,width=30)
entry1.place(x=200,y=100)

entry2 = Entry(screen,width=30)
entry2.place(x=200,y=200)

def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    addition = num1 + num2
    add_label = Label(screen,text=f"result:{addition} ")
    add_label.place(x=200,y=300)

add_button = Button(screen,text="Add",command=add,bg="Green")
add_button.place(x=200,y=250)

mainloop()