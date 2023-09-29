"""create version data

Revision ID: 96ee36f9259a
Revises: 9a95d41ec8dd
Create Date: 2023-09-15 13:15:43.938023

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '96ee36f9259a'
down_revision: Union[str, None] = '9a95d41ec8dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('weather_version',
                    sa.Column('id', sa.Integer, primary_key=True, index=True, autoincrement=True, comment=''),
                    sa.Column('status', sa.VARCHAR(45), nullable=False, comment='상태값 / success 00'),
                    sa.Column('status_str', sa.VARCHAR(45), nullable=False, comment='상태값 설명'),
                    sa.Column('type', sa.VARCHAR(45), nullable=True,
                              comment='VSRT : 초단기예보 , ODAM : 초단기실황 , SHRT : 단기예보  '),
                    sa.Column('version', sa.VARCHAR(45), nullable=True, comment='버전 정보'),
                    sa.Column('call_datetime', sa.DATETIME, nullable=False, comment='호출 시간'),
                    sa.Column('datetime', sa.VARCHAR(45), nullable=False, comment='수집기 돌린 시간'),
                    sa.Column('used', sa.Integer, nullable=False, comment='수집시 체크',default=0),
                    )


def downgrade() -> None:
    op.drop_table('weather_version')

