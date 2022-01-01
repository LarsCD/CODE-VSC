# libaries
import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import time, os

# programs
from A1encoder_v2 import A1encoder
from toolkit import log

# global vars
defaultKey = 1000
currentOpenPath = None

programTitle = 'Text Editor'


class CreateWindow:

    def __init__(self):
        log.message('[!!] CreateWindow created')
        self.folderPath = None
        self.filename = None
        self.key = None

        self.entryRoot = tk.Tk()
        self.entryRoot.configure(bg='lightgray')
        self.entryRoot.geometry('450x250')
        self.entryRoot.title('Create File')

        self.frame1 = Frame(self.entryRoot, relief=RAISED, borderwidth=1)
        self.frame1.pack(fill=BOTH, expand=True)
        self.frame2 = Frame(self.entryRoot, relief=RAISED, borderwidth=1)
        self.frame2.pack(fill=BOTH, expand=False)

        labelEntry1 = tk.Label(self.frame1, text='Filename')
        # labelEntry2 = tk.Label(self.frame1, text='Encoding Key (0, 1000)')
        lableEntry3 = tk.Label(self.frame1, text='Filepath')

        lableMessage1 = tk.Label(self.frame1, text='Folder selected:')
        self.lableMessage1B = tk.Label(self.frame1, text='')
        self.lableMessage2 = tk.Label(self.frame1, fg='red', text='')

        self.entry1Var = tk.StringVar()
        # self.entry2Var = tk.IntVar()
        self.entry1 = tk.Entry(self.frame1, textvariable=self.entry1Var, width=20, borderwidth=1)
        # self.entry2 = tk.Entry(self.frame1, textvariable=self.entry2Var, width=20, borderwidth=1)
        button1 = tk.Button(self.frame1, text='Open', command=self.selectDir)
        button1B = tk.Button(self.frame1, text='Apply Current Folder', command=self.selectCurrentDir)

        buttonCreate = tk.Button(self.frame2, text='Create', width=6, borderwidth=2, command=self.completeCreate)
        buttonCancel = tk.Button(self.frame2, text='Cancel', width=6, borderwidth=2, command=self.cancelButton)

        labelEntry1.grid(row=0, column=0, sticky="w", padx=5)
        # labelEntry2.grid(row=1, column=0, sticky="w", padx=5)
        lableEntry3.grid(row=2, column=0, sticky="w", padx=5)
        lableMessage1.grid(row=4, column=0, sticky="w", padx=5)
        self.lableMessage1B.grid(row=4, column=1, sticky="w", padx=5)
        self.lableMessage2.grid(row=5, column=0, sticky="w", padx=5)

        self.entry1.grid(row=0, column=1, sticky="w", padx=5)
        # self.entry2.grid(row=1, column=1, sticky="w", padx=5)
        button1.grid(row=2, column=1, sticky="w", padx=5)
        button1B.grid(row=3, column=1, sticky="w", padx=5)

        buttonCreate.grid(row=0, column=1, padx=65, pady=5)
        buttonCancel.grid(row=0, column=0, padx=65, pady=5)

        # self.entryRoot.mainloop()


    def destroyWindow(self):
        self.entryRoot.destroy()
        log.message('[!!] CreateWindow destroyed')


    def cancelButton(self):
        log.message('CreateWindow: cancel')
        self.destroyWindow()


    def selectDir(self):
        dirPath = tk.filedialog.askdirectory()
        if not dirPath:
            return
        self.folderPath = dirPath
        self.lableMessage1B.config(text=f'{self.folderPath}')
        log.message(f'folderPath: {self.folderPath}')


    def selectCurrentDir(self):
        dirPath = os.path.dirname(os.path.abspath(__file__))
        self.folderPath = dirPath
        self.lableMessage1B.config(text=f'{self.folderPath}')
        log.message(f'folderPath: {self.folderPath}')


    def completeCreate(self):
        log.message('CreateWindow: attempt create')
        completion = False
        completeFilename = False
        completeKey = True
        completeFolderPath= False

        # get values from entries
        self.filename = f'{self.entry1.get()}.txt'
        # self.key = self.entry2.get()

        # check if valid folderPath
        if self.folderPath == None:
            log.error('no folder selected')
            self.lableMessage2.config(text='Please select a folder')
        else:
            completeFolderPath = True

        # check if filename
        if self.entry1.get() == '':
            log.error('no filename entered')
            self.lableMessage2.config(text='Please enter a filename')
        else:
            completeFilename = True

        if completeFilename and completeKey and completeFolderPath:
            completion = True

        if completion:
            log.message('CreateWindow: succesful create')
            dataList = [self.filename, self.key, self.folderPath]
            # message = f'create: filename: {self.filename} / key: {self.key} / folderPath: {self.folderPath}'
            # log.message(message)
            self.destroyWindow()
            MainWindow.createFileComplete(dataList)


