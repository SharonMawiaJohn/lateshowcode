import os
from flask import Flask, jsonify, request
from config import Config
from models import db, migrate  # Import from models

# Ensure the instance folder exists
if not os.path.exists('instance'):
    os.makedirs('instance')

# Initialize the Flask app
app = Flask(__name__)

# Configure the app
app.config.from_object(Config)

# Set up the database and migration
db.init_app(app)
migrate.init_app(app, db)

# Import models after db setup to avoid circular imports
from models.episode import Episode
from models.guest import Guest
from models.appearance import Appearance

# Index route to serve as the home page
@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the API for the Late Show!"}), 200


# Endpoint to get all episodes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200

# Endpoint to get a specific episode by ID
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict()), 200
    return jsonify({"error": "Episode not found"}), 404

# Endpoint to get all guests
@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200

# Endpoint to create an appearance (POST)
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        # Extract and validate input data
        rating = data['rating']
        episode_id = data['episode_id']
        guest_id = data['guest_id']

        # Validate rating range (1 to 5)
        if not (1 <= rating <= 5):
            return jsonify({"errors": ["Validation errors: Rating must be between 1 and 5"]}), 400

        # Create new appearance record
        appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)

        # Add appearance to the session and commit to the database
        db.session.add(appearance)
        db.session.commit()

        # Return success response
        return jsonify(appearance.to_dict()), 201

    except KeyError:
        # Return error if required fields are missing
        return jsonify({"errors": ["Validation errors: Missing required fields"]}), 400

# Entry point for running the app
if __name__ == "__main__":
    app.run(debug=True)
