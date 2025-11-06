from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import os
import random
    
# --- Step 1: Generate a random fact ---
facts = [
    "Rolls Royce cars are so quiet that engineers add artificial noise for safety.",
    "Each Rolls Royce engine takes over 2 months to build by hand.",
    "The Spirit of Ecstasy ornament can automatically retract to prevent theft.",
    "The paint on some Rolls Royce cars contains real diamond dust.",
    "Every Rolls Royce has an umbrella hidden in the door for luxury convenience."
]

fact = random.choice(facts)
print("Selected fact:", fact)

# --- Step 2: Convert text to speech ---
tts = gTTS(text=fact, lang='en')
tts.save("voice.mp3")

# --- Step 3: Create video from image + audio ---
image = "rolls.jpg"  # add an image file in repo
clip = ImageClip(image).set_duration(10)
audio = AudioFileClip("voice.mp3")
clip = clip.set_audio(audio)

# --- Step 4: Export final video ---
clip.write_videofile("final_video.mp4", fps=24)
print("🎬 Video created successfully!")
