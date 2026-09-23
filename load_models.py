from atlas_provider_sqlalchemy.ddl import print_ddl

from app.users.model import User

print_ddl("sqlite", [User])
