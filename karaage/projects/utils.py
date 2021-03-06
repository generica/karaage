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

from karaage.datastores import create_account
from karaage.projects.models import Project


def add_user_to_project(person, project):
    for mc in project.machine_categories.all():
        if not person.has_account(mc):
            create_account(person, project, mc)
    project.users.add(person)
    project.save()


def remove_user_from_project(person, project):
    project.users.remove(person)
    project.save()


def get_new_pid(institute):
    """ Return a new Project ID
    Keyword arguments:
    institute_id -- Institute id
    """
    number = '0001'
    prefix = 'p%s' % institute.name.replace(' ', '')[:4]

    found = True
    while found:
        try:
            Project.objects.get(pid=prefix + number)
            number = str(int(number) + 1)
            if len(number) == 1:
                number = '000' + number
            elif len(number) == 2:
                number = '00' + number
            elif len(number) == 3:
                number = '0' + number
        except Project.DoesNotExist:
            found = False

    return prefix + number