class MainWindow():

    def __init__(self):

        self.window = tk.Tk() # root
        # self.window.configure(bg='blue')
        self.window.title(programTitle)
        self.window.geometry('700x425')
        self.window.resizable(False, False)
        # self.window.rowconfigure(0, minsize=800, weight=1)
        # self.window.columnconfigure(1, minsize=800, weight=1)

        textFrame = tk.Frame(self.window, relief=tk.RAISED, height=50)
        buttonsFrame = tk.Frame(self.window, relief=tk.RAISED, bd=2)
        self.txt_edit = tk.Text(self.window, relief=tk.RAISED, bd=2)

        self.currentOpenPathVar = tk.StringVar()
        self.currentKeyVar = tk.IntVar()

        self.labelCurrentOpenPath = Label(textFrame, text='Current folder')
        self.labelCurrentOpenPathB = Label(textFrame, textvariable=self.currentOpenPathVar)
        self.labelCurrentKey = Label(textFrame, text='Current key')
        self.entryCurrentKey = Entry(textFrame)

        self.labelErrorMessage = Label(textFrame, fg='red', text='')

        btn_create = tk.Button(buttonsFrame, text="Create File", command=self.createFileBegin)
        btn_open = tk.Button(buttonsFrame, text="Open", command=self.openFile)
        btn_save = tk.Button(buttonsFrame, text="Save", command=self.saveFile)
        btn_clear = tk.Button(buttonsFrame, text="Clear", command=self.clear)
        btn_quit = tk.Button(buttonsFrame, text="Quit", command=self.on_closing)

        self.labelCurrentOpenPath.grid(row=0, column=0, sticky="w", padx=5)
        self.labelCurrentOpenPathB.grid(row=0, column=1, columnspan=2, sticky="w", padx=5)
        self.labelCurrentKey.grid(row=1, column=0, sticky="w", padx=5)
        self.entryCurrentKey.grid(row=1, column=1, sticky="w", padx=5)
        self.labelErrorMessage.grid(row=1, column=2, sticky="w", padx=5)

        btn_create.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_open.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        btn_save.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        btn_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=40)
        btn_quit.grid(row=4, column=0, sticky="ew", padx=5, pady=90)

        textFrame.grid(row=0, columnspan=3, sticky="w")
        buttonsFrame.grid(row=1, column=0, sticky="ns")
        self.txt_edit.grid(row=1, column=1, sticky="nsew")

        self.window.after(1000, self.update)
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.window.mainloop()


    def createFileBegin(self):
        self.updateErrorLabel('', 'red')
        self.txt_edit.delete(1.0, tk.END)
        CreateWindow()
        print('waiting')


    def createFileComplete(dataList): # gets called from other class (CreateWindow)
        global currentOpenPath
        filename = dataList[0]
        key = dataList[1]
        folderPath = dataList[2]
        message = f'selected: filename: {filename} / key: {key} / folderPath: {folderPath}'
        log.message(message)
        currentOpenPath = os.path.join(folderPath, filename)


    def update(self):
        self.currentOpenPathVar.set(currentOpenPath)
        self.currentKeyVar.set(self.entryCurrentKey.get())
        # log.message(f'updated: labelCurrentOpenPathB={currentOpenPath}')

        self.window.after(10, self.update)


    def openFile(self):
        self.updateErrorLabel('', 'red')
        global currentOpenPath
        currentOpenPath = None



        # open file for editing
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return

        # check if valid key
        currentKey = self.entryCurrentKey.get()
        try:
            if currentKey == '':
                log.error('no key entered')
                self.updateErrorLabel('Please enter a key', 'red')
                return
            elif int(currentKey) < A1encoder.key[0] or int(currentKey) > A1encoder.key[1]:
                log.error('invalid key entered: key boundries')
                self.updateErrorLabel('Please enter a valid key', 'red')
                return
            else:
                completeKey = True
        except ValueError:
            log.error('invalid key entered: no int')
            self.updateErrorLabel('Please enter a valid key', 'red')
            return

        # set currentOpenPath
        currentOpenPath = filepath
        self.txt_edit.delete(1.0, tk.END)
        # decoding file
        try:
            currentKey = self.currentKeyVar.get()
        except:
            self.updateErrorLabel('No key entered', 'red')
        else:
            datadump = A1encoder.loadFromFile(filepath, self.currentKeyVar.get())
            text = A1encoder.processDataString(datadump)
            # update editor window with decoded text
            self.txt_edit.insert(tk.END, text)


    def saveFile(self):
        global currentOpenPath
        self.updateErrorLabel('', 'red')

        # check if file open
        if currentOpenPath == None:
            log.error('no file currently open: currentOpenPath = None')
            self.updateErrorLabel('No file selected', 'red')
            return

        # chek if valid key
        currentKey = self.entryCurrentKey.get()
        try:
            if currentKey == '':
                log.error('no key entered')
                self.updateErrorLabel('Please enter a key', 'red')
                return
            elif int(currentKey) < A1encoder.key[0] or int(currentKey) > A1encoder.key[1]:
                log.error('invalid key entered: key boundries')
                self.updateErrorLabel('Please enter a valid key', 'red')
                return
            else:
                completeKey = True
        except ValueError:
            log.error('invalid key entered: no int')
            self.updateErrorLabel('Please enter a valid key', 'red')
            return

        currentKey = int(currentKey)

        # get text from editor
        text = self.retrieveInput()
        self.updateErrorLabel('File saved', 'green')
        # encode and write to file
        A1encoder.writeToFile(currentOpenPath, text, currentKey)
        currentOpenPath = None

        self.txt_edit.delete(1.0, tk.END)


    def clear(self):
        global currentOpenPath
        self.updateErrorLabel('', 'red')
        self.currentOpenPathVar.set('')
        self.txt_edit.delete(1.0, tk.END)
        currentOpenPath = None



    def retrieveInput(self):
        input = self.txt_edit.get("1.0", tk.END)
        return input


    def updateErrorLabel(self, message, color):
        self.labelErrorMessage.config(text=str(message), fg=str(color))


    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.window.destroy()


def main():
    log.message('[!!] program start')
    MainWindow()
    log.message('[!!] program quit')

if __name__ == '__main__':
    main()
