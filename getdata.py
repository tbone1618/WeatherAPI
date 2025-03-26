import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_txt_files(base_url, save_dir):
    """
    Downloads all .txt files from the specified URL and saves them to the given directory.

    Parameters:
    - base_url (str): The URL to scrape for .txt files.
    - save_dir (str): The local directory to save the downloaded files.
    """

    # Ensure the save directory exists
    os.makedirs(save_dir, exist_ok=True)

    # Fetch the webpage
    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to access {base_url} (Status: {response.status_code})")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Find and download all .txt files
    for link in soup.find_all("a"):
        file_name = link.get("href")

        # Skip invalid links and only process .txt files
        if file_name and file_name.endswith(".txt"):
            file_url = urljoin(base_url, file_name)  # Full URL of the file
            save_path = os.path.join(save_dir, file_name)  # Local save path
            
            # Download the file
            file_response = requests.get(file_url, stream=True)
            if file_response.status_code == 200:
                with open(save_path, "wb") as file:
                    for chunk in file_response.iter_content(chunk_size=1024):
                        file.write(chunk)
                print(f"Downloaded: {save_path}")
            else:
                print(f"Failed to download: {file_url} (Status: {file_response.status_code})")

# Example usage
BASE_URL = "https://www.ncei.noaa.gov/pub/data/normals/1981-2010/products/hourly/"
SAVE_DIR = "data/normals/1981-2010/products/hourly/"

download_txt_files(BASE_URL, SAVE_DIR)