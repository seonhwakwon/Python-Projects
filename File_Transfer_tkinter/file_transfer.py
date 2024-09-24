import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import time
import datetime


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10),pady=(30,0))

        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10),pady=(15,10))

        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))

    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0,END)
        self.source_dir.insert(0, selectSourceDir)
        self.sourceDir_btn = Button(text="Select Source", width=20)

    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0,END)
        self.destination_dir.insert(0, selectDestDir)
        
    def transferFiles(self):
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        source_files = os.listdir(source)
        #put current time as timestamp in the variable 'now'
        now = datetime.datetime.now().timestamp()
        for i in source_files:
                #file path
                path = source +'/' + i
                #file edited time 
                modification_time = os.path.getmtime(path)
                #if less than Deduct from current time to file edited time than 86400second(24hours), transfer file.
                if (now - modification_time) <= 86400:
                    print(now - modification_time)
                    shutil.move(source + '/' + i, destination)
                    print(i+ ' was successfully transferred.')

    def exit_program(self):
        root.destroy()

if __name__ =="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
