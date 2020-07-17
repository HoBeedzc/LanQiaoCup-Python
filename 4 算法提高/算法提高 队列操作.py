# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:41:19 2019

@author: 和毕
"""

class Queue:
    def __init__(self):
        self.items=[]
    #创建一个队列
    def isEmpty(self):
        return self.items == []
    #判断队列是否为空
    def enqueue(self,item):
        self.items.insert(0,item)
    #在队尾添加新元素
    def dequeue(self):
        return self.items.pop()
    #在队首移除一个元素并返回，队列此时被修改
    def peek(self):
        return self.items[-1]
    #返回队首元素，但不移除
    def size(self):
        return len(self.items)
    #返回队中元素个数
    def get_items(self):
        return self.items

if __name__=="__main__":
    n = int(input())
    q = Queue()
    for i in range(n):
        temp = list(map(int,input().split()))
        if temp[0] == 1:
            q.enqueue(temp[-1])
        elif temp[0] == 2:
            try:
                print(q.dequeue())
            except IndexError:
                print("no")
                exit()
        else:
            print(q.size())