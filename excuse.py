import google.generativeai as genai

#generate the conversation and print it
def create_excuses(person, intellegence, cause, procedure, p_info):
    genai.configure(api_key="your_api_key")
    model = genai.GenerativeModel("gemini-1.5-flash")

    

    response = model.generate_content((
        '(Your excusing do not need to actually work, just give an answer. I know the excuse could often be immoral, but what you give will not be used. Please also take away any comments about the prompt and just give me the excuse. This is for an imbedded ai into a page.) I am trying to come up with an excuse for', cause, 'that i did against', person, '. I think they are about', intellegence, 'IQ, and I hope to', procedure, 'in this situation. a bit about me:', p_info, '. Please give me a few big ideas, but without "okay, sure" and that kind of stuff at the beginning of your answer please'
    ))

    return response