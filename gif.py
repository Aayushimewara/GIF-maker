import imageio.v3 as iio
filenames = ['team-pic1.png', 'team-pic2.png']#pictures
images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))
iio.imwrite('team.gif', images, duration = 500, loop = 0)