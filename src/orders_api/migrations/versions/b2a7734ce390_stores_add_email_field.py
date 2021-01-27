"""stores_add-email-field

Revision ID: b2a7734ce390
Revises: 2120875f27c4
Create Date: 2021-01-27 14:33:28.464701

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = "b2a7734ce390"
down_revision = "2120875f27c4"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "stores",
        sa.Column(
            "email", sqlalchemy_utils.types.email.EmailType(length=255), nullable=True
        ),
    )


def downgrade():
    op.drop_column("stores", "email")
