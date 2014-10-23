# Copyright 2014 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""extra_dhcp_options IPv6 support

Revision ID: 16cdf118d31d
Revises: 1f71e54a85e7
Create Date: 2014-10-23 17:04:19.796731

"""

# revision identifiers, used by Alembic.
revision = '16cdf118d31d'
down_revision = '1f71e54a85e7'

from alembic import op
import sqlalchemy as sa



def upgrade():
    op.add_column('extradhcpopts', sa.Column('ip_version', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('extradhcpopts', 'ip_version')
