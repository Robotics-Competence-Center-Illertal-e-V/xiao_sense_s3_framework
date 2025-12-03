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
            g = data[x*width+y] 
            img[x][y][0] = g
            img[x][y][1] = g
            img[x][y][2] = g
    return img

def clamp(value):
    return max(0, min(255, int(value)))

def yuv_to_rgb(Y, U, V):
    C = Y - 16
    D = U - 128
    E = V - 128
    R = clamp(1.164 * C + 1.596 * E)
    G = clamp(1.164 * C - 0.392 * D - 0.813 * E)
    B = clamp(1.164 * C + 2.017 * D)
    return (R, G, B)

def convert_image_YUV422_to_rgb(data, height, width):
    if len(data) != height*width*2:
        raise Exception(f"data to not correct length {len(data)}!={height*width*2}")
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for x in range(height):
        for y in range(int(width/2)): #process two pixel at the same time
            Y0 = data[(x*width+y*2)*2] 
            U = data[(x*width+y*2)*2+1]
            Y1 = data[(x*width+y*2)*2+2]
            V = data[(x*width+y*2)*2+3]
            R, G, B = yuv_to_rgb(Y0, U, V)
            img[x][y*2][0] = R
            img[x][y*2][1] = G
            img[x][y*2][2] = B
            R, G, B = yuv_to_rgb(Y1, U, V)
            img[x][y*2+1][0] = R
            img[x][y*2+1][1] = G
            img[x][y*2+1][2] = B            
    return img