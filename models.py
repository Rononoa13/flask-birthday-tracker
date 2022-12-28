from app import db, app

# ------------------------------------------
# Models
#----------------------------------------------
class Birthdays(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"Item {self.name}"

db.init_app(app)

with app.app_context():
    db.create_all()