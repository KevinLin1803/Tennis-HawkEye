# Tennis-Hawkeye

## Introduction
This project simulates the tennis hawkeye system, analysing player speeds and shots. Players and tennis balls are detected using the YOLOv8 and YOLOv5 models respectively. Keypoints on the court are extracted using CNNs.

## Method Summary
The YOLOv5 model was trained on a tennis ball dataset to improve accuracy. A pre-trained YOLOv8 model was used to track the players. Pytorch was used to create the CNN for keypoint detection and trained on a set of tennis courts, viewed from an aerial angle. Using these models, the videos were analysed frame by frame. The bounding box coordinates for the players, ball, and time between frames were used to calculate player and shot speed. 

## Technologies
- python
- ultralytics
- pytorch
- pandas
- numpy
- opencv

## Example Snapshot
![image](https://github.com/user-attachments/assets/a1f6c173-a977-4719-9c7c-1c472f38e193)
