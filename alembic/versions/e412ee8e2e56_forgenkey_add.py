"""forgenkey add 

Revision ID: e412ee8e2e56
Revises: 46878860020c
Create Date: 2023-09-21 10:50:30.949398

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e412ee8e2e56'
down_revision: Union[str, None] = '46878860020c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key('incheon_airport_fk', source_table="incheon_airport_fine_dust", referent_table="incheon_airport_fine_dust_station",
                          local_cols=['dustStationIdx'], remote_cols=['id'], ondelete="CASCADE")
    op.create_foreign_key('airkorea_dust_fk', source_table="airkorea_dust_data", referent_table="airkorea_dust_station",
                          local_cols=['dustStationIdx'], remote_cols=['id'], ondelete="CASCADE")

def downgrade() -> None:
    pass
