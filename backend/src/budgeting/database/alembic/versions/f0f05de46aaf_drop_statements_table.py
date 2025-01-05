"""drop statements table

Revision ID: f0f05de46aaf
Revises: cc0cd0f35ccd
Create Date: 2025-01-05 16:49:25.803310

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0f05de46aaf'
down_revision: Union[str, None] = 'cc0cd0f35ccd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("statements")


def downgrade() -> None:
    op.create_table(
        "statements",
        sa.Column("id", sa.UUID, primary_key=True),
        sa.Column("valid_as_of", sa.DateTime),
        sa.Column("number_of_transactions", sa.Integer)
    )
