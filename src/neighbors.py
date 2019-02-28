#!/usr/bin/env python3
from preprocessing import preprocess

def generate_index(slides):
    index = {}
    for slide in slides:
        for image in slide:
            for tag in image.tags:
                if tag not in index:
                    index[tag] = []
                index[tag].append(slide)

    #for key in index:
    #    print(key, index[key])
    return index

def neighbors(slide, index):
    result = set()
    slide_tags = set()

    for image in slide:
        slide_tags = slide_tags.union(image.tags)

    for tag in slide_tags:
        result.union(set(index[tag]))

    result = result.difference(slide)

    return result

if __name__ == '__main__':
    # Test, should give score = 1
    slides = preprocess('a')

    generate_index(slides)
