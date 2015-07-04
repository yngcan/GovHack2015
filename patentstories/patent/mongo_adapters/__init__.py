__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .IPGOD101 import IPGOD101Adapter

# Iterable list of event adapters
MONGO_PATENT_EVENT_ADAPTERS = [
    IPGOD101Adapter,
]