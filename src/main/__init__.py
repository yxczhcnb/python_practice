import en_ui
import wx


if __name__=="__main__":
    app = wx.App()
    frame = en_ui.en_ui(None,"En",size=(900,600))
    frame.Show()
    app.MainLoop()