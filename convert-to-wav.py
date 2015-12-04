from pydub import AudioSegment
import os

# convert all m4a files to wav
files_in_dir = os.listdir('/Users/nick/personal/voicemail-automation/audio_files')
for file_in_dir in files_in_dir:
	if "m4a" not in str(file_in_dir): 
    		continue
	print file_in_dir
	filename = file_in_dir.replace('.m4a', '')
	m4a = AudioSegment.from_file(filename + ".m4a", format="m4a")
	m4a.export(filename + ".wav", format="wav")