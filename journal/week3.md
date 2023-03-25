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
1. For the purpose of this application, we will be intergrating Amazon Cognito with our backend application with custom login pages.
2. AWS Cognito is a User Directory for Customer that can be used to access AWS resources.

## Tasks
- Provision via ClickOps a Amazon Cognito User Pool
- Implement API calls to Amazon Coginto for custom login, signup, recovery and forgot password page
- Show conditional elements and data based on logged in or logged out
- Verify JWT server side to serve authenticated API endpoints in Flask Application

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

### Install and configure Amplify client-side library for Amazon Congito
### Provision via ClickOps a Amazon Cognito User Pool
**Step 1 - Configure a User pool using AWS Cognito Cosnole**
- We will first use the AWS Console to configure a Userpool which is necessary to intergrate an application and we want to authenticate users.

### 
**Step 2 - implementing the Cognito Authentication in our frontend-js application**
- In the front-end-js folder, we will install the AWS Amplify libraries in the package.json file by pasting in and running the code in the terminal:
```
cd frontend-js
npm i aws-amplify --save
```

- To connect/hook-up our front-end application with AWS , we will open the ```app.js``` file in ```frontend-js/src/``` and paste in line 2:
```
cd frontend-js/src/app.js
import { Amplify } from 'aws-amplify';
```

- To configure amplify and connect our cognito pool to our frontend app.js, we will paste in the following in the ```app.js``` file.
```
Amplify.configure({
  "AWS_PROJECT_REGION": process.env.REACT_APP_AWS_PROJECT_REGION,
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

-In the Docker-compose file, in the frontend section of the code, we will add in the following:
```
   REACT_APP_AWS_PROJECT_REGION: "${AWS_DEFAULT_REGION}"
   REACT_APP_AWS_COGNITO_REGION: "${AWS_DEFAULT_REGION}"
   REACT_APP_AWS_USER_POOLS_ID: "us-east-1_randomrandom"
   REACT_APP_CLIENT_ID: ""    
```

***An error that I kept on encountering while trying to run the command below
``` aws cognito-idp admin-set-user-password --user-pool-id us-east-1_vvv --username maureen --password Nxxxxxxxx --permanent```
An error occurred (InvalidParameterException) when calling the AdminSetUserPassword operation: 1 validation error detected: Value at 'password' failed to satisfy constraint: Member must satisfy regular expression pattern: ^[\S]+.*[\S]+$***
***I had to make sure to create a new user in the Cognito user pool and delete the previous one.***

### Show conditional elements and data based on logged in or logged out
**Step 3 - Home Page to show components only when logged in/out**
- In the frontend add the follwoing lines:
```
cd frontend-js/src/pages/HomeFeedPage.js
import { Amplify } from 'aws-amplify';
```

- We will replace the existing on-submit code-block with:
```
// check if we are authenicated
const checkAuth = async () => {
  Auth.currentAuthenticatedUser({
    // Optional, By default is false. 
    // If set to true, this call will send a 
    // request to Cognito to get the latest user data
    bypassCache: false 
  })
  .then((user) => {
    console.log('user',user);
    return Auth.currentAuthenticatedUser()
  }).then((cognito_user) => {
      setUser({
        display_name: cognito_user.attributes.name,
        handle: cognito_user.attributes.preferred_username
      })
  })
  .catch((err) => console.log(err));
};
```

- In the ```ProfileInfo.js``` page, we will replace the Athentication with cookies page with the code in line 2below:
```
import Cookies from 'js-cookie';

with

import { Auth } from 'aws-amplify';
```

- Since we will not be using cookies anymore, we will paste in the code below:
```
const signOut = async () => {
  try {
      await Auth.signOut({ global: true });
      window.location.href = "/"
  } catch (error) {
      console.log('error signing out: ', error);
  }
}
```

- Make sure that our up is running without errors by starting up the container using Docker-compose up.

**Step 4 - Modifying the Sign in page**
- In the ```Signin.js``` page, we will replace the Athentication with cookies page with the code below:
```
cd frontend-js/src/pages/SignInPage.js
import Cookies from 'js-cookie';

with

import { Auth } from 'aws-amplify';
```

- Then add in:
```
const onsubmit = async (event) => {
  setErrors('')
  event.preventDefault();
  try {
    Auth.signIn(email, password)
      .then(user => {
        console.log('user', user)
        localStorage.setItem("access_token", user.signInUserSession.accessToken.jwtToken)
        window.location.href = "/"
      })
      .catch(err => { console.log('Error!', err) });
  } catch (error) {
    if (error.code == 'UserNotConfirmedException') {
      window.location.href = "/confirm"
    }
    setCognitoErrors(error.message)
  }
  return false
}

