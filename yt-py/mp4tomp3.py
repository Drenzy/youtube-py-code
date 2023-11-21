import os
from tkinter import Tk, Label, Button, filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip

class VideoToMP3Converter:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Video to MP3 Converter")
        
        # Label to display the selected file path or a message
        self.file_path_label = Label(root, text="No file selected")
        self.file_path_label.pack(pady=10)

        # Button to trigger the file selection dialog
        self.select_file_button = Button(root, text="Select MP4 File", command=self.select_file)
        self.select_file_button.pack(pady=10)

        # Button to start the conversion process
        self.convert_button = Button(root, text="Convert to MP3", command=self.convert_to_mp3)
        self.convert_button.pack(pady=10)

    def select_file(self):
        # Open a file dialog to select an MP4 file
        file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        self.file_path_label.config(text=file_path)

    def convert_to_mp3(self):
        # Get the selected file path from the label
        input_file_path = self.file_path_label.cget("text")

        # Check if a valid MP4 file is selected
        if not input_file_path or not input_file_path.endswith(".mp4"):
            self.file_path_label.config(text="Please select a valid MP4 file")
            return

        # Generate the output file path with a .mp3 extension
        output_file_path = os.path.splitext(input_file_path)[0] + ".mp3"

        try:
            # Use moviepy to open the video file and extract audio
            video_clip = VideoFileClip(input_file_path)
            audio_clip = video_clip.audio

            # Write the audio to an MP3 file
            audio_clip.write_audiofile(output_file_path, codec="mp3")

            # Close the audio and video clips
            audio_clip.close()
            video_clip.close()

            # Update the label with a success message
            self.file_path_label.config(text=f"Conversion successful: {output_file_path}")
        except Exception as e:
            # Update the label with an error message if conversion fails
            self.file_path_label.config(text=f"Error during conversion: {str(e)}")

if __name__ == "__main__":
    # Create the main Tkinter window and start the application
    root = Tk()
    app = VideoToMP3Converter(root)
    root.mainloop()
