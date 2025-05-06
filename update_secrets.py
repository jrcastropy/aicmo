import boto3, os, json
from dotenv import load_dotenv, dotenv_values

# Load env file
# load_dotenv(dotenv_path=".env")
# Load the .env file (it returns a dict but doesn't touch system env)
env_vars = dotenv_values(".env")

# Get only the keys
secret_value = {k:env_vars[k] for k in list(env_vars.keys())}
with open("costing.json", "r") as f:
    # Read the JSON file and parse it, NO NEED to load it into a dict
    secret_value['COST'] = f.read()

# Initialize the boto3 client for Secrets Manager
AWS_ACCESS_KEY_ID = secret_value.get("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = secret_value.get("AWS_SECRET_ACCESS_KEY", None)
AWS_REGION = secret_value.get("AWS_REGION", None)
aws_creds = {}
# If the AWS credentials are not set in the environment, load them from the .env.dev file
if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY or not AWS_REGION:
    env_vars_dev = dotenv_values(".env.dev")
    aws_creds = {
        "aws_access_key_id": env_vars_dev.get("AWS_ACCESS_KEY_ID", None),
        "aws_secret_access_key": env_vars_dev.get("AWS_SECRET_ACCESS_KEY", None),
        "region_name": env_vars_dev.get("AWS_REGION", None),
    }


client = boto3.client('secretsmanager', **aws_creds)

# Put the secret into AWS Secrets Manager
response = client.put_secret_value(
    SecretId='lambda',
    SecretString=json.dumps(secret_value)
)

# Print the response
# print(response)
