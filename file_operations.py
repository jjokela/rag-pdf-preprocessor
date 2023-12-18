import glob
import os


def get_image_paths():
    results = []

    for doc_folder in os.listdir(os.path.join('docs', 'img')):
        doc_path = os.path.join('docs', 'img', doc_folder)

        if os.path.isdir(doc_path):
            print(f"Files in '{doc_folder}':")

            for png_file in glob.glob(os.path.join(doc_path, '*.png')):
                print(os.path.basename(png_file))
                results.append(png_file)

    return results


def get_image_path(document_name, page, docs_dir, temp_dir):
    return f'{docs_dir}/{temp_dir}/{os.path.splitext(document_name)[0].lower()}/page_{page.page_number}.png'
