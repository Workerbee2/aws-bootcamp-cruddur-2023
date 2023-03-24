# Week 3 — Decentralized Authentication

 
## Introduction
**What is Decentralized Authentication?**


**What is Amazon Cognito?**


**User pools vs User Identity pools in AWS Cognito?**


**What is the User Lifecycle Management?**


**What is Token Lifecycle Management?**


## Prerequisites
1. An AWS Account.
2. Github account
3. Gitpod account

## Use Cases
1. AWS Cognito is a User Directory for Customer that can be used to access AWS resources.

## Tasks
Provision via ClickOps a Amazon Cognito User Pool
Implement API calls to Amazon Coginto for custom login, signup, recovery and forgot password page
Show conditional elements and data based on logged in or logged out
Verify JWT server side to serve authenticated API endpoints in Flask Application

### Decentralized Authentication in AWS Cloud
**Types of Authentication**
- OAuth
- OpenID Connect (used with OAuth)
- Username/Password
- SAML/ Single Sign on & Identity Provider
- Traditional Authentication

**Benefits of using AWS Cognito**
- Provides a User Directory for Customers.
- Provides ability to access AWS Resources for the Application being built.
- Identity Broker for AWS Resources with Temporary Credentials.
- Can extend users to AWS resources easily.

**Amazon Cognito Security Best Practises - for AWS**
- AWS Services - API Gateway, AWS Resources shared with the App Client(Backend or Back Channels).
- AWS WAF with Web ACLs for Rate Limiting, Allow/Deny List, Deny access from region & many more waf managementrules similar to OWASP.
- Amazon Cognito Compliance standard is what your business requires.
- Amazon Cognito should only be in the AWs region that you are legally allowed to be holding user data in.
- Amazon Organizations SCP - to manage User Pool deletion, creation, region lock etc
- AWS CloudTrail is enabled & monitored to trigger alerts on malicious Cognito behaviour by an identity in AWS.

**Amazon Cognito Security Best Practises - for the Application**
- Application should use an industry standard for Authentication & Authorization(SAML, OpenID Connect, OAuth2.0)
- App User Lifecycle Management - create, Modify, Delete users
- AWS User Access Lifecycle Management - Change of roles/ Revoke Roles
- Role based Access to manage how much access to AWS resources for the Application being built
- Token Lifecycle Management - Issue new tokens, revoke compromised tokens, where to store (client/server).
- Security tests of the application thropugh penetration testing.
- Access Token Scope - should be limited
- JWT(JSON Web Token) best practise - no sensitive info
- Encryption in Transit for API calls


### Intergrating Amazon Cognito with the backend application with custom login branches
### Install and configure Amplify client-side library for Amazon Congito
**Step 1 - Configure a User pool using AWS Cognito Cosnole**
- We will first use the AWS Console to configure a Userpool which is necessary to intergrate an application and we want to authenticate users.

**Step 2 - **
- In the front-end-js folder, we will install the AWS Amplify libraries in the package.json file by pasting in and running the code in ```frontend-js```
```
npm i aws-amplify --save
```

- To connect/hook-up our front-end application with AWS , we will open the ```app.js``` file in ```frontend-js/src/``` and paste in:
```
import { Amplify } from 'aws-amplify';
```

- To connect our cognito pool to our frontend app.js, we will paste in the following
```
Amplify.configure({
  "AWS_PROJECT_REGION": process.env.REACT_AWS_PROJECT_REGION,
  "aws_cognito_region": process.env.REACT_APP_AWS_COGNITO_REGION,
  "aws_user_pools_id": process.env.REACT_APP_AWS_USER_POOLS_ID,
  "aws_user_pools_web_client_id": process.env.REACT_APP_CLIENT_ID,
  "oauth": {},
  Auth: {
    // We are not using an Identity Pool
    // identityPoolId: process.env.REACT_APP_IDENTITY_POOL_ID, // REQUIRED - Amazon Cognito Identity Pool ID
    region: process.env.REACT_AWS_PROJECT_REGION,           // REQUIRED - Amazon Cognito Region
    userPoolId: process.env.REACT_APP_AWS_USER_POOLS_ID,         // OPTIONAL - Amazon Cognito User Pool ID
    userPoolWebClientId: process.env.REACT_APP_AWS_USER_POOLS_WEB_CLIENT_ID,   // OPTIONAL - Amazon Cognito Web Client ID (26-char alphanumeric string)
  }
});
```

-In the Docker-compose file, in the frontend section, we will add in the following:
```
   REACT_AWS_PROJECT_REGION:
   REACT_APP_AWS_COGNITO_REGION:
   REACT_APP_AWS_USER_POOLS_ID:
   REACT_APP_CLIENT_ID:    
```

An error that I kept on encountering while trying to run the command below

aws cognito-idp admin-set-user-password --user-pool-id us-east-1_vvv --username maureen --password Nxxxxxxxx --permanent

An error occurred (InvalidParameterException) when calling the AdminSetUserPassword operation: 1 validation error detected: Value at 'password' failed to satisfy constraint: Member must satisfy regular expression pattern: ^[\S]+.*[\S]+$

I had to make sure to create a new user in the Cogniuto user pool and delete the previous one.


**Step 3 - Sign Up Page **
- Paste the following in the ```frontend-js/signup.js/```:
```
import { Auth } from 'aws-amplify';
```

- We will replace the existing on-submit code-block with:
```
  const onsubmit = async (event) => {
    event.preventDefault();
    setErrors('')
    try {
      const { user } = await Auth.signUp({
        username: email,
        password: password,
        attributes: {
          name: name,
          email: email,
          preferred_username: username,
        },
        autoSignIn: { // optional - enables auto sign in after user is confirmed
            enabled: true,
        }
      });
      console.log(user);
      window.location.href = `/confirm?email=${email}`
    } catch (error) {
        console.log(error);
        setErrors(error.message)
    }
    return false
  }
```


**Step 4 - T**


**Step **


## Next Steps - Additional Homework Challenges



**RESOURCES**
1. [](https://docs.amplify.aws/lib/auth/emailpassword/q/platform/js/)
