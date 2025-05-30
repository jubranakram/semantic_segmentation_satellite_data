import os 
import zipfile 
from kaggle.api.kaggle_api_extended import KaggleApi

from dotenv import load_dotenv

load_dotenv('.env')

def download_kaggle_dataset(dataset: str, download_path: str = '.', unzip: bool = True):
    """
    Download a Kaggle dataset using the Kaggle API.

    Parameters:
    - dataset: str. Kaggle dataset identifier in the format "owner/dataset-name".
    - download_path: str. Directory where the dataset should be saved.
    - unzip: bool. If True, unzip the downloaded file.

    Example:
    download_kaggle_dataset("zynicide/wine-reviews", "./data")
    """
    # Ensure kaggle.json is available
    if "KAGGLE_CONFIG_DIR" not in os.environ:
        raise FileNotFoundError(
            "kaggle.json not found. Place it in ~/.kaggle/ or set the KAGGLE_CONFIG_DIR environment variable."
        )
    print(os.environ)
    api = KaggleApi()
    api.authenticate()

    print(f"Downloading dataset: {dataset}")
    api.dataset_download_files(dataset, path=download_path, unzip=unzip)

    print(f"Dataset downloaded to '{download_path}'")

    if not unzip:
        print("Unzipping manually...")
        zip_path = os.path.join(download_path, dataset.split('/')[-1] + '.zip')
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(download_path)
        print("Unzipped successfully.")
    