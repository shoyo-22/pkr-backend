"""create tournament table

Revision ID: 4951ff7cf249
Revises: 
Create Date: 2023-10-29 00:06:05.724241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4951ff7cf249"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tournaments",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("name", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("tournaments")
    pass
