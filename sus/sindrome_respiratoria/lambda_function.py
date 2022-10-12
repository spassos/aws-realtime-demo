import logging
import datetime


from sus.sindrome_respiratoria.ingestors import AwsImunizationIngestor
from sus.sindrome_respiratoria.writers import SNSWriter


def lambda_handler(event, context):
    logging.info(f"event received: {event}")

    AwsImunizationIngestor(
        writer=SNSWriter,
        default_start_date=datetime.date(2022, 10, 10),
    ).ingest()
