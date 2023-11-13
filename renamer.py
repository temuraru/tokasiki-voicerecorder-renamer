import os
import shutil
from datetime import datetime

# Ex:
# data-2016-9-14-16-55-29.3gp + 2016-9-14-16-55-29.txt "2016-9-14-16-55-29,tfytgggg,22456663" ===>  2016-09-14 - tfytgggg (16-55-29).3gp

# Path to the directory containing the audio files and metadata
base_path = r"d:\Backup\com.tokasiki.android.voicerecorder"


# Function to extract metadata from the text file, considering commas in the filetitle
def extract_metadata(txt_path):
    """
    Extract metadata from the text file.

    Args:
        txt_path (str): Path to the text file.

    Returns:
        str: Extracted metadata.
    """
    with open(txt_path, 'r') as txt_file:
        content = txt_file.read().strip()
        fields = content.split(',')
        return ','.join(fields[1:-1])


# Function to format the new filename
def format_new_filename(date, filetitle, time):
    """
    Format the new filename based on date, filetitle, and time.

    Args:
        date (str): Date in the format 'Y-m-d'.
        filetitle (str): File title.
        time (str): Time in the format 'H-i-s'.

    Returns:
        str: Formatted filename.
    """
    formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")

    # Extract only the relevant parts of the time
    time_parts = time.split('-')[-3:]

    # Ensure each part of the time is padded with zeros
    formatted_time = '-'.join([part.zfill(2) for part in time_parts])

    return f"{formatted_date} - {filetitle} ({formatted_time}).3gp" if filetitle else f"{formatted_date} - ({formatted_time}).3gp"


# Iterate through each audio file in the directory
for audio_filename in os.listdir(base_path):
    """
    Main function to iterate through audio files, extract metadata, and copy with a new filename.

    This script is designed to process audio files exported by an Android voice recorder app (tokasiki voicerecorder).
    For each recording, it looks for an associated text file containing metadata and copies the audio file with a new
    filename based on extracted date, filetitle, and time information. If the text file is missing, the new filename
    is generated without the optional filetitle field. The original modification time of the file is preserved for
    the copied file.

    Directory Structure:
    - The script assumes a directory structure where audio files (extension '.3gp') have names starting with 'data-'
      and corresponding text files have similar names but with '.txt' extension.

    Filename Format:
    - Audio file: data-YYYY-MM-DD-HH-II-SS.3gp
    - Text file: YYYY-MM-DD-HH-II-SS.txt

    Metadata Format (inside text file):
    - YYYY-MM-DD-HH-II-SS, filetitle, number

    New Filename Format:
    - With filetitle: YYYY-MM-DD - filetitle (HH-II-SS).3gp
    - Without filetitle: YYYY-MM-DD - (HH-II-SS).3gp
    """
    if audio_filename.endswith(".3gp") and audio_filename.startswith("data-"):
        # Construct full paths
        audio_path = os.path.join(base_path, audio_filename)
        txt_filename = audio_filename.replace("data-", "").replace(".3gp", ".txt")
        txt_path = os.path.join(base_path, txt_filename)

        date_parts = audio_filename.replace("data-", "").replace(".3gp", "").split('-')[:3]
        date = '-'.join([part.zfill(2) for part in date_parts]).strip()

        time_parts = audio_filename.split('-')[-3:]
        time = '-'.join([part.zfill(2) for part in time_parts]).replace('.3gp', '').strip()

        # Check if the corresponding text file exists
        if os.path.exists(txt_path):
            # Extract metadata from the text file
            filetitle = extract_metadata(txt_path)
        else:
            # If the text file doesn't exist, use default values
            filetitle = ''

        # print(audio_filename, date, filetitle, time)

        # Format the new filename
        new_filename = format_new_filename(date, filetitle, time)

        # Construct the new audio file path
        new_audio_path = os.path.join(base_path, new_filename)

        # Copy the audio file to the new filename
        shutil.copy(audio_path, new_audio_path)

        # Retrieve the original modification time
        original_mtime = os.path.getmtime(audio_path)

        # Set the modification time of the new file to the original time
        os.utime(new_audio_path, (original_mtime, original_mtime))

        print(f"File copied: {audio_filename}  ===>  {new_filename}")
