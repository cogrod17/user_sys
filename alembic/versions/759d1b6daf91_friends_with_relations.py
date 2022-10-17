"""friends with relations

Revision ID: 759d1b6daf91
Revises: 8d35771eae4a
Create Date: 2022-10-12 01:51:47.365501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '759d1b6daf91'
down_revision = '8d35771eae4a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("FriendRequests",
                    sa.Column("request_id", sa.Integer,
                              primary_key=True, index=True),
                    sa.Column('Message', sa.Text, default=None),
                    sa.Column("sender_id", sa.Integer, sa.ForeignKey(
                        'Users.id'), nullable=False),
                    sa.Column('recipient_id', sa.Integer, sa.ForeignKey('Users.id'), nullable=False)),


def downgrade() -> None:
    op.drop_table('FriendRequests')
