# Underwater-Image-Rest
Underwater Image Restoration

## Theory Behind This Project

Underwater images usually are very poorly visible, due to various absorption and scattering effects. The goal of this project is to restore the images as it would look in bright daylight instead of looking hazy submerged.

## The Process

1. White Balancing is first corrected where it takes in individual RGB channels and corrects each of them. This is done since most of the underwater images have greenish blue tint augmented over their original colour. 
2. Unsharp Masking is the process of sharpening the image by blending a blurred version of the image with itself. 
3. Gamma Correction

## Sample Outputs
Input
![Input](https://github.com/keshav99/Underwater-Image-Rest/blob/master/7.jpg)

Output
![Output](https://github.com/keshav99/Underwater-Image-Rest/blob/master/result6.jpg)
