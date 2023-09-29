"""create table airkorea dust station 

Revision ID: 37c019228a56
Revises: 3348179d5520
Create Date: 2023-09-19 17:08:07.348023

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37c019228a56'
down_revision: Union[str, None] = '3348179d5520'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('airkorea_dust_station',
    sa.Column('id', sa.Integer, primary_key=True, index=True, autoincrement=True, comment=''),
        sa.Column('stationName', sa.VARCHAR(45),primary_key=True, nullable=False, comment='측정소 이름'),
        sa.Column('items', sa.VARCHAR(45), nullable=False, comment='측정값'),
        sa.Column('addr', sa.VARCHAR(512), nullable=False, comment='주소'),
        sa.Column('year', sa.VARCHAR(45), nullable=True, comment='설치날짜'),
        sa.Column('mangName', sa.VARCHAR(45), nullable=False, comment='측정망'),
        sa.Column('dmX', sa.VARCHAR(45), nullable=False, comment='x좌표'),
        sa.Column('dmY', sa.VARCHAR(45), nullable=False, comment='y좌표'),
        sa.Column('callDate', sa.DATETIME, nullable=False, comment='호출시간'),
    )


def downgrade() -> None:
    op.drop_table('airkorea_dust_station')