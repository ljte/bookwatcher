"""add author and book tables

Revision ID: 595a831d2889
Revises: 
Create Date: 2025-10-22 11:54:45.287366

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

from bookwatcher.tables import Author, Book, gen_ulid

# revision identifiers, used by Alembic.
revision: str = '595a831d2889'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        Author.__tablename__,
        sa.Column(
            "id",
            sa.String(26),
            primary_key=True,
            index=True,
            default=gen_ulid,
        ),
        sa.Column("first_name", sa.String(255)),
        sa.Column("last_name", sa.String(255)),
        sa.Column(
            "birthday",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
            index=False,
        ),
    )

    op.create_table(
        Book.__tablename__,
        sa.Column(
            "id",
            sa.String(26),
            primary_key=True,
            index=True,
            default=gen_ulid,
        ),
        sa.Column("title", sa.String(255)),
        sa.Column(
            "isbn",
            sa.BigInteger(),
            unique=True,
            index=True,
            nullable=True,
        ),
        sa.Column(
            "author_id",
            sa.String(26),
            nullable=False,
            index=True,
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
            index=False,
        ),
        sa.Column(
            "finished_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
    )
    op.create_foreign_key(
        "book_author_id_fkey",
        Book.__tablename__,
        Author.__tablename__,
        ["author_id"],
        ["id"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("book_author_id_fkey", Book.__tablename__)
    op.drop_table(Book.__tablename__)
    op.drop_table(Author.__tablename__)
