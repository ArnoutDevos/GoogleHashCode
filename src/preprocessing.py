from parser import load_dataset
from parser import Image

def images_to_slides(images):
    slides = []
    vert_slide = []
    for image in images:
        if image.orientation == 'H':
            slides.append([image])
        else:
            vert_slide.append(image)
            if len(vert_slide) == 2:
                slides.append(vert_slide)
                vert_slide = []

    return slides


if __name__ == '__main__':
    preprocess('a')
