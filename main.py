import openai
import os

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("API key is not set. Make sure the OPENAI_API_KEY environment variable is configured.")

client = openai.OpenAI(api_key=api_key)

def create_messages(report):
    return [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Classify this report into categories: Equipment Malfunction, Human Errors, Design Issues, Environment, Communication and Network Errors, Suspended Load. Report: {report}"}
    ]

def classify_report(report):
    messages = create_messages(report)
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # or "gpt-4o-mini"
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    report_example = "During the shift, the loader collided with a support beam due to poor visibility and malfunctioning headlights."
    category = classify_report(report_example)
    if category:
        print(f"The category of the report is: {category}")
    else:
        print("Failed to classify the report.")

if __name__ == "__main__":
    main()
