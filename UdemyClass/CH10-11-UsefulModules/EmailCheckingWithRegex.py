import re


# ?????@???.???
regex = r"\b[a-zA-Z0-9._+%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
# 也可以寫成簡單點：
regex2 = r"[^@]+@[^@]+\.[^@]+"


def check_email(email):
    if re.fullmatch(regex2, email):
        print(f"{email} 是正確的email!")
    else:
        print(f"{email} 並不是正確的email! ")


email1 = "ahsdklfhoi2j2%%.+jj+_122@g.m-ai2A.cO"
email2 = "add@gma.cc"
email3 = "!!456^^@jk.cc"
email4 = "ahah@abd.c"
check_email(email1)
check_email(email2)
check_email(email3)
check_email(email4)
