import os
import shutil

from dotenv import load_dotenv

from file_operations import get_image_paths
from llm_operations import get_image_texts

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

'''
TODO: if summary file already exists, skip it
- cleanup as a config flag
- logging


feats:
- get the summaries
- remove image pages from pdfs
- copypaste modified pdf files and summary files to a target folder
'''



if __name__ == '__main__':
    # check all documents, and get all the images
    # documents_with_images = process_folder()

    # gets files and saves to images
    # save_image_pages(documents_with_images)

    # get the image paths
    image_paths = get_image_paths()

    # get the contents of images using llm, and save to disk
    get_image_texts(image_paths, api_key)

