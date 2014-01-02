# Used to create the database. User has to repeat his name 10 times, everytime after he sees the recording option

import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 2
training = 10

fileaddress = '/home/prathik/recordings/s1'

for Counter in range(0,training):

 WAVE_OUTPUT_FILENAME = fileaddress + '/' + str(Counter+1) + '.wav'
 p = pyaudio.PyAudio()

 stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

 print("* recording")

 frames = []

 for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

 print("* done recording")

 stream.stop_stream()
 stream.close()
 p.terminate()

 wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
 wf.setnchannels(CHANNELS)
 wf.setsampwidth(p.get_sample_size(FORMAT))
 wf.setframerate(RATE)
 wf.writeframes(b''.join(frames))
 wf.close()


