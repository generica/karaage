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

from django.contrib import admin

from karaage.software.models import SoftwareCategory, SoftwarePackage, SoftwareVersion, SoftwareLicense, SoftwareLicenseAgreement, SoftwareAccessRequest


class SoftwareLicenseAgreementAdmin(admin.ModelAdmin):
    list_display = ('user', 'license', 'date')


class SoftwareAccessRequestAdmin(admin.ModelAdmin):
    list_display = ('person', 'software_license', 'request_date')

admin.site.register(SoftwareAccessRequest, SoftwareAccessRequestAdmin)
admin.site.register(SoftwareLicenseAgreement, SoftwareLicenseAgreementAdmin)
admin.site.register(SoftwareCategory)
admin.site.register(SoftwarePackage)
admin.site.register(SoftwareVersion)
admin.site.register(SoftwareLicense)
