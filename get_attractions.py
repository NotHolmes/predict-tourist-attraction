import requests as r
from bs4 import BeautifulSoup

def scrape():
    url="https://th.wikipedia.org/wiki/รายชื่อสถานที่ท่องเที่ยวในประเทศไทย"
    # Make the GET request to the URL
    response = r.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the <li> tags
        li_tags = soup.find_all('li')

        # Extract the text from each <li> tag
        with open("wiki_data.txt", "w", encoding="utf-8") as file:
            for li in li_tags:
                file.write(li.text + "\n")
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
    
def remove_lines(file_path, strings_to_remove):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(file_path, "w", encoding="utf-8") as f:
        for line in lines:
            if not any(string in line for string in strings_to_remove):
                f.write(line)
                
remove_lines("./wiki_data.txt", ['สถานี', 'วัด', 'โรงพยาบาล', 'ถนน', 'วัง', 'สวน', 'จุดค้าขาย', 'เมือง', 'แหล่ง', 'น้ำตก', 'อุทยาน', 'ถ้ำ', 'ไร่', 'เขา', 'สนาม', 'ฟาร์ม'])