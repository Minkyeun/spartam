from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('homework4.html')


## API 역할을 하는 부분
@app.route('/homework4s', methods=['POST'])
def write_homework4():
    name_receive = request.form['name_give']
    Groupselect_receive = request.form['Groupselect_give']
    adress_receive = request.form['adress_give']
    number_receive = request.form['number_give']

    homework4 = {
       'name': name_receive,
       'Groupselect': Groupselect_receive,
       'adress': adress_receive,
       'number': number_receive
    }

    db.homework4s.insert_one(homework4)
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 접수되었습니다.'})


@app.route('/homework4s', methods=['GET'])
def read_homework4s():
    homework4s = list(db.homework4s.find({},{'_id':False}))
    return jsonify({'result': 'success', 'homework4s': homework4s})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)