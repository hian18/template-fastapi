"""inicio

Revision ID: c1e61995ddeb
Revises: 476b84a40efb
Create Date: 2025-07-25 17:06:27.910096

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = 'c1e61995ddeb'
down_revision = '476b84a40efb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schemas', sa.Column('teste', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('schemas', 'teste')
    # ### end Alembic commands ###
