import numpy as np

def convert_image_rgb565_to_rgb(data, height, width):
    if len(data) != height*width*2:
        raise Exception(f"data to not correct length {len(data)}!={height*width*2}")
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for x in range(height):
        for y in range(width):
            im = data[x*width*2+y*2+0] << 8  | data[x*width*2+y*2+1]
            
            MASK5 = 0b011111
            MASK6 = 0b111111

            # TODO: BGR or RGB? Who knows!
            b = (im & MASK5) << 3
            g = ((im >> 5) & MASK6) << 2
            r = ((im >> (5 + 6)) & MASK5) << 3
            img[x][y][0] = r
            img[x][y][1] = g
            img[x][y][2] = b
    return img

def convert_image_grayscale_to_rgb(data, height, width):
    if len(data) != height*width:
        raise Exception(f"data to not correct length {len(data)}!={height*width}")
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for x in range(height):
        for y in range(width):
            g = data[x*width+y+0] 
            img[x][y][0] = g
            img[x][y][1] = g
            img[x][y][2] = g
    return img