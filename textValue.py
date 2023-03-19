from flask import Flask, request, render_template
app = Flask(__name__)
import requests



@app.route("/")
def input_form():
  return render_template('index.html')


# View our quick start guide to get your API key:
# https://www.voiceflow.com/api/dialog-manager#section/Quick-Start


api_key = "VF.DM.641654237683eb0007641490.GuP5FuwvU7noF1Vh"
user_id = "TEST_USER"  # Unique ID used to track conversation state
user_input = "Hello world!"  # User's message to your Voiceflow assistant

body = {"action": {"type": "text", "payload": "Hello world!"}}

# Start a conversation
response = requests.post(
    f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact",
    json=body,
    headers={"Authorization": api_key},
)

print(response.json())
# Log the response

  


# @app.route('/', methods=['POST'])
# def input_form_post():
#   text = request.form['journal']
#   return text

if __name__ == "__main__":
  app.run()