from tgaimage import TGAImage, TGAColor, Format

WHITE = TGAColor(255, 255, 255, 255)
GREEN = TGAColor(0, 255, 0, 255)
RED = TGAColor(255, 0, 0, 255)

# Fully optimized version that only works with integers
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

    dx = x1 - x0
    dy = y1 - y0

    # How much to increase error by each iteration. N.B. that multiplying by 2 we
    # no longer have to compare against the float `0.5`
    derror = abs(dy) * 2

    # As we continue to draw pixels on the X axis, this tracks how far the line
    # of horizontal pixels we're drawing is deviating from the actual sloped
    # line we're trying to render
    error = 0
    y = y0
    for x in range(x0, x1):
        if(steep):
            # We need to compensate for the swap we performed earlier
            img.set(int(y), int(x), color)
        else:
            img.set(int(x), int(y), color)

        error += derror

        # Once error exceepds this threshold, it is time to move up one
        # vertical pixel
        if error > dx:
            if y1 > y0:
                y += 1
            else:
                y -= 1

            error -= dx * 2


img = TGAImage(100, 100, Format.RGB)
line(13, 20, 80, 40, img, WHITE)

line(20, 13, 40, 80, img, GREEN)

line(80, 40, 13, 20, img, RED)

img.flip_vertically()
img.write_tga_file("output.tga", True)
