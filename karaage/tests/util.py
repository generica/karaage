# Copyright 2007-2010 VPAC
#
# This file is part of Karaage.
#
# Karaage is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Karaage is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Karaage  If not, see <http://www.gnu.org/licenses/>.

from django.contrib.auth.models import User

import datetime

from karaage.people.models import Person, Institute
from karaage.projects.models import Project
from karaage.machines.models import Machine, MachineCategory, UserAccount


def fill_database():
    institute = Institute.objects.create(name='VPAC', gid=3)
    machine_category = MachineCategory.objects.create(name='VPAC')
    Machine.objects.create(
        name='tango', 
        no_cpus=20, 
        no_nodes=10, 
        category=machine_category,
        start_date='2008-01-01',
        )
    super_user = User.objects.create_user('super', 'sam@vpac.org', 'aq12ws')
    super_user.is_superuser = True
    super_user.save()
    s_user = Person.objects.create(
        user=super_user,
        first_name='Super',
        last_name='Test',
        title='Mr',
        institute=institute,
        country='AU',
    )
    user = User.objects.create_user('delegate', 'sam@vpac.org', 'aq12ws')
    delegate = Person.objects.create(
        user=user,
        first_name='Delegate',
        last_name='Test',
        title='Mr',
        institute=institute,
        country='AU',
    )
    dummy_user = User.objects.create_user('dummy', 'sam@vpac.org', 'aq12ws')
    dummy = Person.objects.create(
        user=dummy_user,
        first_name='Dummy',
        last_name='Test',
        title='Mr',
        institute=institute,
        country='AU',
    )
    institute.delegate = delegate
    institute.active_delegate = delegate
    institute.save()
    user = User.objects.create_user('leader', 'sam@vpac.org', 'aq12ws')
    leader = Person.objects.create(
        user=user,
        first_name='Leader',
        last_name='Test',
        title='Mr',
        institute=institute,
        country='AU',
    )
    project = Project.objects.create(
        pid='test',
        name='test project',
        leader=leader,
        start_date = datetime.date.today(),
        machine_category=machine_category,
        institute=institute,
        is_active=True,
        is_expertise=True,
        is_approved=True,
    )