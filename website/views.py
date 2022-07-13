#from crypt import methods
#from re import T
from flask import Blueprint, render_template, request, redirect, url_for
from website import dataS
import time

views = Blueprint("views",__name__)

@views.route("/")
def home():
    return render_template("mainpage.html")

@views.route("/memo/create",methods=['POST'])
def createMemo():
    Mname = request.form['name']
    Mcontent = request.form['content']
    Mtag = request.form['tag']
    Mdate = time.strftime('%Y.%m.%d %X', time.localtime(time.time()))
    if(dataS.detectOverlap(Mname) == True):
        tmp = dataS.save(str(Mname), str(Mcontent), str(Mtag), Mdate)
    else:
        return "failed: Duplicate names exist"
    if tmp == False:
        return "failed"
    #return str(Mname)+ "<br>" + str(Mcontent)+ "<br>" + str(Mtag) + "<br>" + str(Mdate) + "<br>id: " + str(dataS.count - 1)
    return redirect("/")
    

@views.route("/memo/read")
def readMemo(): 
    Mname = request.args.get('name','')
    Temp = dataS.load(Mname)
    if Temp == False or Mname == '':
        return "failed"
    
    return render_template("viewMemo.html", Mname = str(dataS.Memos[Temp][0]), 
                           Mcontent = str(dataS.Memos[Temp][1]), Mtag = str(dataS.Memos[Temp][2]), Mdate = str(dataS.Memos[Temp][3]), Mid = str(dataS.Memos[Temp][4]))

@views.route("/memo/delete",methods=['POST'])  
def deleteMemo():
    Mname = str(request.form['name'])
    print("Mname : ", Mname)
    dataS.delete(Mname)
    return redirect("/")

@views.route("/memo/modify",methods=['POST'])
def modifyMemo():
    Mname = request.form['name']
    Mfixname = request.form['fixname']
    Mcontent = request.form['content']
    Mtag = request.form['tag']
    Mdate = time.strftime('%Y.%m.%d %X', time.localtime(time.time()))
    if Mname == '': 
        return "failed"
    else:
        dataS.Modify(Mname,Mfixname,Mcontent,Mtag,Mdate)
        return redirect("/")