### Satellite Data with Deep Learning

## Dataset: Semantic Segmentation of Aerial Imagery

The dataset can be downloaded from Kaggle ![Link](https://www.kaggle.com/datasets/humansintheloop/semantic-segmentation-of-aerial-imagery)

## Load Data

Use the `download_kaggle_data` function from the `kaggle_utils.loader` and load the data by providing the dataset name and the download folder path.

The dataset contains tiles (images) and relevant masks to classify the input images.

Make sure al the tiles and masks image size is the multiple of patch size, which will affect the batch size in data processing. Smaller patches --> large batch, and larger patches --> small batch.

We'll split our images and masks further to match our patch size.

One-hot enconding transformation is also applied to the labels.

#### Data Processing