# Voice Recorder File Renamer

This Python script is designed to process audio files exported by an Android voice recorder app (tokasiki voicerecorder). For each recording, it looks for an associated text file containing metadata and copies the audio file with a new filename based on extracted date, filetitle, and time information. If the text file is missing, the new filename is generated without the optional filetitle field. The original modification time of the file is preserved for the copied file.

## Usage

1. Clone or download this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/voice-recorder-renamer.git
   ```

2. Ensure you have Python installed on your machine.

3. Open a terminal and navigate to the project directory.

   ```bash
   cd voice-recorder-renamer
   ```

4. Run the script.

   ```bash
   python renamer.py
   ```

   The script will iterate through each audio file in the specified directory, extract metadata from the corresponding text file, and copy the audio file with a new filename. If the text file is missing, the new filename is generated without the optional filetitle field.

## Directory Structure

- The script assumes a directory structure where audio files (extension '.3gp') have names starting with 'data-' and corresponding text files have similar names but with '.txt' extension.

### Filename Format

- Audio file: `data-YYYY-MM-DD-HH-II-SS.3gp`
- Text file: `YYYY-MM-DD-HH-II-SS.txt`

### Metadata Format (inside text file)

- `YYYY-MM-DD-HH-II-SS, filetitle, number`

### New Filename Format

- With filetitle: `YYYY-MM-DD - filetitle (HH-II-SS).3gp`
- Without filetitle: `YYYY-MM-DD - (HH-II-SS).3gp`

## Author

- Teodor Muraru

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
