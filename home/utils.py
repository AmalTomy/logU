from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
from .models import UserLocation

def get_users_in_area(latitude, longitude, radius_km):
    return UserLocation.objects.annotate(
        distance=((F('latitude') - latitude) ** 2 + (F('longitude') - longitude) ** 2) ** 0.5
    ).filter(distance__lte=radius_km)

def send_notification(user, notification):
    # Your notification sending logic here
    pass

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='UTF-8')
    if not pdf.err:
        return result.getvalue()
    return None