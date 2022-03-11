import tkinter as tk
import utils
import pyttsx3
from matplotlib.pyplot import text
from tkinter.messagebox import showinfo
from tkinter import END, HORIZONTAL, filedialog as fd
from tkinter.ttk import Combobox

def select_folder(textbox):
    filename = fd.askdirectory()
    textbox.delete(0, END)
    textbox.insert(0, filename)

def select_file(textbox):
    filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )
    textbox.delete(0, END)
    textbox.insert(0, filename)

def configure_settings(engine):
    engine.setProperty('rate',int(rate_value.get()))
    #slider values go from 0-100 so it has to be divided by 100 to fit the 0-1 range for volume
    volume_normalized = volume_slider.get() / 100 
    engine.setProperty('volume',volume_normalized)
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[voice_combobox.current()].id)
   
def convert(engine,filetype):
    configure_settings(engine)
    pdf_string = utils.pdf_to_string(file_textbox.get())
    utils.string_to_audio(engine, pdf_string, filetype)

root = tk.Tk()
engine = pyttsx3.init()
root.title("PDF To Audio")
root.resizable(False, False)
root.geometry('800x500')

file_label = tk.Label(
    root,
    text="Input File",
    font=40
).grid(
    row=0, 
    column=1
    )
   
file_textbox = tk.Entry(
    root, 
    font = 40,
    width = 50
)
file_textbox.grid(
    row = 0,
    column = 2,
    padx = 10,
    pady = 10
)

open_button = tk.Button(
    root,
    text='Open a File',
    font=40,
    command=lambda : select_file(file_textbox)
).grid(
    row=0, 
    column=3
    )


folder_label = tk.Label(
    root,
    text="Output Folder",
    font=40
).grid(
    row=1, 
    column=1
    )


folder_textbox = tk.Entry(
    root, 
    font = 40,
    width = 50
)
folder_textbox.grid(
    row = 1,
    column = 2,
    padx = 10,
    pady = 10
)

open_folder_button = tk.Button(
    root,
    text='Open a folder',
    font=40,
    command=lambda : select_folder(folder_textbox)
).grid(
    row=1, 
    column=3
    )

    
rate_label= tk.Label(
    root,
    text ="Rate",
    font=40
).grid(
    row=3, 
    column=1
    )
rate_value = tk.StringVar()
rate_value.set("125")
rate_textbox = tk.Entry(
    root,
    font=40,
    textvariable=rate_value
).grid(
    row=3,
    column=2,
    sticky=tk.W
    )

volume_label= tk.Label(
    root,
    text="Volume",
    font=40
).grid(
    row=4, 
    column=1
    )

volume_slider = tk.Scale(
    root,
    from_ = 0,
    to = 100,
    font = 40,
    orient = HORIZONTAL,
    tickinterval = 10,
    length = 400
)
volume_slider.grid(
    row = 4, 
    column = 2,
    sticky = tk.W
    )

voice_label = tk.Label(
    root,
    text ="Voice",
    font = 40
).grid(
    row=6, 
    column=1
    )


voice_combobox = Combobox(
    root, 
    values= ["Male", "Female"],
    state= 'readonly'
)
voice_combobox.current(0)

voice_combobox.grid(
    row=6, 
    column=2,
    sticky=tk.W
    )

file_type_label = tk.Label(
    root,
    text ="File Type",
    font = 40
).grid(
    row=7, 
    column=1
    )

file_type_combobox = Combobox(
    root, 
    values= [".mp3", ".wav", ".flac" , ".wma"],
    state= 'readonly'
)
file_type_combobox.current(0)

file_type_combobox.grid(
    row=7, 
    column=2,
    sticky=tk.W
    )

convert_button = tk.Button(
    root,
    text='Convert',
    font=40,
    command=lambda : convert(engine, str(file_type_combobox.get()) )
).grid(
    row=8, 
    column=2
    )

root.mainloop()
