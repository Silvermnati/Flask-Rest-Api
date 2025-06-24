# Set the correct Flask app entry point
export FLASK_APP=server.app:app

# Add the project root to Python path
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Run the application
flask run