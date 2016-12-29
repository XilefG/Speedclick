import tkinter as tk

root = tk.Tk()

def get_action(button):
    def action():
        button.config(bg="green")
    return action
        
buttons = []
for i in range(5):
    b = tk.Button(root, text=i)
    b.config(command=get_action(b))
    buttons.append(b)
    b.grid(row=i, column=0)

#Keep this at bottom
root.mainloop()
