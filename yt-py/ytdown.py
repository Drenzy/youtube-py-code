import tkinter as tk
from tkinter import ttk
from pytube import YouTube

# Function to handle video download
def download_video():
    # Get video URL and output directory from entry widgets
    video_url = url_entry.get()
    output_directory = output_entry.get() or "."

    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution video stream
        video_stream = yt.streams.get_highest_resolution()

        # Update the download label with the video title
        download_label.config(text=f"Downloading: {yt.title}...")

        # Download the video to the specified output directory
        video_stream.download(output_directory)

        # Update the download label to indicate completion
        download_label.config(text="Download complete!")
    except Exception as e:
        # Handle exceptions and display an error message
        download_label.config(text=f"An error occurred: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("YouTube Video Downloader")

# URL Entry Widgets
url_label = ttk.Label(window, text="Enter YouTube Video URL:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

url_entry = ttk.Entry(window, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Output Directory Entry Widgets
output_label = ttk.Label(window, text="Enter Output Directory:")
output_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

output_entry = ttk.Entry(window, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Download Button Widget
download_button = ttk.Button(window, text="Download", command=download_video)
download_button.grid(row=2, column=0, columnspan=2, pady=10)

# Download Status Label Widget
download_label = ttk.Label(window, text="")
download_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the GUI
window.mainloop()
