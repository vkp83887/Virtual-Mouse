# VIRTUAL-MOUSE

This Python code uses the OpenCV library and the cvzone.HandTrackingModule to create an interactive image viewer application with hand gestures. Here's a breakdown of the code in points:

1. Import necessary libraries:
    i. cv2: OpenCV library for computer vision tasks.
    ii. os: Operating system module for file and folder handling.
    iii. HandDetector from cvzone.HandTrackingModule: A custom hand tracking module that simplifies hand detection and gesture recognition.
    iv. numpy as np: NumPy library for numerical operations.

2. Define constants:
    i. width and height: Set the width and height of the video capture window.
    ii. cap: Initialize the video capture object (camera) with the specified width and height.
    iii. folderpath: Specify the folder path where images for the interactive viewer are stored.
    iv. pathImages: Get a list of image filenames in the specified folder.
        hs and ws: Define the height and width for the small image (displayed on the right).

3. Create a HandDetector object:
    i. Initialize a hand detection object with parameters like detectionCon (detection confidence) and maxHands (maximum number of hands to detect).

4. Initialize variables for gesture recognition:
    i. imgnum: Track the currently displayed image index.
    ii. gestureThreshold: A threshold used for gesture recognition.
    iii. buttonpressed: Tracks if a button press gesture is detected.
    iv. pressedCounter: Counts the duration of a button press.
    v. buttondelay: Sets a delay for button presses.
    vi. annote_list: A list to store annotation points for drawing.
    vii. annote_num: Tracks the current annotation being drawn.
    viii. annote_start: Tracks if an annotation drawing has started.

5. Start a continuous loop for video capture and gesture recognition:
    i. success, img = cap.read(): Capture a frame from the camera.
    ii. img = cv2.flip(img, 1): Flip the image horizontally (mirror effect).

6. Handle hand tracking and gesture recognition:
    i. Use the detector.findHands method to detect hands in the frame.
    ii. Draw a green line as a threshold for gesture recognition.
    iii. Check for various hand gestures:
           ->Left and right swipes to navigate through images.
           ->Pointing gesture for highlighting a point.
           ->Drawing gesture to annotate the image.
           ->Erasing gesture to remove the last annotation.

7. Handle button press logic:
    i. Track the duration of a button press and reset it after a delay.

8. Draw annotations on the image:
    i. Iterate through the annotation lists and draw lines between points to create annotations.

9. Display the small image (thumbnail) on the right side of the main image.

10. Use cv2.imshow to display the images, and cv2.waitKey to wait for a key press.

11. The main loop continues until the 'q' key is pressed, at which point the application exits.

Created with Python, this code showcases a mesmerizing image viewer. Experience the joy of navigating through images effortlessly while adding a personal touch through hand-drawn lines. And here's the best part - with a simple hand gesture, you can erase those annotations using the power of your webcam. Get ready for an interactive journey like no other.The main functionality relies on hand tracking and gesture recognition, making it an interactive and engaging application for viewing and annotating images.
