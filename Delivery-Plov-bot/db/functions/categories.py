from db.table import CategoriesTable
from db.engine import engine
from sqlalchemy.orm import sessionmaker


def get_categories():
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(CategoriesTable).all()
    return result if result else None


