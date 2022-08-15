from flask import jsonify,request
from flask_restful import Api, Resource
from flask import Flask

from pymongo import MongoClient

client = MongoClient(host="test_mongodb",
                     port = 27017,
                     username = "root",
                     password = "rootpassword",
                     authSource = "admin"
                    )

#client = MongoClient("mongodb://test_mongodb:27017/")

#db is same as directory created to identify database
#default port is 27017

db = client.aNewDB
#db is a new database 
UserNum = db["UserNum"]
#UserNum is a new Collection
UserNum.insert_one({'num_of_users':0})
#MongoDB waits until you have created a collection (table), with at least one document (record) before it actually creates the database (and collection).

class Visit(Resource):
    def get(self):
        prev_users = UserNum.find({})[0]['num_of_users']
        UserNum.update({},{'$set':{'num_of_users':prev_users+1}})
        return str("Hello User "+str(prev_users+1))

app = Flask(__name__)
api = Api(app)

api.add_resource(Visit,"/hello")

def validatePostedData(postedData,functionName):
    if(functionName == "add" or functionName == "subtract" or functionName == "multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301 
        else:
            return 200
    else:
        if "x" not in postedData or "y" not in postedData:
            return 301 
        elif "y" in postedData and int(postedData["y"])==0:
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = validatePostedData(postedData,"add")
        if(status_code!=200):
            retJson = {
                "Message":"An Error Occured",
                "Status Code":status_code
            }
            return jsonify(retJson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)
            ret = x+y 
            retJson = {
                "Message":ret,
                "Status Code": 200,
            }
            return jsonify(retJson)

class Subtract(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = validatePostedData(postedData,"subtract")
        if(status_code!=200):
            retJson = {
                "Message":"An Error Occured",
                "Status Code":status_code
            }
            return jsonify(retJson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)
            ret = x-y 
            retJson = {
                "Message":ret,
                "Status Code": 200,
            }
            return jsonify(retJson)

class Divide(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = validatePostedData(postedData,"divide")
        if(status_code!=200):
            if(status_code==301):
                retJson = {
                    "Message":"An Error Occured",
                    "Status Code":status_code
                }
                return jsonify(retJson)
            else:
                retJson = {
                    "Message":"Don't divide by 0",
                    "Status Code":status_code
                }
                return jsonify(retJson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)
            ret = x*y 
            retJson = {
                "Message":ret,
                "Status Code": 200,
            }
            return jsonify(retJson) 

class Multiply(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = validatePostedData(postedData,"multiply")
        if(status_code!=200):
            retJson = {
                "Message":"An Error Occured",
                "Status Code":status_code
            }
            return jsonify(retJson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)
            ret = x*y 
            retJson = {
                "Message":ret,
                "Status Code": 200,
            }
            return jsonify(retJson)


api.add_resource(Add, "/add")
api.add_resource(Subtract,"/subtract")
api.add_resource(Multiply,"/multiply")
api.add_resource(Divide,"/divide")

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/retJson")
def fun():
    retJson = {
        "home":"something",
        "else":"somethings"
    }
    return jsonify(retJson)

@app.route('/add_two_nums',methods = ["POST"])
def addtwonums():
    data_dictionary = request.get_json()
    x = data_dictionary["x"]
    y = data_dictionary["y"]
    z = x+y
    retJson = {
        "sum":z
    }
    return jsonify(retJson), 200

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True)