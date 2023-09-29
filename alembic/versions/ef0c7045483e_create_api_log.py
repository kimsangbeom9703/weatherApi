"""create api_log

Revision ID: ef0c7045483e
Revises: e412ee8e2e56
Create Date: 2023-09-21 11:07:40.870680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'ef0c7045483e'
down_revision: Union[str, None] = 'e412ee8e2e56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('auth_api_service_log',
                    sa.Column('id', sa.Integer, primary_key=True, index=True, autoincrement=True, comment=''),
                    sa.Column('serviceKey', sa.VARCHAR(90), nullable=False, unique=True,
                              comment='서비스키'),
                    sa.Column('serviceTypeId', sa.Integer, nullable=False, unique=True,
                              comment='서비스타입 ID'),
                    sa.Column('serviceType', sa.VARCHAR(90), nullable=False, unique=True,
                              comment='서비스타입 / all / incheon / weather / airkorea '),
                    sa.Column('endpoint', sa.VARCHAR(255), nullable=False, comment='url'),
                    sa.Column('request_count', sa.Integer, nullable=True, comment='요청 횟수'),
                    sa.Column('last_used_at', sa.DATETIME, nullable=True, comment='마지막 사용 날짜 '),
                    )
    op.create_foreign_key('auth_api_log_fk', source_table="auth_api_service_log",
                          referent_table="auth_api_service_key",
                          local_cols=['serviceKey'], remote_cols=['serviceKey'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_table('auth_api_service_key')
