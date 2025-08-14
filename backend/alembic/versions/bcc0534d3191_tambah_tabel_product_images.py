"""tambah tabel 'product_images'

Revision ID: bcc0534d3191
Revises: 0b5148d2a196
Create Date: 2025-08-15 00:49:41.444936

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'bcc0534d3191'
down_revision: Union[str, Sequence[str], None] = '0b5148d2a196'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "product_images",
        sa.Column("image_id", sa.Integer, primary_key=True, autoincrement=True, index=True),
        sa.Column("produk_id", sa.Integer, sa.ForeignKey("produk.produk_id", ondelete="CASCADE"), nullable=False),
        sa.Column("indeks", sa.Integer, nullable=False),
        sa.Column("url", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("product_images")
