"""create table authservice_key 

Revision ID: 2b23e210a34a
Revises: c38cbaeb9ed3
Create Date: 2023-09-21 10:07:25.756109

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2b23e210a34a'
down_revision: Union[str, None] = 'c38cbaeb9ed3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('auth_api_service_key',
                    sa.Column('id', sa.Integer, primary_key=True, index=True, autoincrement=True, comment=''),
                    sa.Column('serviceKey', sa.VARCHAR(90),  nullable=False, unique=True,
                              comment='서비스키'),
                    sa.Column('serviceTypeId', sa.Integer,  nullable=False,
                              comment='서비스타입 ID'),
                    sa.Column('serviceType', sa.VARCHAR(90), nullable=False,
                              comment='서비스타입 / all / incheon / weather / airkorea '),
                    sa.Column('description', sa.TEXT, nullable=True, comment='설명'),
                    sa.Column('created_at', sa.DATETIME, nullable=True, comment='생성 시간'),
                    sa.Column('expires_at', sa.DATETIME, nullable=True, comment='만료 시간'),
                    sa.Column('is_active', sa.Integer, nullable=True, default=0, comment='활성화 여부 / 활성화 0 / 비활성화 1'),
                    )


def downgrade() -> None:
    op.drop_table('auth_api_service_key')
