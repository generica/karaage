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

from karaage.datastores.institutes import base
from karaage.datastores import ldap_schemas

class InstituteDataStore(base.InstituteDataStore):
    
    def create_institute(self, institute):
        cn = str(institute.name.lower().replace(' ', ''))
        if institute.gid:
            try:
                lgroup = ldap_schemas.group.objects.get(gidNumber=institute.gid)
            except ldap_schemas.group.DoesNotExist:
                lgroup = ldap_schemas.group()
                lgroup.set_defaults()
                lgroup.cn = cn
                lgroup.gidNumber = institute.gid
                lgroup.pre_create(master=None)
                lgroup.pre_save()
                lgroup.save()
        else:
                 
            try:
                lgroup = ldap_schemas.group.objects.get(cn=cn)
            except ldap_schemas.group.DoesNotExist:
                lgroup = ldap_schemas.group()
                lgroup.set_defaults()
                lgroup.cn = cn
                lgroup.pre_create(master=None)
                lgroup.pre_save()
                lgroup.save()
        return lgroup.gidNumber

    def delete_institute(self, institute):
        try:
            lgroup = ldap_schemas.group.objects.get(gidNumber=institute.gid)
        except ldap_schemas.group.DoesNotExist:
            pass
        else:
            lgroup.delete()
