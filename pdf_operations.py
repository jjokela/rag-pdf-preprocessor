import os
from typing import List, Tuple

import pdfplumber
from pdfplumber.page import Page

from file_operations import get_image_path


def save_page_as_image(image_path: str, page: Page):
    directory = os.path.dirname(image_path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    img = page.to_image(resolution=512)
    img.save(image_path)


def process_pdf(pdf_path: str) -> List[Page]:
    pages_with_images: List[Page] = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.images:
                pages_with_images.append(page)

    return pages_with_images


def save_image_pages(documents_with_images: List[Tuple[str, List[Page]]]):
    for doc_name, pages_list in documents_with_images:
        for page in pages_list:
            image_path = get_image_path(doc_name, page, 'docs', 'img')
            save_page_as_image(image_path, page)


def process_folder(folder_path: str = 'docs') -> List[Tuple[str, List[Page]]]:
    results: List[Tuple[str, List[Page]]] = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            pages_info = process_pdf(file_path)
            results.append((filename, pages_info))

    return results
