# meant for Python 3, will not work with Python 2
import requests # pip install requests

api_key = "VF.DM.641654237683eb0007641490.GuP5FuwvU7noF1Vh" # it should look like this: VF.DM.XXXXXXX.XXXXXX... keep this a secret!

# user_id defines who is having the conversation, e.g. steve, john.doe@gmail.com, username_464
def interact(user_id, request):
    response = requests.post(
        f'https://general-runtime.voiceflow.com/state/user/{user_id}/interact',
        json={ 'request': request },
        headers={ 'Authorization': api_key },
    )

    for trace in response.json():
        if trace['type'] == 'speak' or trace['type'] == 'text':
            print(trace['payload']['message'])
        elif trace['type'] == 'end':
            # an end trace means the the voiceflow dialog has ended
            return False
    return True

name = "User123"
isRunning = interact(name, { 'type': 'launch' })
script = ""

while (isRunning):
    nextInput = input("")
    temp = nextInput
    script = temp

    # send a simple text type request with the user input
    isRunning = interact(name, { 'type': 'text', 'payload': temp })
  