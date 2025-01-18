import pyaudio
import wave

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
frames = []

for i in range(0, int(44100 / 1024 * 5)):
    data = stream.read(1024)
    frames.append(data)

stream.stop_stream()
stream.close()
audio.terminate()

wf = wave.open('output.wav', 'wb')
wf.setnchannels(1)
wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)
wf.writeframes(b''.join(frames))
wf.close()

audio = pyaudio.PyAudio()
wf = wave.open('output.wav', 'rb')

stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

data = wf.readframes(1024)
while data:
    stream.write(data)
    data = wf.readframes(1024)

stream.stop_stream()
stream.close()
audio.terminate()
