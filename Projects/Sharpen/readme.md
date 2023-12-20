# How is **Sharpening** being done?
  * So the basic idea is to use the cv2.addWeighted() function to combine 2 images.
  * In the same as we use cv2.add() function while combining 2 different images.
  * First we will take the original image and other the same image we will process it with the cv2.GaussianBlur().
  * Then we will combine both of them and the resultant image is shown below.

## cv2.addWeighted(img_1, Trnsp_level, img_2, trnsp_level, brigh_level)
  * This function contains 5 arguments.
      -  arg-1: Image_1 source
      -  arg-2: Transparency level of Image_1(must be b/w **0-1**)
      -  arg-3: Image_2 source
      -  arg-4: Transparency level of Image_2(must be b/w **0-1**)
      -  arg-5: Brightess Level

## Sharpening 
**-->    Sharpening is a common image processing technique used to enhance the edges and details in an image.
-->      OpenCV, a popular computer vision library, provides functions to perform image sharpening.**

### Original Image

![1](https://github.com/Prerak8880/OpenCV_Python-Basics/assets/96664052/6d9bb323-a6bf-43c7-8e27-f485feafc950)

### Sharpened Image
![4](https://github.com/Prerak8880/OpenCV_Python-Basics/assets/96664052/aba82a8e-a785-4416-972b-ef1abbcdd749)
