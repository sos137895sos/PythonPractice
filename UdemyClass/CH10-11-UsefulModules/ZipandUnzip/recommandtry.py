# 建議做法：使用shutil module

import shutil

# 壓縮指定資料夾
# folder_we_want_to_zip = "/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH10-11-UsefulModules/RE_Practice/Employee/Manager"
# out_put_name = "/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH10-11-UsefulModules/ZipandUnzip/Mansgeroutput"

# shutil.make_archive(out_put_name, "zip", folder_we_want_to_zip)


# 解壓縮
something_we_want_to_unzip = "/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH10-11-UsefulModules/ZipandUnzip/Mansgeroutput.zip"
unzipped_folder_name = "/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH10-11-UsefulModules/ZipandUnzip/Manageroutput"

shutil.unpack_archive(something_we_want_to_unzip, unzipped_folder_name, "zip")
