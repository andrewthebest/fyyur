"""empty message

Revision ID: a12d00a1fd34
Revises: 
Create Date: 2022-08-19 20:14:23.446458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a12d00a1fd34'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('Artist', 'genres',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
    op.alter_column('Venue', 'address',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('Venue', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('Venue', 'genres',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'genres',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
    op.alter_column('Venue', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('Venue', 'address',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('Artist', 'genres',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
    op.alter_column('Artist', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###