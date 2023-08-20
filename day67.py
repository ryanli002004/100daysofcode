import tkinter as tk
window = tk.Tk()
window.title("find person")
window.geometry("500x500")

filenamemo = "day67mo.png"
filenamekatie = "day67katie.png"
filenamegerald = "day67gerald.png"
filenamecharlotte = "day67charlotte.png"


def findperson ():
    guess = text.get("1.0","end").strip()
    if guess == "mo":
        canvas.itemconfig(container, image = imagemo)
    elif guess == "katie":
        canvas.itemconfig(container, image = imagekatie)
    elif guess == "charlotte":
        canvas.itemconfig(container, image = imagecharlotte)
    elif guess == "gerald":
        canvas.itemconfig(container, image = imagegerald)
    text.delete("1.0", "end")


imagecharlotte = tk.PhotoImage(file = filenamecharlotte)
imagecharlotte = imagecharlotte.subsample(3)
imagegerald = tk.PhotoImage(file = filenamegerald)
imagegerald = imagegerald.subsample(3)
imagekatie = tk.PhotoImage(file = filenamekatie)
imagekatie = imagekatie.subsample(3)
imagemo = tk.PhotoImage(file = filenamemo)
imagemo = imagemo.subsample(3)
canvas = tk.Canvas(window, height = 200, width = 200)
canvas.pack()
container = canvas.create_image(100,60,  image = "")
label = tk.Label(text="enter a name")
label.pack()
text = tk.Text(window,height = 1, width = 25)
text.pack()
find = tk.Button(command = findperson, text = "find person")
find.pack()


tk.mainloop()