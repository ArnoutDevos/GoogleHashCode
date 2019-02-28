import os
from parser import Image


def format_slideshow(slides):
    """
    Write the required text file
    :param slides: List of list of images
    :return: string
    """
    lines = [str(len(slides))]
    for slide in slides:
        assert len(slide) in [1, 2]
        line = " ".join([str(img.id) for img in slide])
        lines.append(line)
    return '\n'.join(lines) + '\n'


def save_slideshow(dataset_letter, slides):
    """
    Save a slideshow
    :param dataset_letter: a, b, c, d, e, used for output filename
    :effect: write file in ../output/b.txt
    """
    content = format_slideshow(slides)
    curdir = os.path.dirname(os.path.realpath(__file__))
    outputdir = os.path.join(curdir, '..', 'output')
    filename = os.path.join(outputdir, dataset_letter + '.txt')
    with open(filename, 'w') as fp:
        fp.write(content)
    print('Wrote slideshow to file {}'.format(os.path.realpath(filename)))


if __name__ == '__main__':
    # Test
    save_slideshow('c', [
        [Image(3, 'H', set(['monkey', 'sun']))],
        [Image(64, 'V', set(['green', 'sun'])),Image(85, 'V', set(['purple', 'sun']))],
    ])
