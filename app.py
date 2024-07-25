from flask import Flask
from src.routes.products_page import *
from src.config import *

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    db.init_app(app)
    
    app.route('/api/fake/data', methods=['GET'])(get_products_list)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5001, debug=True)