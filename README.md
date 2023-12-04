# Tangerine ~ OSS Hackathon @ Cornell Tech

## Problem
Whenever I attend a networking panel, I'm often overwhelmed by the amount of insight shared by the panel speakers and struggle to maintain meaningful connections with fellow audience members. These two pain points make networking much harder than it needs to be, which is why I've individually developed a solution to this problem. 

## Solution
What if the interviewer was able to toss their phone aside on a coffee table (close to the panel speakers), and have a Speech2Text model that delivers valuable insights into a discord community for the audience to reference later on? I developed an IOS application that records dialogues, parses this information into text using Python's Speech to Recognition (I couldn't use Whisper because at that time I didn't have any more API credits), and then passes this information into GPT3.5 Turbo to summarize key insights from these lengthy dialogues. I then used the Discord API to send over these key insights into a private Discord channel that is only accessible to 1 audience member at a time. This way, they can write back to the discord bot about additional notes without having to share this personal information in a public channel accessible to everyone. 

I like to think of this application as a magic notebook/XYZ MeetingGPT that I can constantly interact with and learn from weeks after a networking event has occurred. 

## Future Work
I was planning on generating a new server link every time a Cal.com invitation is sent from the interviewer to the panel speakers to decide a common time. This link would be later shared with participants either through Partiful or by manually sharing it with the audience once they enter the room. I wanted to automatically create this guild/server room for every meeting because this is the fastest way to build a community, and allow audience members to share valuable links in different channels and already have everyone's contact information without having to ask everyone in the room by themselves. Unfortunately, I couldn't fork this specific Cal.com feature because of time constraints, but I plan on continuing this part of the project after my hackathon and understanding Cal's documentation in detail. 

Since this was a 1 person effort (not including GPT), I couldn't stream my dialogue data in time and instead had to pass in the audio once it was done recording, which isn't ideal since the Speech-Recognition model would read all this at once, which takes a lot of time. 

## Demo as of December 3rd: 
### Step 1: IOS App Screenshots 
![simulator_screenshot_BF409A62-C381-4409-B1E5-378935CE857F](https://github.com/MaanasPeri23/Tangerine/assets/43656322/46c1eb41-5800-4952-9fed-c51ec2f41f27 | width=200) 
![simulator_screenshot_8DFC23C5-CFB2-4316-B3EA-E38E13F386CB](https://github.com/MaanasPeri23/Tangerine/assets/43656322/ec59b12c-0182-4806-a8c2-5ab4bf681b47 | width=200)


### Step 2: OUTPUT of Speech to Text Results: 
"Text from audio:  begin today that's all the notes said there was no indication from where it came or who may have written it had it been meant for someone else Megan looked around the room but nobody made eye contact back for a brief moment she thought it might be a message for her to follow her dreams but ultimately decided it was easier to ignore it as she crumpled it up and threw it away"

### Step 3: OUTPUT of GPT Key Insights from Audio Text
"ChatCompletionMessage(content='Summary: Megan discovers a note without any clear source or intended recipient. She considers the possibility that it could be a message for her to follow her dreams but ultimately chooses to ignore it, dismissing it as an insignificant message.\n\nKey takeaways:\n1. Megan finds a note without any identifiable origin or recipient.\n2. The note does not provide any indication of its purpose or intended audience.\n3. Megan briefly entertains the idea that the note may be encouraging her to pursue her dreams.\n4. However, she ultimately chooses to disregard the note and throws it away.', role='assistant', function_call=None, tool_calls=None)"

### Step 4: Sending message on Discord Screenshot
<img width="835" alt="Screenshot 2023-12-04 at 5 26 01 PM" src="https://github.com/MaanasPeri23/Tangerine/assets/43656322/ee6af4d5-96d3-4afa-b757-abc3c405dce0">

## Citations (coming soon) 
Although this was a open-source hackathon I will still be referring to all the helpful resources that I used to build this  







