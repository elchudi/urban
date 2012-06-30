from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from geoalchemy import *
from geoalchemy.postgis import PGComparator


# Setup the database engine and session


from sqlalchemy import (create_engine, MetaData, Column, Integer, String,
        Unicode, Numeric, func, literal, select)
from sqlalchemy.orm import sessionmaker, column_property
from sqlalchemy.ext.declarative import declarative_base

from geoalchemy import (Geometry, Point, LineString, Polygon,
GeometryColumn, GeometryDDL, WKTSpatialElement)

engine = create_engine('sqlite:///:memory:', echo=True)
session = sessionmaker(bind=engine)()

print engine.execute("select 1").scalar()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    group_id = Column(Integer)
    
    def __init__(self, user_id, group_id=0):
        self.group_id = group_id
        self.id = user_id

    def __repr__(self):
        return "<User('%d','%d')>" % (self.id, self.group_id)



class Video(Base):
    __tablename__ = 'videos'
    
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    pos_x = Column(Float)
    pos_y = Column(Float)
    votes_up = Column(Integer)
    votes_down = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False  )

    def __init__(self, video_id, pos_x, pos_y, votes_up, votes_down, user_id):
        self.id = video_id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.votes_up = votes_up
        self.votes_down = votes_down
        self.user_id = user_id

    def __repr__(self):
        return "<Video('%d','%d','%d','%d','%d','%d')>" % (self.id, self.pos_x, self.pos_y, self.votes_up, self.votes_down, self.user_id)



class Zone(Base):
    __tablename__ = 'zones'
    
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    group_id = Column(Integer)
    group_img_url = Column(String)
    zone_geom = GeometryColumn(Polygon(2), nullable=False)


    def __repr__(self):
        print self.zone_geom 
        print dir(self.zone_geom)
        #for i in self.zone_geom.coords:
        #    print i
        return "<Zone('%d','%d','%s')>" % (self.id, self.group_id, self.group_img_url)


user1 = User(1)
user2 = User(2)
user3 = User(3)
print user3

video1 = Video(1,5.0,6.7,0,0,1)
video3 = Video(1,5.0,6.7,0,0,8)
print video3

zone1 = Zone(id=21, group_id=1, group_img_url="www.google.com", zone_geom='POLYGON((-88.1147292993631 42.7540605095542,-88.1548566878981 42.7824840764331,-88.1799363057325 42.7707802547771,-88.188296178344 42.7323248407643,-88.1832802547771 42.6955414012739,-88.1565286624204 42.6771496815287,-88.1448248407643 42.6336783439491,-88.131449044586 42.5718152866242,-88.1013535031847 42.565127388535,-88.1080414012739 42.5868630573248,-88.1164012738854 42.6119426751592,-88.1080414012739 42.6520700636943,-88.0980095541401 42.6838375796178,-88.0846337579618 42.7139331210191,-88.1013535031847 42.7423566878981,-88.1147292993631 42.7540605095542))')

session.add_all([user1, user2, user3, video1, video3, zone1])

print zone1
