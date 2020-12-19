from pytube import YouTube
import os
from tkinter import *

root=Tk()
root.geometry('800x400')
root.title('Youtube Video DOWNLOAD')

Label_1=Label(root,text="Enter the Link Here", font=("bold",25))
Label_1.place(x=120,y=30)

mylink=StringVar()
pastelink=Entry(root, width=50, textvariable=mylink)
pastelink.place(x=150, y=100)

def downloadVideo():
    x=str(mylink.get())
    ytvideo=YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('F:/'):
        os.makedirs('E:/')
    ytvideo.download('E:/') 

Button(root,text="Download Video", width=30, bg='green',fg="white", command=downloadVideo).place(x=200, y=140)

root.mainloop()

