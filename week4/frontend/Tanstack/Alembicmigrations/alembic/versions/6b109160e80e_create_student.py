"""create student

Revision ID: 6b109160e80e
Revises: 
Create Date: 2026-06-25 14:57:51.267282

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b109160e80e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('Student',
        sa.Column('id',sa.Integer(),primary_key=True),
        sa.Column('name',sa.String(100),nullable=True),
        sa.Column('age',sa.Integer(),nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
