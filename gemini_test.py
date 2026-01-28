from google import genai
from config import gemini_api_key
client=genai.Client(api_key=gemini_api_key)
def generate(prompt):
    res=client.models.generate_content(
        model='gemma-3-4b',
        contents=prompt
    )
    return res.text
def prompt(v_prompt,c_prompt,cc_prompt):
    print(generate(v_prompt))
    print(generate(c_prompt))
    print(generate(cc_prompt))
def main():
    v_prompt=input("")
    c_prompt=input("")
    cc_prompt=input("")
    print(prompt(v_prompt,c_prompt,cc_prompt))
if __name__=='__main__':
    main()