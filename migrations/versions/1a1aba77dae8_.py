"""empty message

Revision ID: 1a1aba77dae8
Revises: f8e96074bfa7
Create Date: 2020-11-24 16:57:26.942106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a1aba77dae8'
down_revision = 'f8e96074bfa7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('sessionId', sa.String(length=128), nullable=True),
    sa.Column('isValid', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_session_sessionId'), 'session', ['sessionId'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_session_sessionId'), table_name='session')
    op.drop_table('session')
    # ### end Alembic commands ###
