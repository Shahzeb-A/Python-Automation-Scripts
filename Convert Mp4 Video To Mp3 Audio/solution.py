import os
import tkinter as tk
from pathlib import Path
from tkinter import END, filedialog
from tkinter import messagebox

from moviepy.editor import VideoFileClip


def convert_video_to_audio(video_file: str, output_folder: str, output_ext="mp3") -> None:
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood

    :param video_file: The filename of the video to extract the audio
    :param output_folder: The folder to save the output audio
    :param output_ext: The extension of the output audio
    :return: returns None

    """

    name_of_video_file = Path(video_file).stem
    output_path_of_audio = os.path.join(output_folder, name_of_video_file)

    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{output_path_of_audio}.{output_ext}")


def select_folder_to_save_audio(folder_name_textbox: tk.Entry) -> None:
    """Selects the folder to be used to
    save the the mp3 extracted from the Mp4

    :param folder_name_textbox: The textbox to display the were the audio will be saved
    :return: returns None
    """
    folder_name = filedialog.askdirectory()
    folder_name_textbox.delete(0, END)
    folder_name_textbox.insert(0, folder_name)


def select_video_file(filename_textbox: tk.Entry) -> None:
    """Selects the video file to be used
    in creating the mp3

    :param filename_textbox: The textbox to display the video path selected
    :return: returns None
    """

    filetypes = (
        ('Video files(MP4)', '*.mp4'),
    )
    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )
    filename_textbox.delete(0, END)
    filename_textbox.insert(0, filename)


def process_video() -> None:
    """process the video information to audio

    :return: returns None
    """

    video_file_path = file_textbox.get()
    folder_name = folder_textbox.get()

    if not os.path.exists(video_file_path):
        messagebox.showerror("Error", "Video file path cannot be empty")
        return

    video_extension = Path(video_file_path).suffix
    if video_extension not in ['.mp4']:
        messagebox.showerror("Error", "Wrong video format")
        return

    convert_video_to_audio(video_file_path, output_ext="mp3", output_folder=folder_name)
    reset_user_interface()
    messagebox.showinfo("Success", "The file has been converted !")


def reset_user_interface() -> None:
    """Reset the user interface so that the user can
    use it again

    :return: returns None
    """
    file_textbox.delete(0, END)
    folder_textbox.delete(0, END)


root = tk.Tk()
root.title("Convert your MP4 To Mp3")
root.resizable(False, False)
root.geometry('550x200')

file_label = tk.Label(root, text="Video File", font=30).grid(row=0, column=1)

file_textbox = tk.Entry(root, font=30, width=30)
file_textbox.grid(row=0, column=2, padx=10, pady=10)

open_button = tk.Button(root, text='Find video', font=30, command=lambda: select_video_file(file_textbox))
open_button.grid(row=0, column=3)

folder_label = tk.Label(root, text="Output Folder", font=30).grid(row=1, column=1)

folder_textbox = tk.Entry(root, font=30, width=30)
folder_textbox.grid(row=1, column=2, padx=10, pady=10)

open_folder_button = tk.Button(root, text='Find folder',
                               font=30, command=lambda: select_folder_to_save_audio(folder_textbox))
open_folder_button.grid(row=1, column=3)

convert_button = tk.Button(root, text='Convert Video to Audio',font=30, command=lambda: process_video())
convert_button.grid(row=8, column=2)

in_progress_label = tk.Label(root, text="", font=30)
in_progress_label.grid(row=10, column=2)

root.mainloop()