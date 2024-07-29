import sqlite3

conn = sqlite3.connect(
    "/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH14/sqlite3/datafile.db")
cursor = conn.cursor()

name = input("請輸入您想搜尋的名字：")
# result = cursor.execute(
#     """select * from people where name = '{}'""".format(name))
# 此方法很容易產生SQL Injection攻擊，只要使用者輸入 1' OR '1' ='1 就可以查到所有的資料，
# 因為select * from people where name = 1' OR '1' ='1永遠是TRUE
# 當沒有選擇任何東西時就會選擇所有東西

# 預防SQL Injection攻擊的方法 1
# result = cursor.execute(
#     """select * from people where name = :username""", {"username": name})

# 預防SQL Injection攻擊的方法 2
result = cursor.execute(
    """select * from people where name = ?""", (name,))


print(result.fetchall())
conn.close
