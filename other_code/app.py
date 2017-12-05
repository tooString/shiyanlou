import os
import json
from flask import Flask


def create_app():
    app = Flask('rmon')
    file = os.environ,get('RMON_CONFIG')
    content =''
    with open(file) as f:
        for l in f:
            l.strip()
            if l.startswith('#'):
                continue
            else:
                content += l
    data = json.loads(content)
    for key in data:
        app.config[key.upper()] = data.get(key)

    return app
