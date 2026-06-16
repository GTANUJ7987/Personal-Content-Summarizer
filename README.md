| Category           | Libraries                    |
| ------------------ | ---------------------------- |
| NLP/LLM            | transformers, datasets, nltk |
| Deep Learning      | torch                        |
| Evaluation         | rouge_score, sacrebleu       |
| Data Processing    | pandas                       |
| Visualization      | matplotlib                   |
| Utility            | tqdm, PyYAML, python-box     |
| Compression        | py7zr                        |
| Cloud              | boto3                        |
| Type Safety        | mypy-boto3-s3, ensure        |
| API Serving        | fastapi, uvicorn             |
| Frontend Templates | Jinja2                       |
| Development        | notebook                     |
| Packaging          | -e .                         |


## Workflow

    1. Create Configuration file `config/config.yaml` which setup all paths application
    2. Create Parameter file `params.yaml` which sets up all the parameters of the model
    3. Create Entity file `entity/__init__.py` which create defined structure of each object
    4. # Personal-Content-Summarizer
