# Bilateral Filtering

**Bilateral filtering is a non-linear, edge-preserving smoothing filter that can reduce noise while preserving the edges in an image.
It is particularly useful in situations where traditional smoothing filters, such as Gaussian blurring, might result in a loss of important edge information.
Bilateral filtering achieves this by taking into account both the spatial closeness and intensity similarity of pixels.**


-->      In OpenCV, the cv2.bilateralFilter function is used to apply bilateral filtering to an image. 
-->      cv2.bilateralFilter: This function takes the input image (gray in this case), the diameter of each pixel neighborhood (d), the standard deviation 
         of the color space (sigmaColor), and the standard deviation of the coordinate space (sigmaSpace). 
-->      Adjusting these parameters allows you to control the extent of smoothing and the preservation of edges.
-->      d: Diameter of each pixel neighborhood. A larger d means that more distant pixels will influence each other.
-->      sigmaColor: Standard deviation of the color space. A larger value for sigmaColor means that pixels with a color
         different from the central pixel will have less influence on the smoothing.
-->      sigmaSpace: Standard deviation of the coordinate space. A larger value for sigmaSpace means that pixels farther away
         from the central pixel will have less influence on the smoothing.

### Original Noise Image
<img src="https://github.com/Prerak8880/OpenCV_Python-Basics/assets/96664052/9a6e041e-d234-40a5-8170-f33136e0f805" width="300" height="300">
<img src="https://github.com/Prerak8880/OpenCV_Python-Basics/assets/96664052/ad59fcf7-a296-4318-ac42-6c3b7e047ec1" width="300" height="300">


### Removed Noise Image(Using Bilateral_filtering)

<img src="https://github.com/Prerak8880/OpenCV_Python-Basics/assets/96664052/de437ede-926a-46d4-b797-5aa12446539a" width="300" height="300">
<img src="https://github.com/Prerak8880/OpenCV_Python-Basics/assets/96664052/df967ac8-2f3d-444b-b5bf-14b3d299e799" width="300" height="300">
