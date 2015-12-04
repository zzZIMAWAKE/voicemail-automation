import pyaudio
import wave
import sys
import datetime

CHUNK = 1024

# play the wav file
def playfile(wf):
	p = pyaudio.PyAudio()

	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
	                channels=wf.getnchannels(),
	                rate=wf.getframerate(),
	                output=True)

	data = wf.readframes(CHUNK)

	while data != '':
	    stream.write(data)
	    data = wf.readframes(CHUNK)

	stream.stop_stream()
	stream.close()

	p.terminate()


# TODO: open lync and maximise window.

# TODO: use co-ordinates to click on the correct numbers to work our way through the menu

# date will always be in format 01 / 02 ... 31
# files should be named in the same way e.g. day-01.wav month-01.wav
d = datetime.date.today()
month = '{:02d}'.format(d.month)
day   = '{:02d}'.format(d.day)

filename = wave.open('audio_files/initial-greeting.wav', 'rb')
playfile(filename)
filename = wave.open('audio_files/day-' + day + '.wav', 'rb')
playfile(filename)
filename = wave.open('audio_files/month-' + month + '.wav', 'rb')
playfile(filename)
filename = wave.open('audio_files/after-date.wav', 'rb')
playfile(filename)
filename = wave.open('audio_files/if-urgent.wav', 'rb')
playfile(filename)

# TODO: click # then 1 in lync to finish, and save your message. Close lync and be free from the corporate powers