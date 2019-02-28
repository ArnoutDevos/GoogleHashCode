#!/usr/bin/env python3

import os
from argparse import ArgumentParser

FILES = {
    'a': 'a_example.txt',
    'b': 'b_lovely_landscapes.txt',
    'c': 'c_memorable_moments.txt',
    'd': 'd_pet_pictures.txt',
    'e': 'e_shiny_selfies.txt',
}


def load_dataset(dataset_letter):
    """
    Load a dataset by its letter
    :param dataset_letter: a, b, c, d, or e
    :returns: list of { id: integer, orientation: H/V, tags: set()}
    """
    curdir = os.path.dirname(os.path.realpath(__file__))
    datadir = os.path.join(curdir, '..', 'data')
    filename = os.path.join(datadir, FILES[dataset_letter])

    images = []

    with open(filename, 'r') as fp:
        for i, line in enumerate(fp.readlines()):
            if i == 0:
                continue
            entries = line.strip().split(' ')
            orientation = entries[0]
            tags = set(entries[2:])
            images.append({
                'id': i - 1,
                'orientation': orientation,
                'tags': tags
            })

    return images


def main():
    parser = ArgumentParser()
    parser.add_argument('dataset', choices=['a', 'b', 'c', 'd', 'e'])
    args = parser.parse_args()

    dataset = load_dataset(args.dataset)

    print('Length', len(dataset))


if __name__ == '__main__':
    main()
