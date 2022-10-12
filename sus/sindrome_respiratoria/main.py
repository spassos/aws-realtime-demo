import datetime

from sus.sindrome_respiratoria.ingestors import ImunizationIngestor
from sus.sindrome_respiratoria.writers import SNSWriter


if __name__ == "__main__":
    ImunizationIngestor(
        writer=SNSWriter,
        default_start_date=datetime.date(2022, 10, 10)
    ).ingest()


