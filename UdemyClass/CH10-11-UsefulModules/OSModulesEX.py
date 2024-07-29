import os

print(os.getcwd())  # 獲取當前工作目錄
print(os.listdir())  # 列出目錄中的文件
print(os.curdir)
print(os.listdir(os.curdir))  # 列出目錄中的文件
print(os.pardir)
print(os.listdir(os.pardir))  # 列出父目錄的文件
print(os.path.join("CH10-UsefulModules", "index.html"))  # 合併路徑
print(os.path.split("CH10-UsefulModules/index.html"))   # 分割路徑
print(os.path.basename("CH10-UsefulModules/ModulesEX.py"))  # 獲取檔名
print(os.path.dirname("CH10-UsefulModules/ModulesEX.py")) # 獲取目錄
