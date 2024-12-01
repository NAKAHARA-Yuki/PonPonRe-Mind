from app import app, db
from flask_cors import CORS  # 追加

# CORS の設定を追加
CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
