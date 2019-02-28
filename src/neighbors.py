#!/usr/bin/env python3
from preprocessing import preprocess

def generate_index(slides):
    index = {}
    for slide in slides:
        for image in slide:
            for tag in image.tags:
                index[tag] = set().union(index[tag]).union(image)

    print(index)
    return index

if __name__ == '__main__':
    # Test, should give score = 1
    generate_index([
        [Image(3, 'H', set(['monkey', 'sun']))],
        [Image(64, 'V', set(['green', 'sun'])),Image(85, 'V', set(['purple', 'sun']))],
    ])
