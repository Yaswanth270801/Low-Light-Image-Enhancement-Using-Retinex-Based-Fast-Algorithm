Low Light Enhancement Using Retinex-Based Fast Algorithm:

I have used Python 3.9 with technology OpenCV by using OpenCv2 and math libraries to implement the algorithm.

How to run my project:

Run python sourceCode.py by changing to directory in which source code.py  in the editor in which you are using to execute. Don't terminate the process until cdf value prints in the console for all input images given. We get one cdf value each input image  

Objective:

The objective of this project is to enhance low-light images by extensively increasing brightness and contrast using a Retinex-Based Fast Algorithm (RBFA). "The project builds on established Retinex theory to restore detail and enhance visual quality in images captured in low-light conditions, while introducing several new enhancements and optimizations for better performance.

Project Overview:
This project is based on the Retinex-based fast algorithm for low-light image enhancement as described in a published paper by Liu et al. (2021). The approach involves enhancing low-light images using:
1. Conversion to HSV color space.
2. Dynamic range stretching of the V (value) component.
3. Illumination estimation via adaptive gamma correction.
4. Brightness enhancement using the Retinex model.
5. Dynamic range expansion for improved contrast.
6. Saturation adjustment for natural color rendering.
7. Conversion back to RGB for final output.
The project introduces new modifications and extensions that improve upon the original method.


Algorithms Used:

1. Retinex Model
The algorithm utilizes Retinex theory to decompose an image into its illumination and reflectance components, simulating the way how human vision interprets scenes under varying lighting conditions, and incorporates gamma correction for further enhancement of brightness and contrast.

2. Gamma Correction
A nonlinear method for adjusting image brightness that employs a dynamically computed gamma parameter, allowing for adaptive enhancement of low-light areas.

3. HSV Color Space Transformation
The image is processed in the HSV color space, focusing on enhancing the V (Value) component to modify brightness while preserving hue and saturation.

4. Dynamic Range Expansion
Applied after brightness enhancement to expand pixel intensities over a wider range, avoiding excessive clustering in the brighter areas.

5. Saturation Adjustment
Maintains a balance between color saturation and brightness adjustments to prevent colors from appearing washed out in the enhanced image.


Extensions and Additional Features:
The project introduces several new extensions and additional features beyond what was described in the original paper

1. Integration of Noise Reduction Techniques:
A noise reduction step utilizing median filtering has been incorporated before the Retinex-based enhancement to remove noise in low-light images. This step helps in producing cleaner outputs, especially for images with a high amount of noise in dark regions. 

2. Automatic Parameter Tuning:
An automated method for calculating parameters, including gamma values, weights, and thresholds, has been implemented based on the image histogram and contrast levels. This extension allows the algorithm to adapt more effectively to different lighting conditions and image characteristics. 

3. Multi-Scale Retinex Option:
Support for multi-scale Retinex processing has been introduced, allowing for simultaneous enhancement of images at various scales. This feature offers greater flexibility for applications that prioritize the preservation of fine details.

4. Edge Preservation Techniques:
Edge-preserving filters, including bilateral filtering, have been integrated into the enhancement process to retain sharpness and prevent edge blurring.

5. Histogram Matching Post-Processing
Following the enhancement, histogram matching is performed to ensure the output images exhibit a more natural appearance. This step helps mitigate artifacts and over-enhancement, particularly in areas with significant brightness enhancement.

6. Enhanced Saturation Adjustment:
The saturation adjustment technique has been refined to consider local variations, enabling more accurate corrections in various regions of the image.

7. Adaptive Dynamic Range Compression:
An optional step has been introduced for adaptive compression of the dynamic range in regions with high contrast, minimizing the risk of overexposure and preserving details in bright areas.



Modifications from the Original Paper:

This project enhances the techniques presented in the original paper through various modifications and optimizations.
1. Dynamic Gamma Parameter Adjustment:
Rather than relying on a static gamma calculation, the parameter is dynamically adjusted based on the mean intensity of the V component and the histogram distribution. This adaptation allows the algorithm to perform effectively across a broader range of low-light conditions.

2. Optimized Saturation Adjustment Method:
The saturation adjustment formula has been improved to incorporate a blend of global and local image statistics, leading to better color preservation and enhanced visual appearance.

3. Noise Reduction Integration:
A pre-processing step for noise reduction has been introduced, which was absent in the original paper. This addition enhances the quality of the output, especially for images that contain significant noise.

4. Multi-Scale Retinex Processing:
An option for multi-scale Retinex processing has been included, allowing for varying levels of detail enhancement in images. This serves as an extension to the single-scale approach utilized in the original paper.

5. Additional Dynamic Range Compression:
A dynamic range compression technique has been integrated to tackle extreme contrast issues that the original algorithm did not address.

Implementation Details:
1. Programming Language: Python 3.9
2. Libraries Used:
OpenCV (cv2): For image processing functions.
math: For array and mathematical operations.

Key Classes and Functions:

1. Class RBFAlgorithm
Manages the image enhancement process, including pre-processing, enhancement, and post-processing steps.

2. Additional Functions for Extensions
applyNoiseReduction(): Reduces noise in the original image.
applyMultiScaleRetinex(): Provides multi-scale enhancement based on different levels of detail.
applyEdgePreservingFilter(): Preserves edge details while enhancing brightness and contrast.
adjustDynamicRange(): Dynamically compresses the range in very bright areas.
applyHistogramMatching(): Matches the histogram of the enhanced image to that of a reference distribution for natural appearance.

**Evaluation Metrics**:

- **Quantitative Metrics**:
    - **Mean Squared Error (MSE)**: Measures the average squared difference between the input and enhanced images.
    - **Entropy**: Quantifies the amount of information or detail present in the image before and after enhancement.
    - **Peak Signal-to-Noise Ratio (PSNR)**: Evaluates the quality of the enhanced image compared to the input.
    - **Structural Similarity Index (SSIM)**: Measures structural similarity between the input and output images, reflecting how closely the enhanced image resembles the original.
    - **Delta E (Color Difference)**: Assesses the perceptual color difference between the input and enhanced images.
    - **Histogram Similarity**: Compares the pixel intensity distribution of the input and enhanced images.

- **Visual Comparison**
    - **Histogram Analysis**: Visualizes the pixel intensity distribution of input and output images to observe the dynamic range expansion and contrast improvements.
    - **Image Brightness and Contrast**: Evaluates how well the brightness and contrast are improved while preserving details.

- **Aspects of Evaluation**
    - **Robustness**: The algorithm was tested across a variety of low-light images to ensure consistent performance under diverse conditions (e.g., noise levels, lighting variations). Noise reduction techniques and multi-scale Retinex processing helped enhance robustness.
    - **Privacy**: The algorithm was designed to process images locally on the user's device, ensuring no image data is transmitted to external servers, thereby preserving privacy.
    - **Fairness**: The algorithm does not favor specific types of images or scenes. Its adaptive parameter tuning ensures uniform enhancement across various lighting conditions and image types.


References:
Liu, S., Long, W., He, L., Li, Y., & Ding, W. (2021). Retinex-Based Fast Algorithm for Low-Light Image Enhancement. Entropy, 23(6), 746. DOI:10.3390/e23060746.
OpenCV Library: https://opencv.org/








