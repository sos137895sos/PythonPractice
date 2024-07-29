import csv

# 開啟指定csv文件
with open("/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH14/14-1file.csv", newline="", encoding="utf8") as f:
    csv_data = csv.reader(f)
    print(csv_data)
    for row in csv_data:
        print(row)  # 輸出每一行的資料
        print(row[1].title())  # 把row[1]的資料每第一個字改成大寫

# 新增一個csv檔案並新增單行數據
# with open("/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH14/newfile.csv", mode="w", newline="", encoding="utf8") as nf:
#     csv_writer = csv.writer(nf, delimiter=",")
#     csv_writer.writerow(['a', "b", 'c'])

# 添加多行數據至既有的csv檔案
with open("/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH14/newfile.csv", mode="a", newline="", encoding="utf8") as nf:
    csv_writer = csv.writer(nf, delimiter=",")
    csv_writer.writerows([['e', 'f', 'g'], ['i', 'j', 'k']])
