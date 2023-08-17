# Locate (Thai) tourist attraction from a picrure

----------------

## Introduction

Locate (Thai) tourist attraction from a picture using deep learning. This project is a part of my final project in [CS364](https://cs.sci.ku.ac.th/curriculum/bachelor/y2565/course-2/) course at KU.

## Data

- Images have been gathered using [Google Image Scraper](https://github.com/NotHolmes/Google-Image-Scraper/tree/29c7b9fec67cfda02dae7bf37d90a38b00996fbb) then convert, and store them in 224x224 RGB images in a directory with the name of the place.
- Identical images were cleaned using [perceptual hashing technique](https://www.pyimagesearch.com/2017/11/27/image-hashing-opencv-python/), also we manually deleted some images which are not related to the place.

## Usage

### Scraping

- in `Google-Image-Scraper` repository's directory.
- install required packages with `pip install -r requirements.txt`.
- run `main.py`, this will read queries line by line in file, specify your input file in `main.py` with variable `PATH`.
- images will be stored in `photos/SEARCH_KEY/..`

### Train a model

- in this repository, install required packages with `pip install -r requirements.txt`. (this will include packages which are required for running the web app)
- then simply run `main.ipynb` to train the model and see the result.
- dataset will be downloaded automatically using [gdown](https://github.com/wkentaro/gdown).

### Run the web app

- if you have never install the `requirements.txt` before, in this repository, install required packages with `pip install -r requirements.txt`.
- specify the model path in `app.py` with variable `MODEL_PATH` (for example `model.h5` that you have trained).
- run `python app.py` to start the web app using Flask.
- connect to `localhost:5000` to see the web app and start predicting.
