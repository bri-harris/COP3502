from pathlib import Path
import json

nums = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(nums)
path.write_text(contents)