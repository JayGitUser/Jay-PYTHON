

import PySimpleGUI as sg
import pytube
from pytube import YouTube


# Create the layout
layout = [
    [sg.Text("Enter the URL:")],
    [sg.Input(key="url")],
    [sg.Button("DOWNLOAD")]
]
# Create the window
window = sg.Window("UTUBE DOWNLOADER", layout,size=(450,100))





# Run the event loop to process user inputs
while True:

    try:
        event, values = window.read()
        
        # If the button is clicked, run the download
        if event == "DOWNLOAD":

            # run the download
            url = values["url"]
            video = YouTube(url).streams.filter(res="720p").first().download()

    

        # If the window is closed, break the loop
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
    except pytube.exceptions.RegexMatchError:
        # If the URL is invalid, print an error message
        print("Invalid URL. Please try again.")
    except pytube.exceptions.VideoUnavailable:
        # If the video is unavailable, print an error message
        print("Video is unavailable. Please try again.")

# Close the window
window.close()











