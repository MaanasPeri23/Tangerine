import os
import speech_recognition as sr
from pydub import AudioSegment
from openai import OpenAI
import dotenv

dotenv.load_dotenv()

import discord
from discord.ext import commands 

intents = discord.Intents.default()
intents.members = True
intents.guilds = True  # Enable the guilds intent
intents.messages = True  # Enable the messages intent
intents.guild_messages = True  # Enable the guild messages intent

bot = commands.Bot(command_prefix='!', intents=intents)
global analysis

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # obj = bot.get_all_channels()
    # for channel in obj:
    #     print(f'Channel Name: {channel.name}, Channel ID: {channel.id}')
    # print(bot.get_all_channels())
    channel = bot.get_channel(1180954470595706890)
    await channel.send(analysis)
    print("done")



@bot.command()
@commands.has_permissions(create_instant_invite=True)
async def create_guild(ctx):
    # Replace 'Your Guild Name' with the desired name for your guild
    guild_name = 'Your Guild Name'

    try:
        # Creating a new guild
        new_guild = await bot.create_guild(name=guild_name)

        # Constructing an invite link for the new guild
        invite_link = await new_guild.create_invite()

        # Sending a message with the invite link
        await ctx.send(f"Guild '{guild_name}' created successfully! Invite link: {invite_link}")
        print(invite_link)
        
    except discord.HTTPException as e:
        # Handling exceptions if guild creation fails
        await ctx.send(f"Failed to create guild. Error: {e}")

def keyInsights(raw_text): 
    client = OpenAI()
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful secretary who takes lots of raw dialogues and generates the most insightful summaries and key takeaways that helps the user interact with this more"},
            {"role": "user", "content": raw_text}
        ]
    )
    insights = completion.choices[0].message.content
    return insights

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
            # print("Text from audio: ", text)
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
    
    # converted_audio_path = convert_m4a_to_wav(audio_file_path, desired_output_path)
    # raw_text = convert_audio_to_text(converted_audio_path)
    # analysis = keyInsights(raw_text)
    # print(analysis)

    bot.run(os.getenv("BOT_TOKEN"))


