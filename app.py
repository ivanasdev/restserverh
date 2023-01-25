from flask import Flask
import os
from routes.users import users
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Se importan las rutas de users
app.register_blueprint(users)



if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8000)))