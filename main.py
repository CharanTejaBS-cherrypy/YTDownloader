import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        ytObject.streams
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded ✅")
    except:
        finishLabel.configure(text="Download Error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size-bytes_remaining
    percentage_of_completion = bytes_downloaded/total_size*100
    # print(percentage_of_completion)
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per+"%")
    pPercentage.update()

    # update Progress bar
    progressBar.set(float(percentage_of_completion)/100)


# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI elements
title = customtkinter.CTkLabel(
    app, text="Insert a youtube link", fg_color="#581845", corner_radius=5, padx=3, pady=3)
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, corner_radius=10, fg_color="#DAF7A6",
                              text_color="#C70039", placeholder_text="YouTube link here.....", placeholder_text_color="#FFC300")
link.pack(pady=30)

# finished Downloading
finishLabel = customtkinter.CTkLabel(
    app, text="", fg_color="#800000", text_color="#FFC300", corner_radius=10)
finishLabel.pack(padx=10, pady=10)

# progress percentage
pPercentage = customtkinter.CTkLabel(
    app, text=" 0% ", text_color="#66CDAA", fg_color="#191970", corner_radius=50)
pPercentage.pack(padx=20, pady=10)

progressBar = customtkinter.CTkProgressBar(app, width=400, height=30, border_width=5, corner_radius=20,
                                           fg_color="#00FF7F", border_color="#355E3B", progress_color="#7FFFD4", mode="determinate")
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(
    app, text="Download", command=startDownload, fg_color="#4CBB17", hover_color="#32CD32", border_color="#008080", border_width=1, text_color="#023020")
download.pack(padx=10, pady=10)


# Run app
app.mainloop()
