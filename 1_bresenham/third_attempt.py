from tgaimage import TGAImage, TGAColor, Format

WHITE = TGAColor(255, 255, 255, 255)
GREEN = TGAColor(0, 255, 0, 255)
RED = TGAColor(255, 0, 0, 255)

# Improved version that handles more cases
def line(x0, y0, x1, y1, img: TGAImage, color: TGAColor):
    steep = False

    # The line is steep if dy > dx
    if abs(x0 - x1) < abs(y0 - y1):
        # Swapping x/y coords will prevent steep lines from having holes by
        # ensuring we have enough samples on the line
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        steep = True

    # If the line runs right to left, reverse it so it runs left to right
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    for x in range(x0, x1):
        # Figure out how far along the X axis this sample is, in range [0.0, 1.0]
        t = (x - x0)/(x1 - x0)
        # Interpolate on the Y-axis based on the X axis
        y = y0 * (1 - t) + y1 * t

        if(steep):
            # We need to compensate for the swap we performed earlier
            img.set(int(y), int(x), color)
        else:
            img.set(int(x), int(y), color)


img = TGAImage(100, 100, Format.RGB)
line(13, 20, 80, 40, img, WHITE)

line(20, 13, 40, 80, img, GREEN)

line(80, 40, 13, 20, img, RED)

img.flip_vertically()
img.write_tga_file("output.tga", True)
