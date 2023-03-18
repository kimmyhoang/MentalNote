import openai as openai

response = openai.Image.create(
  prompt="I had tea with my friends today. I was so happy.",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
# a close up, studio photographic portrait of a white siamese cat that looks curious, backlit ears
print(image_url)