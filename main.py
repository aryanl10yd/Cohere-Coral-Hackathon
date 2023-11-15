import cohere
import requests
import json
from cohere.responses.classify import Example

co = cohere.Client('ach323kiA02McS2BAk0JrP5OgOygulKz4hyNlq6h')  # This is your trial API key
response = co.chat(
    model='command-light-nightly',
    message='what is an LLM?',
    temperature=0.3,
    chat_history=[],
    prompt_truncation='auto',
    stream=False,
    citation_quality='accurate',
    connectors=[{"id": "web-search"}],
    documents=[]
)
#
# new_response = co.generate(
#     model="command-light",
#     prompt="please explain to me how LLMs work",
# )

examples = [
    Example("How do I find my insurance policy?", "Finding policy details"),
    Example("How do I download a copy of my insurance policy?", "Finding policy details"),
    Example("How do I find my policy effective date?", "Finding policy details"),
    Example("When does my insurance policy end?", "Finding policy details"),
    Example("Could you please tell me the date my policy becomes effective?", "Finding policy details"),
    Example("How do I sign up for electronic filing?", "Change account settings"),
    Example("How do I change my policy?", "Change account settings"),
    Example("How do I sign up for direct deposit?", "Change account settings"),
    Example("I want direct deposit. Can you help with that?", "Change account settings"),
    Example("Could you deposit money into my account rather than mailing me a physical cheque?",
            "Change account settings"),
    Example("How do I file an insurance claim?", "Filing a claim and viewing status"),
    Example("How do I file a reimbursement claim?", "Filing a claim and viewing status"),
    Example("How do I check my claim status?", "Filing a claim and viewing status"),
    Example("When will my claim be reimbursed?", "Filing a claim and viewing status"),
    Example("I filed my claim 2 weeks ago but I still haven’t received a deposit for it.",
            "Filing a claim and viewing status"),
    Example("I want to cancel my policy immediately! This is nonsense.", "Cancelling coverage"),
    Example("Could you please help my end my insurance coverage? Thank you.",
            "Cancelling coverage"),
    Example("Your service sucks. I’m switching providers. Cancel my coverage.", "Cancelling coverage"),
    Example("Hello there! How do I cancel my coverage?", "Cancelling coverage"),
    Example("How do I delete my account?", "Cancelling coverage"),
    Example("How do I use an LLM?", "LLM"),
    Example("Can I use a connector with an LLM?", "LLM"),
    Example("What connectors are there that I can use in my code?", "LLM"),

]

a = True
inputs = []
b = 0

# while a == True:
#     new_input = input("what is your prompt?\n")
#     inputs.append(new_input)
#     ask = input("are those all your prompts? y/n?\n").lower()
#     if ask == 'y':
#         a = False
# response1 = co.classify(
#     model='large',
#     inputs=inputs,
#     examples=examples,
# )

# print(response.classifications)

# print(f"{new_response}\n{response1.classifications}")

# response_1 = response1.classifications[0]

# print(f"Confidences\n{response_1.confidences}")
# print(f"Classification_Type\n{response_1.classification_type}")
# print(response_1.input)
# print(response_1.id)
# print(response_1.predictions)
# print(response_1.labels)

hi = open('export.json',)
hi = json.load(hi)
hi = hi.get("page_data")
new_text = ""

for page_data in hi:
    page_number = page_data["page"]
    words_list = page_data["words"]
    for word in words_list:
        text = word["text"]
        new_text += text + " "
        print(f"Page {page_number}, Text: {text}")

print(new_text)

