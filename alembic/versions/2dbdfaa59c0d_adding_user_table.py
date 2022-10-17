"""adding user table

Revision ID: 2dbdfaa59c0d
Revises: 
Create Date: 2022-08-13 19:20:02.047859

"""
from alembic import op
import sqlalchemy as sa
from core.models.users import User


# revision identifiers, used by Alembic.
revision = '2dbdfaa59c0d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "Users",
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String(16), nullable=False, unique=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('bio', sa.Text, nullable=True),
        sa.Column('password', sa.String, nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table("Users")
