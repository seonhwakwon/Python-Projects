import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web page Generator")
        
        self.lbl_input = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.lbl_input.grid(row=0, column=0, padx=(10,0), pady=(10,0),sticky=W)

        self.input_text = Entry(self.master,text="",width=120)
        self.input_text.grid(row=1, column=0, columnspan=3,padx=(20,10), pady =(10,20))
    

        self.btn = Button(self.master, text="Defalult HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=3,column=1, padx=(0,0), pady=(10,10),sticky= N+E)

        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.UserHTML)
        self.btn.grid(row=3,column=2, padx=(20,10), pady=(10,10),sticky= N+E)


    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale! "
        htmlFile = open("index.html", "w")
        htmlContent ="<html>\n<body>\n<h1>" +htmlText+ "</h1>\n<body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
    def UserHTML(self):
        htmlText = self.input_text.get()
        htmlFile = open("index.html", "w")
        htmlContent ="<html>\n<body>\n<h1>" +htmlText+ "</h1>\n<body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
    
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
