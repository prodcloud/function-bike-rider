# function-bike-rider

## Cloud Environment (AWS Cloud9)
`$ python3 -m venv ~/.function-bike-rider`
`$ source ~/.function-bike-rider/bin/activate`

## SSH Keys
`ssh-keygen -t ed25519 -b 4096`

Upload pubkey to github

## Create Scaffold (with Marco Polo function)

* Makefile
* hello.py
* requirements.txt

## Continuous Integration and Github Actions

* test_hello.py
* installed `pylint`, `pytest`, `black`

## Bulding a command-line tool

* use click to build a cli
*

## Explored AWS Lambda

```
def lambda_handler(event, context):
    print(f"This is my event {event}")
    if event["name"] == "Marco":
        return "Polo"
    return "No!"
```

### Use Boto3

* install boto3 and use `ipython`
* checkout https://github.com/noahgift/edge-computer-vision/face.py
*

### Build a computer vision cli

### Build a trigger that automatically runs a Lambda Function

```python
import boto3
from urllib.parse import unquote_plus

def label_function(bucket, name):
    """This takes an S3 bucket and a image name!"""
    print(f"This is the bucketname {bucket} !")
    print(f"This is the imagename {name} !")
    rekognition = boto3.client("rekognition")
    response = rekognition.detect_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": name,}},
    )
    labels = response["Labels"]
    print(f"I found these labels {labels}")
    return labels


def lambda_handler(event, context):
    """This is a computer vision lambda handler"""

    print(f"This is my S3 event {event}")
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        print(f"This is my bucket {bucket}")
        key = unquote_plus(record['s3']['object']['key'])
        print(f"This is my key {key}")

    my_labels = label_function(bucket=bucket,
        name=key)
    return my_labels
```

### GCP Cloud Function taht Translates

```python
import wikipedia

from google.cloud import translate

def sample_translate_text(text="YOUR_TEXT_TO_TRANSLATE",
    project_id="YOUR_PROJECT_ID", language="fr"):
    """Translating Text."""

    client = translate.TranslationServiceClient()

    parent = client.location_path(project_id, "global")

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        parent=parent,
        contents=[text],
        mime_type="text/plain",  # mime types: text/plain, text/html
        source_language_code="en-US",
        target_language_code=language,
    )
    print(f"You passed in this language {language}")
    # Display the translation for each input text provided
    for translation in response.translations:
        print(u"Translated text: {}".format(translation.translated_text))
    return u"Translated text: {}".format(translation.translated_text)

def translate_test(request):
    """Takes JSON Payload {"entity": "google"}
    """
    request_json = request.get_json()
    print(f"This is my payload: {request_json}")
    if request_json and 'entity' in request_json:
        entity = request_json['entity']
        language = request_json['language']
        sentences = request_json['sentences']
        print(entity)
        res = wikipedia.summary(entity, sentences=sentences)
        trans=sample_translate_text(text=res, project_id="cloudai-194723",
            language=language )
        return trans
    else:
        return f'No Payload'
```

#### Example Output of GCP Cloud Function

Send payload in:
```
{
        "entity":"google",
        "language":"es",
        "sentences":"3"
}
```
The result below:

Translated text: Google LLC es una empresa de tecnología multinacional estadounidense que se especializa en servicios y productos relacionados con Internet, que incluyen tecnologías de publicidad en línea, un motor de búsqueda, computación en la nube, software y hardware. Se considera una de las cuatro grandes empresas de tecnología junto con Amazon, Apple y Microsoft. Google fue fundada en septiembre de 1998 por Larry Page y Sergey Brin mientras eran Ph.D. estudiantes de la Universidad de Stanford en California. Juntos poseen alrededor del 14 por ciento de sus acciones y controlan el 56 por ciento del poder de voto de los accionistas a través de acciones de supervotación.


Finally, you can call from the CLI:

```bash
gcloud functions call translate-wikipedia --data '{"entity":"google", "sentences
": "20", "language":"es"}'
```
