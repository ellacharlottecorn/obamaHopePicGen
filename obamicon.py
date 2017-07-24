from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76) #(<182)
red = (217, 26, 33) #(between 182 and 364),
lightBlue = (112, 150, 158) #(between 364 and 546),
yellow = (252, 227, 166) #(>546)

# Import image.
my_image = Image.open("IMG_3330.JPG") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.
my_image.show()

# change pic colors
recolored = [] #list that will hold the pixel data for the new image.

for pixel in image_list:
    red = pixel[0]
    blue = pixel[1]
    green = pixel[2]
    pixIntense = red + blue + green
    if pixIntense <= 182:
        recolored.append((0, 51, 76))
    elif 182 < pixIntense <= 364:
        recolored.append((217, 26, 33))
    elif 364 < pixIntense <= 546:
        recolored.append((112, 150, 158))
    elif pixIntense > 546:
        recolored.append((252, 227, 166))


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
