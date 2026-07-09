"""create course

Revision ID: c7cc2414295b
Revises: 6b109160e80e
Create Date: 2026-06-25 15:03:33.523051

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7cc2414295b'
down_revision: Union[str, Sequence[str], None] = '6b109160e80e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.Create_table=('Course',
        sa.Column('id',sa.Integer(),primarykey=True),
        sa.Column('course',sa.String(100),nullable=True),
        sa.Column('student_id',sa.Integer(),nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
