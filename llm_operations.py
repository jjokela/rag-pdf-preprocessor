import base64
import os

import requests


def encode_image(image_path: str) -> str:
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def get_headers(api_key: str) -> dict[str, str]:
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }


def get_payload(base64_image: str) -> dict[str, str]:
    return {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "The following image is a page of a pdf document. "
                                "Give me a summary of the contents of the page."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": "low"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 1500
    }


def save_image_text(file_path: str, content: str) -> None:
    path_parts = file_path.split(os.sep)
    path_parts[0] = 'result'
    file_path = os.path.join(*path_parts)

    file_path, _ = os.path.splitext(file_path)
    new_file_path = file_path + '.txt'

    directory = os.path.dirname(new_file_path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Content saved to {new_file_path}")


def get_content(base64_image: str, api_key: str) -> str:
    headers = get_headers(api_key)
    payload = get_payload(base64_image)
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    json_response = response.json()
    content = json_response['choices'][0]['message']['content']

    return content


def get_image_texts(image_paths: list[str], api_key: str):
    for file_path in image_paths:
        base64_image = encode_image(file_path)

        content = get_content(base64_image, api_key)

        save_image_text(file_path, content)
