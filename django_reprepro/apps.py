# This file is part of django-reprepro (https://github.com/mathiasertl/django-reprepro).
#
# django-reprepro is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# django-reprepro is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See
# the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with django-reprepro.  If
# not, see <http://www.gnu.org/licenses/>.

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoRepreproConfig(AppConfig):
    name = 'django_reprepro'
    verbose_name = _('Package repositories')
