#!/usr/bin/env bash

sam build
sam deploy  --stack-name test-app\
            --region us-west-2\
            --force-upload\
            --capabilities CAPABILITY_IAM\
            --confirm-changeset\
            --s3-bucket aws-sam-cli-managed-default-samclisourcebucket-1r1e095fjjfep