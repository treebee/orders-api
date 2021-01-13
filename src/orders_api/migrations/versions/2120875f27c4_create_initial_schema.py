"""create-initial-schema

Revision ID: 2120875f27c4
Revises:
Create Date: 2021-01-12 16:23:24.297032

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "2120875f27c4"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "orders",
        sa.Column("order_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "date", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("order_id"),
    )
    op.create_table(
        "stores",
        sa.Column("store_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("city", sa.Text(), nullable=False),
        sa.Column("country", sa.Text(), nullable=False),
        sa.Column("currency", sa.String(length=3), nullable=False),
        sa.Column("domain", sa.Text(), nullable=True),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("phone", sa.Text(), nullable=True),
        sa.Column("street", sa.Text(), nullable=False),
        sa.Column("zipcode", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("store_id"),
    )
    op.create_table(
        "products",
        sa.Column("product_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("store_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("price", sa.Numeric(precision=12, scale=2), nullable=False),
        sa.ForeignKeyConstraint(
            ["store_id"],
            ["stores.store_id"],
        ),
        sa.PrimaryKeyConstraint("product_id"),
        sa.UniqueConstraint("name", "store_id", name="uix_products"),
    )
    op.create_table(
        "order_items",
        sa.Column("order_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("product_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["order_id"],
            ["orders.order_id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.product_id"],
        ),
        sa.PrimaryKeyConstraint("order_id", "product_id"),
    )


def downgrade():
    op.drop_table("order_items")
    op.drop_table("products")
    op.drop_table("stores")
    op.drop_table("orders")
