import openai as openai
openai.api_key = ""
response = openai.Image.create(
  prompt="positive colors",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
# a close up, studio photographic portrait of a white siamese cat that looks curious, backlit ears
print("image_url")