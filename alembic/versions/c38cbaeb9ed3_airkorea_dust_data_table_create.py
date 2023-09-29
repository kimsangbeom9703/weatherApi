"""airkorea dust data table create 

Revision ID: c38cbaeb9ed3
Revises: 37c019228a56
Create Date: 2023-09-20 10:45:29.437055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c38cbaeb9ed3'
down_revision: Union[str, None] = '37c019228a56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('airkorea_dust_data',
                sa.Column('uniqueVal', sa.VARCHAR(45), primary_key=True, nullable=False, comment='유니크값'),
                sa.Column('dustStationIdx', sa.Integer, nullable=False, comment='측정소 id'),
                sa.Column('dustStationName', sa.VARCHAR(45), nullable=False, comment='측정소 이름'),
                sa.Column('dustStationCode', sa.VARCHAR(45), nullable=False, comment='api에서 제공되는 코드'),

                sa.Column('fcstRealDate', sa.VARCHAR(45), nullable=False, comment='예측일'),
                sa.Column('fcstDate', sa.VARCHAR(45), nullable=False, comment='예측일자'),
                sa.Column('fcstTime', sa.VARCHAR(45), nullable=False, comment='예측시간'),
                sa.Column('callDate', sa.DATETIME, nullable=False, comment='호출시간'),

                sa.Column('mangName', sa.VARCHAR(45), nullable=True, comment='측정망 정보'),
                sa.Column('sidoName', sa.VARCHAR(45), nullable=False, comment='시도 이름'),
                sa.Column('so2Value', sa.VARCHAR(45), nullable=True, comment='아황산가스'),
                sa.Column('coValue', sa.VARCHAR(45), nullable=True, comment='일산화탄소 농도'),
                sa.Column('o3Value', sa.VARCHAR(45), nullable=True, comment='오존 농도'),
                sa.Column('no2Value', sa.VARCHAR(45), nullable=True, comment='이산화질소 농도'),
                sa.Column('pm10Value', sa.VARCHAR(45), nullable=True, comment='미세먼지(pm10)'),
                sa.Column('pm10Value24', sa.VARCHAR(45), nullable=True, comment='미세먼지(PM10)24시간예측이동농도'),
                sa.Column('pm25Value', sa.VARCHAR(45), nullable=True, comment='미세먼지(PM2.5)'),
                sa.Column('pm25Value24', sa.VARCHAR(45), nullable=True, comment='미세먼지(PM2.5)24시간예측이동농도'),
                sa.Column('khaiValue', sa.VARCHAR(45), nullable=True, comment='통합대기환경수치'),
                sa.Column('khaiGrade', sa.VARCHAR(45), nullable=True, comment='통합대기환경지수'),
                sa.Column('so2Grade', sa.VARCHAR(45), nullable=True, comment='아황산가스 지수'),
                sa.Column('o3Grade', sa.VARCHAR(45), nullable=True, comment='오존 지수'),
                sa.Column('no2Grade', sa.VARCHAR(45), nullable=True, comment='이산화질소 지수'),
                sa.Column('pm10Grade', sa.VARCHAR(45), nullable=True, comment='미세먼지(PM10) 24시간 등급자료'),
                sa.Column('pm25Grade', sa.VARCHAR(45), nullable=True, comment='미세먼지(PM2.5) 24시간 등급자료'),
                sa.Column('pm10Grade1h', sa.VARCHAR(45), nullable=True, comment='미세먼지(PM10) 1시간 등급자료'),
                sa.Column('pm25Grade1h', sa.VARCHAR(45), nullable=True, comment='미세먼지(PM2.5) 1시간 등급자료'),
                sa.Column('so2Flag', sa.VARCHAR(45), nullable=True, comment='아황산가스 플래그'),
                sa.Column('coFlag', sa.VARCHAR(45), nullable=True, comment='일산화탄소 플래그'),
                sa.Column('o3Flag', sa.VARCHAR(45), nullable=True, comment='오존 플래그'),
                sa.Column('no2Flag', sa.VARCHAR(45), nullable=True, comment='이산화질소 플래그'),
                sa.Column('pm10Flag', sa.VARCHAR(45), nullable=True, comment='미세먼지(PM10) 플래그'),
                sa.Column('pm25Flag', sa.VARCHAR(45), nullable=True, comment='미세먼지(PM2.5) 플래그'),

                )


def downgrade() -> None:
    op.drop_table('airkorea_dust_data')

