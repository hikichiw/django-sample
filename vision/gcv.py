import io

from PIL import Image, ImageDraw
from google.cloud import vision


def draw_boxes(image, bounds, color):
    """
    画像内に枠線を書き出す

    :param image: 画像ファイル
    :param bounds: 枠線位置
    :param color: 色
    """
    draw = ImageDraw.Draw(image)

    for bound in bounds:
        draw.polygon([
            bound.vertices[0].x, bound.vertices[0].y,
            bound.vertices[1].x, bound.vertices[1].y,
            bound.vertices[2].x, bound.vertices[2].y,
            bound.vertices[3].x, bound.vertices[3].y], None, color)


def output_image(bounds, in_file):
    """
    枠線を追加した画像出力

    :param bounds: 枠線出力位置
    :param in_file: 入力ファイル
    :return 画像オブジェクト
    """
    image = Image.open(in_file)
    draw_boxes(image, bounds['block'], 'blue')
    draw_boxes(image, bounds['paragraph'], 'red')
    draw_boxes(image, bounds['word'], 'yellow')
    byte_io = io.BytesIO()
    image.save(byte_io, format='PNG')
    return byte_io.getvalue()


def label_detection(client, image):
    """
    ラベル検出

    :param client: APIクライアント
    :param image: 画像ファイル
    :return: 検出結果
    """
    labels = []
    response = client.label_detection(image=image)
    for label in response.label_annotations:
        labels.append((label.description, label.score))
    return labels


def document_text_detection(client, image):
    """
    OCR検出

    :param client: APIクライアント
    :param image: 画像ファイル
    :return: 検出位置
    """
    bounds = {
        'symbol': [],
        'word': [],
        'paragraph': [],
        'block': [],
    }
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    bounds['word'].append(word.bounding_box)
                bounds['paragraph'].append(paragraph.bounding_box)
            bounds['block'].append(block.bounding_box)
    return bounds


def text_detection(client, image):
    """
    テキスト検出

    :param client: APIクライアント
    :param image: 画像ファイル
    :return: 検出結果
    """
    response = client.text_detection(image=image)
    text = response.text_annotations
    return text[0].description


def analyze_img(in_file):
    """
    画像ファイル解析

    :param in_file: 入力ファイル
    :return: ラベル検出結果、テキスト検出結果、画像オブジェクト
    """
    with io.open(in_file, 'rb') as image_file:
        content = image_file.read()
    # noinspection PyTypeChecker
    image = vision.Image(content=content)
    # google cloud vision apiクライアント
    client = vision.ImageAnnotatorClient()
    # ラベル検出
    # noinspection PyTypeChecker
    labels = label_detection(client, image)
    # ドキュメントテキスト検出
    # noinspection PyTypeChecker
    bounds = document_text_detection(client, image)
    # テキスト検出
    # noinspection PyTypeChecker
    texts = text_detection(client, image)
    # イメージ出力
    out_image = output_image(bounds, in_file)
    return labels, texts, out_image
