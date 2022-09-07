from flask_cors import CORS

from app import create_app
from app.config import server_port

if __name__ == "__main__":
    app = create_app()
    app.app_context().push()

    cors = CORS(app)

    port = server_port

    app.run(port=port, debug=True)