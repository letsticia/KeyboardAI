# KeyboardAI

A virtual keyboard based on Artificial intelligence

# Requirements

If you're using a virtual environment, activate it first. Then, install the required packages using the following command:

```bash
pip install -r requirements.txt
```

# Usage

To run the program, execute the following command:

```bash
python main.py
```

# About the project

This is a virtual keyboard that uses the webcam to detect the user's hand and track the movement of the fingers. The program uses the [MediaPipe](https://mediapipe.readthedocs.io/en/latest/solutions/hands.html) library to detect the hand landmarks and [OpenCV](https://opencv.org/) to process the video feed. The index finger is used like a cursor, making the keys dark. To press a key, the user must
put the thumb and index tips together. The program will then type the corresponding letter on whatever text field is currently selected.
