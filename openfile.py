from tkinter import *
from tkinter import filedialog
import shutil
import cv2
import numpy as np
from PIL import ImageTk, Image
import tkinter.messagebox

root = Tk()
def openFile(event):
    global filename
    filename = filedialog.askopenfilename()
    shutil.copy(filename, "import.tif")
def nextWin(Event):
    top = Toplevel()
    button2 = Button(top, text="open image")
    button4 = Button(top, text="veriy Fingerprints")
    def selectFile(event):
        global filename2
        filename2 = filedialog.askopenfilename()
        shutil.copy(filename2, "verify.tif")

    def verify(event):
        image1 = cv2.imread('import.tif')
        image2 = cv2.imread('verify.tif')
        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)
        if result == True:
            result = Toplevel()
            result.geometry("1500x1000")
            canvas = Canvas(result, width=1500, height=600, bg="white")
            canvas.grid(row=12, column=9)
            photo = ImageTk.PhotoImage(file ="import.tif")
            canvas.create_image(200, 280, image=photo)
            photo2 = ImageTk.PhotoImage(file = "verify.tif")
            canvas.create_image(800,280, image=photo2)
            tkinter.messagebox.showinfo('window title','Fingerprints Match')

        else:
            result = Toplevel()
            result.geometry("1500x1000")
            canvas = Canvas(result, width=1500, height=600, bg="white")
            canvas.grid(row=12, column=9)
            photo = ImageTk.PhotoImage(file ="import.tif")
            canvas.create_image(200, 280, image=photo)
            photo2 = ImageTk.PhotoImage(file = "verify.tif")
            canvas.create_image(800,280, image=photo2)
            tkinter.messagebox.showinfo('window title','Fingerprints DO NOT Match')
    button2.bind("<Button-1>", selectFile)
    button2.pack()
    button4.bind("<Button-1>", verify) 
    button4.pack()
    
button = Button(root, text="Browse")
button.bind("<Button-1>", openFile)
button.pack()
button3 = Button(root, text="Next")
button3.bind("<Button-1>", nextWin)
button3.pack()
root.mainloop()