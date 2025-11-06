from moviepy.editor import TextClip, CompositeVideoClip, ColorClip
import random

facts = [
    "Rolls-Royce engines power most luxury jets and cars.",
    "Every Rolls-Royce car takes nearly 6 months to build.",
    "The iconic ‘Spirit of Ecstasy’ ornament was created in 1911.",
    "No two Rolls-Royce cars are exactly the same.",
    "Rolls-Royce paint colors can be customized to anything — even lipstick shades."
]

# Pick random fact
fact = random.choice(facts)

# Background color and text
bg = ColorClip(size=(1280, 720), color=(10, 10, 10), duration=10)
txt = TextClip(fact, fontsize=48, color='white', font='Arial-Bold', size=(1100, None), method='caption')
txt = txt.set_position('center').set_duration(10)

# Combine video
video = CompositeVideoClip([bg, txt])
video.write_videofile("video.mp4", fps=24)
