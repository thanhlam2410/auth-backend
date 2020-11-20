"""remove index country.name

Revision ID: ae6346ce3d65
Revises: 34ff620ab59e
Create Date: 2020-11-21 00:43:19.809641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae6346ce3d65'
down_revision = '34ff620ab59e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_country_name', table_name='country')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_country_name', 'country', ['name'], unique=1)
    # ### end Alembic commands ###