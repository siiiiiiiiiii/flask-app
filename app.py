from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置資料庫
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 建立留言的資料表
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# 初始化資料庫
with app.app_context():
    db.create_all()

# 首頁路由（顯示留言和表單）
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # 如果收到 POST 請求
        message_content = request.form.get('message')  # 從表單中獲取留言
        if message_content:
            new_message = Message(content=message_content)  # 建立新留言
            db.session.add(new_message)  # 新增到資料庫
            db.session.commit()  # 保存變更
    messages = Message.query.all()  # 從資料庫中獲取所有留言
    return render_template('index.html', messages=messages)  # 回傳留言和表單

if __name__ == '__main__':
    app.run(debug=True)

