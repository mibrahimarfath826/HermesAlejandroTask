from google.cloud import storage
import json

def upload_to_gcs(file_name, data, bucket_name="your-default-bucket"):
    try:
        #GCP storage client
        client = storage.Client()
        
        #Get the bucket
        bucket = client.bucket(bucket_name)
        
        #Create a blob and upload the data
        blob = bucket.blob(file_name)
        blob.upload_from_string(json.dumps(data), content_type="application/json")
        
        print(f"File {file_name} successfully uploaded to bucket {bucket_name}.")
    except Exception as e:
        print(f"An error occurred while uploading to GCS: {e}")
