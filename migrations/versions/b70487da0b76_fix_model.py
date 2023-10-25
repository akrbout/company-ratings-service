"""Fix model

Revision ID: b70487da0b76
Revises: 330296f6ee0f
Create Date: 2023-10-25 10:06:12.278211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b70487da0b76'
down_revision: Union[str, None] = '330296f6ee0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organisation', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'organisation', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'organisation', type_='foreignkey')
    op.drop_column('organisation', 'user_id')
    # ### end Alembic commands ###
