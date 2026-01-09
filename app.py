import os

from dotenv import load_dotenv

from switchbot_dashboard import create_app


load_dotenv()

app = create_app()


if __name__ == "__main__":
    host = os.environ.get("FLASK_HOST", "127.0.0.1")
    port = int(os.environ.get("FLASK_PORT", "5000"))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"

    app.run(host=host, port=port, debug=debug)
