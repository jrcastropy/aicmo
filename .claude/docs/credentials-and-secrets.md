# Credentials & Secrets Management

## Overview

Secrets are managed through AWS Secrets Manager and local `.env` files. The `update_secrets.py` script syncs local `.env` + `costing.json` to AWS Secrets Manager under the secret name `lambda`.

## Environment Files

- `.env` — Production credentials (git-ignored)
- `.env.dev` — Development/local credentials with AWS keys for Secrets Manager access (git-ignored)

## Required Secret Keys

| Key | Service |
|-----|---------|
| `OPENAI_API_KEY` | OpenAI API |
| `OPENAI_ORG_KEY` | OpenAI organization |
| `OPENROUTER_API_KEY` | OpenRouter API |
| `OPENROUTER_BASE_URL` | OpenRouter endpoint |
| `OPENROUTER_MODEL` | Default OpenRouter model |
| `SCRAPINGBEE_API_KEY` | ScrapingBee web scraping |
| `AWS_S3_BUCKET` | S3 bucket name |
| `AWS_ACCESS_KEY_ID` | AWS access key |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key |
| `AWS_REGION` | AWS region |
| `URLBOX_API_KEY` | URLBox screenshot API |
| `URLBOX_API_SECRET` | URLBox HMAC secret |
| `SLACK_WEBHOOK` | Slack error notifications |
| `TS_HOST` | Typesense host |
| `TS_PORT` | Typesense port |
| `TS_API_KEY` | Typesense API key |
| `COST` | Serialized JSON from `costing.json` |

## Updating Secrets

```bash
python update_secrets.py
```

This reads `.env` and `costing.json`, merges them, and uploads to AWS Secrets Manager. If `.env` lacks AWS credentials, it falls back to `.env.dev` for the boto3 client.

## Client Initialization

Credentials can be provided two ways (`aicmo/__init__.py:14-27`):
1. **Direct dict**: Pass `secret_dict` with all keys above
2. **AWS Secrets Manager**: Pass `aws_secret_name` (and optionally AWS credentials) to auto-load
