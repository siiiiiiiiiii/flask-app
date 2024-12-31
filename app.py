from flask import Flask, render_template, request

app = Flask(__name__)

# 文件路徑
MESSAGE_FILE = "messages.txt"

# 從文件讀取留言
def load_messages():
    try:
        with open(MESSAGE_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# 將留言保存到文件
def save_message(message):
    with open(MESSAGE_FILE, "a") as file:
        file.write(message + "\n")

# 初始化留言
messages = load_messages()

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/add_message', methods=['POST'])
def add_message():
    msg = request.form['message']
    if msg:
        messages.append(msg)
        save_message(msg)  # 將留言保存到文件
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)

