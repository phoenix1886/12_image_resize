# Image Resizer
This script is designed for resizing images.

It requires python3.5, side packages can be installed using requirements file using the following command:
```
python pip install -r requirements.txt
```

Script takes 5 arguments:
* path (positional): path to original image user wants to resize
* --width (optional): desired width of an image
* --height (optional): desired heigh of an image
* --scale (optiona): desired scale of resize
* --output (optional): path for saving the output image

For succesful resizing user can give height or width of scale factor. One of these arguments will be enough for resizing. If user gives both scale and dimension parameters (width|heigt), script will break. If user gives both heigh and width, resize operation can change ratio of an image, so if ratio changed, ther will be a warning about it.

Output argument is optional, so if empty, output will be saved to current location. 

## How to run
```
python image_resize.py 'pic.jpg'  --height 300 --width 300
Beware! Ratio of image changed!
```
Output image 'pic_300x300.jpg' was saved to current directory.


```
python image_resize.py 'pic.jpg'  --scale 2 'Users/double_pic.jpg'
```
Output image will be saved to Users/double_pic.jpg'.


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
