"""Add pkgrel column

Revision ID: 2b1c28c108e
Revises: 1285478e434
Create Date: 2015-03-22 19:44:02.981605

"""

# revision identifiers, used by Alembic.
revision = '2b1c28c108e'
down_revision = '1285478e434'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('package', sa.Column('downloads', sa.Integer(), nullable=True))
    op.add_column('package', sa.Column('pkgrel', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('package', 'pkgrel')
    op.drop_column('package', 'downloads')
    ### end Alembic commands ###