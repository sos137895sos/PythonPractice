import datetime

# 查看當前日期時間
now = datetime.datetime.now()

print(datetime.datetime.now())
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

# 不同時間相減
x = datetime.datetime.now()
y = datetime.datetime(2024, 1, 1)
print(y - x)
print(type(x - y))  # 返回<class 'datetime.timedelta'>


# 使用strftime 格式化 轉換指定的格式的字符串
# 年 月 日 星期幾 時 分 秒
print(x.strftime(("%Y-%m-%d %A %H:%M:%S")))


# timedelta Class介紹
today = datetime.datetime.now()
oneday = datetime.datetime(2025, 1, 1)

diff = oneday - today
print(diff)
print(type(diff))

# timedelta ready-only attribute, method
print(diff.days)
print(diff.total_seconds())
