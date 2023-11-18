from flask import Blueprint, request
from services.stations_service import get_stations_service
stations_route = Blueprint('stations_route', __name__)


@stations_route.route("/api/v1/stations/", methods=['GET'])
def get_stations():
    return get_stations_service()