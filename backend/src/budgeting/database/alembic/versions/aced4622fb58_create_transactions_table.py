"""create transactions table

Revision ID: aced4622fb58
Revises: f0f05de46aaf
Create Date: 2025-01-05 16:49:37.561490

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aced4622fb58'
down_revision: Union[str, None] = 'f0f05de46aaf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "transactions",
        sa.Column("id", sa.UUID, primary_key=True),
        sa.Column("transaction_date", sa.DateTime),
        sa.Column("posting_date", sa.DateTime),
        sa.Column("amount", sa.Numeric(8, 2)),
        sa.Column("description", sa.Text),
        sa.Column("transaction_hash", sa.String(100))
    )


def downgrade() -> None:
    op.drop_table("transactions")
