import random
from gtts import gTTS
from moviepy.editor import *

# 1️⃣ Rolls Royce Facts List
facts = [
    "Rolls Royce cars are so quiet, engineers had to add fake engine sounds for drivers to feel movement.",
    "Each Rolls Royce is handcrafted, taking up to six months to build.",
    "The Spirit of Ecstasy ornament can automatically hide to prevent theft.",
    "Rolls Royce uses special paint that can take over 20 coats for perfection.",
    "The iconic Rolls Royce grille is made and polished entirely by hand."
]

# 2️⃣ Pick a random fact
fact = random.choice(facts)
print("🎙️ Fact selected:", fact)

# 3️⃣ Convert fact to speech
tts = gTTS(fact)
tts.save("voice.mp3")

# 4️⃣ Create background video or image
clip = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=10)  # plain black background

# 5️⃣ Add text overlay
txt_clip = TextClip(fact, fontsize=50, color='white', size=(1000, None), method='caption')
txt_clip = txt_clip.set_position('center').set_duration(10)

# 6️⃣ Add audio and combine
audioclip = AudioFileClip("voice.mp3")
final_clip = CompositeVideoClip([clip, txt_clip])
final_clip = final_clip.set_audio(audioclip)

# 7️⃣ Export video
final_clip.write_videofile("video.mp4", fps=24)

print("✅ Video generated successfully: video.mp4")
