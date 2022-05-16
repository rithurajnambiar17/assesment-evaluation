from distutils.command.upload import upload
import os
import io
from xml.dom.minidom import Document
import boto3
import logging
from PIL import Image, ImageDraw
from botocore.exceptions import ClientError
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.static_folder = 'static'

@app.route('/')
def main():
   return render_template('index.html')

@app.route('/submit', methods = ['POST', 'GET'])
def result(): 
   # Taking all the inputs
   reg = request.form.get('reg')
   name = request.form.get('name')
   email = request.form.get('email')
   f = request.files['file']

   # Storing the file in the working directory in the static folder
   file_extension = str(f.filename).split('.')[1]
   f_name = reg+ '-' +name + '.' + file_extension
   f_path = 'static/working/' + f_name
   f.save(f_path)

   #Uploading the file to S3 bucket
   AWS_ACCESS_KEY_ID = ''
   AWS_SECRET_ACCESS_KEY = ''

   def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

   upload_file(f_path, bucket='assesmentevaluation')

   #OCR detection on the document
   client = boto3.client('textract', 'ap-south-1')
   response = client.detect_document_text(
      Document={
         'Bytes': b'bytes',
         'S3Object': {
               'Bucket': 'assesmentevaluation',
               'Name': f_name
         }
      }
   )

   #Sending the text to plag-api
   def plag(doc):
      pass

   #Creating Rubiric
   '''
   Plag below 30%: 
      All components contain 5 marks each and thus making the total marks 35, if any of 
      the component is missing 5 marks would be deducted directly.
   Plag between 30-50%:
      The marks would be calculated according to the above rule itself but 10 marks would 
      deducted directly due to presence of plagirism.
   Plag between 50-70%:
      The marks would be calculated according to the above rule itself but 20 marks would 
      deducted directly due to presence of plagirism.
   Plag between 70-100%
      The marks would be calculated according to the above rule itself but 30 marks would 
      deducted directly due to presence of plagirism.   
   '''
   #Sending the percentage to the rubiric
   def feedback(model, rubiric, text):
      pass
   
   def similarity(model, text1, text2):
      '''
      if two feedback returns same marks along with same amount of plagirism, then these
      two text would be assesed by similarity function, where-in the original texts of 
      both the students would be compared and cosine-similarity would be calculated.
      Given a threshold: if the similarity is more, then 10 marks would be deducted from
      each of the student, else the function would pass and no operation would be performed.
      '''
      pass

   f = open("static/working/assignment.txt", "a")
   res = response['block']
   f.write(res)
   f.close()
   return render_template('result.html', res = res)

if __name__ == '__main__':
   app.run(debug = True)