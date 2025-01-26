import json
from os import error
from pathlib import Path
import boto3
from botocore.exceptions import ClientError
from mypy_boto3_textract.type_defs import DetectDocumentTextResponseTypeDef

RESPONSE_PATH: str = Path(__file__).parent / "data" / "response.json"
IMAGE_PATH: str = Path(__file__).parent / "images" / "lista-material-escolar.jpeg"


def get_document_lines() -> list[str]:
    try:
        with open(RESPONSE_PATH) as file:
            data: DetectDocumentTextResponseTypeDef = json.loads(file.read())
            blocks: list = data["Blocks"]
        return extract_lines_for_blocks(blocks)
    except IOError:
        detect_file_text(aws_detect_file_text)
    return []


def detect_file_text(fn):
    data_json = fn()
    with open(RESPONSE_PATH) as file:
        file.write(data_json)


def aws_detect_file_text() -> str:
    client = boto3.client("textract")
    with open(IMAGE_PATH, "rb") as file:
        image_bytes = file.read()
    try:
        response = client.detect_document_text(Document={"Bytes": image_bytes})
        return json.dumps(response)
    except ClientError as e:
        print(f"Error in processing: {e}")


def extract_lines_for_blocks(blocks: list):
    return [block["Text"] for block in blocks if block["BlockType"] == "LINE"]


if __name__ == "__main__":
    for line in get_document_lines():
        print(line)
    pass
