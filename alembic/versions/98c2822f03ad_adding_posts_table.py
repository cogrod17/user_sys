"""adding posts table

Revision ID: 98c2822f03ad
Revises: bbe4d3de1ef1
Create Date: 2022-10-16 17:25:46.432727

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '98c2822f03ad'
down_revision = 'bbe4d3de1ef1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('Posts',
                    sa.Column('id', sa.Integer, primary_key=True, index=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.sql.func.now()),
                    sa.Column('text', sa.Text, nullable=False),
                    sa.Column('user_id', sa.Integer, sa.ForeignKey(
                        'Users.id'), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('Posts')
