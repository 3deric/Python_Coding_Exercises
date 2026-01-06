from PIL import Image, ImageFilter, ImageDraw
import os
import sys

#loops through all images files in a specific folder
#resizes the images to a specified resolution
#applies a blur filter to the background, in case the image does not fit the aspect ratio

#OutputResolution
out_width = 1920
out_height = 1080

def resize_blur(file, export_dir):
    print(file)
    img = Image.open(file)
    #Calculate percentage difference
    h_percent = (out_height / float(img.size[1]))

    #Change width based on percentage difference
    w_size = int((float(img.size[0]) * float(h_percent)))

    #resize image
    img = img.resize((w_size, out_height), Image.Resampling.LANCZOS)

    #copy image for background blur
    #resize image for backgroudn blur
    w_percent = (out_width/float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))

    blur_img = img.resize((out_width, h_size), Image.Resampling.LANCZOS)
    v_crop = (int(blur_img.size[1]) -1080 )/2
    blur_img = blur_img.crop((0,0+v_crop,1920,blur_img.size[1]-v_crop))

    #blur image for background
    blur_img = blur_img.filter(ImageFilter.GaussianBlur(10))

    #compose foreground image over background
    out_img = blur_img
    offset = int((1920 - img.size[0]) / 2)
    out_img.paste(img, (offset,0))

    #add original filename as a watermark on the image
    draw = ImageDraw.Draw(out_img)
    text = os.path.basename(file)
    draw.text((5, 5), text, align="left")

    new_filename = os.path.basename(file).split('.')[0] + '_converted.jpg'
    out_img.save(export_dir + new_filename)
  
#get all images of type jpg and apply filters
def convert_images(dir):
    export_dir = dir + 'converted/'
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
    for file in os.listdir(dir):
        print(file)
        if file.endswith('.jpg') or file.endswith('.jpeg'):
            resize_blur(dir + file, export_dir)

if __name__ == '__main__':
    dir = sys.argv[1]
    convert_images(dir)

