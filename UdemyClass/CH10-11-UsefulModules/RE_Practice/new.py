# 尋找文檔內的inline-citation內嵌引用例如：(Campbell, 2014)
# 條件：(任何字符像是數字、空白鍵、英文大小寫, 大於等於四個數字)

import re

with open("/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH10-11-UsefulModules/RE_Practice/11-5researchpaper.txt", encoding="utf8") as my_paper:
    text = my_paper.read()


# inline = re.findall(r"\(+[a-zA-z0-9\s]+, +\d{4,}\)", text)
# # print(inline)

inline = r"\(+[a-zA-z0-9\s]+, +\d{4, }\)"


def check_inline(paper):
    if re.match(inline, paper):
        print(f"內嵌引用：{paper} ")


check_inline(text)
