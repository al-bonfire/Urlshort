from src import create_app
from src.config import settings as s


app = create_app(__name__)


if __name__ == "__main__":
    app.run(debug=s.DEBUG, port=8000)