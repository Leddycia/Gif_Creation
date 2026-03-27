# Let's make a Super Gif
import imageio.v2 as imageio

filenames = ['team-pic1.png', 'team-pic2.png'] # Files Path
images = [] # image files

for filename in filenames:
  images.append(imageio.imread(filename))

imageio.mimsave('team.gif', images, duration = 1) # Finally the Gif

# That's it!!!
