"""Change Token model

Revision ID: bc3e6ab92065
Revises: 790dfab0ee7d
Create Date: 2023-10-26 01:17:11.137179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc3e6ab92065'
down_revision: Union[str, None] = '790dfab0ee7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('token', sa.Column('expires_in', sa.DateTime(), nullable=False))
    op.add_column('token', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('token', 'is_active')
    op.drop_column('token', 'expires_in')
    # ### end Alembic commands ###