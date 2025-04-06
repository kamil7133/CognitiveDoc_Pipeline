import typing
def split_text(text: str, chunk_size: int = 5000) -> typing.List[str]:
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

from azure.ai.textanalytics import TextAnalyticsClient, RecognizeEntitiesResult
from azure.core.credentials import AzureKeyCredential

def analyze_entities(text_analytics_client, documents):
    results = []
    for i in range(0, len(documents), 5):
        batch = documents[i:i+5]
        response = text_analytics_client.recognize_entities(documents=batch)
        results.extend(response)
    return results