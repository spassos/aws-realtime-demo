import datetime
import os
from abc import ABC, abstractmethod

import logging
import ratelimit
import requests
from backoff import on_exception, expo, constant
from dotenv import load_dotenv

load_dotenv()

SUS_API_USER = os.getenv('SUS_API_USER')
SUS_API_PASSWORD = os.getenv('SUS_API_PASSWORD')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class SusApi(ABC):

    def __init__(self) -> None:
        self.size = "100"
        self.base_endpoint = "https://imunizacao-es.saude.gov.br/desc-imunizacao/_search"

    @abstractmethod
    def _get_endpoint(self, **kwargs) -> str:
        pass

    @on_exception(constant, ratelimit.exception.RateLimitException, max_tries=10)
    @ratelimit.limits(calls=30, period=30)
    @on_exception(expo, requests.exceptions.HTTPError, max_tries=10)
    def get_data(self, **kwargs) -> dict:
        endpoint = self._get_endpoint(**kwargs)
        logger.info(f"Getting data from endpoint: {endpoint}")
        response = requests.post(endpoint, json={"size": self.size}, auth=(SUS_API_USER, SUS_API_PASSWORD))
        response.raise_for_status()
        json_data = response.json()
        return json_data['hits']['hits']


class ImunizationApi(SusApi):
    type = "imunization"

    def _get_endpoint(self, date: datetime.date) -> str:
        return f"{self.base_endpoint}"
