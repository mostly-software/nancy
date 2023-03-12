import pyaudio
import wave
import speech_recognition as sr
import gtts
from playsound import playsound 
from AppOpener import open as op
command = ""

def record_command():
    chunk = 1024
    sample_format = pyaudio.paInt16 
    channels = 2
    fs = 44100  
    seconds = 5
    filename = "command.wav"
    p = pyaudio.PyAudio()

    print('Awaiting a command...')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = [] 

    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    print('Finished recording command')

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcribe_command():
    global command
    recognizer = sr.Recognizer()
    with sr.AudioFile("command.wav") as source:
        audio = recognizer.record(source)
        command = recognizer.recognize_google(audio)

def interpret_command():
    global command
    if command.lower() == "please open discord kitten":
        print("===================")
        print("Opening Discord...")
        op("discord")
    elif command.lower() == "am i a good little gamer":
        print("===================")
        tts = gtts.gTTS("You are a good little gamer")
        tts.save("encouragement.mp3")
        playsound("encouragement.mp3")
    elif command.lower() == "open apex":
        print("===================")
        op("apex legends")
       


record_command()
transcribe_command()
interpret_command()
