
import io
import sys
import json

from rich import print

file_ = sys.argv[1]
with io.open(file=file_, mode='r', encoding='utf-8') as fs: print(
    json.loads(fs.read())
)