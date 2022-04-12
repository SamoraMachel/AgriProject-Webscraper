from config import app
from api import *
import os
from dotenv import load_dotenv

load_dotenv()


if __name__ == '__main__':
    # run the application
    app.run(debug=os.getenv("DEBUG"), host='0.0.0.0', port=5500)