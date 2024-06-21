import wolframalpha
import pyautogui

# App id obtained by the above steps
app_id = 'TXGLLY-YQAK65E2UY'
  
# Instance of wolf ram alpha 
# client class
client = wolframalpha.Client(app_id)

while True:

    try:

        # Taking input from user
        question = input('Question: ')

        # Stores the response from 
        # wolf ram alpha
        res = client.query(question)

        # Includes only text from the response
        answer = next(res.results).text
    
        print(answer)
        print("\n")
    
    except StopIteration:

        print("Cannot be answered.")

        

