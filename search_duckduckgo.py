from duckduckgo_images_api import search
from io import BytesIO
from PIL import Image
import requests
import os

def download_images(name, query, max_results=100):
    results = search(query, max_results)
        
    images_url = []                              
    for r in results["results"]:
        images_url.append(r["image"])

    i = 0
    while i < len(images_url):
        url = images_url[i]
        
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Request error occurred: {err}")
        else:
            if response.status_code == 200 and response.content:
                try:
                    img = Image.open(BytesIO(response.content))
                    
                    img = img.convert("RGB")
                    
                    # Resize the image
                    img.thumbnail((500, 500))
                    
                    # Save the resized image
                    save_path = "./images/"+ f"{name}/{name}_{i}.jpg"

                    if not os.path.exists(os.path.dirname(save_path)):
                        os.makedirs(os.path.dirname(save_path))

                    img.save(save_path, format="JPEG")
                except:
                    continue
            else:
                print(f"Skipping URL {url} due to status code {response.status_code} and no content")

        i = i + 1
        
    print(f"Downloaded {len(images_url)} images for '{query}'.")
    return len(images_url)

        
# download images from wiki_data.txt

with open("wiki_data.txt", "r", encoding="utf-8") as file:
    # Loop through the first 5 lines
    for i in range(10):
        # Read the next line from the file
        line = file.readline().strip()
        # Do something with the line
        download_images(line, line+"", 50)