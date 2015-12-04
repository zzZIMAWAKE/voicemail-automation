# Voicemail automation

## Setup

There are a few dependencies that can be set up easily using homebrew

### For converting to wav script
To begin with, install using either of the below commands, I found one didn't work for me so if you run in to problems use the other.

```bash
# libav
brew install libav --with-libvorbis --with-sdl --with-theora

####    OR    #####

# ffmpeg
brew install ffmpeg --with-libvorbis --with-ffplay --with-theora
```
Then:

	pip install pydub

### For the voicemail script

Nice and simple:

	brew install portaudio 
	pip install pyaudio

### MISC / Required files (audio)
All audio files must be in wav format. Store them in /audio_files within the project directory.

The naming conventions for your audio files should be:
For days:
	'day-01.wav' through to 'day-31.wav'
For months:
	'month-01.wav' through to 'month-12.wav'

You also need a generic messages described below:
	
	initial-greeting.wav : 'This is .... today is the'
	after-date.wav       : 'I'm in the office but unable to take your call'
	if-important.wav     : 'If it's something oh so urgent, call <some poor sap> on <#>'

Enjoy not having to talk through a really long script every morning.