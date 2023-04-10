import pandas as pd

"""
使用pandas读取CSV文件
"""
class en_csv:
    __SOURCE_PATH="res/EnWords.csv"
    word=""
    translation=""
    length=0
    def __init__(self):
        self.csv=pd.read_csv(self.__SOURCE_PATH)
        self.word=self.csv.keys()[0]
        self.translation=self.csv.keys()[1]
        self.length=self.csv.__len__()

    def read_word(self,index):
        return self.csv.iloc[index][self.word]

    def read_tanslation(self,index):
        return self.csv.iloc[index][self.translation]


