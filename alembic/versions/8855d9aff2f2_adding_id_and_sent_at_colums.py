"""adding ID and sent_at colums"

Revision ID: 8855d9aff2f2
Revises: 759d1b6daf91
Create Date: 2022-10-12 02:05:34.082578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8855d9aff2f2'
down_revision = '759d1b6daf91'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('FriendRequests', 'request_id')
    op.add_column('FriendRequests', sa.Column(
        'id', sa.Integer, primary_key=True, index=True))
    op.add_column('FriendRequests', sa.Column('sent_at', sa.DateTime(
        timezone=True), server_default=sa.sql.func.now()))
    op.drop_column('FriendRequests', 'Message')
    op.add_column('FriendRequests', sa.Column(
        'message', sa.Text, default=None))


def downgrade() -> None:
    op.drop_column('FriendRequests', 'id')
    op.add_column('FriendRequests', sa.Column(
        'request_id', sa.Integer, primary_key=True, index=True))
    op.drop_column('FriendRequests', 'sent_at')
    op.drop_column('FriendRequests', 'message')
    op.add_column('FriendRequests', sa.Column(
        'Message', sa.Text, default=None))
