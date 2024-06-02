from tgaimage import TGAImage, TGAColor, Format

WHITE = TGAColor(255, 255, 255, 255)
GREEN = TGAColor(0, 255, 0, 255)
RED = TGAColor(255, 0, 0, 255)

# Instead of using an arbitrary step to determine how many samples we should draw,
# we instead draw the number of pixels between the x coords
# ERROR: can't handle cases where x1 < x0
# ERROR: lines where the diff in y is greater than the diff in x will have holes
#       b/c we're not accounting for the Y delta, only the X delta
def line(x0, y0, x1, y1, img: TGAImage, color: TGAColor):
    for x in range(x0, x1):
        # Figure out how far along the X axis this sample is, in range [0.0, 1.0]
        t = (x - x0)/(x1 - x0)
        # Interpolate on the Y-axis based on the X axis
        y = y0 * (1 - t) + y1 * t
        img.set(int(x), int(y), color)


img = TGAImage(100, 100, Format.RGB)
line(13, 20, 80, 40, img, WHITE)

line(20, 13, 40, 80, img, GREEN)

line(80, 40, 13, 20, img, RED)

img.flip_vertically()
img.write_tga_file("output.tga", True)
