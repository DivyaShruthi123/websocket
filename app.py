from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def fetch_stock_price():
    # Replace this with actual code to fetch stock prices
    return "Stock price: $100.00"

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True)

while True:
    time.sleep(1)  # Update price every second
    stock_price = fetch_stock_price()
    socketio.emit('stock_price_update', {'message': stock_price})
