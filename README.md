# Tangerine ~ OSS Hackathon @ Cornell Tech

## Problem
Whenever I attend a networking panel, I'm often overwhelmed by the amount of insight shared by the panel speakers and struggle to maintain meaningful connections with fellow audience members. These two pain points make networking much harder than it needs to me, which is why I've individually developed a solution to this problem. 

## Solution
What if the interviewer was able to toss their phone aside on a coffee table (close to the panel speakers), and have a Speech2Text model that delivers valuable insights into a discord community for the audience to reference later on? I developed an IOS application that records dialogues, parses this information into text using Python's Speech to Recognition (I couldn't use Whisper because at that time I didn't have any more API credits), and then pass this information into GPT3.5 Turbo to summarize key insights from these lengthy dialogues. I then used the Discord API to send over these key insights into a private discord channel that is only accessible to 1 audience member at a time. This way, they can write back to the discord bot about additional notes without having to share this personal informaiton in a public channel accessible to everyone. 

I like to think of this application as a magic notebook/XYZ MeetingGPT that I can constantly interact and learn from weeks after a networking event has occurred. 

## Future Work
I was planning on generating a new server link every time a Cal.com invitation is sent from the interviewer to the panel speakers to decide a common time. This link would be later shared with participants either through Partiful or by manually sharing it with the audience once they enter the room. I wanted to automatically create this guild/server room for every meeting because this is the fastest way to build a community, and allow audience members to share valuable links in different channels and already have everyone's contact information without having to ask everyone in the room by themselves. Unfortunately I couldn't fork this specific Cal.com feature because of time constraints, but I definitely plan on continuing this part of the project after my hackathon and understanding Cal's documentation in detail. 

Since this was a 1 person team effort, I couldn't stream my dialogue data and instead had to pass in the audio once it was done recording, which isn't ideal since the Speech-Recognition model would read all this at once, which takes a lot of time. 


