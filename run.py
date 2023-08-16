import os
import openai
openai.api_key = os.environ["OPEN_AI_KEY"]

chat_messages = []

while True:
  user_message = input("You: ")


  chat_messages.append({ "role": "user", "content": user_message})

  response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=chat_messages,
  temperature=0
  )

  ai_response = response.choices[0].message.content

  chat_messages.append({ "role": "assistant", "content": ai_response})

  print("AI: ", ai_response)