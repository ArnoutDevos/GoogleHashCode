#!/usr/bin/env python3
from preprocessing import preprocess

def generate_index(slides):
    index = {}
    for slide in slides:
        for image in slide:
            for tag in image.tags:
                if tag not in index:
                    index[tag] = []
                index[tag].append(image)

    for key in index:
        print(key, index[key])
    return index

def neighbors(slide):
    pass

if __name__ == '__main__':
    # Test, should give score = 1
    slides = preprocess('a')

    generate_index(slides)
