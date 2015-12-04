import pyaudio
import wave
import sys
import datetime

CHUNK = 1024

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
