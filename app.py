from flask import Flask,jsonify
from celery.result import AsyncResult
from tasks import  add
from databaseInfo import *


app = Flask(__name__)

@app.route('/')
def index():
    params = {
        "Status Code": 200,
        "Message": "Hi from test API"
    }
    return jsonify(params)


@app.route('/calculate/<int:number1>/<int:number2>' )
def calculate(number1, number2):
    sum = add.delay(number1, number2)

    # database, collection, id
    Insert('pending', 'pending_task', sum.id)

    params = {
        "id": sum.id,
        "status": 200
    }
    return jsonify(params)



@app.route('/get_answer/<string:id>')
def get_answer(id):
    res = AsyncResult(id)
    if res.status == 'PENDING':
        return jsonify(QueryForPending("pending", "pending_task", id))
    return jsonify(QueryForSuccess("jobs", "success_task", id))

if __name__ == '__main__':
    app.run(debug=True)