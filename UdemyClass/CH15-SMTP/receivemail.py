import imaplib
import email as em
import getpass

M = imaplib.IMAP4_SSL("imap.gmail.com")


email = input("輸入你的信箱帳號：")
password = getpass.getpass("請輸入密碼：")


M.login(email, password)
M.select("inbox")
result, ids = M.search(None, "FROM icefwkacc425@gmail.com")
rest, content = M.fetch(ids[0], "(RFC822)")

raw_content = content[0][1]
email_content = raw_content.decode("utf-8")
email_massage = em.message_from_string(email_content)

for part in email_massage.walk():  # 常見的查看信件特定部分內容寫法
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)
        with open("email_content.txt", mode="wb") as f:
            f.write(body)
