"""penambahan relasi 'pesanan' di User

Revision ID: 2f792a001c70
Revises: b79c9df419d5
Create Date: 2025-08-14 09:34:27.331023
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2f792a001c70'
down_revision: Union[str, Sequence[str], None] = 'b79c9df419d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Tidak ada perubahan DB, hanya update ORM"""
    pass

def downgrade() -> None:
    """Tidak ada perubahan DB, downgrade hanya ORM"""
    pass
