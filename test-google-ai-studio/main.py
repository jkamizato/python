from google import genai
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())
apikey = os.getenv('GEMINI_API_KEY')

#print(apikey)

print(os.environ)

# client = genai.Client(api_key=apikey)
#
# text_prompt = input("Please enter your prompt: ")
#
# response = client.models.generate_content(
#     model="gemini-3-flash-preview", contents=f"{text_prompt}"
# )
# print(response.text)
#
