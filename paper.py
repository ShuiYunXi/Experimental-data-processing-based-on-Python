from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtCore import Qt

from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
fontproperties=font_set




class Paper:

        def __init__(self):
            # 从文件中加载UI定义
            qfile_stats = QFile("ui/paper.ui")
            qfile_stats.open(QFile.ReadOnly)
            qfile_stats.close()
            # 从 UI 定义中动态 创建一个相应的窗口对象
            # 注意：里面的控件对象也成为窗口对象的属性了
            # 比如 self.ui.button , self.ui.textEdit
            self.ui = QUiLoader().load(qfile_stats)
            self.ui.pushButton.clicked.connect(self.deal_data)  # 按钮1
            self.ui.pushButton_2.clicked.connect(self.handleCalc1)
            #try:
            #    self.ui.pushButton.clicked.connect(self.deal_data)  # 按钮1
            #    self.ui.pushButton_2.clicked.connect(self.handleCalc1)
            #except BaseException as b:
            #    print("请将数据填入表格内！")
            #    print(b)
            #except ValueError as e:
            #    print(e)
            #else:
            #    print('程序运行正常')
            self.ui.lineEdit.setPlaceholderText('螺旋测微器的仪器误差')
            self.ui.lineEdit_2.setPlaceholderText('螺旋测微器的零点误差')
            self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
            #合并单元格
            self.ui.tableWidget.setSpan(2, 0, 2, 1)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  2行数  1列数
            self.ui.tableWidget.setSpan(1, 0, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(4, 0, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(4, 0, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(5, 0, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(6, 0, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(7, 0, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(8, 0, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            #self.ui.tableWidget.setSpan(0, 0, 2, 1)  # 其参数为： 要改变单元格的   1行数  2列数     要合并的  3行数  4列数
            self.ui.tableWidget.setSpan(7, 2, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(6, 2, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(5, 2, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(8, 2, 1, 6)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(7, 4, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(6, 4, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(5, 4, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(7, 6, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(6, 6, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数
            self.ui.tableWidget.setSpan(5, 6, 1, 2)  # 其参数为： 要改变单元格的   1行数  0列数     要合并的  1行数  2列数

            #设定表格文字参数
            self.ui.tableWidget.setItem(1, 0, QTableWidgetItem('砝码（拉力）Kg'))
            self.ui.tableWidget.setItem(2, 0, QTableWidgetItem('望远镜标尺读数你(cm)'))  # 参数 1行，0列
            self.ui.tableWidget.setItem(4, 0, QTableWidgetItem('金属丝直径d_ (mm)'))
            self.ui.tableWidget.setItem(5, 0, QTableWidgetItem('平面镜与标尺的距离D(cm)'))
            self.ui.tableWidget.setItem(6, 0, QTableWidgetItem('光杠杆臂长b(cm)'))
            self.ui.tableWidget.setItem(7, 0, QTableWidgetItem('钢丝长L(cm)'))
            self.ui.tableWidget.setItem(8, 0, QTableWidgetItem('拉力F(N)'))

            self.ui.tableWidget.setItem(2, 1, QTableWidgetItem('增加砝码'))
            self.ui.tableWidget.setItem(3, 1, QTableWidgetItem('减少砝码'))
            self.ui.tableWidget.setItem(2, 1, QTableWidgetItem('增加砝码'))
            self.ui.tableWidget.setItem(5, 4, QTableWidgetItem('U_d'))
            self.ui.tableWidget.setItem(6, 4, QTableWidgetItem('U_b'))
            self.ui.tableWidget.setItem(7, 4, QTableWidgetItem('U_l'))
            #文本居中对齐
            #self.ui.tableWidget.setTextAlignment(Qt.AlignHCenter)
            #self.ui.qtablewidge.item(1, 0).setTextAlignment(Qt.AlignHCenter)
            item = QTableWidgetItem()
            item.setText('砝码（拉力）Kg')
            item.setTextAlignment(Qt.AlignHCenter)
            self.ui.tableWidget.setItem(1, 0, item)
            #单元格不允许操作
            #self.ui.QTableWidgetItem('减少砝码').setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改# 设定列的宽度为 100像素
            #x=0
            #while x<5:
            #    self.ui.tableWidget.setColumnWidth(x, 100)
            #    x+=1

        def handleCalc(self):
            info = self.ui.plainTextEdit.toPlainText()  # toPlainText 方法获取编辑框内的文本内容
            QMessageBox.about(self.ui, "输入得结果为", info)

        def abs(self,y):
            if y<0:
                return -y
            else:
                return y
        def deal_data(self):
            print('这是一个测试')
            # 计算数值
            instrumental_error = self.ui.lineEdit.text()  # 仪器误差
            print(instrumental_error)
            zero_error = self.ui.lineEdit_2.text()  # 零点误差
            # 获取表格得数据
            # 就获取了 第1行，第1列 的单元格里面的文本 table.item(0, 0).text()
            # self.ui.plainTextEdit_2.setPlainText('望远镜标尺读数n（mm）:')
            read_scopdata_av = 0
            lst1 = []  # 存储砝码的平均值
            lst2 = []  # 存储变化量的平均值
            lst3 = []  #存储直径的变化量
            lst4 = [] #存储获取到的金属丝的直径
            for x in range(0, 6):  # 获取望远镜标尺读数你(cm)
                #self.ui.tableWidget.setItem(0, i, new QTableWidgetItem(""))
                read_scopdata_1 = self.ui.tableWidget.item(2,x+2).text()
                read_scopdata_2 = self.ui.tableWidget.item(3,x+2 ).text()
                read_scopdata_av = (float(read_scopdata_1)+float(read_scopdata_2))/2
                lst1.append(read_scopdata_av)
                # 求解变化量的平均值
            print(lst1)
            for i in range(0, 3):
                read_scopdata_3 =lst1[i+2]-lst1[i]
                delt_n_av = read_scopdata_3/3
                print('read_scopdata_3=',read_scopdata_3)
                test=abs(abs(delt_n_av)-abs(read_scopdata_3))
                lst2.append(abs(delt_n_av-read_scopdata_3))
                print('delt_n_av=',abs(delt_n_av))
            print('lst2=',lst2)
            print('test=',test)
            #计算金属丝的平均直径d
            d_av=0.0
            delt_d_av =0.0
            read_Ddata_5 = 0.0
            for i in range(0, 6):
                read_Ddata_4 = self.ui.tableWidget.item(4, i + 2).text()
                lst4.append(read_Ddata_4)
                read_Ddata_5+=float(read_Ddata_4)
                d_av=read_Ddata_5/5
            print(d_av)
            for i in range(0, 6):
                delt_d = abs(d_av - float(lst4[i]))
                delt_d_av += delt_d
                lst3.append(delt_d)
            print(lst3)
            print(delt_d_av/5)
            #平面镜与标尺的距离D(cm)
            distance_D = self.ui.tableWidget.item(5, 2).text()
            #光杠杆臂长b(cm)
            arm_length = self.ui.tableWidget.item(6, 2).text()
            #钢丝长L(cm)
            matiral_length = self.ui.tableWidget.item(7, 2).text()
            #u_d
            U_D = self.ui.tableWidget.item(5, 6).text()
            #U_b
            U_b = self.ui.tableWidget.item(6, 6).text()
            #u_l
            U_l = self.ui.tableWidget.item(7, 6).text()
            #拉力F(N)
            F_N = self.ui.tableWidget.item(8, 2).text()
            # #求解误差
            U_d =float(instrumental_error)+delt_d_av
            print(U_d)
            #u_∆n=(∆(∆n) ) ̅+∆仪_∆n
            #U_deltn = abs(delt_n_av)+float(instrumental_error)
            U_deltn =delt_d_av + float(instrumental_error)
            print(U_deltn)

            print('平面镜与标尺的距离D(cm)',distance_D)
            print('臂长', arm_length)
            print('钢丝', matiral_length)
            print('U_b=', U_b)
            print('u_d=', U_D)
            print('u_l=', U_l)
            print('F_N=', F_N)
            #数据处理
            E=(8*float(F_N)*(float(arm_length)/100.0)*(float(distance_D))/(3.142*(delt_d_av/5))*(delt_d_av/5)*(float(arm_length)/100.0)*(abs(delt_n_av)/100.0))  #求解杨氏模量
            UE_DIV=(float(U_D)/(float(distance_D)))+(float(U_b)/(float(arm_length)))+(float(U_l)/(float(matiral_length)))+(2*float(U_d))/(float(distance_D))+(float(U_deltn)/abs(delt_n_av))      #求U/E
            U_E=float(E)*float(UE_DIV)
            ADD_UE=E+U_E
            SUB_UE=E-U_E

            #显示结果
            self.ui.plainTextEdit_2.clear()
            self.ui.plainTextEdit_2.appendPlainText("E=")
            self.ui.plainTextEdit_2.insertPlainText(str(E))
            self.ui.plainTextEdit_2.insertPlainText(',')
            self.ui.plainTextEdit_2.appendPlainText("UE_DIV=")
            self.ui.plainTextEdit_2.insertPlainText(str(UE_DIV))
            self.ui.plainTextEdit_2.insertPlainText(',')
            self.ui.plainTextEdit_2.appendPlainText("ADD_UE=")
            self.ui.plainTextEdit_2.insertPlainText(str(ADD_UE))
            self.ui.plainTextEdit_2.insertPlainText(',')
            self.ui.plainTextEdit_2.appendPlainText("SUB_UE=")
            self.ui.plainTextEdit_2.insertPlainText(str(SUB_UE))

            QMessageBox.about(self.ui, "结果","数据分析完毕！")
           # 图表分析

        def handleCalc1(self):
            # 如果只传入一个数组作为参数， matplotlib 认为是 Y 轴的坐标
            # 并自动产生 从 0 开始的 对应 X 轴坐标： 0、1、2、3 ...
            plt.plot([2, 4, 6, 8])
            plt.ylabel('杨氏模量变化', fontproperties=font_set)
            plt.xlabel('拉力变化' ,fontproperties=font_set)
            plt.title('杨氏模量随拉力的变化曲线', fontproperties=font_set)  # subplot 211 title
            plt.show()



                #if(read_scopdata == ""):
                #   print("错误！")
                #read_scopdata_1 = int(read_scopdata) + read_scopdata_1
                #print(read_scopdata_1)
                #显示数据
            #for i in range(0, 5):
            #lst1 = []
            #read_diameter = self.ui.tableWidget.item(2, i).text()  # 金属丝直径d_ (mm)
            #lst1.append(read_diameter)
            #print(lst1)
            #for i in range(0, 5):
            #    lst2 = []
                #read_distance = self.ui.tableWidget.item(3, i).text()  # 平面镜与标尺的距离D(cm)
                #lst2.append(read_distance)
            #print(lst2)

            #for i in range(0, 5):
                #   lst3 = []






app = QApplication([])
paper = Paper()
paper.ui.show()
app.exec_()
