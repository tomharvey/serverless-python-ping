# Serverless Python Ping

A very basic python function, but with the Cloudformation and CircleCI config required to get a Python function deployed onto AWS Lambda, through CircleCI, using [Serverless](https://serverless.com)

## Functionality
When invoked it will make a GET request of google.com and report the status code of the response. It's useless, but I needed a project which needed a dependancy (requests) and had some tests.

## Problems which are solved here

1. To allow your CI provider to deploy a function to AWS, you need to give your CI platform some permission to do certain things to your AWS account. This is generally handled by giving the CI platform your admin level secret access key info. **This seems like a bad idea**

2. The [serverless framework](https://serverless.com) is great, and comes with a nice `serverless deploy` command to deploy from your workstation. I want my CI provider to run this for me, not to have a developer workstation do the deployment. This way, the usual tests and branch management processes are still adhered to.

3. Python packages are tricky to deploy through serverless. The [serverless-python-requirements plugin](https://github.com/UnitedIncome/serverless-python-requirements) is demonstrated here, as a way to get your package deployed with all of the dependancies.

4. I have a lot less bandwidth than my CI provider. If I deploy from my workstation, I have to wait for packages to upload from my machine. Here, we're only using [requests](http://docs.python-requests.org) but realistically your packages will grow and you will be left waiting for the upload. There is a timeout, with enough dependancies you will find it. By deloying from the CI platform, you only ever need to upload the git diff.


### Deployment permissions
You need to give your deployment platform (in this case, CircleCI) permission to do certain things to your AWS account. It's not made easy to find what permissions `serverless deploy` requires, and it does seem to change from version to version. This is tested using version 1.25.0

The serverless community have been tracking this on https://github.com/serverless/serverless/issues/1439 - check there if this breaks in future.

The file in `deploy/ci-user.cform` is a Cloudformation template which will create a user with the currently required permissions. Have a look at this file for a better understanding of what it grants access to. I could have restricted the permissions further, but instead opted to restrict the resources which the broad permissions can be applied to.

When using this Cloudformation template, you must provide the same service name as you specify in your `serverless.yml` file.

### CircleCI
The file in `.circleci/config.yml` will be enough to run some python tests and run a deployment process as well. The deploy process requires both Node (for serverless operations) and python.


### Usage
Example:
```
aws cloudformation deploy --template deploy/ci-user.cform --stack-name theStackName --parameter-overrides ServiceName=ChangeThis --capabilities CAPABILITY_IAM --output text
```
