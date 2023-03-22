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


**Step 2 - fffgg**


**Step 3 -  **


**Step 4 - **


**Step **

### Security best practises for DynamoDB
**Types of Access to DynamoDB**
- Using Internet Gateway.
- Using VPC/Gateway Endpoints
- DynamoDB Accelerator(DAX)
- Cross Account

**Security best Practises - AWS***
Amazon Dynamodb is part of an  account NOT a virtual Network
- Use VPC endpoints: Use Amazon VPC to create a private network from our application or Lambda to a DynamoDB . This prevents unauthorized access to the instance from the public internet.
- Data Security & Compliance: Compliance standard should be followed for the business requirements.
- Amazon DynamoDB should only be in the AWS region that we are legally allowed to hold user data in.
- Amazon organizations SCP - to manage DynamoDB Table deletion, DynbamoDB creation, region lock.
- AWS CloudTrail is enabled & monitored to trigger alerts on malicious DynamoDB behabv=viou by an identity in AWS.
- AWS Config rules is enabled in the account and region of DynamoDB.



## Next Steps - Additional Homework Challenges



**RESOURCES**
1. [NoSQL DynamoDB Workbench](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.html)
