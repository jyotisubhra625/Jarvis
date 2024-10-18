import google.generativeai as genai

genai.configure(api_key="<API KEY>")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)