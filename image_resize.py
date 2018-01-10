from __future__ import print_function
from PIL import Image
import sys
import os
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Image resizing script')

    parser.add_argument(
        'path',
        help='Path to original image'
    )
    parser.add_argument(
        '--width',
        help='Target width',
        type=float
    )
    parser.add_argument(
        '--height',
        help='Target width',
        type=float
    )
    parser.add_argument(
        '--scale',
        help='scale of resize',
        type=float
    )
    parser.add_argument(
        '--output',
        help='path for saving result'
    )

    arguments = parser.parse_args()
    return arguments


def resize_image(original_image, new_width=None, new_height=None, scale=None):
    if new_height and new_width:
        return original_image.resize([int(new_width), int(new_height)])
    elif new_height:
        ratio = new_height / original_image.height
        new_width = ratio * original_image.width
    elif new_width:
        ratio = new_width / original_image.width
        new_height = ratio * original_image.height
    else:
        new_height = scale * original_image.height
        new_width = scale * original_image.width

    return original_image.resize([int(new_width), int(new_height)])


def create_output_image_name(path_to_source_image, output_image):
    filename = os.path.basename(path_to_source_image)
    filename_list = filename.split('.')
    filename_list[0] += ('__'
                         + str(output_image.width)
                         + 'x'
                         + str(output_image.height)
                         + '.')
    return ''.join(filename_list)


def is_ratio_equal(image_a, image_b):
    accuracy_degree = 2
    ratio_a = image_a.height / image_a.width
    ratio_b = image_b.height / image_b.width
    return round(ratio_a, accuracy_degree) == round(ratio_b, accuracy_degree)


if __name__ == '__main__':
    arguments = parse_arguments()
    if arguments.scale and (arguments.width or arguments.height):
        print('Scope and dimensions (height or width) are mutually exclusive')
        sys.exit(2)
    elif not arguments.scale and not arguments.width and not arguments.height:
        print('At least one parameter (height|width|scope) required')
        sys.exit(2)

    width = arguments.width
    height = arguments.height
    scale = arguments.scale
    path_to_source_image = arguments.path
    path_to_output_image = arguments.output

    source_image = Image.open(path_to_source_image)
    output_image = resize_image(source_image, width, height, scale)
    if not is_ratio_equal(source_image, output_image):
        print('Beware! Ratio of image changed!')
    if not path_to_output_image:
        path_to_output_image = create_output_image_name(
            path_to_source_image,
            output_image
        )
    output_image.save(path_to_output_image)
