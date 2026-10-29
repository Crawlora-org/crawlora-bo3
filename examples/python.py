import os

from crawlora_bo3 import BO3Client

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with BO3Client(api_key=api_key) as client:
    match_history = client.match_history()
    print('match_history', match_history)
    economy_baseline = client.economy_baseline()
    print('economy_baseline', economy_baseline)
