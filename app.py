from flask import Flask, render_template, request
from transformers import pipeline, AutoTokenizer, AutoModelWithLMHead

import openai as openai

from chatbot import script

import requests

#api key
openai.api_key = "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" #add key
#pip install transformers[sentencepiece] <-- might have to install

import requests

app = Flask('app_name')
classifier = pipeline("sentiment-analysis")
tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-emotion")
model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-emotion")

emotion_imgs = {
  '<pad> joy': 'imgs/joy.png',
  '<pad> sadness': 'imgs/sadness.png',
  '<pad> love': 'imgs/love.png',
  '<pad> anger': 'imgs/anger.png',
  '<pad> fear': 'imgs/fear.png',
  '<pad> surprise': 'imgs/surprise.png'
}

tempInput = script
index = 0

def get_all_imgs():
  emotion = get_emotion_type(tempInput)
  content_image_url = get_content_img(tempInput)
  style_image_path = emotion_imgs[emotion]

  content_image_path = 'imgs/pic' + index

  with open('imgs/pic1.jpg', 'wb') as handle:
      response = requests.get(content_image_url, stream=True)
      if not response.ok:
          print(response)
      for block in response.iter_content(1024):
          if not block:
              break
          handle.write(block)

  return content_image_path, style_image_path

#have both
def get_content_img(input):
  response = openai.Image.create(
    prompt= input,
    n=1,
    size="1024x1024"
  )
  url = response['data'][0]['url']
  return url

def get_sentiment_imgs(isPositive, sentiment_type):
  sentiment = ""
  return sentiment

def get_emotion_type(input):
  input_ids = tokenizer.encode(input + '</s>', return_tensors='pt')
  output = model.generate(input_ids=input_ids, max_length=2)
  dec = [tokenizer.decode(ids) for ids in output]
  emotion_type = dec[0]
  return emotion_type

@app.route("/")
def root():
  return render_template("/templates/index.html")

#change tempInput 
# @app.route("/")
def submit():
  isPositive = classifier(tempInput)
  emotion = get_emotion_type(tempInput)
  content_image_url = get_content_img(tempInput)
  style_image_path = emotion_imgs[emotion]
  print(emotion)
  
submit()