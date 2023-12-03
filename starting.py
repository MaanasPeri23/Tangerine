import os
import speech_recognition as sr
from pydub import AudioSegment

def convert_m4a_to_wav(input_file, output_dir):
    # Load the M4A file
    audio = AudioSegment.from_file(input_file, format="m4a")

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Export as WAV
    output_file = os.path.join(output_dir, "converted_audio.wav")
    audio.export(output_file, format="wav")

    return output_file

def convert_audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

        try:
            # Using Google Web Speech API for speech recognition
            text = recognizer.recognize_google(audio_data)
            print("Text from audio: ", text)
            return text
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            return None

if __name__ == "__main__":
    audio_file_path = "/Users/maanasperi/Library/Developer/CoreSimulator/Devices/5FDEFAFB-B97C-496C-AB9C-6AC45E8EA8E7/data/Containers/Data/Application/29326FD7-78D0-40E7-B232-D7921AE053B0/Documents/CO-Voice : 02-12-23 at 22:38:11.m4a"
    desired_output_path = "/Users/maanasperi/Desktop/Desktop - Maanas’s MacBook Pro/Cornell/Hackathon Stuff"
    
    converted_audio_path = convert_m4a_to_wav(audio_file_path, desired_output_path)
    convert_audio_to_text(converted_audio_path)
