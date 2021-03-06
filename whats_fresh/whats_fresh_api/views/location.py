from django.http import HttpResponse
from whats_fresh.whats_fresh_api.models import Vendor
import json


def locations(request):
    """
    */locations/*

    Returns a list of city names for all vendors. Useful for populating
    selection lists.
    """
    vendor_list = Vendor.objects.all()
    cities = [vendor.city for vendor in vendor_list]
    unique_cities = [
        {'location': city[0], 'name': city[1]}
        for city in enumerate(set(cities))]

    data = {
        'locations': unique_cities,
        'error': {
            'status': False,
            'name': None,
            'text': None,
            'level': None,
            'debug': None
        }
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
