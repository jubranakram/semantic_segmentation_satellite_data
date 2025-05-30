from kaggle_utils.loader import download_kaggle_dataset

if __name__ == '__main__':
    DATASET_URL = 'humansintheloop/semantic-segmentation-of-aerial-imagery'
    DOWNLOAD_DIR = './data'
    download_kaggle_dataset(DATASET_URL, DOWNLOAD_DIR)