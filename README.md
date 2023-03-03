# Description
Locate (Thai) tourist attraction from a picture.  
currently on a data gathering process.


# Usage
- run `pip install -r requirements.txt`.
- then simply run `main.ipynb` to train the model and see the result.
- dataset will be downloaded automatically using [gdown](https://github.com/wkentaro/gdown).


# ความคืบหน้า
- โมเดลปัจจุบันยังติดปัญหา overfitting เนื่องจากข้อมูลมีจำนวนน้อย (~500 images per class) โดยการทำ data augmentation สามารถช่วยได้แต่ไม่เพียงพอ
- ซึ่งทำให้จำเป็นต้อง scrape ข้อมูลเพิ่มเติมด้วย query ที่ต่างจากเติม ()