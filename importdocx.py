from collections import Counter

filename = '研一学生共性工作.txt'
txt = open(filename,'r',encoding='gbk')  # read读取字符
char_txt = txt.read()
count = Counter(char_txt)  # 得到count字典
print(count)
txt.close()
# print(list(count.values()))
# print(list(count.keys()))

