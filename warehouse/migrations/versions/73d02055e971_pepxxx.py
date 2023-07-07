# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
pepxxx

Revision ID: 73d02055e971
Revises: 4a0276f260c7
Create Date: 2023-07-07 06:59:32.041509
"""

import sqlalchemy as sa

from alembic import op

revision = "73d02055e971"
down_revision = "4a0276f260c7"


def upgrade():
    op.execute(
        """
        INSERT INTO admin_flags(id, description, enabled, notify)
        VALUES (
            'disallow-pepxxx-upload',
            'Disallow projects using PEP XXX reserved names',
            FALSE,
            FALSE
        )
    """
    )


def downgrade():
    op.execute("DELETE FROM admin_flags WHERE id = 'disallow-pepxxx-upload'")
