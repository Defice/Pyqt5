from PyQt5 import QtWidgets, QtCore, QtGui
from AddDataSet import Ui_MainWindow
import sys
# import win32con
# import win32gui
# import pyautogui
# import time
# import os
# def read_table(Elem):
#     #df = pd.read_excel('RTSN.xlsx')
#     future_rst = []
#     first_line = '123                                             24.10.900'
#     second_line = f'10.0    10    9'
#     third_line = f'  25. 20.0  6.3  .0010.50  .0015.00 81.50'
#     f_line = f'  25. 20.0  6.3  .0010.50  .0015.00 81.50'
#     fife_line = f'  32.230.0  6.3  .0011.50  .0014.00101.20            1\n'
#     six_line = f'1C      .2                                                  '
#     new_line = []
#
#     new_line.append(Elem)
#
#
#    for
#
#     future_rst.append(second_line)
#     future_rst.append(third_line)
#     f = open('new.txt','w')
#     for index in future_rst:
#         f.write(index+'\n')


NAME={'PEN':1,'KN1':2,'KN2':3,'BEN':4,'CN':5,'NZK':6,'NPE':7,"D":8,'DV':9,
   'VGD':10,'MV':11, 'NNCM':12, 'NPT':13}

class mywindow(QtWidgets.QMainWindow):
    a=[]
    def GetDV(self):
        DV1 = self.ui.lineEdit.text()
        DV2 = self.ui.lineEdit_2.text()
        DV3 = self.ui.lineEdit_7.text()
        DV4 = self.ui.lineEdit_3.text()
        DV5 = self.ui.lineEdit_8.text()
        DV6 = self.ui.lineEdit_4.text()
        DV7 = self.ui.lineEdit_5.text()
        DV8 = self.ui.lineEdit_6.text()
        DV9 = self.ui.lineEdit_9.text()
        DV10 = self.ui.lineEdit_10.text()
        DV11 = self.ui.lineEdit_11.text()
        DV12 = self.ui.lineEdit_12.text()
        DV13 = self.ui.lineEdit_13.text()
        DV14 = self.ui.lineEdit_14.text()
        DV15 = self.ui.lineEdit_15.text()
        DV16 = self.ui.lineEdit_16.text()
        DV17 = self.ui.lineEdit_17.text()
        DV18 = self.ui.lineEdit_18.text()
        DV19 = self.ui.lineEdit_19.text()
        DV=[DV1,DV2,DV3,DV4,DV5,DV6,DV7,DV8,DV9,DV10,DV11,DV12,DV13,DV14,DV15,DV16,DV17,DV18,DV19]
        s = ''
        for i in range(0,len(DV)):
            s += str(DV[i])+' '
        self.ui.textEdit.append(s)
        a.append(DV)
        return DV
    def clearLineedit(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_9.clear()
        self.ui.lineEdit_10.clear()
        self.ui.lineEdit_11.clear()
        self.ui.lineEdit_12.clear()
        self.ui.lineEdit_13.clear()
        self.ui.lineEdit_14.clear()
        self.ui.lineEdit_15.clear()
        self.ui.lineEdit_16.clear()
        self.ui.lineEdit_17.clear()
        self.ui.lineEdit_18.clear()
        self.ui.lineEdit_19.clear()
    def clearText(self):
        self.ui.textEdit.clear()
        print(a)
        a.clear()
    # def do_RST(self):
    #     C1=[]
    #     C2=[]
    #     C3=[]
    #     line_1 = '123                                             24.10.900'
    #     line_2 = f'10.0    10    9'
    #     line_3 = f'  25. 20.0  6.3  .0010.50  .0015.00 81.50'
    #     line_4 = f'  25. 20.0  6.3  .0010.50  .0015.00 81.50'
    #     line_5 = f'  32.230.0  6.3  .0011.50  .0014.00101.20            1\n'
    #     line_6 = f'1C      .2                                                  '
    #     for i in a:
    #         if i[17] != 0:
    #             if (i[0] in list(NAME.keys())):
    #                 C1.append(f'  {i[0]}         {NAME.setdefault(i[0])}          {i[2]} {i[15]}{i[10]}  {i[11]} {i[13]}  {i[12]} {i[14]}')
    #         if i[18] != 0:
    #             if (i[0] in list(NAME.keys())):
    #                 C2.append(f'  {i[0]}         {NAME.setdefault(i[0])}          {i[2]} {i[15]}{i[10]}  {i[11]} {i[13]}  {i[12]} {i[14]}')
    #     if len(C1) <=20:
    #         for i in range(0,20-len(C1)):
    #             C1.append(' ')
    #     if len(C2) <=20:
    #         for i in range(0,20-len(C2)):
    #             C1.append(' ')
    #     line_7 = '2C      .2                                                  '
    #     line_8 = '3C        .2                                                                \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
    #     line_9 = '4C        .2                                                                \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
    #     for i in a:
    #         for j in list(NAME.keys()):
    #             if list(NAME.keys()[j]) == i[0]:
    #                 C3.append(f'  {NAME.setdefault(i[0])} {i[1]}{i[5]} {i[6]}   {i[4]/100} {i[8]}  {i[7]}  {i[9]}  {i[16]}     ')
    #     if len(C3) <=20:
    #         for i in range(0,20-len(C3)):
    #             C1.append(' ')
    #     line_10 = ''
    #     new_line =[line_1,line_2,line_3,line_4,line_5,line_6,C1,line_7,C2,line_8,line_9,C3,line_10]
    #     print(new_line)
    def textEdittext(self):
        print(len(self.ui.textEdit.toPlainText()))
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.GetDV)
        self.ui.pushButton_2.pressed.connect(self.textEdittext)
        self.ui.pushButton_2.pressed.connect(self.clearText)
        self.ui.pushButton_3.pressed.connect(self.clearLineedit)
        self.ui.pushButton_4.pressed.connect(self.do_RST)
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())

