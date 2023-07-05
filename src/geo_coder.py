import osmnx as ox
import geopandas as gpd
import geopy as gpy
from geopy.geocoders import Nominatim  # Required to get geo coordinates from the address


address_home = 'Newtonstraße 14, 12489 Berlin'


class GeoCoder:
    def __init__(self, address=address_home):
        self.address = address
        self.geocoder = Nominatim(user_agent='Isochrone calculator')
        self.location = self.geocoder.geocode(address)

    def setAddress(self, address):
        print('Address updated: ', self.address)
        self.address = address
        self.update()

    def update(self):
        self.location = self.geocoder.geocode(self.address)

    def getGPSLocation(self, format = 'Format DMS'):
        if format == 'Format DMS':
            point = gpy.Point(self.location.latitude, self.location.longitude, self.location.altitude)
            point = point.format()
            point = point.split(",")

            return point
        else:
            return self.location.latitude, self.location.longitude
