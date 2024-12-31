from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 設定資料庫路徑（使用 SQLite）
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 資料庫模型
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# 初始化資料庫（確保僅執行一次）
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # 從資料庫中獲取所有留言
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

@app.route('/add', methods=['POST'])
def add_message():
    # 從表單中獲取留言內容
    message_content = request.form['message']
    if message_content:
        new_message = Message(content=message_content)
        db.session.add(new_message)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

