#-*-coding:utf8;-*-
import InputUtils
import datetime
from time import sleep
from random import randint
import bagua

def getNextYao(yaoTime):
    if yaoTime.microsecond%1000==0:
        if (yaoTime.microsecond/1000)%2==0:
            #阳爻
            return 1
        else:
            #阴爻
            return 0
    else:
        if (yaoTime.microsecond)%2==0:
            #阳爻
            return 1
        else:
            #阴爻
            return 0

def printYaoMessage(yao):
    if yao==1:
        return "阳爻"
    else:
        return "阴爻"
        
def printYaoFigure(yao):
    if yao==1:
        return "——"
    else:
        return "--"


print("\nPython版简易易经八卦占卜\n")

mode=InputUtils.readIntParam("请输入占卜模式：\n(1)一键占卜\n(2)手动占卜\n",1)

yao1=0
yao2=0
yao3=0
yao4=0
yao5=0
yao6=0

if mode==1:
    print("<<<<<<<<<<<<<")
    print("选择一键占卜模式")
    print(">>>>>>>>>>>>>")
    
    print ("抽取第一爻...")
    sleep(randint(1,100)/70)
    yao1=getNextYao(datetime.datetime.now())
    print ("抽取第二爻...")
    sleep(randint(1,100)/70)
    yao2=getNextYao(datetime.datetime.now())
    print ("抽取第三爻...")
    sleep(randint(1,100)/70)
    yao3=getNextYao(datetime.datetime.now())
    print ("抽取第四爻...")
    sleep(randint(1,100)/70)
    yao4=getNextYao(datetime.datetime.now())
    print ("抽取第五爻...")
    sleep(randint(1,100)/70)
    yao5=getNextYao(datetime.datetime.now())
    print ("抽取第六爻...")
    sleep(randint(1,100)/70)
    yao6=getNextYao(datetime.datetime.now())
    
    print("\n=============")
    print("六爻分别为：")
    print("=============")
    print(printYaoMessage(yao6))
    print(printYaoMessage(yao5))
    print(printYaoMessage(yao4))
    print(printYaoMessage(yao3))
    print(printYaoMessage(yao2))
    print(printYaoMessage(yao1))
    
    print("\n==============")
    print("=     "+printYaoFigure(yao6)+"     =")
    print("=     "+printYaoFigure(yao5)+"     =")
    print("=     "+printYaoFigure(yao4)+"     =")
    print("=     "+printYaoFigure(yao3)+"     =")
    print("=     "+printYaoFigure(yao2)+"     =")
    print("=     "+printYaoFigure(yao1)+"     =")
    print("==============")
    
    print("\n"+bagua.explainResult(yao1,yao2,yao3,yao4,yao5,yao6))
    
elif mode==2:
    print("<<<<<<<<<<<<<")
    print("选择手动占卜模式")
    print(">>>>>>>>>>>>>")

    yao1=getNextYao(InputUtils.readEnterForTime("按确认键选取第一爻"))
    yao2=getNextYao(InputUtils.readEnterForTime("按确认键选取第二爻"))
    yao3=getNextYao(InputUtils.readEnterForTime("按确认键选取第三爻"))
    yao4=getNextYao(InputUtils.readEnterForTime("按确认键选取第四爻"))
    yao5=getNextYao(InputUtils.readEnterForTime("按确认键选取第五爻"))
    yao6=getNextYao(InputUtils.readEnterForTime("按确认键选取第六爻"))

    print("\n=============")
    print("六爻分别为：")
    print("=============")
    print(printYaoMessage(yao6))
    print(printYaoMessage(yao5))
    print(printYaoMessage(yao4))
    print(printYaoMessage(yao3))
    print(printYaoMessage(yao2))
    print(printYaoMessage(yao1))
    
    print("\n==============")
    print("=     "+printYaoFigure(yao6)+"     =")
    print("=     "+printYaoFigure(yao5)+"     =")
    print("=     "+printYaoFigure(yao4)+"     =")
    print("=     "+printYaoFigure(yao3)+"     =")
    print("=     "+printYaoFigure(yao2)+"     =")
    print("=     "+printYaoFigure(yao1)+"     =")
    print("==============")
    
    print("\n=============")
    print("该卦为：")
    print("=============")
    
    print("\n"+bagua.explainResult(yao1,yao2,yao3,yao4,yao5,yao6))
else:
    print("模式选择有误！")