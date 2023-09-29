"""create table auth_service_type 

Revision ID: dee9b96934dc
Revises: 2b23e210a34a
Create Date: 2023-09-21 10:31:31.359724

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dee9b96934dc'
down_revision: Union[str, None] = '2b23e210a34a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('auth_api_service_type',
    sa.Column('id', sa.Integer, primary_key=True, index=True, autoincrement=True, comment=''),
        sa.Column('serviceType', sa.VARCHAR(45), nullable=False, comment='서비스타입 / all / incheon / weather / airkorea '),
    )


def downgrade() -> None:
    op.drop_table('auth_api_service_type')
