"""create statements table

Revision ID: cc0cd0f35ccd
Revises: 
Create Date: 2025-01-04 19:56:03.537077

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc0cd0f35ccd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "statements",
        sa.Column("id", sa.UUID, primary_key=True)
    )


def downgrade() -> None:
    op.drop_table("statements")
