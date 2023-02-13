places = []
file_path = "./wiki_data.txt"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        places.append(line)
        
search_keys = places