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

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Deletes expired applications in the NEW state and applications that have been complete for a month"
    
    def handle(self, **options):
        from karaage.applications.models import Application, UserApplication, ProjectApplication
        import datetime
        now = datetime.datetime.now()
        
        verbose = int(options.get('verbosity'))
        # Delete all expired applications
        for application in Application.objects.filter(expires__lte=now, state=Application.NEW):
            if verbose >= 1:
                print "Deleted expired application #%s" % application.id
            application.delete()
 
        month_ago = now - datetime.timedelta(days=30)
        # Delete all User applications that have been complete for 1 month
        for application in UserApplication.objects.filter(state__in=[Application.COMPLETE, Application.DECLINED], complete_date__lte=month_ago):
            if verbose >= 1:
                print "Deleted completed user application #%s" % application.id

            application.delete()

        # Delete all project applications that have been complete for 1 month
        for application in ProjectApplication.objects.filter(state__in=[Application.COMPLETE, Application.DECLINED], complete_date__lte=month_ago):
            if verbose >= 1:
                print "Deleted completed project application #%s" % application.id

            application.delete()
