import imageio.v3 as iio

#In our Python program, we'll create a list that contains the locations of the image files. We also need to create an empty list that will be used to store the actual image data from these files.
filenames = ['team-pic1.png', 'team-pic2.png']
images = []

# Next, let’s use a for loop to go through the file paths and read the images using imageio library’s .imread() method:
for filename in filenames:
  images.append(iio.imread(filename))

# Lastly, let’s use the .imwrite() method to turn the images into a GIF:
iio.imwrite('team.gif', images, duration = 500, loop = 0)