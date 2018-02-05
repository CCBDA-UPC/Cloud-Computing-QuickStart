# Getting Started in the Cloud (with AWS)

We advise you to join the [**AWS Educate Program**](https://aws.amazon.com/education/awseducate/) to take advantage of educational material such as hands-on experience with AWS technology, training, content, career pathways and the AWS Educate job board. Students from member institutions, such as Universitat Politècnica de Catalunya - BarcelonaTech, can obtain 100USD in credits to explore all AWS services.

To get quick overview of AWS, watch this [quick tour of the basics of AWS](https://youtu.be/ubCNZRNjhyo) for anybody who wants to begin using AWS. If you get carried out by the video, before you fill in the form, remember that if you are a student, you'd better register as so to obtain the extra perks.

## Create EC2 AWS instances
Amazon Elastic Compute Cloud (EC2) is the Amazon Web Service you can use to create and run virtual machines in the cloud (AWS call these virtual machines 'instances'). If you are not familiar with Debian-based distributions like Ubuntu, don't worry, you can choose a 14.04 or 16.04 version, that currently are the most commonly used. Amazon Linux is similar and for our purposes works fine too.
If you have not yet created an EC2 instance, you can follow this [step-by-step guide to launch a Linux virtual machine](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/) on Amazon EC2 within an [AWS Free Tier](https://aws.amazon.com/free/).

## Connecting to your Linux Instance Using SSH
After you launch your instance, using this [link](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html) you can find more details about how to interact with your EC2 instance

### Obtain your AWS credentials

Check [Creating, Disabling, and Deleting Access Keys for Your AWS Account](https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html) to obtain the `Access Key ID` and `AWS Secret Access Key` for the configuration.

Use your AWS account email address and password to sign in to the AWS Management Console as the AWS account root user.

Usually, you need to create users and groups to control who has access to what resource. Since this hands-on is thinking of a student who connects to an AWS account for training purposes, we are going to use the maximum privileged "root" account. In a production environment, you may want to have root access keys disabled or under severe control. On the [IAM Dashboard page](https://console.aws.amazon.com/iam/home?region=eu-west-1#/home), go to Security Status, expand "Delete root access keys", and then choose Manage Security Credentials.

![Lab06-11](./img/aws02.png "User")

If you see a warning about accessing the security credentials for your AWS account, choose to Continue to Security Credentials.

![Lab06-10](./img/aws01.png "Group")


Expand the Access keys (access key ID and secret access key) section. Choose to Create New Access Key.


![Lab06-12](./img/aws03.png "Group")

Then choose Download Key File to save the access key ID and secret access key to a file on your computer.


![Lab06-13](./img/aws04.png "Group")

### Install and configure AWS CLI and EB CLI

[AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) and [Elastic Beanstalk Command Line Interface](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html) will allow you to interact with Amazon Web Services from your command line and through Python, or other programming languages, libraries. They provide convenient access to the AWS REST API.

Check the [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) to for detailed instructions on how to install the `aws` command on your operating system. Obtain your AWS credentials and configure it.


```
_$ pip install awscli --upgrade
_$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: eu-west-1
Default output format [None]: ENTER
_$ aws --version
aws-cli/1.14.32 Python/3.6.1 Darwin/17.4.0 botocore/1.8.36
```

Check that `aws --version` and `eb --version` prompt something similar to what you can read above and below.

```
_$ pip install awsebcli —upgrade
_$ eb —version
EB CLI 3.12.1 (Python 3.6.3)
```



## Alternative
If you prefer to use another Cloud provider instead AWS, please feel free to do so. However, you should communicate your decision to your teacher (an email is enough) before starting the assignments.
