from data.orm import SyncORM
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from flasgger import Flasgger, swag_from, Swagger
from aiogram import Bot, Dispatcher   
from bot.config import settings
import asyncio
from bot.handlers import rt
app = Flask(__name__)
app.config["SWAGGER"] = {"title": "Мой API", "uiversion": 3}

Swagger(app)
CORS(app)

SyncORM.create_table()
SyncORM.insert_data()

# @app.route('/', methods=['GET'])
# def hello_world():
#     data = request.args.get('id')
#     data = 1
#     return jsonify({'site': render_template('temp1.html', data=SyncORM.select_data(data)), 'data': data})


@app.route('/get_user_history', methods=['GET'])
@swag_from('swagger/get_user_history.yaml')
def get_user_history():
    lender_tg = request.args.get('lender_tg')
    debtor_tg = request.args.get('debtor_tg')
    return jsonify(SyncORM.get_user_history(lender_tg, debtor_tg))


@app.route('/get_user_debtors', methods=['GET'])
@swag_from('swagger/get_user_debtors.yaml')
def get_user_debtors():
    lender_tg = request.args.get('lender_tg')
    return jsonify(SyncORM.get_user_debtors(lender_tg))

@app.route('/get_user_lenders', methods=['GET'])
@swag_from('swagger/get_user_lenders.yaml')
def get_user_lenders():
    print('aaaa')
    debtor_tg = request.args.get('debtor_tg')
    print('aaaa')
    return jsonify(SyncORM.get_user_lenders(debtor_tg))

@app.route('/insert_debt', methods=['POST'])
@swag_from('swagger/insert_debt.yaml')
def insert_debt():
    lender_tg = request.args.get('lender_tg')
    debtors_tg_list = request.args.get('debtors_tg_list')
    event_name = request.args.get('event_name')
    return jsonify(SyncORM.insert_debt(lender_tg, debtors_tg_list, event_name))


@app.route('/remove_debt', methods=['DELETE'])
@swag_from('swagger/remove_debt.yaml')
def remove_debt():
    lender_tg = request.args.get('lender_tg')
    debtor_tg = request.args.get('debtor_tg')
    return SyncORM.remove_debt(lender_tg, debtor_tg)

@app.route('/get_trips', methods=['GET'])
@swag_from('swagger/get_trips.yaml')
def get_trips():
    tg_tag = request.args.get('tg_tag')
    return jsonify(SyncORM.get_trips(tg_tag))

@app.route('/create_trip', methods=['POST'])
@swag_from('swagger/create_trip.yaml')
def create_trip():
    lender_tg = request.args.get('lender_tg')
    debtors_tg_debpt_dict = request.args.get('debtors_tg_debpt_dict')
    trip_name = request.args.get('trip_name')
    event_name = request.args.get('event_name')
    return jsonify(SyncORM.create_trip(lender_tg, debtors_tg_debpt_dict, trip_name, event_name))


@app.route('/add_trip_debt', methods=['POST'])
@swag_from('swagger/add_trip_debt.yaml')
def add_trip_debt():
    lender_tg = request.args.get('lender_tg')
    debtors_tg_debpt_dict = request.args.get('debtors_tg_debpt_dict')
    trip_id = request.args.get('trip_id')
    event_name = request.args.get('event_name')
    return jsonify(SyncORM.add_trip_debt(lender_tg, debtors_tg_debpt_dict, trip_id, event_name))



@app.route('/get_trip_debts', methods=['GET'])
@swag_from('swagger/get_trip_debts.yaml')
def get_trip_debts():
    trip_id = request.args.get('trip_id')
    return jsonify(SyncORM.get_trip_debts(trip_id))


@app.route('/get_trip_user_debtors', methods=['GET'])
@swag_from('swagger/get_trip_user_debtors.yaml')
def get_trip_user_debtors():
    lender_tg = request.args.get('lender_tg')    
    trip_id = request.args.get('trip_id')
    return jsonify(SyncORM.get_trip_user_debtors(lender_tg, trip_id))

@app.route('/close_trip', methods=['DELETE'])
@swag_from('swagger/close_trip.yaml') #TODO добавить
def close_trip():
    trip_id = request.args.get('trip_id')
    return jsonify(SyncORM.close_trip(trip_id))


dp = Dispatcher()
bot = Bot(settings.TOKEN)

async def main():
    dp.include_router(rt)
    await dp.start_polling(bot)

async def start_back():
    await app.run(host='0.0.0.0', port=5000)

async def start():
    try:
        # Создаём две задачи
        task1 = asyncio.create_task(main())
        task2 = asyncio.create_task(start_back())

        # Запускаем обе задачи параллельно
        await asyncio.gather(task1, task2)
    except Exception as e:
        print(f"Ошибка: {e}")



if __name__ == '__main__':
    asyncio.run(start())