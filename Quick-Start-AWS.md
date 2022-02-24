# Getting Started in the Cloud (with AWS)

We advise you to join the [**AWS Educate Program**](https://aws.amazon.com/education/awseducate/) to take advantage of educational material such as hands-on experience with AWS technology, training, content, career pathways and the AWS Educate job board. Students from member institutions, such as Universitat Politècnica de Catalunya - BarcelonaTech, can obtain 100USD in credits to explore all AWS services.

To get a quick overview of AWS, watch this [quick tour of the basics of AWS](https://youtu.be/ubCNZRNjhyo) for anybody who wants to begin using AWS. If you get carried out by the video, before you fill in the form, remember that if you are a student, you'd better register as so to obtain the extra perks.

## Create EC2 AWS instances
Amazon Elastic Compute Cloud (EC2) is the Amazon Web Service you can use to create and run virtual machines in the cloud (AWS call these virtual machines 'instances'). If you are not familiar with Debian-based distributions like Ubuntu, don't worry, you can choose between 14.04 and 16.04 version, which currently are the most commonly used. Amazon Linux is similar and for our purposes works fine too.

If you have not yet created an EC2 instance, you can follow this [step-by-step guide to launch a Linux virtual machine](https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html) on Amazon EC2 within an [AWS Free Tier](https://aws.amazon.com/free/).

## Connecting to your Linux Instance Using SSH
After you launch your instance, using this [link](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html) you can find more details about how to interact with your EC2 instance

## Obtain your AWS credentials

AWS allows you to interact programmatically with their services using a REST API. You can use the REST API directly, through a command line Interface (AWS CLI) or invoking libraries available for different programming languages.

You, therefore, need a set of credentials to authenticate and authorize the access to your AWS resources.

Check [Creating, Disabling, and Deleting Access Keys for Your AWS Account](https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html) to obtain the `Access Key ID` and `AWS Secret Access Key` for the configuration.

Use your AWS account email address and password to sign in to the AWS Management Console as the AWS account root user.

Usually, you need to create users and groups to control who has access to what resource. Since this hands-on is thinking of a student who connects to an AWS account for training purposes, we are going to use the maximum privileged "root" account. In a production environment, you may want to have root access keys disabled or under severe control. On the [IAM Dashboard page](https://console.aws.amazon.com/iam/home?region=eu-west-1#/home), go to Security Status, expand "Delete root access keys", and then choose Manage Security Credentials.

![aws02](./img/aws02.png "User")

If you see a warning about accessing the security credentials for your AWS account, choose to Continue to Security Credentials.

![aws01](./img/aws01.png "Group")


Expand the Access keys (access key ID and secret access key) section. Choose to Create New Access Key.


![aws03](./img/aws03.png "Group")

Then choose Download Key File to save the access key ID and secret access key to a file on your computer.


![aws04](./img/aws04.png "Group")

## Install and configure AWS CLI and EB CLI

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

## Access your AWS resources using the command line interface (CLI)

```
_$ aws ec2 describe-instances
{
    "Reservations": [
        {
            "OwnerId": "46436xx84yy9",
            "ReservationId": "r-07c8aa893424bddec",
            "Groups": [],
            "Instances": [
                {
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "PublicDnsName": "",
                    "RootDeviceType": "ebs",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "EbsOptimized": false,
                    "LaunchTime": "2018-01-05T10:37:18.000Z",
                    "PrivateIpAddress": "172.31.12.184",
                    "ProductCodes": [],
                    "VpcId": "vpc-b4b433d3",
                    "StateTransitionReason": "User initiated (2018-01-05 10:45:36 GMT)",
                    "InstanceId": "i-04d3757be201d3f1b",
                    "EnaSupport": true,
                    "ImageId": "ami-d6cda0af",
                    "PrivateDnsName": "ip-172-31-12-184.eu-west-1.compute.internal",
                    "KeyName": "ccbda_upc",
                    "SecurityGroups": [
                        {
                            "GroupName": "ccbda_upc_security_group",
                            "GroupId": "sg-d5b478af"
                        }
                    ],
                    "ClientToken": "",
                    "SubnetId": "subnet-83962fe4",
                    "InstanceType": "t2.micro",
                    "NetworkInterfaces": [
                        {
                            "Status": "in-use",
                            "MacAddress": "02:5e:3c:ab:35:7c",
                            "SourceDestCheck": true,
                            "VpcId": "vpc-b4b433d3",
                            "Description": "",
                            "NetworkInterfaceId": "eni-6d476e43",
                            "PrivateIpAddresses": [
                                {
                                    "PrivateDnsName": "ip-172-31-12-184.eu-west-1.compute.internal",
                                    "Primary": true,
                                    "PrivateIpAddress": "172.31.12.184"
                                }
                            ],
                            "PrivateDnsName": "ip-172-31-12-184.eu-west-1.compute.internal",
                            "Attachment": {
                                "Status": "attached",
                                "DeviceIndex": 0,
                                "DeleteOnTermination": true,
                                "AttachmentId": "eni-attach-75573304",
                                "AttachTime": "2018-01-01T18:12:58.000Z"
                            },
                            "Groups": [
                                {
                                    "GroupName": "ccbda_upc_security_group",
                                    "GroupId": "sg-d5b478af"
                                }
                            ],
                            "SubnetId": "subnet-83962fe4",
                            "OwnerId": "46436xx84yy9",
                            "PrivateIpAddress": "172.31.12.184"
                        }
                    ],
                    "SourceDestCheck": true,
                    "Placement": {
                        "Tenancy": "default",
                        "GroupName": "",
                        "AvailabilityZone": "eu-west-1b"
                    },
                    "Hypervisor": "xen",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "Status": "attached",
                                "DeleteOnTermination": true,
                                "VolumeId": "vol-049fc23e02887bcc5",
                                "AttachTime": "2018-01-01T18:12:59.000Z"
                            }
                        }
                    ],
                    "Architecture": "x86_64",
                    "StateReason": {
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown",
                        "Code": "Client.UserInitiatedShutdown"
                    },
                    "RootDeviceName": "/dev/sda1",
                    "VirtualizationType": "hvm",
                    "Tags": [
                        {
                            "Value": "ccbda_ubuntu",
                            "Key": "Name"
                        }
                    ],
                    "AmiLaunchIndex": 0
                }
            ]
        }
    ]
}
```

Check the results and compare the data provided with what you can see on your web interface: in particular **Instance ID**, **Instance Type**, **Instance State**.

![aws05](./img/aws05.png "Group")

You can now start the stopped instance. Check on the web interface that it is being started.

```
_$ aws ec2 start-instances --instance-ids i-04d3757be201d3f1b
{
    "StartingInstances": [
        {
            "InstanceId": "i-04d3757be201d3f1b",
            "CurrentState": {
                "Code": 0,
                "Name": "pending"
            },
            "PreviousState": {
                "Code": 80,
                "Name": "stopped"
            }
        }
    ]
}


```

![aws06](./img/aws06.png "Running")

Don't forget to stop your EC2 instance to avoid unnecessary expenses.

## Create AWS S3 bucket

AWS S3 service stands for Simple Cloud Storage Service. The popular [Dropbox](https://www.dropbox.com/) tool is based on AWS S3. The costs of S3 are very moderate therefore we can create our version of Dropbox in less than 5 minutes.

Go to [AWS S3 management console](https://s3.console.aws.amazon.com/s3/home?region=eu-west-1) and create a new bucket following the wizard instructions.

![aws07](./img/aws07.png "Running")

Once it is created it can be accessed using AWS CLI:


```
_$ aws s3 ls s3://ccbda-upc
```

You can copy a set of files:

```
_$ aws s3 cp img s3://ccbda-upc --recursive
upload: img\aws06.png to s3://ccbda-upc/aws06.png
upload: img\README.md to s3://ccbda-upc/README.md
...
upload: img\workflow.png to s3://ccbda-upc/workflow.png
upload: img\terminology.png to s3://ccbda-upc/terminology.png
```

And you can also keep both folders in sync:

```
_$ aws s3 sync img s3://ccbda-upc/img --exclude *.md
upload: img\PyCharmConda.png to s3://ccbda-upc/img/PyCharmConda.png
upload: img\aws01.png to s3://ccbda-upc/img/aws01.png
...
upload: img\workflow.png to s3://ccbda-upc/img/workflow.png
upload: img\firstgithubcontent.png to s3://ccbda-upc/img/firstgithubcontent.png

```

Check that your files are available using the AWS S3 console.

![aws08](./img/aws08.png "Running")
