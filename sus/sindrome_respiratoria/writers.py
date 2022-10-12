import datetime
import json
import os
from typing import List
import boto3
from dotenv import load_dotenv

load_dotenv()

SNS_TOPIC = os.getenv('SNS_TOPIC')


class DataTypeNotSupportedForIngestionException(Exception):
    def __init__(self, data):
        self.data = data
        self.message = f"Data type {type(data)} is not supported for ingestion"
        super().__init__(self.message)


class DataWriter:

    def __init__(self, api: str) -> None:
        self.api = api
        self.sns = boto3.client('sns')
        self.topic_arn = SNS_TOPIC

    def _write_json(self, data):
        pass

    def _write_to_topic(self, data: [List, dict]):
        pass

    def write(self, data: [List, dict]):
        pass


class SNSWriter(DataWriter):

    def __int__(self, api) -> None:
        super().__init__(api)

    def _write_json(self, data):
        return json.dumps(data)

    def _write_to_topic(self, data: [List, dict]):
        if isinstance(data, dict):
            self._write_json(data)
        elif isinstance(data, List):
            for element in data:
                self.write(element)
        else:
            raise DataTypeNotSupportedForIngestionException(data)

    def write(self, data: [List, dict]):
        self._write_to_topic(data=data)

    def _write_to_topic(self, data):
        for item in data:
            self.sns.publish(
                TopicArn=self.topic_arn,
                Message=json.dumps(item)
            )
