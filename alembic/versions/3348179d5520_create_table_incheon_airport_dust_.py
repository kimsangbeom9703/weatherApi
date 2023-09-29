"""create table Incheon Airport Dust collectrion list data 

Revision ID: 3348179d5520
Revises: e68f251487c7
Create Date: 2023-09-19 11:15:02.913948

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3348179d5520'
down_revision: Union[str, None] = 'e68f251487c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('incheon_airport_fine_dust_station',
        sa.Column('id', sa.Integer, primary_key=True, index=True,autoincrement=True,comment=''),
        sa.Column('stationName', sa.VARCHAR(45), nullable=False, comment='측정소 이름'),
        sa.Column('stationType', sa.VARCHAR(45), nullable=False, comment='실내 / 실외'),
    )


def downgrade() -> None:
    op.drop_table('incheon_airport_fine_dust_station')


