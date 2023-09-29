"""forgenkey 

Revision ID: 46878860020c
Revises: dee9b96934dc
Create Date: 2023-09-21 10:44:06.242666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46878860020c'
down_revision: Union[str, None] = 'dee9b96934dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key('service_type_auth_key_fk', source_table="auth_api_service_key", referent_table="auth_api_service_type",
                          local_cols=['serviceTypeId'], remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    pass
