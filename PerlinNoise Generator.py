import matplotlib.pyplot as plt
from random import seed
from random import randint
import noise 
from PIL import Image
import numpy as np
from perlin_noise import PerlinNoise

#Variables
randSeedInt = randint(100, 10000000) #you can change this to your liking

noise1 = PerlinNoise(octaves=6, seed=randSeedInt)
noise2 = PerlinNoise(octaves=12, seed=randSeedInt)
noise3 = PerlinNoise(octaves=24, seed=randSeedInt)
noise4 = PerlinNoise(octaves=48, seed=randSeedInt)
noise5 = PerlinNoise(octaves=96, seed=randSeedInt)
noise6 = PerlinNoise(octaves=196, seed=randSeedInt)

persistence = float(input("Enter A number For Persistence : "))


#specify image size
xpic = int(input("Enter number: "))
ypic = int(input("Enter number: "))
xpix, ypix = xpic, ypic
#generate noise
img = []

for i in range (xpix):
    row = []
    for j in range (ypix):
        noise_val = noise1([i/xpix, j/ypix])
        noise_val += 0.5 * noise2([i/xpix, j/ypix])
        noise_val += 0.25 * noise3([i/xpix, j/ypix])
        noise_val += 0.125 * noise4([i/xpix, j/ypix])
        noise_val += 0.0625 * noise5([i/xpix, j/ypix])
        noise_val += 0.03125 * noise6([i/xpix, j/ypix])


        persistence = persistence

        row.append(noise_val)
    img.append(row)

print("Seed is : ",randSeedInt)
#color the image
    
blue  = [65,105,225]
green = [34,139,34]
beach = [238, 214, 175]
snow = [255, 250, 250]
mountain = [139, 137, 137]
darkgreen = [0,100,0]
sandy = [210,180,140]
lightblue = [65,150,255]

threshold = 0


def add_color(img):
    color_world = img
    for i in range(xpix):
        for j in range(ypix):
            if img[i][j] < threshold + 0.02:
                color_world[i][j] = blue
            elif img[i][j] < threshold + 0.03:
                color_world[i][j] = lightblue
            elif img[i][j] < threshold + 0.055:
                color_world[i][j] = sandy
            elif img[i][j] < threshold + 0.1:
                color_world[i][j] = beach
            elif img[i][j] < threshold + 0.25:
              color_world[i][j] = green
            elif img[i][j] < threshold + 0.4:
                color_world[i][j] = darkgreen
            elif img[i][j] < threshold + 0.7:
                color_world[i][j] = mountain
            elif img[i][j] < threshold + 1.0:
                color_world[i][j] = snow
    return color_world

color_world = add_color(img)

fig=plt.figure(frameon=False)
fig.set_size_inches(xpix, ypix)
plt.imshow(color_world, aspect='auto')
plt.savefig("output.png")
print('Image Saved!')





#image = Image.new('RGB' , (xpix, ypix))
#pixels = image.load()
#image = Image.fromarray(img.array(color_world) * 255, 'RGB')
#image.save('output.png', "png")

