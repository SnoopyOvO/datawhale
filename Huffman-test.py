'''
    huffman编码
'''
import copy
import math
from collections import Counter
import pysnooper

class Node:
    def __init__(self, name, weight):
        self.name = name #节点名
        self.weight = weight #节点权重
        self.left = None #节点左孩子
        self.right = None #节点右孩子
        self.father = None # 节点父节点
    #判断是否是左孩子
    def is_left_child(self):
        return self.father.left == self  # 是左节点则1，否则0

#创建最初的叶子节点
def create_prim_nodes(labels,times):
    if(len(times) != len(labels)):
        raise Exception('数据和标签不匹配!')
    nodes = []
    for i in range(len(labels)):
        nodes.append( Node(labels[i],times[i]) )
    return nodes   # list 存放Node类


# 创建huffman树
def create_HF_tree(nodes):
    #copy()属于浅拷贝,因为nodes不能都删掉，需要用浅拷贝来做
    # 在浅拷贝时，拷贝出来的新对象的地址和原对象是不一样的，
    # 但是新对象里面的可变元素（列表）的地址与原对象里的可变元素的地址相同，
    # 也就是说浅拷贝它拷贝的是浅层次的数据结构（不可变元素），
    # 对象里的可变元素——深层次的数据结构并没有被拷贝到新地址里面去，
    # 而是和原对象里的可变元素指向同一个地址，
    # 所以在新对象或原对象里对这个可变元素做修改时，两个对象是同时改变的，
    # 这是浅拷贝相对于深拷贝最根本的区别。

    tree_nodes = nodes.copy() 
    while len(tree_nodes) > 1: #只剩根节点时，退出循环
        tree_nodes.sort(key=lambda node: node.weight)#以节点权重作为key，升序排列
        new_left = tree_nodes.pop(0)  #pop 删除
        new_right = tree_nodes.pop(0) #删除权重最小的两项
        new_node = Node(None, (new_left.weight + new_right.weight))
        new_node.left = new_left
        new_node.right = new_right
        new_left.father = new_right.father = new_node  # 构建父、子节点关系
        tree_nodes.append(new_node) #增加新的父节点
    tree_nodes[0].father = None #根节点父亲为None
    # return tree_nodes[0] #返回根节点

#获取huffman编码
# @pysnooper.snoop()
def get_huffman_code(nodes):
    encode = {}   # 编码结果存至字典
    for node in nodes:
        code=''
        name = node.name
        while node.father != None:
            if node.is_left_child():
                code = '0' + code
            else:
                code = '1' + code   #左0右1
            node = node.father
        encode[name] = code

    encode = dict(sorted(encode.items(),key = lambda x:len(x[1])))
    # 按编码由短到长排序
    return encode

#计算信息熵
@pysnooper.snoop("debug.log")
def calcHX(times):
    t = len(times)
    prob = 0  # 各字符出现的概率
    total = 0 # 总次数
    HX = 0 # 信息熵
    for each in range(t):  # 计算总次数
        total = total + times[each]

    for each in range(t):
        prob = times[each] / total
        HX = HX -prob * math.log2(prob)
    return HX

# 获取文本文档字符及其出现频次
def calcTXT(filename):
    txt = open(filename,'r',encoding='gbk')  # read读取字符
    char_txt = txt.read()
    count = Counter(char_txt)  # 得到count字典
    txt.close()
    return list(count.keys()),list(count.values())

if __name__ == '__main__':
    
    labels = ['b','a','c','d','e'] # labels 列表，存放字符名
    times = [2,1,3,4,34] # times 列表，存放字符出现次数

    # labels,times = calcTXT('研一学生共性工作.txt')

    nodes = create_prim_nodes(labels,times)#创建初始叶子节点
    create_HF_tree(nodes) #创建huffman树
    encode = get_huffman_code(nodes) #获取huffman编码
    HX = calcHX(times)

    #打印信息熵
    print('信息熵为:',HX)
    #打印huffman码
    for key in encode.keys():
        print(key,':',encode[key])