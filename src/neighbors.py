#!/usr/bin/env python3
from preprocessing import images_to_slides
from parser import load_dataset

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
    result = []
    result_ids = set([slide[0].id])
    slide_tags = set()

    for image in slide:
        slide_tags = slide_tags.union(image.tags)

    for tag in slide_tags:
        for slide_1 in index[tag]:
            if slide_1[0].id not in result_ids:
                result.append(slide_1)
                result_ids = result_ids.union([slide_1[0].id])

    #print(result)
    return result

if __name__ == '__main__':
    # Test, should give score = 1
    images = load_dataset('a')
    slides = images_to_slides(images)

    #for slide in slides:
    #    print(slide)

    index = generate_index(slides)
    neighbors(slides[0], index)
