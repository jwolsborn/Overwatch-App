from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ARRAY
Base = declarative_base()


class OwlTeam(Base):

    __tablename__ = 'owl_teams'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    players = Column(ARRAY(String))

    def __repr__(self):
        return f"<Team(id='{self.id}',name={self.name},location={self.location},players={self.players}"
