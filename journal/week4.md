# Week 4 — Postgres and RDS

## Introduction

Whry AWS RDS Postgres over AWS Aurora?
## Prerequisites
1. AWS FRee Tier account
2. AWS CLI on your local environment
3. Knowledge of SQL and PostgreSQL.
4. 

## Use Cases

## Tasks

**Step 1 - Spin up an PostgreSQL RDS(Relational Database System) via the AWS GUI**
- We will first have to spin up an RDS instance on AWS then stop it.
1. Search for RDS and choose **Create database**
2. On **Engine options**, choose Postgres
3. Choose the **Free tier** check box
4. Choose the **Instance configuration**
5. For **Storage**, leave the default option.
6. For **Connectivity** and **Network type** leave the default options.
7. For **Public Access** , allow public access
8. Use the **Default VPC** security group.
9. For **Database port**, leave it as the default 5432
10. For **Database authentication**, aloow for password authentication.
11. As for Monitoring, so that we can see 
12. We will turn off Backup, which is whnen AWS takes a snapshot of th DB for backup whuich reduces costs 
13. Enable **Encryption**
14. Do not enable **Log exports**
15. Do not **Enable Deletion protection**, which for production should be turned on for backup purposes.

**Step 2 - Use the AWS CLI in Gitpod to create/provision an RDS instance **
- Use the following command to create an RDS instance via the CLI, notice that the commands follow the set up in Step 1.
```
aws rds create-db-instance \
  --db-instance-identifier cruddur-db-instance \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --engine-version  14.6 \
  --master-username cruddurroot \
  --master-user-password milkyway2023 \
  --allocated-storage 20 \
  --availability-zone us-east-1a \
  --backup-retention-period 0 \
  --port 5432 \
  --no-multi-az \
  --db-name cruddur \
  --storage-type gp2 \
  --publicly-accessible \
  --storage-encrypted \
  --enable-performance-insights \
  --performance-insights-retention-period 7 \
  --no-deletion-protection
```

- Switch over to the AWS Console and view the creation process of the database instance. 
- When the database instance has been fully created, the status will read created.
- Click into the Database instance and Stop temporarily, it is stopped for 7 days (be sure to check on it after 7 days).
- Start up Docker compose, then open the Docker extension and make sure that Postgres has started up,( we added Postgres into the Docker-compose file in the earlier weeks)
- Open the Postgres bash then, to be able to run psql commands inside the database instance we created above, run the following commands:
```
sudo apt update
sudo apt install -y postgresql-client-12
psql -Upostgres --host localhost
(When it prompts for password enter: ***password***
```

- Then to list existing databases run ```\l```
- To create a new database called cruddur we will run
``` CREATE database cruddur; ```

- 
 
**Step 3 -  **




**Step 4 - T**


**Step **


## Next Steps - Additional Homework Challenges



**RESOURCES**
1. [AWS RDS CLI - Documentation](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html)
2. 
