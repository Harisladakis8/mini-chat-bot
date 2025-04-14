
import google.generativeai as genai2
from config import KEY

genai2.configure(api_key=KEY)
model = genai2.GenerativeModel("gemini-1.5-flash", 
                              system_instruction="You are an experienced python software engineer. You write python code using best practices")
def Runner():
    message = """
    You must open the file temp.csv which looks like this:
    Description,Qty,Unit Price (EUR),VAT (%),Net (EUR),Gross (EUR)
    "Tiramisu Ice Cream 10L",3.46,€452.75,24%,€1566.51,€1942.48
    "Pineapple Coconut 5L",9.09,€25.72,24%,€233.79,€289.91

    You will create a bar chart that shows the total gross amount for each product using matplotlib.

    """


    response = model.generate_content(
        message,
        generation_config= genai2.GenerationConfig(
        temperature=0.5,
            )
        )
    return response
response = Runner()
print(response.text)