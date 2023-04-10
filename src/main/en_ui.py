import wx
import read_data as epro

class en_ui(wx.Frame):
    __ICONPATH="res/OIP.jpg"
    __data=None
    __lastDate=None
    __choicesTranslation=[]
    __choices=[]
    __listBoxLength=0
    def __init__(self,parent,title,size):
        super().__init__(parent=parent,title=title,size=size)
        self.ep=epro.readData()
        self.__listBoxLength=self.ep.length
        splitter=wx.SplitterWindow(self,-1)
        self.panel1=wx.Panel(splitter,-1)
        self.panel2=wx.Panel(splitter,-1)
        self.createBut()
        self.createInputBorder()
        self.createPanel2Layout()
        self.createPanel1Layout()
        self.time=wx.Timer()
        self.eventBind()
        splitter.SplitVertically(self.panel1,self.panel2,730)
        self.createDisplayText()
        self.displayIcon()


    def createDisplayText(self):
        self.staticText_translation=wx.StaticText(self.panel1,label="请点击跳过，开始敲单词",pos=(5,100))
        self.staticText_translation.SetFont(wx.Font(12,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))
        self.staticText_word=wx.StaticText(self.panel1,pos=(340,260))
        self.staticText_word.SetFont(wx.Font(18,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))
        self.promptText=wx.StaticText(self.panel1,pos=(350,300))
        self.staticText_word.SetFont(wx.Font(16,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))
        self.accuracyText=wx.StaticText(self.panel1,pos=(328,20))
        self.accuracyText.SetFont(wx.Font(16,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))
        self.listBox.SetFont(wx.Font(14,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))

    def createInputBorder(self):
        self.t_ctr=wx.TextCtrl(self.panel1,-1,style=wx.TE_PROCESS_ENTER,size=(0,0))

    def createBut(self):
        self.lookBut=wx.Button(parent=self.panel1,label="瞟一眼")
        self.skipBut=wx.Button(parent=self.panel1,label="跳过")
        self.familiarBut=wx.Button(parent=self.panel1,label="熟悉")

    def displayIcon(self):
        self.familiarBut.Show(False)
        icon=wx.Icon(self.__ICONPATH,wx.BITMAP_TYPE_ANY)
        self.SetIcon(icon)


    def createPanel1Layout(self):
        self.gridBagSizer=wx.GridBagSizer(1,1)
        self.gridBagSizer.Add(self.lookBut,pos=(23,10))
        self.gridBagSizer.Add(self.skipBut,pos=(23,48))
        self.gridBagSizer.Add(self.familiarBut,pos=(23,28))
        self.gridBagSizer.Add(self.t_ctr,pos=(18,17),flag=wx.EXPAND)
        self.panel1.SetSizer(self.gridBagSizer)

    def createPanel2Layout(self):
        self.boxSizer=wx.BoxSizer(wx.HORIZONTAL)
        self.listBox=wx.ListBox(self.panel2,size=(150,0))
        self.boxSizer.Add(self.listBox,flag=wx.EXPAND|wx.ALL)
        self.panel2.SetSizerAndFit(self.boxSizer)

    def lookButOnClick(self,event):
        if self.__data==None:
            return
        self.staticText_word.SetLabel(self.__data[0])

    def lookButUp(self,event):
        self.staticText_word.SetLabel("")

    def skipButOnclick(self,event):
        self.time.Start(1000)
        self.familiarBut.Show(True)
        self.lookBut.Show(False)
        if self.__data!=None:
            self.__lastDate=self.__data
            self.__choices.insert(0,self.__lastDate[0]+" ×")
            self.__choicesTranslation.insert(0,self.__lastDate[1])
        self.__data=self.ep.data()
        if len(self.__choices)>0:
            self.accuracyCalculate()
            self.listBox.Set(self.__choices)
        if len(self.__choices)==self.__listBoxLength:
            self.__choices.pop()
        self.staticText_translation.SetLabel(self.__data[1])
        self.t_ctr.SetSize(300,30)

    def enterKeyOnclick(self,event):
        value=self.t_ctr.GetValue()
        if self.__data[0]==value:
            self.nextTranslation()
            self.accuracyCalculate()
            self.listBox.Set(self.__choices)
            self.lookBut.Show(False)
        else:
            self.promptText.SetLabel("输入不匹配!!!")
            self.promptText.SetForegroundColour("red")
            self.time.Start(3000)
            self.lookBut.Show(True)
        self.t_ctr.SetValue("")

    def nextTranslation(self):
        self.__lastDate=self.__data
        self.__choices.insert(0,self.__lastDate[0]+" √")
        self.__choicesTranslation.insert(0,self.__lastDate[1])
        self.__data=self.ep.data()
        self.staticText_translation.SetLabel(self.__data[1])

    def timing_display(self,event):
        self.promptText.SetLabel("")

    def familiarButOnclick(self,event):
        self.__data=self.ep.data()
        self.staticText_translation.SetLabel(self.__data[1])

    def displayWordTranslation(self,event):
        message=self.__choices[self.listBox.GetSelection()].split(" ")[0]+"\n"+ \
                self.__choicesTranslation[self.listBox.GetSelection()]
        self.messageDialog=wx.MessageDialog(self,message,"释义",style=wx.YES_DEFAULT)
        self.messageDialog.ShowModal()

    def accuracyCalculate(self):
        count=0
        for i in range(len(self.__choices)):
            if self.__choices[i].split(" ")[1]=="√":
                count+=1
        accuracy=round((count/(len(self.__choices))*100),2)
        self.accuracyText.SetLabel("正确率："+str(accuracy)+"%")

    def eventBind(self):
        self.lookBut.Bind(wx.EVT_ENTER_WINDOW,self.lookButOnClick)
        self.lookBut.Bind(wx.EVT_LEAVE_WINDOW,self.lookButUp)
        self.t_ctr.Bind(wx.EVT_TEXT_ENTER,self.enterKeyOnclick)
        self.skipBut.Bind(wx.EVT_BUTTON,self.skipButOnclick)
        self.familiarBut.Bind(wx.EVT_BUTTON,self.familiarButOnclick)
        self.time.Bind(wx.EVT_TIMER,self.timing_display)
        self.listBox.Bind(wx.EVT_LISTBOX,self.displayWordTranslation)
