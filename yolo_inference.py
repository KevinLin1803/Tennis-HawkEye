# Used to detect the objects
    # Questions to answer: Why did we choose YOLO? Why did we choose this particular AI model?
    # What are tensors?

# Goal: adjust the code a little bit
from ultralytics import YOLO

model = YOLO('models/yolov5ball.pt')

result = model.predict('input_videos/input_video.mp4', save=True)

for box in result[0].boxes:
    print(box)

# then I think we use pytorch to train to identify key points?

# Imported something from Yolo to determine stuffs :3
# Then other things