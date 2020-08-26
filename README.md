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


