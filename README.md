### Object Detection and Classification with 3D Tracking

This project employs methods for visual perception to detect, classify and track objects on a conveyor belt even under occlusions.
While the object detection and tracking methods are based on classical image processing approaches aided with Kalman Filter for state estimation, we have used Convolutional Neural Networks for the multiclass Obejct Classification.

## Overview and Setup

1. Clone the repository
2. Obtain the Data files pertaining to the video sequence with and without occlusions from <link>
3. Run the notebook Tracking_wOcclusions.ipynb
4. Calibrate the camera and get the parameters.
5. Rectify and Undistort the video sequence.
6. Load the video sequence frame by frame
7. Employ Background Subtraction and Morphology Operations to detect Object
8. Classify the Object with pre-trained CNN Model
9. Perform State Estimation using Kalman Filter
10. Calculate Disparity and Depth for each frame and display along with tracking coordinates
