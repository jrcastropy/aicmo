# CLAUDE.md — AICMO

## Project Overview

AICMO is a Python package providing an AI/ML toolkit for serverless-ready applications (AWS Lambda, GCP Cloud Functions). It wraps multiple services — LLM APIs, web scraping, screenshot capture, image processing, vector search, and AWS storage — into a single `AICMOClient` class.

**Author**: Jayr Castro | **Version**: 0.0.4 (see `setup.py:3`) | **Python**: 3.12

## Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.12 |
| LLM | OpenAI SDK (`openai`), OpenRouter |
| Web Scraping | ScrapingBee, requests, BeautifulSoup |
| Screenshots | ScrapingBee, URLBox |
| Image Processing | OpenCV (headless), NumPy |
| AWS | boto3 (S3, Secrets Manager, Step Functions) |
| Vector Search | Typesense |
| Tokenization | tiktoken |
| Publishing | PyPI via GitHub Actions |

## Key Directories and Their Purpose

```
aicmo/
├── aicmo/__init__.py       # Entire package — single AICMOClient class (~880 lines)
├── setup.py                # Package metadata, version, dependencies
├── costing.json            # LLM model pricing (OpenAI text, image, embedding models)
├── requirements.txt        # Pip dependencies
├── update_secrets.py       # Syncs .env + costing.json -> AWS Secrets Manager
├── .env / .env.dev         # Credentials (git-ignored, never commit)
├── test.ipynb              # Integration test notebook (git-ignored)
├── .github/workflows/      # CI/CD — PyPI publish on GitHub Release
└── todo                    # Project TODO items
```

## Essential Commands

### Setup & Development

```bash
# Install build tools
pip install setuptools wheel twine

# Build distribution
python setup.py sdist bdist_wheel

# Install locally for development
pip install -e .

# Sync secrets to AWS
python update_secrets.py
```

### Testing

No automated test suite. Testing is done via `test.ipynb` (Jupyter notebook with integration tests).

### Publishing

Automatic on GitHub Release via `.github/workflows/python-publish.yml`. Requires `PYPI_API_TOKEN` in GitHub repo secrets. To bump version, edit `setup.py:3`.

## Key Conventions

- **Single module**: All logic is in `aicmo/__init__.py` within the `AICMOClient` class
- **Credentials**: Loaded from AWS Secrets Manager or passed as a `secret_dict` at init (`aicmo/__init__.py:14-38`)
- **LLM provider**: Controlled by `use_openrouter` flag — toggles between OpenAI native and OpenRouter (`aicmo/__init__.py:48-56`)
- **Cost tracking**: Token usage and costs tracked per API call; pricing defined in `costing.json`
- **Scraping fallbacks**: `scrape()` cascades through `requests` -> ScrapingBee SDK -> ScrapingBee API (`aicmo/__init__.py:417`)
- **Error reporting**: Errors sent to Slack via webhook (`aicmo/__init__.py:295`)

## Adding Features or Fixing Bugs (MANDATORY)

**Always follow this workflow:**

1. Create a new git branch before making any changes
2. Perform all work in that branch for the remainder of the session
3. Do NOT modify code on the main branch directly

```bash
git checkout -b feature/<short-description>
# or
git checkout -b fix/<short-description>
```

## Additional Documentation

Consult these files when working in specific areas:

| Topic | File |
|-------|------|
| Architecture & method reference | `.claude/docs/architecture.md` |
| Credentials & secrets management | `.claude/docs/credentials-and-secrets.md` |
| Deployment & publishing | `.claude/docs/deployment.md` |
