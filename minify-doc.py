# minify-doc

import os
import openai
openai.api_key = os.environ["OPEN_AI_KEY"]

 
input_text = ""

with open ("text.txt", "r") as file:
  input_text = file.read()


response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[{
  "role": "system",
   "content": "You are a text summarizer chat bot. Your goal is to summarize the text that is given to you by the user"
},
{
  "role": "user",
  "content": input_text
}],
temperature=0
)

ai_response = response.choices[0].message.content


print("Summarized text:\n\n ", ai_response)

with open("summary.txt", "w") as file:
  file.write(ai_response)