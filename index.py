from dotenv import load_dotenv

load_dotenv()
import openai
import os

# Set up the OpenAI API client
openai.api_key = os.getenv('OPENAI_API_KEY')
INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"

# Set up the model and prompt
MODEL_ENGINE = "text-davinci-003"

def get_string_from_file(file_name):
    with open(file_name, "r") as f:
        return f.read()

        


def ask_chat_gpt_question(text):
    print('Asking chat GPT question: ', text)
    completion = openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    return response

def flush_string_to_file(file_name, string):
    with open(file_name, "w") as f:
        f.write(string)

def main():
    prompt = 'please edit the following text as a technology paper: \n'
    prompt += get_string_from_file(INPUT_FILE_NAME)
    response = ask_chat_gpt_question(prompt)
    print('Chat GPT Responded with' , response)
    flush_string_to_file(OUTPUT_FILE_NAME, response)

main()  

