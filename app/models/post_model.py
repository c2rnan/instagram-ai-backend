from sqlalchemy import Column, Integer, String, Text
from app.database import Base
from sqlalchemy import DateTime
from datetime import datetime

class Post(Base):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)

    keyword = Column(String(255))

    caption = Column(Text)

    hashtags = Column(Text)

created_at = Column(DateTime, default=datetime.utcnow)