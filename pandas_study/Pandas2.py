import pandas as pd

######################[csv 파일 불러오기]######################
data = pd.read_csv("books_data.csv", encoding="euc-kr")
print(data)
print()
print(data.columns)
print()
print(data["도서명"])
print()
print(data.loc[data["도서명"] == "퇴사 후 독립출판 책만들기"].iloc[0])

# import csv
# f= open("books_data.csv", "r")
# csvData = csv.reader(f)
# i = 0
# for data in csvData:
#     if i < 10:
#         print(data)
#     else:
#         break
#     i += 1