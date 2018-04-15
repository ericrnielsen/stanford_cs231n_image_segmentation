import os, gdal

# File paths

TRAIN_PATH = 'train/'
TEST_PATH = 'test/'

ORIGINAL_PATH = 'original/'
SPLIT_256_PATH = 'split_256/'
SPLIT_512_PATH = 'split_512/'

CITY_PATH = "city/"
COAST_PATH = "coast/"
DESERT_PATH = "desert/"

ALL_PATHS = [CITY_PATH, COAST_PATH, DESERT_PATH]

tile_size_x = 256
tile_size_y = 256

tile_size_x2 = 512
tile_size_y2 = 512

for image_type in ALL_PATHS:

    count = 0
    num_files = len([x for x in os.listdir(TRAIN_PATH + ORIGINAL_PATH + image_type) if not x == '.DS_Store'])

    for filename in os.listdir(TRAIN_PATH + ORIGINAL_PATH + image_type):
        if not filename == '.DS_Store':

            count += 1
            print("\n\n\n[%s] Image %d / %d\n\n\n" % (image_type, count, num_files))

            ds = gdal.Open(TRAIN_PATH + ORIGINAL_PATH + image_type + filename)
            band = ds.GetRasterBand(1)
            xsize = band.XSize
            ysize = band.YSize

            # 256x256 split
            for i in range(0, xsize, tile_size_x):
                for j in range(0, ysize, tile_size_y):
                    com_string = "gdal_translate -of GTIFF -srcwin " + \
                        str(i)+ ", " + str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + \
                        str(TRAIN_PATH + ORIGINAL_PATH + image_type + filename) + " " + \
                        str(TRAIN_PATH + SPLIT_256_PATH + image_type + filename[:-4]) + "_" + str(i) + "_" + str(j) + ".tif"
                    os.system(com_string)

            # 512x512 split
            for i in range(0, xsize, tile_size_x2):
                for j in range(0, ysize, tile_size_y2):
                    com_string = "gdal_translate -of GTIFF -srcwin " + \
                        str(i)+ ", " + str(j) + ", " + str(tile_size_x2) + ", " + str(tile_size_y2) + " " + \
                        str(TRAIN_PATH + ORIGINAL_PATH + image_type + filename) + " " + \
                        str(TRAIN_PATH + SPLIT_512_PATH + image_type + filename[:-4]) + "_" + str(i) + "_" + str(j) + ".tif"
                    os.system(com_string)
    