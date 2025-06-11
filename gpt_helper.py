from openai import OpenAI
import os

messages = []
_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
_system_prompt="You are a professional interviewer."

def on_prompt_entered(prompt):
    try:
        newMessage = {"role": "user", "content": prompt}
        
        response = _client.chat.completions.create(
            model="gpt-4.1-nano", 
            messages=[
                {"role": "system", "content": _system_prompt},
                *messages,
                newMessage
            ])
        assitantResponse = {"role": "assistant", "content": response.choices[0].message.content}
        
        messages.append(newMessage)    
        messages.append(assitantResponse)
        
    except Exception as e:
        print("Error: " + str(e))
        return f"Error: {str(e)}" 