import tkinter
from tkinter import Scrollbar, PhotoImage, StringVar, Tk, Frame, Label, Entry, Button, Listbox, BOTH, RIGHT, LEFT, END

# Initialize the main window
root = Tk()
root.title("To-do list")
root.geometry("400x650")
root.resizable(False, False)

task_list = []


try:
    Image_icon = PhotoImage(file="task.png")
    root.iconphoto(False, Image_icon)
except Exception as e:
    print(f"Error loading task.png: {e}")


heading = Label(root, text="All Tasks", font="arial 20 bold")
heading.place(x=130, y=20)

frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0, textvariable=task)
task_entry.place(x=10, y=7)
task_entry.focus()


def add_task():
    task_text = task.get()
    if task_text != "":
        listbox.insert(END, task_text)
        task_list.append(task_text)
        task.set("")  # Clear the entry box
    else:
        print("No task entered")


add_button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=add_task)
add_button.place(x=300, y=0)

frame1 = Frame(root, bd=3, width=400, height=280, bg="#32405b")
frame1.pack(pady=(240, 0))


listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        task_list.pop(selected_task_index)
    except IndexError:
        print("No task selected")


try:
    Delete_icon = PhotoImage(file="delete.png")
    delete_button = Button(root, image=Delete_icon, bd=0, command=delete_task)
    delete_button.pack(side='bottom', pady=13)
except Exception as e:
    print(f"Error loading delete.png: {e}")


root.mainloop()
