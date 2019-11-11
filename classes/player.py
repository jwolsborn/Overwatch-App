from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class OwlPlayer(Base):

    __tablename__ = 'owl_players'

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer)
    role = Column(String)
    name = Column(String)
    team = Column(String)
    avg_elim_per10m = Column(Integer)
    avg_death_per10m = Column(Integer)
    avg_herodmg_per10m = Column(Integer)
    avg_heals_per10m = Column(Integer)
    avg_ult_per10m = Column(Integer)
    avg_final_blow_per10m = Column(Integer)

    def __repr__(self):
        return f"<Player(id={self.id},team_id={self.team_id},name={self.name},team={self.team}," \
               f"avg_elim_per10m={self.avg_elim_per10m}, avg_death_per10m={self.avg_death_per10m}," \
               f"avg_herodmg_per10m={self.avg_herodmg_per10m}, avg_heals_per10m={self.avg_heals_per10m}," \
               f"avg_ult_per10m={self.avg_ult_per10m},avg_final_blow_per10m={self.avg_final_blow_per10m}"
