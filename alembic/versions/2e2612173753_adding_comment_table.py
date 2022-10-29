"""adding comment table

Revision ID: 2e2612173753
Revises: 98c2822f03ad
Create Date: 2022-10-29 18:35:50.425996

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2e2612173753'
down_revision = '98c2822f03ad'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('Comments',
                    sa.Column('id', sa.Integer, primary_key=True, index=True),
                    sa.Column('created_at', sa.DateTime(
                        timezone=True), server_default=sa.sql.func.now()),
                    sa.Column('text', sa.Text, nullable=False),
                    sa.Column('user_id', sa.Integer, sa.ForeignKey(
                        'Users.id'), nullable=False),
                    sa.Column('post_id', sa.Integer, sa.ForeignKey(
                        'Posts.id'), nullable=False)

                    )


def downgrade() -> None:
    op.drop_table('Comments')
    # ### end Alembic commands ###
