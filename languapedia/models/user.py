import arrow
import bcrypt
from languapedia.models.user_role_association import user_role_association_table
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ArrowType

from languapedia.models.meta import Base

class User(Base):
    """ The SQLA declarative base model for users. """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, index=True)
    created = Column(ArrowType, default=arrow.now())
    updated = Column(ArrowType, default=arrow.now(), onupdate=arrow.now())
    email = Column(String(64), unique=True, index=True)
    password_hash = Column(String)
    roles = relationship("Role", secondary=user_role_association_table,
                         backref="roles")

    def set_password(self, password):
        hased = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
        self.password_hash = hashed.decode("utf8")

    def check_password(self, password):
        if self.password_hash is not None:
            expected_hash = self.password_hash.encode("utf8")
            return bcrypt.checkpw(password.encode("utf8"), expected_hash)
        return False