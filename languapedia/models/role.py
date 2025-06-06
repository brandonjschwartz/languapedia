from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ArrowType
import arrow

from languapedia.models.meta import Base
from languapedia.models.user_role_association import user_role_association_table

class Role(Base):
    """ The SQLA declarative base model for roles. """
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
    created = Column(ArrowType, default=arrow.now())
    updated = Column(ArrowType, default=arrow.now(), onupdate=arrow.now())
    users = relationship("User", secondary=user_role_association_table)