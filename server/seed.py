from config import app, db
from models import User, Recipe

with app.app_context():
    # Clear out old data
    User.query.delete()
    Recipe.query.delete()

    # Create users with passwords
    u1 = User(
        username="Prabhdip",
        image_url="https://picsum.photos/200",
        bio="Loves cooking Punjabi dishes"
    )
    u1.password_hash = "password123"   # ✅ sets the hashed password

    u2 = User(
        username="Elissa",
        image_url="https://picsum.photos/200",
        bio="Enjoys baking and coding"
    )
    u2.password_hash = "supersecret"   # ✅ sets the hashed password

    db.session.add_all([u1, u2])
    db.session.commit()

    # Create recipes
    r1 = Recipe(
        title="Chana Masala",
        instructions="Soak chickpeas overnight, cook with spices.",
        minutes_to_complete=45,
        user=u1
    )
    r2 = Recipe(
        title="Chocolate Cake",
        instructions="Mix ingredients, bake at 180C for 30 minutes.",
        minutes_to_complete=60,
        user=u2
    )

    db.session.add_all([r1, r2])
    db.session.commit()

    print("✅ Database seeded successfully!")
