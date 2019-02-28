#!/usr/bin/env python3

def score(slides)
    for (slide1, slide2) in zip(slides[:-1], slides[1:]):
        for image in slide1:
            common_tags = slide1.intersection(slide2)

def horizontal_score(slides):
    for (slide1, slide2) in zip(slides[:-1], slides[1:]):
        for image in slide1:
            for image in slide2:
                common_tags = slide1.intersection(slide2)
                unique_1    = slide1.difference(slide2)
                unique_2    = slide2.difference(slide1)

                score = min([common_tags, unique_1, unique_2])

def main():


if __name__ == '__main__':
    main()
