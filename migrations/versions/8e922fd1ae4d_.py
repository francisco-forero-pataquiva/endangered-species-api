"""empty message

Revision ID: 8e922fd1ae4d
Revises: 
Create Date: 2022-05-08 19:12:05.155950

"""
from alembic import op
import sqlalchemy as sa
from example import populate

# revision identifiers, used by Alembic.
revision = '8e922fd1ae4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('endangered_species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fauna_flora', sa.String(length=200), nullable=True),
    sa.Column('group', sa.String(length=200), nullable=True),
    sa.Column('family', sa.String(length=200), nullable=True),
    sa.Column('species_simplified', sa.String(length=200), nullable=True),
    sa.Column('common_name', sa.String(length=200), nullable=True),
    sa.Column('threat_category', sa.String(length=200), nullable=True),
    sa.Column('biome', sa.String(length=200), nullable=True),
    sa.Column('main_threats', sa.String(length=400), nullable=True),
    sa.Column('presence_in_protected_areas', sa.String(length=200), nullable=True),
    sa.Column('national_action_plan_for_conservation_pan', sa.String(length=200), nullable=True),
    sa.Column('fishing_management', sa.String(length=200), nullable=True),
    sa.Column('level_of_protection_in_the_national_strategy', sa.String(length=200), nullable=True),
    sa.Column('exclusive_species_in_brazil', sa.String(length=200), nullable=True),
    sa.Column('states_of_occurrence', sa.String(length=200), nullable=True),
    sa.Column('image_link', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    populate.get_processed_csv()
    # ### end Alembic commands ###

    

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('endangered_species')
    # ### end Alembic commands ###
