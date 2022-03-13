from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

# application program 
app = Flask(__name__)


if __name__ == '__main__':
    # run the application
    app.run(debug=os.getenv("DEBUG"), host='0.0.0.0', port=5500)