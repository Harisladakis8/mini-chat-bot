from google import genai
from config import KEY

client = genai.Client(api_key=KEY)

reception = client.chats.create(model="gemini-2.0-flash")

SYSTEM_PROMPT = """
You are AI assistant, who receive messages from user and you must determine the context
of discussion.
You must respond with word "GENERIC" if user wants general information.
You must respond with word "CODE" if user wants some code.
You must respond with word "BOOK" if user wants information about the book stored in memory
"""

reception.send_message(SYSTEM_PROMPT)


generic = client.chats.create(model="gemini-2.0-flash")

coder = client.chats.create(model="gemini-2.0-flash")

CODE_PROMPT = """
You are an expert coder in python, you leverage best practices and write clean code. Use loguru logger instead of print function." \
"""

coder.send_message(CODE_PROMPT)

book = client.chats.create(model="gemini-2.0-flash")

with open("book.txt", encoding="utf-8") as f:
    book_text = f.read()

BOOK_PROMPT = f"""
You are an expert in literature, you know everything about the book stored in memory.
Here is the book: {book_text} . 
Your job is to answer questions about the book.
"""

book.send_message(BOOK_PROMPT)



user_prompt = "What is the capital of France?"

response = reception.send_message(user_prompt)

print(response.text)

if str(response.text).strip() == "GENERIC":
    print("GENERIC")
    new_response = generic.send_message(user_prompt)
elif str(response.text).strip() == "CODE":
    print("CODE")
    new_response = coder.send_message(user_prompt)
elif str(response.text).strip() == "BOOK":
    print("BOOK")
    new_response = book.send_message(user_prompt)

print(new_response.text)