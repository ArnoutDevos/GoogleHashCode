#!/usr/bin/env python3
from parser import Image

def score(slides):
    score = 0

    for (slide1, slide2) in zip(slides[:-1], slides[1:]):
        score += score_transition(slide1, slide2)

    print('Score: {}'.format(score))

def score_transition(slide1, slide2):
    #print(slide1)
    #print(slide2)

    image_1_tags = set()
    image_2_tags = set()

    for image in slide1:
        #print("Image 1 tags: {}".format(image.tags))
        image_1_tags = image_1_tags.union(image.tags)
        #print("Image 1 tags unionized: {}".format(image_1_tags))

    for image in slide2:
        image_2_tags = image_2_tags.union(image.tags)

    common_tags = image_1_tags.intersection(image_2_tags)
    #print("common: {}".format(len(common_tags)))
    if len(common_tags) == 0: return 0

    unique_1    = image_1_tags.difference(image_2_tags)
    #print("unique1: {}".format(len(unique_1)))
    if len(unique_1) == 0: return 0

    unique_2    = image_2_tags.difference(image_1_tags)
    #print("unique2: {}".format(len(unique_2)))
    if len(unique_2) == 0: return 0

    return min([len(common_tags), len(unique_1), len(unique_2)])

if __name__ == '__main__':
    # Test, should give score = 1
    score([
        [Image(3, 'H', set(['monkey', 'sun']))],
        [Image(64, 'V', set(['green', 'sun'])),Image(85, 'V', set(['purple', 'sun']))],
    ])
