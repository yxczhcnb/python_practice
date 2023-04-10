import  read_csv as rc

class readData():
    __index=0
    length=0
    __csv=None
    def __init__(self):
        self.__csv=rc.en_csv()
        self.length=self.__csv.length
    def data(self):
        if self.__index<self.__csv.length:
            self.word=self.__csv.read_word(self.__index)
            self.translation=self.__csv.read_tanslation(self.__index).\
                replace(";","\n").replace("/","\n")
            self.__index+=1
            return [self.word,self.translation]
        else:
            self.__index=0
