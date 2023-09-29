"""areaCode Table Create

Revision ID: 9a95d41ec8dd
Revises: 
Create Date: 2023-09-14 13:56:26.916577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9a95d41ec8dd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



##
#   `id` int NOT NULL AUTO_INCREMENT,
#   `area_code` bigint NOT NULL COMMENT '행정구역 코드',
#   `level1` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '1단계',
#   `level2` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '2단계',
#   `level3` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '3단계',
#   `grid_x` int NOT NULL COMMENT '격자 x 좌표',
#   `grid_y` int NOT NULL COMMENT '격자 y 좌표',
#   `longitude_hour` int DEFAULT NULL COMMENT '경도(시)',
#   `longitude_minute` int DEFAULT NULL COMMENT '경도(분)',
#   `longitude_second` int DEFAULT NULL COMMENT '경도(초)',
#   `latitude_hour` int DEFAULT NULL COMMENT '위도(시)',
#   `latitude_minute` int DEFAULT NULL COMMENT '위도(분)',
#   `latitude_second` int DEFAULT NULL COMMENT '위도(초)',
#   `longitude_second_div100` decimal(6,2) DEFAULT NULL COMMENT '경도(초/100)',
#   `latitude_second_div100` decimal(6,2) DEFAULT NULL COMMENT '위도(초/100)',
#   `document_update_time` date DEFAULT NULL COMMENT '문서 업데이트 시간',
#   ##


def upgrade() -> None:
    op.create_table('area_data',
        sa.Column('id', sa.Integer, primary_key=True, index=True,autoincrement=True,comment=''),
        sa.Column('area_code', sa.BigInteger, primary_key=True,nullable=False,comment='행정구역 코드'),
        sa.Column('level1', sa.VARCHAR(255), nullable=False,comment='1단계'),
        sa.Column('level2', sa.VARCHAR(255), nullable=True,comment='2단계'),
        sa.Column('level3', sa.VARCHAR(255), nullable=True,comment='3단계'),
        sa.Column('grid_x', sa.INT, nullable=False,comment='격자 x 좌표'),
        sa.Column('grid_y', sa.INT, nullable=False,comment='격자 y 좌표'),
        sa.Column('longitude_hour', sa.INT, nullable=True,comment='경도(시)'),
        sa.Column('longitude_minute', sa.INT, nullable=True,comment='경도(분)'),
        sa.Column('longitude_second', sa.INT, nullable=True,comment='경도(초)'),
        sa.Column('latitude_hour', sa.INT, nullable=True,comment='위도(시)'),
        sa.Column('latitude_minute', sa.INT, nullable=True,comment='위도(분)'),
        sa.Column('latitude_second', sa.INT, nullable=True,comment='위도(초)'),
        sa.Column('longitude_second_div100', sa.DECIMAL(6,2), nullable=True,comment='경도(초/100)'),
        sa.Column('latitude_second_div100', sa.DECIMAL(6,2), nullable=True,comment='위도(초/100)'),
        sa.Column('document_update_time', sa.DATE, nullable=True,comment='문서 업데이트 시간'),
    )


def downgrade() -> None:
    op.drop_table('area_data')
