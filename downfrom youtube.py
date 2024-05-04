import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog 
import moviepy.editor as mp

root=tk.Tk()
root.geometry("580x300")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="#0F0806")

def widgets() :
    head_label = Label(root,
                       text="Video downloader\n By eng:kareem Elsalamty",
                       padx=15,
                       pady=15,
                       fg="#F4BC8C",
                       bg="#0F0806")
    head_label.grid(row=0,
                    column=0,
                    columnspan=3)

    link_label = Label(root,
                       text="Enter YouTube link:",
                       bg="#F4BC8C",
                       fg="black",
                       pady=5,
                       padx=5)
    link_label.grid(row=1,
                    column=0,
                    pady=5,
                    padx=5)
    root.linkText = Entry(root,
                          width=35,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=1,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    quality_label = Label(root,
                          text="Select Quality:",
                          bg="#F4BC8C",
                          fg="black",
                          pady=5,
                          padx=9)
    quality_label.grid(row=2,
                       column=0,
                       pady=5,
                       padx=5)
    quality_menu = OptionMenu(root, quality_var, *quality_options)
    quality_menu.grid(row=2,
                      column=1,
                      pady=5,
                      padx=5)

    mp3_checkbox = Checkbutton(root,
                               text="Convert to MP3",
                               variable=mp3_var,
                               bg="#0F0806",
                               fg="snow",
                               selectcolor="#F4BC8C")
    mp3_checkbox.grid(row=2,
                      column=2,
                      pady=7,
                      padx=7,
                      sticky=W)

    save_asText = Label(root,
                        text="Save as:",
                        bg="#F4BC8C",
                        fg="black",
                        pady=5,
                        padx=9)
    save_asText.grid(row=3,
                     column=0,
                     pady=5,
                     padx=5)
    root.save_asText = Entry(root,
                             width=27,
                             textvariable=download_Path,
                             font="Arial 14")
    root.save_asText.grid(row=3,
                          column=1,
                          pady=5,
                          padx=5)
    browse_Button = Button(root,
                           text="Browse",
                           command=browse,
                           width=10,
                           bg="#F4BC8C",
                           fg="black",
                           relief=GROOVE)
    browse_Button.grid(row=3,
                       column=2,
                       pady=1,
                       padx=1)

    Download_Button = Button(root,
                             text="Download",
                             command=download,
                             width=20,
                             bg="#F4BC8C",
                             fg="black",
                             pady=10,
                             padx=15,
                             relief=GROOVE,
                             font="Georgia, 13")
    Download_Button.grid(row=4,
                         column=1,
                         pady=20,
                         padx=20)
    # Variable initialization
video_Link = StringVar()
quality_var = StringVar()
quality_options = ["720p", "480p", "360p", "240p", "144p"]
mp3_var = IntVar()
download_Path = StringVar()

# Function to browse and select the download path
def browse():
    download_directory = filedialog.askdirectory(initialdir="YOUR/DEFAULT/PATH")
    download_Path.set(download_directory)

# Function to download the video
def download():
    youtube_link = video_Link.get()
    save_path = download_Path.get()
    selected_quality = quality_var.get()

    try:
        # Download the YouTube video
        yt = YouTube(youtube_link)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        
        if stream is not None:
            stream.download(output_path=save_path)
            
            # Convert to MP3 if selected
            if mp3_var.get() == 1:
                video_path = save_path + '/' + stream.default_filename
                mp3_path = save_path + '/' + yt.title + '.mp3'
                video = mp.VideoFileClip(video_path)
                video.audio.write_audiofile(mp3_path)
                video.close()
            
            messagebox.showinfo("Success", "Download completed!")
        else:
            messagebox.showerror("Error", "No suitable video stream found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the GUI elements
widgets()

# Start the main loop
root.mainloop()