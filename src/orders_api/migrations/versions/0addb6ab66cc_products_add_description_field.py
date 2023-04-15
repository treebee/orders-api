"""products_add-description-field

Revision ID: 0addb6ab66cc
Revises: b2a7734ce390
Create Date: 2021-01-27 17:06:53.310843

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0addb6ab66cc"
down_revision = "b2a7734ce390"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("products", sa.Column("description", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("products", "description")
    # ### end Alembic commands ###
