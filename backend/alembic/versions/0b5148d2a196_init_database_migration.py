"""init_database_migration.py

Revision ID: 0b5148d2a196
Revises: 2f792a001c70
Create Date: 2025-08-14 20:46:28.707474

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers
revision: str = '0b5148d2a196'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade: Create all tables (apply schema)"""
    # 1. Create independent tables first (parents)
    op.create_table('users',
        sa.Column('pengguna_id', sa.INTEGER(), server_default=sa.text("nextval('users_pengguna_id_seq'::regclass)"), autoincrement=True, nullable=False),
        sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('peran', postgresql.ENUM('user', 'admin', name='role_type'), autoincrement=False, nullable=False),
        sa.Column('dibuat_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.Column('diperbarui_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('pengguna_id', name='users_pkey'),
        sa.UniqueConstraint('username', name='users_username_key'),
        postgresql_ignore_search_path=False
    )
    op.create_index(op.f('ix_users_pengguna_id'), 'users', ['pengguna_id'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)

    op.create_table('kategori',
        sa.Column('kategori_id', sa.INTEGER(), server_default=sa.text("nextval('kategori_kategori_id_seq'::regclass)"), autoincrement=True, nullable=False),
        sa.Column('nama', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
        sa.Column('deskripsi', sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column('dibuat_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.Column('diperbarui_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('kategori_id', name='kategori_pkey'),
        postgresql_ignore_search_path=False
    )
    op.create_index(op.f('ix_kategori_nama'), 'kategori', ['nama'], unique=True)
    op.create_index(op.f('ix_kategori_kategori_id'), 'kategori', ['kategori_id'], unique=False)

    op.create_table('merek',
        sa.Column('merek_id', sa.INTEGER(), server_default=sa.text("nextval('merek_merek_id_seq'::regclass)"), autoincrement=True, nullable=False),
        sa.Column('nama', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('logo', sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column('deskripsi', sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column('dibuat_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.Column('diperbarui_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('merek_id', name='merek_pkey'),
        postgresql_ignore_search_path=False
    )
    op.create_index(op.f('ix_merek_nama'), 'merek', ['nama'], unique=True)
    op.create_index(op.f('ix_merek_merek_id'), 'merek', ['merek_id'], unique=False)

    # 2. Create dependent tables (children)
    op.create_table('produk',
        sa.Column('produk_id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('nama', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('deskripsi', sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column('harga', sa.NUMERIC(precision=12, scale=2), autoincrement=False, nullable=False),
        sa.Column('stok', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('kategori_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('merek_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('dibuat_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.Column('diperbarui_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['kategori_id'], ['kategori.kategori_id'], name=op.f('produk_kategori_id_fkey'), ondelete='SET NULL'),
        sa.ForeignKeyConstraint(['merek_id'], ['merek.merek_id'], name=op.f('produk_merek_id_fkey'), ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('produk_id', name='produk_pkey')
    )
    op.create_index(op.f('ix_produk_produk_id'), 'produk', ['produk_id'], unique=False)

    op.create_table('alamat',
        sa.Column('alamat_id', sa.INTEGER(), server_default=sa.text("nextval('alamat_alamat_id_seq'::regclass)"), autoincrement=True, nullable=False),
        sa.Column('pengguna_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('label', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('jalan', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('kota', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('provinsi', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('kode_pos', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('negara', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('dibuat_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.Column('diperbarui_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['pengguna_id'], ['users.pengguna_id'], name='alamat_pengguna_id_fkey', ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('alamat_id', name='alamat_pkey'),
        postgresql_ignore_search_path=False
    )
    op.create_index(op.f('ix_alamat_alamat_id'), 'alamat', ['alamat_id'], unique=False)

    op.create_table('pesanan',
        sa.Column('pesanan_id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('pengguna_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('alamat_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('total_harga', sa.NUMERIC(precision=12, scale=2), autoincrement=False, nullable=False),
        sa.Column('status', postgresql.ENUM('pending', 'dibayar', 'dikirim', 'selesai', 'dibatalkan', name='status_pesanan'), autoincrement=False, nullable=False),
        sa.Column('dibuat_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.Column('diperbarui_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['alamat_id'], ['alamat.alamat_id'], name=op.f('pesanan_alamat_id_fkey'), ondelete='SET NULL'),
        sa.ForeignKeyConstraint(['pengguna_id'], ['users.pengguna_id'], name=op.f('pesanan_pengguna_id_fkey'), ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('pesanan_id', name='pesanan_pkey')
    )
    op.create_index(op.f('ix_pesanan_pesanan_id'), 'pesanan', ['pesanan_id'], unique=False)

    op.create_table('item_pesanan',
        sa.Column('item_pesanan_id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('pesanan_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('produk_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('jumlah', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('harga', sa.NUMERIC(precision=12, scale=2), autoincrement=False, nullable=False),
        sa.Column('dibuat_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['pesanan_id'], ['pesanan.pesanan_id'], name=op.f('item_pesanan_pesanan_id_fkey'), ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['produk_id'], ['produk.produk_id'], name=op.f('item_pesanan_produk_id_fkey'), ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('item_pesanan_id', name=op.f('item_pesanan_pkey'))
    )
    op.create_index(op.f('ix_item_pesanan_item_pesanan_id'), 'item_pesanan', ['item_pesanan_id'], unique=False)

    op.create_table('ulasan',
        sa.Column('ulasan_id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('produk_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('pengguna_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('bintang', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('komentar', sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column('foto', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True),
        sa.Column('dibuat_pada', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['pengguna_id'], ['users.pengguna_id'], name=op.f('ulasan_pengguna_id_fkey'), ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['produk_id'], ['produk.produk_id'], name=op.f('ulasan_produk_id_fkey'), ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('ulasan_id', name=op.f('ulasan_pkey'))
    )
    op.create_index(op.f('ix_ulasan_ulasan_id'), 'ulasan', ['ulasan_id'], unique=False)


def downgrade() -> None:
    """Downgrade: Drop all tables (revert schema)"""
    # Drop tables in reverse order (children first)
    op.drop_table('ulasan')
    op.drop_table('item_pesanan')
    op.drop_table('pesanan')
    op.drop_table('alamat')
    op.drop_table('produk')
    op.drop_table('merek')
    op.drop_table('kategori')
    op.drop_table('users')