
from flask import Flask ,render_template,request,redirect,url_for
from google import genai
import webbrowser
from config import KEY
import markdown
from coding import *
from agentic_case import *

app = Flask(__name__)


client = genai.Client(api_key=KEY)

chat = client.chats.create(model='gemini-2.0-flash')
questions=[]
answers=[]
# x = ''
BOOK_PROMPT = f"""
You are an expert in literature, you know everything about the book stored in memory.
Here is the book: {book_text} . 
Your job is to answer questions about the book.
"""
with open("book.txt", encoding="utf-8") as f:
    book = f.read()
chat.send_message(BOOK_PROMPT)

# promt = '''
# You are an expert coder in python, you leverage best practices and write clean code. Use loguru logger instead of print function
# '''
# chat.send_message(promt)



@app.route("/", methods=['GET',"POST"])
def start():
    
    if request.method == 'POST':
        global questions
        global answers
        
        # global x
        question = request.form.get('question')
        message= chat.send_message(question)
        # x = 'temp.csv'
       
        questions.append(question)
        markdown_answers = markdown.markdown(message.text)
        answers.append(markdown_answers)
        # answers.append(x)
        print(answers)
        print(questions)
        l = len(questions)
        return render_template('index.html',questions=questions,answers=answers, l=l)
    
    return render_template('index.html', questions=questions, answers=answers, l=0)
@app.route("/clear", methods=['POST'])
def clear_chat():
    global questions, answers
    questions.clear()
    answers.clear()
    return redirect(url_for('start'))
if __name__ == "__main__":
    app.run(debug=True)



