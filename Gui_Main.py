from PyQt4 import QtCore, QtGui
import sys
from first import find_first
from follow import find_follow
from finalclosures import getclosures
from gen_table import generate_table
from parse_input import parse_input


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        
        self.window = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(600, 614)
        self.centralwidget = QtGui.QWidget(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon("icon/icon.ico"))

        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.verticalLayout_2.addWidget(self.textBrowser_2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setToolTip("Follow")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setToolTip("First")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setToolTip("Parsing table")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setToolTip("Parse input")
        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.setToolTip("LR0 Items")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 275, 336))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 290, 351))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser.setToolTip("Empty grammar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.textBrowser_3 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.textBrowser_3.setToolTip("There is nothing to show")
        self.gridLayout_3.addWidget(self.textBrowser_3, 1, 0, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        #menu bar
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        # Open action
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen.triggered.connect(self.actionOpenFile)
        #Exit action
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.triggered.connect(QtGui.qApp.quit)

        #About action
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout.triggered.connect(self.actionOfAbout)

        #Refresh action
        self.actionRefresh = QtGui.QAction(MainWindow)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionRefresh.triggered.connect(self.RefreshGui)

        
        #First shortcut
        self.actionFirst = QtGui.QAction(MainWindow)
        self.actionFirst.setObjectName(_fromUtf8("First"))
        self.actionFirst.triggered.connect(self.getFirst)
        #Follow shortcut
        self.actionFollow = QtGui.QAction(MainWindow)
        self.actionFollow.setObjectName(_fromUtf8("Follow"))
        self.actionFollow.triggered.connect(self.getFollow)

        #Parse table shortcut
        self.actionParseTable = QtGui.QAction(MainWindow)
        self.actionParseTable.setObjectName(_fromUtf8("actionParseTable"))
        self.actionParseTable.triggered.connect(self.getParsingTable)

        #Item set shortcut
        self.actionItemSet = QtGui.QAction(MainWindow)
        self.actionItemSet.setObjectName(_fromUtf8("LR0 Items"))
        self.actionItemSet.triggered.connect(self.getClosureItems)

        #Run - Parse input

        self.input_string = ""
        self.parse_complete = False

        self.actionParse = QtGui.QAction(MainWindow)
        self.actionParse.setObjectName(_fromUtf8("LR0 Parsing"))
        self.actionParse.triggered.connect(self.getInputToParse)

        #New input action
        self.newInput = QtGui.QAction(MainWindow)
        self.newInput.setObjectName(_fromUtf8("newInput"))
        self.newInput.triggered.connect(self.getNewInput)


        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addAction(self.newInput)
        self.menuFile.addAction(self.menuFile.addSeparator())
        self.menuFile.addAction(self.actionFirst)
        self.menuFile.addAction(self.actionFollow)
        self.menuFile.addAction(self.actionParseTable)
        self.menuFile.addAction(self.actionItemSet)
        self.menuFile.addAction(self.actionParse)
        self.menuFile.addAction(self.menuFile.addSeparator())
        self.menuFile.addAction(self.actionExit)

        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        #Connect each button to respective Event handlers
        #for first
        MainWindow.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.getFirst)
        #for follow
        MainWindow.connect(self.pushButton_2,QtCore.SIGNAL("clicked()"),self.getFollow)
        #for closures
        MainWindow.connect(self.pushButton_3,QtCore.SIGNAL("clicked()"),self.getClosureItems)
        #for generate tables
        MainWindow.connect(self.pushButton_4,QtCore.SIGNAL("clicked()"),self.getParsingTable)
        #To parse input
        
        MainWindow.connect(self.pushButton_5,QtCore.SIGNAL("clicked()"),self.getInputToParse)

        
        
        #Its a grammar list
        self.grammar_list = []
        
        self.retranslateUi(MainWindow)
        MainWindow.setWindowTitle("LR0 Parser")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def RefreshGui(self):
        #print "refresh clicked"
        self.textBrowser.clear()
        self.textBrowser.setToolTip("Empty grammar")
        self.grammar_list = []
        self.input_string = ""
        self.parse_complete = False
        self.textBrowser_3 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.textBrowser_3.setToolTip("There is nothing to show")
        self.gridLayout_3.addWidget(self.textBrowser_3, 1, 0, 1, 2)
        

    def actionOpenFile(self):
        self.grammar_list = []
        self.input_string = ""
        self.parse_complete = False
        self.textBrowser_3 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.textBrowser_3.setToolTip("There is nothing to show")
        self.gridLayout_3.addWidget(self.textBrowser_3, 1, 0, 1, 2)
        
        self.file_name = QtGui.QFileDialog.getOpenFileName()
        #print file_name
        #print "hey"
        f = open(self.file_name,"r")
        self.textBrowser.setText(f.read())
        f.close()
        grammar = list(self.textBrowser.toPlainText().split("\n"))
        self.textBrowser.setToolTip("Grammar")
        #print self.grammar_list
        #self.grammar_list = []
        for eachElement in grammar:
            eachElement = str(eachElement)
            self.grammar_list.append(eachElement)
        self.grammar_list.pop()
        


    
    def getFirst(self):
        #print "first is called"
        self.textBrowser_3 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.gridLayout_3.addWidget(self.textBrowser_3, 1, 0, 1, 2)
        
                
        first = []
        if len(self.grammar_list) == 0:
            self.showWarningMsg()
        else:
            grammar = {}
            for eachElement in self.grammar_list:
                eachElement = eachElement.replace(" ","")
                production = eachElement.split("->")
                if grammar.has_key(production[0]):
                    grammar[production[0]].append(production[1])
                else:
                    grammar[production[0]] = [production[1]]
            #print grammar
            first = find_first(grammar)
            #print first
            self.showFirst(first)
            


    def showFirst(self,first):

        #print first
        
        self.textBrowser_3.clear()
        self.textBrowser_3.append("<font color = 'blue' ><b>First Set</b></font>")
        self.textBrowser_3.append("<font color = 'blue'>" + "-" * 50 +"</font>")
        for eachKey in first:
            line = "<font color = 'blue'>First(" + eachKey + ") : </font>"
            for eachElement in first[eachKey]:
                line = line + "  " + eachElement
            self.textBrowser_3.append(line) 
            self.textBrowser_3.append("\n")
        self.textBrowser_3.setToolTip("First set")

    def getFollow(self):
        
        self.textBrowser_3 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.gridLayout_3.addWidget(self.textBrowser_3, 1, 0, 1, 2)
        
        if len(self.grammar_list) == 0:
            self.showWarningMsg()
        else:
            follow = find_follow(self.grammar_list)

            self.showFollow(follow)

    def showFollow(self,follow):
        
        self.textBrowser_3.clear()
        self.textBrowser_3.append("<font color = 'blue' ><b>Follow Set</b></font>")
        self.textBrowser_3.append("<font color = 'blue'>" + "-" * 50 +"</font>")
        for eachKey in follow:
            line = "<font color = 'blue'>Follow(" + eachKey + ") :</font> "
            for eachElement in follow[eachKey]:
                line = line + "  " + eachElement
            self.textBrowser_3.append(line ) 
            self.textBrowser_3.append("\n")
        self.textBrowser_3.setToolTip("Follow set")

    def getClosureItems(self):
        
        self.textBrowser_3 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.gridLayout_3.addWidget(self.textBrowser_3, 1, 0, 1, 2)
        
        if len(self.grammar_list) == 0:
            self.showWarningMsg()
        else:
            grammar_list = self.grammar_list[:]
            states = getclosures(grammar_list)
            #print states
            
            self.showStates(states)

    def showStates(self,states):
        
        self.textBrowser_3.clear()
        self.textBrowser_3.append("<font color = 'blue' ><b>LR0 Items</b></font>")
        self.textBrowser_3.append("<font color = 'blue'>" + "-" * 50 +"</font>")
        i = 0;
        for eachState in states:
            if i == 0:
                self.textBrowser_3.append("<font style = 'text-decoration:underline' color = 'blue'>"+"State " + str(eachState['to'][0]) + " : "+"</font>")
                i += 1
            else:
                self.textBrowser_3.append("<font style = 'text-decoration:underline' color = 'blue'>"+"State " + str(eachState['to'][0]) + " : " + " goto(" + str(eachState['from'][0]) + "," + str(eachState['on'][0]) + " ) :"+"</font>")
            for eachElement in eachState.keys():
                if eachElement not in ('from','to','on'):
                    for eachRighHandSide in eachState[eachElement]:
                        self.textBrowser_3.append(eachElement + "->" + eachRighHandSide)
            
            self.textBrowser_3.append("\n")
        self.textBrowser_3.setToolTip("LR0 Items")

 
    def getParsingTable(self):
        if len(self.grammar_list) == 0:
            self.showWarningMsg()
        else:
            grammar_list = self.grammar_list[:]
            
            parsing_table = generate_table(grammar_list)
            self.showParsingTable(parsing_table)



    def showParsingTable(self,parsing_table):
        
        
        self.table = QtGui.QTableWidget()
        self.makeTable(self.table,parsing_table)
        self.gridLayout_3.addWidget(self.table, 1, 0, 1, 2)

    def makeTable(self,table,parsing_table):
        table.setRowCount(len(parsing_table))
        symbols_list = parsing_table[0].keys() # symbol list has keys
        table.setColumnCount(len(symbols_list)) 
        non_terminal_list = []
        terminal_list = []
        for eachSymbol in symbols_list:
            if eachSymbol.isupper():
                non_terminal_list.append(eachSymbol)
            else:
                terminal_list.append(eachSymbol)
        if "$" in terminal_list:
            terminal_list.remove("$")
            terminal_list.append("$")
        symbols = ""
        for eachSymbol in terminal_list:
            symbols = symbols + str(eachSymbol) + " "
        for eachSymbol in non_terminal_list:
            symbols = symbols + str(eachSymbol) + " "
        symbols = symbols.strip()
        #print symbols
        #set the horizontal header
        table.setHorizontalHeaderLabels(symbols.split(" "))
        #table.horizontalHeader().setDefaultSectionSize(60)
        table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        #item.setFlags(QtCore.Qt.ItemIsEnabled) - to make an item not editable
        #setItem (self, int row, int column, QTableWidgetItem item)
        #set vertical header
        vertical_header = []
        for i in range(len(parsing_table)):
            vertical_header.append(str(i))
        table.setVerticalHeaderLabels(QtCore.QStringList(vertical_header))
        table.verticalHeader().setDefaultSectionSize(30)
        table.verticalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        #Now its time to populate table accroding to parsing table
        symbols_list = symbols.split(" ")
        #print symbols_list
        #print parsing_table

        for i in range(len(parsing_table)):
            j = 0
            for eachSymbols in symbols_list:
                item = QtGui.QTableWidgetItem(parsing_table[i][eachSymbols])
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                table.setItem(i,j,item)
                j = j + 1
        table.setToolTip("Parsing Table")


    def getInputToParse(self):

        #self.input_string = ""
        #self.parse_complete = False
        
        grammar_list = self.grammar_list[:]
        
        if len(self.grammar_list) == 0:
            self.showWarningMsg()
        else:
            if len(self.input_string) == 0:
                input_string , ok = QtGui.QInputDialog.getText(self.window,"Input","Enter the input string to parse")
                if ok:
                    self.input_string = str(input_string).strip()

            parse_info = parse_input(grammar_list,self.input_string)
            self.showParsing(parse_info)

    def getNewInput(self):
        if len(self.grammar_list) == 0:
            self.showWarningMsg()
        else:
            self.input_string = ""
            self.parse_complete = False
            self.final_table.clear()
            self.getInputToParse()
            
            
            

    def showParsing(self,parse_info):
        
        self.final_table = QtGui.QTableWidget()
        self.makeFinalTable(self.final_table,parse_info)
        self.gridLayout_3.addWidget(self.final_table, 1, 0, 1, 2)
        self.final_table.setToolTip("LR0 Parsing Table")

    def makeFinalTable(self,table,parse_info):

        if parse_info == "Invalid symbol found":
            msg_box = QtGui.QMessageBox()
            self.parse_complete = True
            msg_box.setWindowTitle("Rejected")
            msg_box.setText("The input is rejected!!")
            msg_box.setIconPixmap(QtGui.QPixmap("icon/wrong.png"))
            msg_box.exec_()

        elif parse_info == "Empty string":
            msg_box = QtGui.QMessageBox
            self.parse_complete = True
            msg_box.warning(self.window,"Empty input","Please enter an input string")
            
        else:
            no_of_steps = len(parse_info)
            #make the table now
            table.setRowCount(no_of_steps)
            table.setColumnCount(4)

            table.setHorizontalHeaderLabels("STACK,SYMBOLS,INPUT,ACTION".split(','))
            
            i = 0
            for eachLine in parse_info:
                item = QtGui.QTableWidgetItem(self.getStringForm(eachLine['stack']))
                
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                table.setItem(i,0,item)
                item = QtGui.QTableWidgetItem(self.getStringForm(eachLine['symbols']))
                
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                table.setItem(i,1,item)
                item = QtGui.QTableWidgetItem(self.getStringForm(eachLine['input']))
                
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                table.setItem(i,2,item)
                item = QtGui.QTableWidgetItem(eachLine['state'])

                item.setFlags(QtCore.Qt.ItemIsEnabled)
                table.setItem(i,3,item)
                i = i + 1
            
            if not self.parse_complete:
                self.popUpResult(parse_info)

    def popUpResult(self,parse_info):
        
        msg_box = QtGui.QMessageBox()
        if self.input_string:
            if parse_info[len(parse_info) - 1]['state'] == 'accept':
                self.parse_complete = True
                msg_box.setWindowTitle("Accepted")
                msg_box.setText("The input is accepted!!")
                msg_box.setIconPixmap(QtGui.QPixmap("icon/correct.png"))
                msg_box.exec_()
            else:
                self.parse_complete = True
                msg_box.setWindowTitle("Rejected")
                msg_box.setText("The input is rejected!!")
                msg_box.setIconPixmap(QtGui.QPixmap("icon/wrong.png"))
                msg_box.exec_()
        else:
            msg_box.warning(self.window,"No input","Please Enter an input string")
            self.final_table.clear()

    def getStringForm(self,symbols_list):
        string = ""

        for eachSymbol in symbols_list:
            eachSymbol = eachSymbol.replace("[","")
            eachSymbol = eachSymbol.replace("]","")
            eachSymbol = eachSymbol.replace("'","")
            eachSymbol = eachSymbol.replace(",","")
            string = string + " " + eachSymbol

        
        return string




    def showWarningMsg(self):
        msg_box = QtGui.QMessageBox
        msg_box.warning(self.window,"No grammar specified","Please load a grammar from file!!!")


    def actionOfAbout(self,MainWindow):
        msg_box = QtGui.QMessageBox
        msg_box.information(self.window,"About","<font color = 'blue'>LR0 Parser</font>\n <p>Developed by:</p> \n Abhinav \n<p>Bhuvan</p> \n <p> Krishna </p>\n<p>Venkatesh</p>\n <p>Pravardhan</p>\n ")
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'sans-serif\'; font-size:11pt; font-weight:400; font-style:normal;\" bgcolor=\"#00ccff\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"head\"></a><span style=\" font-family:\'sans-serif\'; font-size:x-large; font-weight:600; color:#0000ff;\">L</span><span style=\" font-family:\'sans-serif\'; font-size:x-large; font-weight:600; color:#0000ff;\">R0 Parser</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#0000ff;\">A parser which parses the string using a LR0 grammar</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">Note:</span> <span style=\" color:#0000ff;\">Use \'e\' for epsilon</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Follow set", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", " First set", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Parsing Table", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "Parse Input", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "LR0 Items", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Grammar:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
      
        self.actionRefresh.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setText(QtGui.QApplication.translate("MainWindow","&Refresh",None,QtGui.QApplication.UnicodeUTF8))
      
        self.newInput.setShortcut(QtGui.QApplication.translate("MainWindow","Ctrl+N",None,QtGui.QApplication.UnicodeUTF8))
        self.newInput.setText(QtGui.QApplication.translate("MainWindow","&New input",None,QtGui.QApplication.UnicodeUTF8))

        self.actionFirst.setShortcut(QtGui.QApplication.translate("MainWindow","Ctrl+F",None,QtGui.QApplication.UnicodeUTF8))
        self.actionFirst.setText(QtGui.QApplication.translate("MainWindow","&First",None,QtGui.QApplication.UnicodeUTF8))

        self.actionFollow.setShortcut(QtGui.QApplication.translate("MainWindow","Ctrl+A",None,QtGui.QApplication.UnicodeUTF8))
        self.actionFollow.setText(QtGui.QApplication.translate("MainWindow","&Follow",None,QtGui.QApplication.UnicodeUTF8))

        self.actionParseTable.setShortcut(QtGui.QApplication.translate("MainWindow","Ctrl+P",None,QtGui.QApplication.UnicodeUTF8))
        self.actionParseTable.setText(QtGui.QApplication.translate("MainWindow","&Parse Table",None,QtGui.QApplication.UnicodeUTF8))

        self.actionItemSet.setShortcut(QtGui.QApplication.translate("MainWindow","Ctrl+I",None,QtGui.QApplication.UnicodeUTF8))
        self.actionItemSet.setText(QtGui.QApplication.translate("MainWindow","&LR0 Items",None,QtGui.QApplication.UnicodeUTF8))

        self.actionParse.setShortcut(QtGui.QApplication.translate("MainWindow","Ctrl+F5",None,QtGui.QApplication.UnicodeUTF8))
        self.actionParse.setText(QtGui.QApplication.translate("MainWindow","&Parse Input",None,QtGui.QApplication.UnicodeUTF8))

        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        
if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

