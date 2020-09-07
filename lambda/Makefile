S3_BUCKET = for-lambda-build-bucket
STACK_NAME = test-app-2
TEMPLATE = template.yaml


clean:
	rm -rf .aws-sam

lambda:
	sam build

build:  clean lambda

deploy: build
	sam package \
    --template-file $(TEMPLATE) \
    --s3-bucket $(S3_BUCKET)
	
	sam deploy \
    --template-file $(TEMPLATE) \
    --stack-name $(STACK_NAME) \
	--s3-bucket $(S3_BUCKET) \
    --capabilities CAPABILITY_IAM \
	--no-confirm-changeset

delete-stack:
	aws cloudformation delete-stack --stack-name $(STACK_NAME)