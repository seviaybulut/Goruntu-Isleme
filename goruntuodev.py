# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:15:17 2021

@author: Mavi
"""


import numpy as np
import cv2
import os

from PyQt5.QtWidgets import QApplication,QTableWidgetItem, QMainWindow, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QTextEdit, QGridLayout, QComboBox
import sys
import tasariUI
import pandas as pd
import csv
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
import matplotlib.pyplot as plt


class Pencere(QMainWindow, tasariUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.yukle)
        self.pushButton_2.clicked.connect(self.yukle1)
        self.pushButton_3.clicked.connect(self.yukle2)

     
    #VERİLERİ COMBOBOXA ATTIM
    def yukle(self):
        imagelist=[]
        klasor='./dataset2/'    
        imagelist=os.listdir(klasor)
        i=0
        for resim in imagelist:
            resim=cv2.imread("./dataset2/"+resim)           
            #cv2.imshow('goster:',resim)#pencere
            #k = cv2.waitKey(0)
            print(imagelist[i]) 
            self.im = QPixmap("./dataset2")
            self.comboBox.addItems(imagelist)           
            i+=1

            
    #HİSTOGRAM
    def yukle1(self):        
        resim=cv2.imread('./dataset2/cloudy1.jpg')
        cv2.imshow('goster:',resim)#pencere
        k = cv2.waitKey(0)
        
        #cv2.convert()
        img = cv2.imread('cloudy1.jpg',0)
        equ = cv2.equalizeHist(img)
        res = np.hstack((img,equ)) #aynı sayfada gösterdi.
        cv2.imwrite('HIST.png',res)#yeni oluşan resim

    #CLAHE   
    def yukle2(self):  
        resim=cv2.imread('./dataset2/cloudy1.jpg')
        cv2.imshow('goster:',resim)#pencere
        k = cv2.waitKey(0)
        
        img = cv2.imread('cloudy1.jpg',0)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl1 = clahe.apply(img)
        cv2.imwrite('CLAHE.jpg',cl1)#yeni oluşan resim
        
        
        
        
        
        
        
        
        
        
        
        
        
        """plt.savefig('cloudy1.jpg')
        self.pixmap=QPixmap("/cloudy1.jpg")
        self.label.setPixmap(self.pixmap)"""
        
        #self.label.setPixmap(QtGui.QPixmap("./datase2/cloudy1.jpg"))
        
        
        """imagelist=[]
        klasor='./dataset2/'    
        imagelist=os.listdir(klasor)                   
        self.x=self.comboBox.currentIndex()
        if(self.x==self.comboBox.currentIndex()):
            plt.savefig('./cloudy1.jpg')
            self.pixmap=QPixmap("/cloudy1.jpg")
            self.label.setPixmap(self.pixmap)"""
        
app=QApplication(sys.argv)
pencere=Pencere()
pencere.show()
sys.exit(app.exec_())




'''
for resim in imagelist:
    cv2.imshow('goster:',resim)#pencere
    k = cv2.waitKey(0)
          
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img)
    cv2.imwrite('CLAHE.jpg',cl1)#yeni oluşan resim  
    
'''
    
           


