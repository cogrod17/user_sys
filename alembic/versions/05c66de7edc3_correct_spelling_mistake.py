"""correct spelling mistake

Revision ID: 05c66de7edc3
Revises: 8855d9aff2f2
Create Date: 2022-10-12 02:17:11.371172

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '05c66de7edc3'
down_revision = '8855d9aff2f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_FriendRequests_id', table_name='FriendRequests')
    op.drop_table('FriendRequests')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('FriendRequests',
    sa.Column('Message', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('sender_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('recipient_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"FriendRequests_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('sent_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['recipient_id'], ['Users.id'], name='FriendRequests_recipient_id_fkey'),
    sa.ForeignKeyConstraint(['sender_id'], ['Users.id'], name='FriendRequests_sender_id_fkey')
    )
    op.create_index('ix_FriendRequests_id', 'FriendRequests', ['id'], unique=False)
    # ### end Alembic commands ###
