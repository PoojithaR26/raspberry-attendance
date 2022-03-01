from tkinter import *
from Functions import *
from AttendanceWebcam import *
from AttendanceImage import *
from AttendanceVideo import *
from tkinter import filedialog
import tkinter.messagebox
from PIL import ImageTk, Image


def clickCapture():
    ans = tkinter.messagebox.askyesno("Confirm", "Capture image?")
    if ans:
        name = enterName.get()
        captureImage(name)

def startProgramWebcam():
    tkinter.messagebox.showinfo("Info","Reading database images")
    startWebcam()

def startProgram():
    rootStart = Tk()
    rootStart.title("Select your choice")
    rootStart.minsize(500, 80)
    rootStart.maxsize(500, 80)
    rootStart.configure(bg="#9ADCFF")
    rootStart.geometry('%dx%d+%d+%d' % (500, 80, 300, 600))
    Button(rootStart, text="Video", fg="#FFF89A", bg="#FFB2A6", width=25, height=2, command=callStartVideo).pack(side='left', padx=(40,0))
    Button(rootStart, text="Image", fg="#FFF89A", bg="#FFB2A6", width=25, height=2, command=callStartImage).pack(side='right', padx=(40, 0))

def callStartVideo():
    filename = filedialog.askopenfile(initialdir=os.path.dirname(__file__), title="Choose folder")
    if len(filename) > 0:
        callStartVideo(filename)
    else:
        tkinter.messagebox.showinfo("Select the video")


def callStartImage():
    filename = filedialog.askopenfile(initialdir=os.path.dirname(__file__), title="Choose folder")
    if len(filename) > 0:
        callStartImage(filename)
    else:
        tkinter.messagebox.showinfo("Select the image")

def openExcelOption():
    rootExcel = Tk()
    rootExcel.title("Choose Option")
    rootExcel.minsize(400, 160)
    rootExcel.maxsize(400, 160)
    rootExcel.configure(bg="#9ADCFF")
    rootExcel.geometry('%dx%d+%d+%d' % (380, 140, 300, 600))
    Button(rootExcel, text="Attendance by Webcam", fg="#FFF89A", bg="#FFB2A6", width=25, height=2, command=openExcelWebcam).pack(pady=(10, 4))
    Button(rootExcel, text="Attendance Image", fg="#FFF89A", bg="#FFB2A6", width=25, height=2,command=openExcelVideo).pack(pady=(10, 4))
    Button(rootExcel, text="Attendance Video", fg="#FFF89A", bg="#FFB2A6", width=25, height=2,command=openExcelImage).pack(pady=(10, 4))


root = Tk()
root.title("Attendance Management System using Facial Recognition")
root.minsize(910, 750)
root.maxsize(910, 750)
root.configure(bg="#9ADCFF")

heading = Label(root, text="Automated Attendance Management System", fg="#000000", bg="#FF8AAE")
heading.configure(font=("Times New Roman", 25))
heading.pack(fill="x")

img = ImageTk.PhotoImage(Image.open('Logo/image.png'))
labelImage = Label(root, image=img, borderwidth=0)
labelImage.pack(pady=20)

enterName = Entry(root, fg="#A73489", bg="#FFF89A")
enterName.configure(font=30)
enterName.pack()

btn1 = Button(root, text="Add Student", fg="#000000", bg="#FFB2A6", width=25, height=2, command=clickCapture).pack(pady=(0, 15))
btn2 = Button(root, text="Record attendance with Webcam", fg="#000000", bg="#FFB2A6", width=25, height=2, command=startProgramWebcam).pack(pady=(0, 15))
btn3 = Button(root, text="Record attendance for online class", fg="#000000", bg="#FFB2A6", width=25, height=2, command=startProgram).pack(pady=(0, 15))
btn4 = Button(root, text="Open Attendance Record", fg="#000000", bg="#FFB2A6", width=25, height=2, command=openExcelOption).pack(pady=(0, 15))


root.mainloop()

