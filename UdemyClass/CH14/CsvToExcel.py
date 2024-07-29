from openpyxl import Workbook
import csv


data_rows = [fields for fields in csv.reader(open(
    "/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH14/14-1file.csv", newline=""))]
print(data_rows)

wb = Workbook()
ws = wb.active
ws.title = "Myfile"
ws.sheet_properties.tabColor = "1072BA"
for row in data_rows:
    ws.append(row)

wb.save("/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH14/Myfile.xlsx")
