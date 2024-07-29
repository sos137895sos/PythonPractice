import os

# 查看指定資料夾裡的所有目錄
for folder, sub_folders, files in os.walk("1"):
    print("------------------------------")
    print("Currently we are looking at folder" + folder)
    print("The subfolders in current directory are:")
    for sub in sub_folders:  # 查看子目錄
        print(sub)
    print("The files in the current directory are:")
    for f in files:  # 查看當前目錄裡的文件
        print(f)


# 移除指定副檔名例如：html
for root, dirs, files in os.walk("1"):
    print(root)
    for f in files:
        filename, filetype = os.path.splitext(f)
        if filetype == '.html':
            os.remove(os.path.join(root, f))
