import json
from flask import Flask,request
from flask_cors import CORS
import requests 

app = Flask(__name__)
CORS(app)

api = "https://pca.oncloud.gr/s1services"



@app.route("/",methods=["GET"])

def main():
    username = request.args.get('username')
    password = request.args.get('password')
    print(username,password)
    #print('Mphke')
    data={
        'service':"login",
        'username':"Sparke",
        'password':"1234",
        'appId':"3001"
    }

    datas = json.dumps(data)
    r=requests.post(api,data=datas)
   # print(r.text)
    clientID = json.loads(r.text)

    data={
        "service": "authenticate",
        "clientID": clientID['clientID'],
        "company": "1001",
        "branch": "1000",
        "module": "0",
        "refid": "1" 
    }
    datas = json.dumps(data)
   # print(datas)
    r=requests.post(api,data=datas)   
    clientID = json.loads(r.text)
   # print(r.text)

    data = { 
        'service':"SqlData",
        'clientID': clientID['clientID'],
        'appId':"3001",
        'SqlName':"AFM-KOD",
        "param1":username,
        "param2":password
    }
    datas= json.dumps(data)
    r = requests.post(api,data=datas)
    print(r.text)


    return r.text 
   
if __name__ == '__main__':
    app.run(debug=True,host="localhost",port="4000")