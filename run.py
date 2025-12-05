import os
from app.main import app  # app exists in app/main.py

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
