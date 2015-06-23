import sys
from Tkinter import *
from tkFileDialog import *
import subprocess
import os


def browse():

    Tk().withdraw() 
    global FilePath
    FilePath = askopenfilename(filetypes = (("ApkFiles","*.apk"),("All files", "*")))
    bar.insert(0, FilePath)
            

def process():

    #get the ApkName 
    os.chdir(FilePath.rsplit('/', 1)[0])
    Parts = FilePath.split("/")
    ApkName = Parts[-1]
    

    #Copy the Apk in the desired location
    subprocess.call (['cp', FilePath, './Temp'])
    
    #Run the Script
    #os.chdir('/home/dinesh010/bin')
    BashCommand1 = "SampleScript.sh"
    os.system(BashCommand1)

    #Check if the csv file is created
    os.chdir('./B')
    
    if os.path.isfile("myfile") is True:
        popup = Tk()  #create an object
        popup.title(" ")
        popup.geometry("200x50+200+100")
        
        GuiLabel1 = Label(popup,text="Module Decoupling Done!!",fg = 'blue', font=("Helvetica", 12))
        GuiLabel1.pack()

        #popup.mainloop()

    if os.path.isfile("myfile") is True:     
        button3.configure(command = ViewFile1, fg = 'black')
        button4.configure(command = ViewFile2, fg = 'black')
        button5.configure(command = ViewFile3, fg = 'black')
        button6.configure(command = ViewFile4, fg = 'black')
        button7.configure(command = ViewFile5, fg = 'black')
        button8.configure(command = ViewFile6, fg = 'black')
        button9.configure(command = ViewFile7, bg = 'black', fg = 'yellow')
        button10.configure(command = ViewFile8, bg = 'black', fg = 'yellow')
        button11.configure(command = ViewFile9, bg = 'black', fg = 'yellow')

def ViewFile1():
    BashCommand = "gnome-open ./FolderStruct.pdf "
    os.system(BashCommand) 

def ViewFile2():
    BashCommand = "gnome-open ./DirectedPKDG.pdf "
    os.system(BashCommand) 
 

def ViewFile3():
    BashCommand = "gnome-open ./FolderStruct_scissored.pdf "
    os.system(BashCommand) 

def ViewFile4():
    BashCommand = "gnome-open ./FolderStruct_scissored.pdf "
    os.system(BashCommand) 


def ViewFile5():
    BashCommand = "gnome-open ./FolderStruct_scissored.pdf "
    os.system(BashCommand) 
 

def ViewFile6():
    BashCommand = "gnome-open ./FolderStruct_scissored.pdf "
    os.system(BashCommand) 

    
def ViewFile7():
    BashCommand = "gnome-open ./ClustersProduced.pdf "
    os.system(BashCommand) 


def ViewFile8():
    BashCommand = "gnome-open ./AdLibModule.pdf "
    os.system(BashCommand) 

def ViewFile9():
    BashCommand = "gnome-open ./Concerns.pdf "
    os.system(BashCommand) 
 

gui = Tk()  #create a gui frame
gui.title("ALD")
gui.geometry("1050x275")
#gui.config(highlightbackground= 'red')
#gui.configure(bg = 'black')


GuiLabel1 = Label(gui,text="Select an app to be clustered",font=("Helvetica", 14))
GuiLabel1.grid(row=0 , column=1)

gui.rowconfigure(1, minsize=30)

GuiLabel2 = Label(gui,text="ApkFile", width = 10, font=("Helvetica", 12))
GuiLabel2.grid(row=2 ,column=0)

bar=Entry(gui, width = 30)
bar.grid(row=2, column=1)


button1= Button(gui, text="Browse                 ", command = browse , font=("Helvetica", 11))
button1.grid(row=2, column=2)

button2= Button(gui, text="Decouple Modules", command = process , font=("Helvetica", 11))
button2.grid(row=3, column=2)

gui.rowconfigure(4, minsize=30)

button3= Button(gui, text="Available Packages", fg='white')
button3.grid(row=5, column=0)

button4= Button(gui, text="Package Dependancy Graph", fg='white')
button4.grid(row=5, column=1)

button5= Button(gui, text="Structural Similarity", fg='white')
button5.grid(row=5, column=2)

button6= Button(gui, text="Semantic Similarity", fg='white')
button6.grid(row=5, column=3)

button7= Button(gui, text="Taxonomical Similarity", fg='white')
button7.grid(row=5, column=4)

button8= Button(gui, text="Combined Similarity", fg='white')
button8.grid(row=5, column=5)

gui.rowconfigure(6, minsize=30)

button9= Button(gui, text="View Modules", fg='white')
button9.grid(row=7, column=0)

button10= Button(gui, text="View Ad Library Modules", fg='white')
button10.grid(row=7, column=2)

button11= Button(gui, text="Security/Privacy Concerns", fg='white')
button11.grid(row=7, column=4)


gui.mainloop()  #necessary for windows