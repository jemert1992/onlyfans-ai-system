import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Print current directory for debugging
current_dir = os.path.dirname(os.path.abspath(__file__))
logger.info(f"Current directory: {current_dir}")
logger.info(f"Directory contents: {os.listdir(current_dir)}")

# Add the current directory to the path
sys.path.insert(0, current_dir)
logger.info(f"Python path: {sys.path}")

try:
    # Try to import the app
    logger.info("Attempting to import app...")
    from app import create_app
    logger.info("Successfully imported app")
    
    app = create_app()
    
    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        logger.info(f"Starting app on port {port}")
        app.run(host="0.0.0.0", port=port)
except Exception as e:
    logger.error(f"Error starting application: {e}")
    import traceback
    logger.error(traceback.format_exc())
