"""add image column

Revision ID: db689eee96c3
Revises: 4951ff7cf249
Create Date: 2023-10-29 01:26:30.954891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "db689eee96c3"
down_revision: Union[str, None] = "4951ff7cf249"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("tournaments", sa.Column("image", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("tournaments", "image")
    pass
