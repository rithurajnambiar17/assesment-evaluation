#Detects text in a document stored in an S3 bucket. Display polygon box around text and angled text 
import boto3
import io

class ocr:
    def process_text_detection(bucket, document, region):

        #Get the document from S3
        s3_connection = boto3.resource('s3')
                            
        s3_object = s3_connection.Object(bucket,document)
        s3_response = s3_object.get()
    
        # Detect text in the document
        client = boto3.client('textract', region_name=region)

        #process using S3 object
        response = client.detect_document_text(
            Document={'S3Object': {'Bucket': bucket, 'Name': document}})

        return response