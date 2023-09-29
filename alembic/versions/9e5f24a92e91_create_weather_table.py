"""create weather table

Revision ID: 9e5f24a92e91
Revises: 96ee36f9259a
Create Date: 2023-09-18 13:49:58.022811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9e5f24a92e91'
down_revision: Union[str, None] = '96ee36f9259a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('collection_weather_data',
                    # sa.Column('id', sa.Integer, primary_key=True, index=True, autoincrement=True, comment=''),
                    sa.Column('uniqueVal', sa.VARCHAR(45), primary_key=True, nullable=False, comment='유니크값'),
                    sa.Column('baseDate', sa.VARCHAR(45), nullable=False, comment='예보 생성일자'),
                    sa.Column('baseTime', sa.VARCHAR(45), nullable=False, comment='예보 생성시간'),
                    sa.Column('fcstRealDate', sa.VARCHAR(45), nullable=False, comment='예측일'),
                    sa.Column('fcstDate', sa.VARCHAR(45), nullable=False, comment='예측일자'),
                    sa.Column('fcstTime', sa.VARCHAR(45), nullable=False, comment='예측시간'),
                    sa.Column('callDate', sa.DATETIME, nullable=False, comment='호출시간'),
                    sa.Column('nx', sa.VARCHAR(45), nullable=False, comment='예보지점X좌표'),
                    sa.Column('ny', sa.VARCHAR(45), nullable=False, comment='예보지점Y좌표'),
                    sa.Column('icon', sa.VARCHAR(45), nullable=True, comment='아이콘'),
                    sa.Column('popVal', sa.VARCHAR(45), nullable=True, comment='강수확률'),
                    sa.Column('ptyVal', sa.VARCHAR(45), nullable=True, comment='강수형태'),
                    sa.Column('pcpVal', sa.VARCHAR(45), nullable=True, comment='강수량'),
                    sa.Column('skyVal', sa.VARCHAR(45), nullable=True, comment='하늘상태'),
                    sa.Column('rehVal', sa.VARCHAR(45), nullable=True, comment='습도'),
                    sa.Column('snoVal', sa.VARCHAR(45), nullable=True, comment='신적설'),
                    sa.Column('tmpVal', sa.VARCHAR(45), nullable=True, comment='기온'),
                    sa.Column('tmnVal', sa.VARCHAR(45), nullable=True, comment='최저기온'),
                    sa.Column('tmxVal', sa.VARCHAR(45), nullable=True, comment='최고기온'),
                    sa.Column('uuuVal', sa.VARCHAR(45), nullable=True, comment='풍속(동서)'),
                    sa.Column('vvvVal', sa.VARCHAR(45), nullable=True, comment='풍속(남북)'),
                    sa.Column('wavVal', sa.VARCHAR(45), nullable=True, comment='파고'),
                    sa.Column('vecVal', sa.VARCHAR(45), nullable=True, comment='풍향'),
                    sa.Column('wsdVal', sa.VARCHAR(45), nullable=True, comment='풍속'),
                    sa.Column('lgtVal', sa.VARCHAR(45), nullable=True, comment='낙뢰'),
                    )
def downgrade() -> None:
    op.drop_table('collection_weather_data')
