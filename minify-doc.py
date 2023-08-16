# minify-doc

import os
import openai
openai.api_key = os.environ["OPEN_AI_KEY"]

 
user_input = input("Enter text that should be summarized: ")


response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[{
  "role": "system",
   "content": "You are a text summarizer chat bot. Your goal is to summarize the text that is given to you by the user"
},
{
  "role": "user",
  "content": user_input
}],
temperature=0
)

ai_response = response.choices[0].message.content


print("Summarized text:\n\n ", ai_response)