import smtplib
import getpass  # 隱藏密碼


smtp_ojb = smtplib.SMTP("smtp.gmail.com", 587)
smtp_ojb.ehlo()
smtp_ojb.starttls()

email = input("輸入你的信箱帳號：")
password = getpass.getpass("請輸入密碼：")
smtp_ojb.login(email, password)

from_address = email
to_address = email
subject = input("Enter subject：")
message = input("Enter message：")
full_message = "Subject:" + subject + "\n" + message

print(smtp_ojb.sendmail(from_address, to_address, full_message))
smtp_ojb.quit()
