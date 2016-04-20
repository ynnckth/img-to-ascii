import sys
from PIL import Image


ASCII_CHARS = ['#', '@', '%', '*', '+', '-', '.', ' ']
WIDTH = 200


# resize an image keeping the original ratio
def scale(img, new_width=WIDTH):
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


def convert_to_ascii(img, width_chars=WIDTH):
    img = scale(img)
    img = to_grayscale(img)

    img_data_ascii = map_pixels_to_ascii_chars(img)

    ascii_img = []
    for i in xrange(0, len(img_data_ascii), width_chars):
        ascii_img.append(img_data_ascii[i:i + width_chars])

    return "\n".join(ascii_img)


def main():
    img_path = sys.argv[1]

    try:
        image = Image.open(img_path)
    except Exception, e:
        print "Unable to open image file {file}.".format(file=img_path)
        print e
        return

    print convert_to_ascii(image)


if __name__=='__main__':
    main()
