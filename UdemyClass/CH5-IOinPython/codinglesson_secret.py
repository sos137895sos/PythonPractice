# 1 - 100
import random
secret = random.randint(1, 100)  # 會在1～100生成一個正整數
min_value = 1
max_value = 100
print(secret)

while True:
    guess = input(f"猜一個數字介於 {min_value} 與 {max_value} 之間")
    if int(guess) < min_value or int(guess) > max_value:
        print("數字超過範圍請重新選擇。")
        continue
    if int(guess) == secret:
        print(f"終極密碼是 {secret}")
        break
    elif int(guess) < secret:
        min_value = int(guess)
    elif int(guess) > secret:
        max_value = int(guess)
