from tgaimage import TGAImage, TGAColor, Format

WHITE = TGAColor(255, 255, 255, 255)
GREEN = TGAColor(0, 255, 0, 255)
RED = TGAColor(255, 0, 0, 255)

# Inefficient algorithm
# Draws pixels by interpolating between coords, sampling at the rate of
# `step`
def line(x0, y0, x1, y1, img: TGAImage, color: TGAColor, step):
    for t in range(step):
        # Interpolate start and (start + diff(end, start)) according to the step
        x = x0 + (x1 - x0) * (t / step)
        y = y0 + (y1 - y0) * (t / step)
        img.set(int(x), int(y), color)


img = TGAImage(100, 100, Format.RGB)
line(13, 20, 80, 40, img, WHITE, 100)
line(13, 20, 80, 40, img, RED, 10)

# Supersampled, produces same results
line(13, 10, 80, 30, img, GREEN, 200)

# N.B. that this appears dotted b/c our sample rate is too low
line(13, 50, 80, 70, img, RED, 10)

img.flip_vertically()
img.write_tga_file("output.tga", True)
