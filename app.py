# from app import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=False, port=8000)  # Set debug=False in production


# from app import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=False)  # Set debug=False in production

from app import create_app
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Creating Flask app...")
app = create_app()
logger.debug("Flask app created: %s", app)

if __name__ == '__main__':
    logger.debug("Running Flask app...")
    app.run(debug=False)