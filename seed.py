import json
from app import app, db
from models.episode import Episode
from models.guest import Guest
from models.appearance import Appearance

with app.app_context():
    # Load data from JSON file
    with open('seed_data.json') as file:
        data = json.load(file)

    # Add episodes
    for episode_data in data['episodes']:
        episode = Episode(date=episode_data['date'], number=episode_data['number'])
        db.session.add(episode)
    
    # Add guests
    for guest_data in data['guests']:
        guest = Guest(name=guest_data['name'], occupation=guest_data['occupation'])
        db.session.add(guest)
    
    # Commit episodes and guests first to get their IDs
    db.session.commit()

    # Add appearances
    for appearance_data in data['appearances']:
        appearance = Appearance(
            rating=appearance_data['rating'], 
            episode_id=appearance_data['episode_id'], 
            guest_id=appearance_data['guest_id']
        )
        db.session.add(appearance)
    
    # Commit the appearances
    db.session.commit()

    print("Database seeded successfully!")
