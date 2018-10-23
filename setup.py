from app import create_app, db


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
