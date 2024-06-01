from tgaimage import TGAImage, TGAColor, Format

white = TGAColor(255, 255, 255, 255)
red = TGAColor(255, 0, 0, 255)

img = TGAImage(100, 100, Format.RGB)
img.set(52, 41, red)
img.flip_vertically()
img.write_tga_file("output.tga", True)

