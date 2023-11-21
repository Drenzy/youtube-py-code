# Import necessary libraries
import re
from youtube_transcript_api import YouTubeTranscriptApi as yta
import easygui

# Get YouTube link from the user using a console popup
youtube_link = easygui.enterbox("Enter YouTube link:")

# Check if the user clicked Cancel
if youtube_link is None:
    exit()

# Extract video ID from the YouTube link using regex
video_id_match = re.search(r'(?<=watch\?v=)[\w-]+|(?<=youtu.be/)[\w-]+', youtube_link)

# Check if a valid video ID was found
if video_id_match:
    vid_id = video_id_match.group(0)
else:
    print("Invalid YouTube link. Please provide a valid link.")
    exit()

# Retrieve transcript data using YouTubeTranscriptApi
data = yta.get_transcript(vid_id)

# Initialize an empty string to store the transcript
transcript = ''

# Loop through the data to extract the text content
for value in data:
    for key, val in value.items():
        if key == 'text':
            transcript += val

# Split the transcript into lines
lines = transcript.splitlines()

# Join the lines to form the final transcript
final_transcript = " ".join(lines)

# Open a file named "ytText.txt" in write mode and write the final transcript to it
with open("ytText.txt", 'w') as file:
    file.write(final_transcript)
