"""Create stores table

Revision ID: 5cb03acc4439
Revises:
Create Date: 2021-01-05 17:34:19.843720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5cb03acc4439"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "stores",
        sa.Column("store_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=True),
        sa.Column("currency", sa.String(length=3), nullable=True),
        sa.Column("country", sa.Text(), nullable=True),
        sa.Column("city", sa.Text(), nullable=True),
        sa.Column("street", sa.Text(), nullable=True),
        sa.Column("zipcode", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("store_id"),
    )


def downgrade():
    op.drop_table("stores")
