[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=stevebowerman_sls-test&metric=alert_status)](https://sonarcloud.io/dashboard?id=stevebowerman_sls-test)

# Serverless API example

Serverless framework example https://serverless.com/
- Data lookup API based on API Gateway + Lambda + S3
- Test client python script

Pre-reqs:
- AWS account with cli and access keys setup on your device
- npm installed (v6 or above, suggested)
- Python3 and pip installed

Bootstrap
- Git clone the repo
- pip install requests (suggest pip install requests --user)
- npm install -g serverless

Deploy
- sls deploy -stage dev
- Make sure you change scripts/test.py to reflect the API Gateway endpoint

Remove
- sls remove -stage dev

Data file
- To upload the mpans.csv test file to S3 (initially and when you change it), use aws cli: (in the data dir) aws s3 cp mpans.csv s3://sls-test-mpans-dev