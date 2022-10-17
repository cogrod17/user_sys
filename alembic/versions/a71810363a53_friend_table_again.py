"""friend table again

Revision ID: a71810363a53
Revises: 05c66de7edc3
Create Date: 2022-10-12 02:21:14.843321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a71810363a53'
down_revision = '05c66de7edc3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("FriendRequests",
                    sa.Column('id', sa.Integer, primary_key=True, index=True),
                    sa.Column('message', sa.Text, default=None),
                    sa.Column('sent_at', sa.DateTime(timezone=True),
                              server_default=sa.sql.func.now()),
                    sa.Column('sender_id', sa.Integer, sa.ForeignKey(
                        'Users.id'), nullable=False),
                    sa.Column('recipient_id', sa.Integer,
                              sa.ForeignKey('Users.id'), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('FriendRequests')
