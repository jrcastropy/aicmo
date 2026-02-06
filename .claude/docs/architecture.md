# Architecture

## Single-Class Design

All functionality lives in `AICMOClient` (`aicmo/__init__.py:13`). The class is initialized with AWS credentials (or a pre-loaded secrets dict) and sets up clients for all integrated services.

### Initialization Flow (`aicmo/__init__.py:14-92`)

1. Load secrets from AWS Secrets Manager or accept a `secret_dict` directly
2. Initialize AWS clients (S3, Step Functions)
3. Initialize OpenAI client (native or OpenRouter based on `use_openrouter` flag)
4. Initialize ScrapingBee client
5. Initialize tiktoken tokenizer
6. Optionally initialize Typesense client
7. Load cost/pricing config from `COST` key in secrets (serialized JSON from `costing.json`)

### Provider Strategy

- **LLM**: Dual-provider support — OpenAI native or OpenRouter proxy (`aicmo/__init__.py:48-56`)
- **Web Scraping**: Cascading fallback — `requests` -> ScrapingBee SDK -> ScrapingBee API (`aicmo/__init__.py:417-445`)
- **Screenshots**: ScrapingBee and URLBox APIs (`aicmo/__init__.py:540-647`)
- **Vector Search**: Typesense for semantic/RAG queries (`aicmo/__init__.py:708-771`)

### Token & Cost Tracking

Token usage is tracked per-call via `get_gpt_tokens()` (`aicmo/__init__.py:196`). Pricing data is loaded from `costing.json` and stored in secrets. Supports cached vs. non-cached input token costs for OpenRouter.

### Error Handling

Errors are reported via Slack webhook through `send_error()` (`aicmo/__init__.py:295`).

## Key Methods by Category

### LLM Interaction
- `tools_call_gpt()` — Function/tool calling (`aicmo/__init__.py:108`)
- `chat_completion_gpt()` — Standard chat completion (`aicmo/__init__.py:146`)
- `get_gpt_tokens()` — Token counting + cost calculation (`aicmo/__init__.py:196`)

### Web Scraping
- `scrape()` — Main entry point with fallbacks (`aicmo/__init__.py:417`)
- `scrape_requests()` — Simple HTTP (`aicmo/__init__.py:397`)
- `scrape_scrapingbee_sdk()` — JS-capable scraping (`aicmo/__init__.py:349`)

### Search & Research
- `google_search_scrapingbee()` — Google search (`aicmo/__init__.py:448`)
- `research()` — Multi-step research with similarity scoring (`aicmo/__init__.py:773`)

### Screenshots
- `screenshot_webpage()` — ScrapingBee screenshots (`aicmo/__init__.py:540`)
- `screenshot_webpage_urlbox()` — URLBox screenshots (`aicmo/__init__.py:596`)
- `crop_images()` — Image segmentation (`aicmo/__init__.py:663`)

### AWS Storage
- `s3_upload_pickle()` — Serialize & upload (`aicmo/__init__.py:230`)
- `s3_upload_image()` — Upload images (`aicmo/__init__.py:252`)
- `s3_upload_json()` — Upload JSON (`aicmo/__init__.py:271`)

### Vector Search (Typesense)
- `ts_semantic_search()` — Semantic search (`aicmo/__init__.py:708`)
- `ts_upsert_data()` — Insert/update records (`aicmo/__init__.py:761`)
