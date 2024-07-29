import sqlite3

# 基本介紹，不建議這樣子寫資料庫

conn = sqlite3.connect(
    "/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH14/sqlite3/datafile.db")
cursor = conn.cursor()

# 添加資料
# cursor.execute(
#     """create table people (id integer primary key, name text, count integer)""")
# cursor.execute(
#     """insert into people (name, count) values ('Otani', 25)""")  # 方法1
# cursor.execute(
#     """insert into people (name, count) values (?, ?)""", ('Shohei', 26))  # 方法2
# cursor.execute("""insert into people (name, count) values (:username, :usercount)""", {
#                "username": "Bett", "usercount": 27})  # 方法3


# cursor.execute("""update people set count = :usercount where name = :username""", {
#                "username": 'Otani', "usercount": 30})  # 更新數據

# cursor.execute("""Delete from people where name = 'Shohei'""")  # 刪除資料


result = cursor.execute("select * from people")
print(result.fetchall())  # 查看全部符合資料
# print(result.fetchone())  # 查看第一個符合資料
# # print(result.fetchmany(2)) # 查看


conn.commit()  # 儲存資料庫任何更改
conn.close()  # 關閉與資料庫的連接
