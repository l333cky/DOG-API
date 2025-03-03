import requests
from requests.exceptions import ConnectionError


def get_image_url(url: str):
    try:
        response = requests.get(url)
        data = response.json()
        if data["status"] == "error":
            print(f"Получена ошибка {data['message']}")
            return None
        return data['message']
    except ConnectionError:
        print("Ошибка сервера")
        return None

def get_image(image_url: str):
    response = requests.get(image_url)
    return response.content

def download_image(image: bytes, name: str):
    with open(name, "wb") as file:
        file.write(image)


N = 5
URL = "https://dog.ceo/api/breeds/image/random"

for i in range(1, N+1):
    image_url = get_image_url(URL)
    print(image_url)
    image = get_image(image_url)
    name = f"dog_{i}.jpg"
    download_image(image, name)





