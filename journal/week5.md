# Week 5 — DynamoDB and Serverless Caching
Hi guys! Welcome back to week 5!! It getting hotter in the kitchen but lets learn about a few definitions today.
This week will be learning about NoSQl Databases and the different types that exist.
- Then we will learn about NoSQL database in AWS which is DynamoDB. So lets start!!

 
## Introduction
**What is NoSQL**
- A flexible document management system for key-value,document, tabular and graphs.
- Non-relational, distributed and scalable. and partition tolerant and 

**Why use NoSQL?**
- Application Development Productivity.
- Large scale data
- They mainatin perfomance no matter the scale of  


**What are the characteristics of NoSQL databases?**
- Non-relational
- Distributed system that can manage large scale data while maintaining high throughput and availability.
- Scalable

**What are the differences between Non-Relational vs Relational Databases?**
| ---Non-Relational Databases---  | ---Relational Databases |
- NOT ONLY tables with fixed columns and rows vs Tables with fixed columns and rows
- Flexible schema vs Fixed Schema
- Scales out(horizontally scaling) vs Scales up(vertical scaling)

**What are the types of NoSQL database types?**
- key-value,
- document, 
- tabular and 
- graphs
- Multi-model type



## Prerequisites



## Business Use Cases
1. Will be used with our application for message caching
2. To create Amazon DynamoDB table for developers to use for their Web Application in AWS to allow for ***uninterrupted flow for a large amount of traffic in microseconds.***
3. For ***milli-second response times***, we add a Amazon DynamoDB Accelerator (DAX) to improve the response time of the DynamoDB tables that has been linked to the Web Application in AWS.
4. 

## Tasks
Have a lecture about data modeling (Single Table Design) for NoSQL
Launch DynamoDB local
Seed our DynamoDB tables with data using Faker
Write AWS SDK code for DynamoDB to query and scan put-item, for predefined endpoints
Create a production DynamoDB table
Update our backend app to use the production DynamoDB
Add a caching layer using Momento Severless Cache


## A lecture about data modeling (Single Table Design) for NoSQL
**Step 1 - DynamoDB Data Modelling Youtube video**
A flat table as we do not hva ejoins as is the case with Relational databases.
NoSQL workbench
DynamoDB Data Modelling

It is better to put similar items in the same table/ reduces complexity in the application
Globale tables?
Sort keys?
Access Patterns?
What are base tables?
What is a GSI?-Global Secondary Index
What are LSI? Local Secondary Indexes
GSI vs LSI?
4kb in read 1kb in writes.

Adavntagews of DynamoDB
Fast
Consistent

### Launch DynamoDB local
**Step 2 - Start up DynamoDB locally**
- In the backend-flask directory, install Boto3(the AWS python SDK) in our backend by pasting line 2 into ```requirements.txt``` and running line 3:
``` 
cd backend-flask/
boto3
pip install -r requirements.txt
```

- Run ```Docker-compose up``` to start up Dynamo-db local.
- In the existing ```bin``` directory, create a new folder named ```db``` and move all the db script files except for the rds script file.
- In the existing ```bin``` directory, create a new folder named ```rds``` and move the remaining rds script file.

### Seed our DynamoDB tables with data using Faker
**Step 3 -  **
- In the existing ```bin``` directory, create a new folder named ```ddb```.
- In Dynamodb, we create tables instead of databases. Therefore one of the scripts will be, ```schema-load```, ```seed```, ```drop```.

- We will then paste into the schema-load script:
```
#! /usr/bin/env python3 

import boto3
import sys 

attrs = ('endpoint_url': 'hhtp://l;ocalhost:8000')

if len(sys.argv) == 2:
 if "prod" in sysy.argv[1]:
  attrs = {}

dynamodb = boto3.client('dynamodb', ""attrs )

table_name = 'cruddur-message'

response = client.create_table(
    TableName='string',
    AttributeDefinitions=[
        {
            'AttributeName': 'pk',
            'AttributeType': 'S'
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'string',
            'KeyType': 'HASH'|'RANGE'
        },
    ],
    LocalSecondaryIndexes=[
        {
            'IndexName': 'string',
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'Projection': {
                'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                'NonKeyAttributes': [
                    'string',
                ]
            }
        },
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'string',
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'Projection': {
                'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                'NonKeyAttributes': [
                    'string',
                ]
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 123,
                'WriteCapacityUnits': 123
            }
        },
    ],
    BillingMode='PROVISIONED'|'PAY_PER_REQUEST',
    ProvisionedThroughput={
        'ReadCapacityUnits': 123,
        'WriteCapacityUnits': 123
    },
    StreamSpecification={
        'StreamEnabled': True|False,
        'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
    },
    SSESpecification={
        'Enabled': True|False,
        'SSEType': 'AES256'|'KMS',
        'KMSMasterKeyId': 'string'
    },
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    TableClass='STANDARD'|'STANDARD_INFREQUENT_ACCESS',
    DeletionProtectionEnabled=True|False
)

```

- Change the permissions of the schema-load bash script file by running, in the terminal:
```chmod u+x bin/ddb/schema-load```

- 




**Step 4 - **


**Step **

### Security best practises for DynamoDB
**Types of Access to DynamoDB**
- Using Internet Gateway.
- Using VPC/Gateway Endpoints
- DynamoDB Accelerator(DAX)
- Cross Account

**Security best Practises - AWS**
Amazon Dynamodb is part of an  account NOT a virtual Network
- Use VPC endpoints: Use Amazon VPC to create a private network from our application or Lambda to a DynamoDB . This prevents unauthorized access to the instance from the public internet.
- Data Security & Compliance: Compliance standard should be followed for the business requirements.
- Amazon DynamoDB should only be in the AWS region that we are legally allowed to hold user data in.
- Amazon organizations SCP - to manage DynamoDB Table deletion, DynbamoDB creation, region lock.
- AWS CloudTrail is enabled & monitored to trigger appropriate alerts on malicious DynamoDB behaviour by an identity in AWS.
- AWS Config rules is enabled in the account and region of DynamoDB.

**Security best Practises - Application**
AWS recommends using Client side encryption when storing sensitive information. But dynamoDB should not be used to store sensitive information, RDS databases should be used instead to store sensitive information for long periods.
- DynamoDB to use appropriate Authentication - Use IAM Roles/ AWS Cognito Identity Pool (Avoid IAM Users/Groups).
- DynamoDB User Lifecycle Management - Create, Modify, Delete Users.
- AWS IAM roles instead of individual users to access and manage DynamoDB.
- DAX Service9IAM) Role to have Read Only Access to DynamoDB.
- Not have DynamoDB be accessed from the internet(use VPC endpoints instead).
- Site-to-Site VPN or Direct Connect for Onpremise and DynamoDB Access.
- Client side encryption is recommended by Amazon for DynamoDB.



## Next Steps - Additional Homework Challenges



**RESOURCES**
1. [NoSQL DynamoDB Workbench](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.html)
2. [AWS SDK Boto3 Python DynamoDB Documentation]([https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/create_table.html))
