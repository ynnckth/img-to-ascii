import sys
from PIL import Image


ASCII_CHARS = ['#', '@', '%', '*', '+', '-', '.', ' ']


# resize an image keeping the original ratio
def scale_image(img, new_width=100):
    (original_width, original_height) = img.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = img.resize((new_width, new_height))
    return new_image


def to_grayscale(img):
    return img.convert('L')


def map_pixels_to_ascii_chars(img):
    pixels_in_img = list(img.getdata())
    pixels_to_chars = [ASCII_CHARS[int(round(float(pixel) / 255 * (len(ASCII_CHARS)-1)))] for pixel in pixels_in_img]

    return "".join(pixels_to_chars)


def convert_image_to_ascii(img, new_width=100):
    img = scale_image(img)
    img = to_grayscale(img)

    pixels_to_chars = map_pixels_to_ascii_chars(img)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            xrange(0, len(pixels_to_chars), new_width)]

    return "\n".join(image_ascii)


def main():
    img_path = sys.argv[1]

    try:
        image = Image.open(img_path)
    except Exception, e:
        print "Unable to open image file {img_path}.".format(image_filepath=img_path)
        print e
        return

    print convert_image_to_ascii(image)


if __name__=='__main__':
    main()
