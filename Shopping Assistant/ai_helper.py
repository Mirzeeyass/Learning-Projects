import requests


class AIHelper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.model = "llama-3.3-70b-versatile"

    def suggest_items(self, items):
        item_names = [item.name for item in items]
        item_list = ", ".join(item_names)

        prompt = f"I have these items on my shopping list: {item_list}. Suggest 5 items I might have forgotten. Be brief, just list the items."

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": self.model,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        data = response.json()
        return data["choices"][0]["message"]["content"]
        
