from huggingface_hub import HfApi, create_repo
import os

token = "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"
api = HfApi(token=token)

try:
    # First get username
    user = api.whoami()["name"]
    repo_id = f"{user}/SattvaX"

    print(f"Creating Space {repo_id}...")
    create_repo(repo_id=repo_id, repo_type="space", space_sdk="docker", exist_ok=True, token=token)

    print("Uploading files...")
    api.upload_folder(
        folder_path=".",
        repo_id=repo_id,
        repo_type="space",
        ignore_patterns=["deploy.py", "__pycache__/*", "*.pyc", ".git/*"]
    )
    print(f"Successfully deployed to https://huggingface.co/spaces/{repo_id}")
except Exception as e:
    print(f"Error during deployment: {e}")
