"""add unique key

Revision ID: eb399ef56c35
Revises: 37483bac1ae1
Create Date: 2022-12-01 15:42:23.854212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb399ef56c35'
down_revision = '37483bac1ae1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_login_data_user_name_email_id_mobile_no_key', 'user_login_data', type_='unique')
    op.create_unique_constraint(None, 'user_login_data', ['mobile_no'])
    op.create_unique_constraint(None, 'user_login_data', ['email_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_login_data', type_='unique')
    op.drop_constraint(None, 'user_login_data', type_='unique')
    op.create_unique_constraint('user_login_data_user_name_email_id_mobile_no_key', 'user_login_data', ['user_name', 'email_id', 'mobile_no'])
    # ### end Alembic commands ###
