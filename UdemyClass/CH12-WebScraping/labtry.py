import bs4
import requests


result = requests.get("https://zh.wikipedia.org/wiki/Google")
soup = bs4.BeautifulSoup(result.text, 'lxml')
all_image = soup.select("img.mw-file-element")
for i in range(len(all_image)):  # 找尋目標圖片所在是第幾個index
    print(i)
    print(all_image[i]["src"])

image = soup.select("img.mw-file-element")[3]
print(image["src"])  # 目標圖片的source
print(image["class"])
print(image["width"])


target_img = requests.get(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Googleplex_HQ_%28cropped%29.jpg/220px-Googleplex_HQ_%28cropped%29.jpg")
print(target_img)
print(target_img.content)  # 回傳以二進位格式存儲或傳輸的數據

# with open("google_img.jpg", "wb") as f:  # 將抓到的照片存下來
#     f.write(target_img.content)
