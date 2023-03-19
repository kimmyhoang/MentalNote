import glob 
from PIL import Image 
from scipy import spatial
import numpy as np

#find way to download image
calendar_imgs_path = "imgsCal"
tile_size = (50,50)

# Get all tiles
tile_paths = []
for file in glob.glob(calendar_imgs_path):
	tile_paths.append(file)

# Import and resize all tiles
tiles = []
for path in tile_paths:
	tile = Image.open(path)
	tile = tile.resize(tile_size)
	tiles.append(tile)


#pixelate and resize background
background = Image.open("imgs\bkg.jpg")
width = int(np.round(background.size[0] / tile_size[0]))
height = int(np.round(background.size[1] / tile_size[1]))
resized_photo = background.resize((width, height))

# Empty integer array to store indices of tiles
closest_tiles = np.zeros((width, height), dtype=np.uint32)

#creates calendar as output image
calendar = Image.new(mode="RGB", size=(200, 200))

# Draw tiles
for i in range(width):
	for j in range(height):
		# Offset of tile
		x, y = i*tile_size[0], j*tile_size[1]
		# Index of tile
		index = closest_tiles[i, j]
		# Draw tile
		calendar.paste(tiles[index], (x, y))






