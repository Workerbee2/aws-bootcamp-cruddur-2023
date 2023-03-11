# Week 3 — Decentralized Authentication

 
## Introduction

## Prerequisites


## Use Cases

## Tasks

**Step 1 - Configure a User pool using AWS Cognito**
- We will first use the AWS Console to configure a Userpool.

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

-In the Docker-compose file, we will add in the following:
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
1. 
