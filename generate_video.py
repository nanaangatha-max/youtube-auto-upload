from moviepy.editor import *

# Create video from image and audio/text
image = ImageClip("rolls.jpg").set_duration(10)  # 10 sec image video
text = TextClip("Interesting Facts About Rolls Royce", fontsize=50, color='white')
text = text.set_position('center').set_duration(10)

video = CompositeVideoClip([image, text])
video.write_videofile("video.mp4", fps=24)
