"""penambahan kolom 'public_id' pada tabel 'product_images'

Revision ID: de219d531d4f
Revises: bcc0534d3191
Create Date: 2025-08-15 08:55:35.570678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de219d531d4f'
down_revision: Union[str, Sequence[str], None] = 'bcc0534d3191'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'product_images',
        sa.Column('public_id', sa.String(length=255), nullable=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('product_images', 'public_id')
