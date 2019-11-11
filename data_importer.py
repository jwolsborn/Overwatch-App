from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def import_data(data):

    engine = create_engine('postgresql+psycopg2:///owl', echo=True)
    session = sessionmaker(bind=engine)
    s = session()

    for idx, val in enumerate(data):
        s.add(val)

    s.commit()
    s.close()
