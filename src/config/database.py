"""Defines the database configuration"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI: str = os.getenv('DATABASE_URL', '')
BASE = declarative_base()
engine = create_engine(DATABASE_URI)
