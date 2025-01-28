from pathlib import Path
import time
import boto3
from mypy_boto3_rekognition.type_defs import (
    CelebrityTypeDef,
    RecognizeCelebritiesResponseTypeDef,
)
from PIL import Image, ImageDraw, ImageFont


client = boto3.client("rekognition")


def recognize_celebrities(photo: str) -> RecognizeCelebritiesResponseTypeDef:
    with open(photo, "rb") as image:
        return client.recognize_celebrities(Image={"Bytes": image.read()})


def draw_boxes(image_path: str, output_path: str, face_details: list[CelebrityTypeDef]):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Arial.ttf", 20)

    width, height = image.size

    for face in face_details:
        box = face["Face"]["BoundingBox"]
        left = int(box["Left"] * width)
        top = int(box["Top"] * height)
        right = int((box["Left"] + box["Width"]) * width)
        bottom = int((box["Top"] + box["Height"]) * height)

        confidence = face.get("MatchConfidence", 0)
        if confidence > 90:
            draw.rectangle([left, top, right, bottom], outline="green", width=3)

            text = face.get("Name", "")
            position = (left, top - 25)
            bbox = draw.textbbox(position, text, font=font)
            draw.rectangle(bbox, fill="green")
            draw.text(position, text, font=font, fill="white")

    image.save(output_path)


def get_path(file_name: str) -> str:
    return str(Path(__file__).parent / "images" / file_name)


if __name__ == "__main__":
    start = time.time()

    PHOTOS_PATHS = (
        get_path("bbc.jpg"),
        get_path("msn.jpg"),
        get_path("neymar-torcedores.jpg"),
    )

    for photo_path in PHOTOS_PATHS:
        response = recognize_celebrities(photo_path)
        faces = response["CelebrityFaces"]
        if not faces:
            print(f"No found celebrities in picture. {photo_path}")
            continue
        output_path = get_path(f"{Path(photo_path).stem}-result.jpg")
        draw_boxes(photo_path, output_path, faces)

    print("Execution completed ({:.5f}ms)".format((time.time() - start)))
