import json
# import sagemaker
import boto3
import base64
# from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2022-10-24-11-38-39-840"

# session = boto3.client(sagemaker) not needed usign runtime client

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['image_data'])
        ## TODO: fill in)

    # Instantiate a Predictor
    # predictor = session.predictor.Predictor(
    #     ENDPOINT,
    # sagemaker_session=session
    # )
    ## TODO: fill in

    # For this model the IdentitySerializer needs to be "image/png"
    # predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    # inferences = predictor.predict(image)
    runtime = boto3.Session().client('sagemaker-runtime')
    inferences = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType='application/x-image', Body=image)
    ## TODO: fill in
    
    # We return the data back to the Step Function 
    event["inferences"] = inferences['Body'].read().decode('utf-8')
    print(event["inferences"])
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }