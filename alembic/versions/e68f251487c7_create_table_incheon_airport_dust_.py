"""create table Incheon Airport Dust collectrion 

Revision ID: e68f251487c7
Revises: 9e5f24a92e91
Create Date: 2023-09-19 09:48:04.500148

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'e68f251487c7'
down_revision: Union[str, None] = '9e5f24a92e91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('incheon_airport_fine_dust',
        sa.Column('uniqueVal', sa.VARCHAR(45),primary_key=True, nullable=False, comment='유니크값'),
        sa.Column('dustStationIdx', sa.Integer, nullable=False, comment='측정소 id'),
        sa.Column('dustStationName', sa.VARCHAR(45), nullable=False, comment='측정소 이름'),
        sa.Column('fcstRealDate', sa.VARCHAR(45), nullable=False, comment='예측일'),
        sa.Column('fcstDate', sa.VARCHAR(45), nullable=False, comment='예측일자'),
        sa.Column('fcstTime', sa.VARCHAR(45), nullable=False, comment='예측시간'),
        sa.Column('callDate', sa.DATETIME, nullable=False, comment='호출시간'),

        sa.Column('locationId', sa.VARCHAR(45), nullable=False, comment='위치'),
        sa.Column('type', sa.VARCHAR(45), nullable=False, comment='실내 = in / 실외 = out'),

        sa.Column('co', sa.VARCHAR(45), nullable=True, comment='일산화탄소'),
        sa.Column('co2', sa.VARCHAR(45), nullable=True, comment='이산화탄소'),
        sa.Column('no2', sa.VARCHAR(45), nullable=True, comment='이산화질소'),
        sa.Column('o3', sa.VARCHAR(45), nullable=True, comment='오존'),
        sa.Column('so2', sa.VARCHAR(45), nullable=True, comment='아황산가스'),

        sa.Column('pm10', sa.VARCHAR(45), nullable=True, comment='미세먼지'),
        sa.Column('pm2_5', sa.VARCHAR(45), nullable=True, comment='초미세먼지'),
    )


def downgrade() -> None:
    op.drop_table('incheon_airport_fine_dust')

