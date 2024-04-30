command = input("Where do you wanna go?")
match command.split(" "):
    case ["Go", "home"]:
        print("You wanna go home")
    case _:
        print("The system cannot determine where you wanna go.")


# day = input("今天星期幾")

# match day:
#     case "Sunday" | "Monday":
#         print("公休")
#     case "Saturday":
#         print("營業半天")
#     case _:
#         print("營業中")


# lang = input("你希望學什麼程式語言？")

# match lang:
#     case "JS":
#         print("做網頁前端")
#     case "PHP":
#         print("網頁後端")
#     case "Python":
#          print("資料科學家")
#     case _:
#          print("其他")

# if lang == "JS":
#     print("做網頁前端")
# elif lang == "PHP":
#     print("網頁後端")
# elif lang == "Python":
#     print("資料科學家")
# elif lang == "Kotlin":
#     print("Android開發")
# elif lang == "Swift":
#     print("IOS")
# else:
#     print(其他)
