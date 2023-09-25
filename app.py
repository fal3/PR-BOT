app.py code:

```python
from flask import Flask, request
from github import Github

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the payload data from the request
    payload = request.get_json()

    # Process the payload data
    # ...

    return 'Webhook received successfully'

if __name__ == '__main__':
    app.run()
```

Note: This is a basic skeleton code for the app.py file. You will need to add the necessary logic to implement the automated PR reviews, integration with GitHub API using PyGithub, and other features mentioned in the description.