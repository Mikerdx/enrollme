"""Add unique constraint on (student_id, course_id)

Revision ID: c85bc4d3dd39
Revises: 52707f89961d
Create Date: 2025-06-20 17:00:16.423832
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c85bc4d3dd39'
down_revision = '52707f89961d'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode for SQLite compatibility
    with op.batch_alter_table('Enrollments', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_student_course', ['student_id', 'course_id'])

    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.alter_column(
            'password',
            existing_type=sa.VARCHAR(length=8),
            type_=sa.String(length=128),
            existing_nullable=False
        )


def downgrade():
    with op.batch_alter_table('Enrollments', schema=None) as batch_op:
        batch_op.drop_constraint('uq_student_course', type_='unique')

    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.alter_column(
            'password',
            existing_type=sa.String(length=128),
            type_=sa.VARCHAR(length=8),
            existing_nullable=False
        )