```

- Go to the AWS Cognito userpool console page and create a user.


**Step 5 - Attempting Log in using the Sign In tab **
- In the terminal, run:
```
aws cognito-idp admin-set-user-password --username andrewbrown --password Testing1234 --userpoolid numbernumber --permanent
```

- Run the frontend page again and it should not give an error when we use the password and username set above. The page should be working!

**Step 6 - Modifying the Sign Up page**
- Paste the following in the ```frontend-js/signup.js/```:
```
cd frontend-js/src/pages/SignUpPage.js
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
      setCognitoErrors(error.message)
  }
  return false
}
```

- Refresh to see if it works, try signing in in the front page

**Step 7 - Modifying the Confirmation Page **
- Paste the following in the ```frontend-js/confimation.js/```:
```
cd frontend-js/src/pages/ConfirmationPage.js
import { Auth } from 'aws-amplify';
```

- We will replace the existing on-submit code-block with:
```
const resend_code = async (event) => {
  setErrors('')
  try {
    await Auth.resendSignUp(email);
    console.log('code resent successfully');
    setCodeSent(true)
  } catch (err) {
    // does not return a code
    // does cognito always return english
    // for this to be an okay match?
    console.log(err)
    if (err.message == 'Username cannot be empty'){
      setCognitoErrors("You need to provide an email in order to send Resend Activiation Code")   
    } else if (err.message == "Username/client id combination not found."){
      setCognitoErrors("Email is invalid or cannot be found.")   
    }
  }
}
```

- We will replace the existing on-submit code-block with:
```
const onsubmit = async (event) => {
  event.preventDefault();
  setErrors('')
  try {
    await Auth.confirmSignUp(email, code);
    window.location.href = "/"
  } catch (error) {
    setCognitoErrors(error.message)
  }
  return false
}
```

- Refresh the page and attempt to use the sign up page and create a new user. This should work and an email should be sent to the email address you have provided!
- Go to the AWS Cognito user pool console to confirm that the user has been created.
- Sign in after verification so that it can be seen as having logged in.

**Step 8 - Modifying the Recovery Page**
- Paste the following in the ```frontend-js/RecoveryPage.js/```:
```
cd frontend-js/src/pages/RecoveryPage.js
import { Auth } from 'aws-amplify';
```

- Then paste in the following code:
```
const resend_code = async (event) => {
  setErrors('')
  try {
    await Auth.resendSignUp(email);
    console.log('code resent successfully');
    setCodeSent(true)
  } catch (err) {
    // does not return a code
    // does cognito always return english
    // for this to be an okay match?
    console.log(err)
    if (err.message == 'Username cannot be empty'){
      setErrors("You need to provide an email in order to send Resend Activiation Code")   
    } else if (err.message == "Username/client id combination not found."){
      setCognitoErrors("Email is invalid or cannot be found.")   
    }
  }
}

const onsubmit = async (event) => {
  event.preventDefault();
  setErrors('')
  try {
    await Auth.confirmSignUp(email, code);
    window.location.href = "/"
  } catch (error) {
    setErrors(error.message)
  }
  return false
}
```

- Refresh the page and attempt to use the Recover password page and attempt to send your password. This should work and an email should be sent to the email address you have provided with the reset code!

### Backend Implementation for AWS Cognito
**Step 9 - Access Token to protect our API endpoints**
- To implement on the backend to differentiate between authenticated and unauthenticated requests.
- Add in the `HomeFeedPage.js` a header eto pass along the access token

```
  headers: {
    Authorization: `Bearer ${localStorage.getItem("access_token")}`
  }
```

- Run Docker-compose up .
- Change to the backend folder then paste in line 2:
```
cd backend-flask/app.py
print (
  request.headers.get("Authorization")
  )
```

- For when we run itno CORS errors when trying to access the frontend-page
```
cors = CORS(
  app, 
  resources={r"/api/*": {"origins": origins}},
  headers=['Content-Type', 'Authorization'], 
  expose_headers='Authorization',
  methods="OPTIONS,GET,HEAD,POST"
)
```

- In backend-flask, create a new folder called lib and create a new file called cognito_token_verification.py:
```
import time
import requests
from jose import jwk, jwt
from jose.exceptions import JOSEError
from jose.utils import base64url_decode
from flask_awscognito.exceptions import FlaskAWSCognitoError, TokenVerifyError


class TokenService:
    def __init__(self, user_pool_id, user_pool_client_id, region, request_client=None):
        self.region = region
        if not self.region:
            raise FlaskAWSCognitoError("No AWS region provided")
        self.user_pool_id = user_pool_id
        self.user_pool_client_id = user_pool_client_id
        self.claims = None
        if not request_client:
            self.request_client = requests.get
        else:
            self.request_client = request_client
        self._load_jwk_keys()

    def _load_jwk_keys(self):
        keys_url = f"https://cognito-idp.{self.region}.amazonaws.com/{self.user_pool_id}/.well-known/jwks.json"
        try:
            response = self.request_client(keys_url)
            self.jwk_keys = response.json()["keys"]
        except requests.exceptions.RequestException as e:
            raise FlaskAWSCognitoError(str(e)) from e

    @staticmethod
    def _extract_headers(token):
        try:
            headers = jwt.get_unverified_headers(token)
            return headers
        except JOSEError as e:
            raise TokenVerifyError(str(e)) from e

    def _find_pkey(self, headers):
        kid = headers["kid"]
        # search for the kid in the downloaded public keys
        key_index = -1
```


## Next Steps - Additional Homework Challenges



**RESOURCES**
1. [AWS Cognito Amplify documentation](https://docs.amplify.aws/lib/auth/emailpassword/q/platform/js/)
2. 
