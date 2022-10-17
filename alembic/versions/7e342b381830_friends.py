"""friends

Revision ID: 7e342b381830
Revises: 2dbdfaa59c0d
Create Date: 2022-10-12 01:15:12.453392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e342b381830'
down_revision = '2dbdfaa59c0d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "FriendRequests",
        sa.Column('request_id', sa.Integer, primary_key=True, index=True),
        sa.Column('message', sa.Text, default=None)
    )


def downgrade() -> None:
    op.drop_table('FriendRequests')
