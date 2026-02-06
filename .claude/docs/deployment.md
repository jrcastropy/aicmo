# Deployment & Publishing

## PyPI Publishing

The package is published to PyPI automatically via GitHub Actions when a GitHub Release is created.

### Workflow: `.github/workflows/python-publish.yml`

- **Trigger**: GitHub Release published
- **Steps**: Checkout -> Setup Python 3.x -> Build with `python -m build` -> Publish via `pypa/gh-action-pypi-publish`
- **Secret required**: `PYPI_API_TOKEN` in GitHub repo secrets

### Manual Build

```bash
pip install setuptools wheel twine
python setup.py sdist bdist_wheel
```

## Versioning

Version is defined in `setup.py:3` as `VERSION = '0.0.4'`. Update this before creating a new release.

## Serverless Deployment

The package is designed to be imported in AWS Lambda and GCP Cloud Functions. Key considerations:
- Uses `opencv-python-headless` (no GUI dependencies)
- Credentials loaded from AWS Secrets Manager at runtime
- All dependencies are pip-installable for Lambda layers

## Updating Model Pricing

1. Edit `costing.json` with new model pricing
2. Run `python update_secrets.py` to sync to AWS Secrets Manager
3. Pricing structure: `costing.json` (see `openai.texts`, `openai.images`, `openai.embeddings`)
