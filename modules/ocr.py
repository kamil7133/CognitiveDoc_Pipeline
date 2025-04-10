import json
from azure.ai.formrecognizer import FormRecognizerClient, DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from cognitivedoc_pipeline.variables.azure_auth import key, endpoint
key = key
endpoint = endpoint

formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"

def ocr_azure(key: str, endpoint: str, formUrl: str) -> str:
    document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=key)

    poller = document_analysis_client.begin_analyze_document_from_url(
        model_id="prebuilt-document", document_url=formUrl)

    result = poller.result()
    result_dict = result.to_dict()

    json_output = json.dumps(result_dict, indent=2, ensure_ascii=False, sort_keys=True)
    return json_output
