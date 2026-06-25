from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.api.routes.db.database import Base


class Research(Base):
    __tablename__ = "research"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String(255))
    report = Column(Text)


class ResearchHistory(Base):
    __tablename__ = "research_history"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(500))
    answer = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)