from sqlalchemy import Table, Column, ForeignKey, Integer

from languapedia.models.meta import Base

user_role_association_table = Table("user_role_associations", Base.metadata,
                                    Column("user_id", Integer, ForeignKey("users.id")),
                                    Column("role_id", Integer, ForeignKey("roles.id")),)