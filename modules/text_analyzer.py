from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from cognitivedoc_pipeline.variables.azure_auth import key, endpoint
from cognitivedoc_pipeline.modules.ocr import ocr_azure
from cognitivedoc_pipeline.helpers.chunking_text import split_text, analyze_entities
import typing
key = key
endpoint = endpoint

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=key)
text = ocr_azure(key, endpoint, "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf")
documents = split_text(text, chunk_size=5000)

result = analyze_entities(text_analytics_client, documents)
result = [text for text in result if not text.is_error]

print(result[:5])


