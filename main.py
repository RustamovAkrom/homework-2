import os
import csv
from pprint import pprint
import json

class FileRaider:
    def __init__(self, first, last=1, step=1):
        if last != 1:
            self.first = first
            self.last = last
        else:
            self.first = 1
            self.last = first

        self.step = step

    def __iter__(self):
        return self
    def __next__(self):
        val = self.first
        self.first += self.step
        if self.first > self.last: 
            raise StopIteration
        return val
def read_csv_file(file_name):
    with open(file_name, 'r') as read:
        print(read.readlines())
def get_discription():
    dir = os.listdir(derectory := "D:/5-oy/homeworks/homework-2/descriptions")
    for index in FileRaider(0, len(dir)):
        output = os.path.join(derectory, dir[index])
        with open(output,'r') as read:
            txt = read.readlines()
            for i in [i for i in txt]:
                write = open('text.csv','a')
                write.write(f"{str(i)}\n")
            write.close()
            
if __name__=='__main__':
    get_discription()  
    # read_csv_file('text.csv') 



#  lens = len(dir)
# def write_csv(text):
#     ls = [i for i in text]
#     for i in ls:
#         f = open("text.csv",'a')
#         f.write(f"{str(i)}\n")
#     f.close()
# write_csv(txt)
                
            # for w in name, lbs, comment:
            #     print(w)
