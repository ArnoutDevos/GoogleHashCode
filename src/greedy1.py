import random
from argparse import ArgumentParser
from formatter import save_slideshow
from parser import load_dataset

import numpy as np

from score import score_transition


def main():
    parser = ArgumentParser()
    parser.add_argument('dataset')
    parser.add_argument('--sample-size', default=10)
    args = parser.parse_args()

    images = load_dataset(args.dataset)

    # Get horizontal-only slides
    slides = [[img] for img in images if img.orientation == 'H']

    random.shuffle(slides)

    slides_left = slides[1:]

    slideshow = [slides[0]]

    sum_scores = 0

    while len(slides_left) > 0:
        print(len(slideshow))
        last_slide = slideshow[-1]
        sample_idx = np.random.choice(len(slides_left), min(len(slides_left), args.sample_size))
        best_score = None
        best_idx = None
        for idx in sample_idx:
            proposal = slides_left[idx]
            score = score_transition(last_slide, proposal)
            if best_score is None or score > best_score:
                best_score = score
                best_idx = idx
        slideshow.append(proposal)
        slides_left.pop(best_idx)
        sum_scores += best_score

    print(sum_scores)
    save_slideshow('{}_{:07d}'.format(args.dataset, sum_scores), slideshow)

if __name__ == '__main__':
    main()
