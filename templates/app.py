from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 設置數據庫
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 數據庫模型
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# 首頁路由
@app.route('/')
def index():
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

# 提交留言路由
@app.route('/submit', methods=['POST'])
def submit():
    content = request.form.get('message')
    if content:
        new_message = Message(content=content)
        db.session.add(new_message)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 創建數據庫
    app.run(debug=True)

