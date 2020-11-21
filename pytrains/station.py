import requests

from .untangle import parse
from .data import getLink, getName
from .service import Service

class Station:
    def __init__(self, crs):
        self.crs = crs
        self.name = getName(crs)
        self.link = getLink(crs)

        self.updateServices()

    def updateServices(self):
        request = requests.get("http://iris2.rail.co.uk/tiger/{}".format(self.link))
        parsedRequest = parse(request.text).StationBoard
        
        self.services = []
        for service in parsedRequest.Service:
            if service.ServiceType["Type"] == "Originating" or service.ServiceType["Type"] == "Through":
                self.services.append(Service(service))

    def __repr__(self):
        return "<Station {} ({})>".format(
            self.name,
            self.crs
        )