"""empty message

Revision ID: 3c3b86dfa3cd
Revises: 132f9830e1e4
Create Date: 2016-06-27 12:33:50.130597

"""

# revision identifiers, used by Alembic.
revision = '3c3b86dfa3cd'
down_revision = '132f9830e1e4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('preSurveys', sa.Column('bq_int', sa.String(length=20), nullable=True))
    op.add_column('preSurveys', sa.Column('bq_know', sa.String(length=20), nullable=True))
    op.add_column('preSurveys', sa.Column('rq_int', sa.String(length=20), nullable=True))
    op.add_column('preSurveys', sa.Column('rq_know', sa.String(length=20), nullable=True))
    op.drop_column('preSurveys', 'answer')
    op.drop_index('ix_users_age', 'users')
    op.create_index('ix_users_age', 'users', ['age'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_age', 'users')
    op.create_index('ix_users_age', 'users', ['age'], unique=1)
    op.add_column('preSurveys', sa.Column('answer', sa.VARCHAR(length=100), nullable=True))
    op.drop_column('preSurveys', 'rq_know')
    op.drop_column('preSurveys', 'rq_int')
    op.drop_column('preSurveys', 'bq_know')
    op.drop_column('preSurveys', 'bq_int')
    ### end Alembic commands ###