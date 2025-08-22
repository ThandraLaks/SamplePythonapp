import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Read logs from file
with open("app.log", "r") as f:
    logs = f.read()

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a DevOps log analyzer."},
        {"role": "user", "content": f"Summarize these logs and highlight issues:\n{logs}"}
    ]
)

print("=== AI Log Analysis ===")
print(response["choices"][0]["message"]["content"])
