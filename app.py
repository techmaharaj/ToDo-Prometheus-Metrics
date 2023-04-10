from flask import Flask, jsonify, render_template, request
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import Summary, make_wsgi_app, Gauge
from redis import Redis

app = Flask(__name__)
redis = Redis(host='localhost', port=7777, db=0) # Configuring Redis

# Prometheus Metrics
REQUEST_TIME_LIST = Summary('request_time_list', 'Time spent for LIST request')
REQUEST_TIME_ADD = Summary('request_time_add', 'Time spent for ADD request')
REQUEST_TIME_REMOVE = Summary('request_time_remove', 'Time spent for DELETE request')
REQUEST_ADD_COUNT = Gauge('request_add_count', ' No. of Requests to add items')
REQUEST_REMOVE_COUNT = Gauge('request_remove_count', 'No. of Requests to remove items')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@REQUEST_TIME_LIST.time()
@app.route('/list', methods=['GET'])
def get_todo_list():
    todo_list = []
    for key in redis.keys():
        todo_list.append(redis.get(key).decode('utf-8'))
    return jsonify(todo_list)

@REQUEST_TIME_ADD.time()
@app.route('/add', methods=['POST'])
def add_todo_item():
    item = request.json['item']
    redis.set(item, item)
    REQUEST_ADD_COUNT.inc()  
    return jsonify({'success': True})

@REQUEST_TIME_REMOVE.time()
@app.route('/remove', methods=['DELETE'])
def delete_todo_item():
    item = request.json['item']
    redis.delete(item)
    REQUEST_REMOVE_COUNT.inc()
    return jsonify({'success': True})

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    app.run(debug=True)



    