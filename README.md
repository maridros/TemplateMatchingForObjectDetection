# TemplateMatchingForObjectDetection
Object detection with template matching after adding different noise levels and comparison with the results obtained when a smoothing filter is applied before the template matching.
## Requirements
- Python
- OpenCV
- Numpy
## Results of the code
The image and the template image that were used are in the folder InputData. The goal was to detect the object of the template image in the original image after adding different noise levels. The result for each noise level is the following:
![noise](https://user-images.githubusercontent.com/89779679/132470753-b67b5966-efb2-40ca-a459-b00cbfe590ed.jpg)

It seems that after 10% noise not all objects corresponding to the template are detected. The same process is repeated, but this time a smoothing filter is applied before the template matching process. The results are the following:
![noise_blur](https://user-images.githubusercontent.com/89779679/132471320-ffa9a090-b4ef-46d9-89b9-203b60a1e630.jpg)

According to the results the smoothing filter deals with the noise, so that the template matching is effective even in case of 20% noise.
