# 一般做法
import zipfile

# 壓縮指定文件
# zipped_file = zipfile.ZipFile("research.zip", "w")

# zipped_file.write("/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH10-11-UsefulModules/ZipandUnzip/research.txt",
#                   compress_type=zipfile.ZIP_DEFLATED)
# zipped_file.write("/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH10-11-UsefulModules/ZipandUnzip/research2.txt",
#                   compress_type=zipfile.ZIP_DEFLATED)
# zipped_file.close()


# 解壓縮指定文件
zipped_obj = zipfile.ZipFile(
    "/Users/ice/Desktop/GitHubRepositories/PythonPractice/research.zip", "r")
zipped_obj.extractall("Unzipresearch")
zipped_obj.close()
