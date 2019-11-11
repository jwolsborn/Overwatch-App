from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql+psycopg2:///owl', echo=True)
Session = sessionmaker(bind=engine)

s = Session()

s.add()
s.commit()
s.close()
