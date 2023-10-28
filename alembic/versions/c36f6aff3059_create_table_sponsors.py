"""create table sponsors

Revision ID: c36f6aff3059
Revises: db689eee96c3
Create Date: 2023-10-29 01:48:54.810784

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c36f6aff3059'
down_revision: Union[str, None] = 'db689eee96c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
