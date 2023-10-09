import matplotlib.pyplot as plt
import numpy as np

x= [1,2,3,4]
y=[2,3,4,5]
plt.plot(x, y)
plt.show()
plt.bar(x,y)
plt.show()

figure = plt.figure()
axes= figure.add_subplot(111)

x2 = np.array(x)
y2 = np.array([4,1,3,6])

axes.plot(x, y, color="red", linestyle="dashed", marker="^")
axes.plot(x2, y2, color="k", linestyle="dotted", marker="o")
plt.show()

x3 = np.array([2,4,1,2])
y3 = np.array([3,1,4,1])

x4 = np.array([2,4,1,3])
y4 = np.array([4,3,2,3])

figure = plt.figure()
axes1 = figure.add_subplot(224)     #1행 2열에서 1열
axes1.plot(x,y)
axes2 = figure.add_subplot(222)     #1행 2열에서 2열
axes2.plot(x2,y2)
axes3 = figure.add_subplot(223)     #1행 2열에서 2열
axes3.plot(x3,y3)
axes4 = figure.add_subplot(221)     #1행 2열에서 2열
axes4.bar(x4,y4)
plt.show()

figure = plt.figure()
axes = figure.add_subplot(111)
axes.bar(x,y)
axes.bar(x2,y2)
plt.show()

figure = plt.figure()
axes1 = figure.add_subplot(111)
axes2 = axes1.twinx()
axes1.bar(x,y, color="blue", label="bar")
axes2.plot(x2,y2, color="red",label="plot")
plt.show()

# 점 그래프 scatter
from matplotlib import font_manager, rc

font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
for font in font_list:
    print(font)

rc("font", family="Hancom Gothic")

figure = plt.figure()
axes = figure.add_subplot(111)
x = [1,2,3,4]
y = [2,4,6,8]
x2= [1,2,3,4]
y2= [6,2,4,6]
axes.scatter(x, y)
axes.scatter(x2,y2)
plt.title("제목")
plt.xlabel("x축이름")
plt.ylabel("y축 이름")
plt.show()

# 원형 그래프
from matplotlib import font_manager, rc

font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
for font in font_list:
    print(font)

rc("font", family="Hancom Gothic")

figure = plt.figure()
axes = figure.add_subplot(111)

label = ["축구","농구","야구","배구"]
data = [10,20,5,30]

axes.pie(data, labels=label)
# plt.show()

plt.savefig("test")