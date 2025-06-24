from server.app import create_app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance


app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    g1 = Guest(name="Taylor Swift", occupation="Singer")
    g2 = Guest(name="Elon Musk", occupation="Entrepreneur")

    e1 = Episode(date="2025-06-01", number=1)
    e2 = Episode(date="2025-06-02", number=2)

    db.session.add_all([g1, g2, e1, e2])
    db.session.commit()

    a1 = Appearance(rating=5, guest_id=g1.id, episode_id=e1.id)
    a2 = Appearance(rating=4, guest_id=g2.id, episode_id=e2.id)

    db.session.add_all([a1, a2])
    db.session.commit()
