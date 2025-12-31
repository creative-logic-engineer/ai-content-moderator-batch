import json
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

# 1. BATCH DATA: Put all comments in one go
comments_to_check = [
    "I love this video, so helpful!",
    "You are an absolute idiot and I hate you.",
    "This is okay, but could be better.",
    "Go away and never come back."
]

# 2. THE PROMPT: Ask for JSON
prompt = f"""
Analyze the sentiment of these comments. 
Return ONLY a valid JSON list of objects with the keys 'text' and 'sentiment'.
Sentiment must be 'SAFE' or 'TOXIC'.

Comments: {comments_to_check}
"""

response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents=prompt,
    # This tells Gemini to strictly output JSON
    config={'response_mime_type': 'application/json'}
)

# 3. PARSING: No more "in response.text" guessing!
results = json.loads(response.text)

for entry in results:
    # Now we check the EXACT value
    if entry['sentiment'] == "TOXIC":
        print(f"❌ FLAGGED: {entry['text']}")
    else:
        print(f"✅ CLEARED: {entry['text']}")
