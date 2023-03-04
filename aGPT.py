import openai
import logging



#@register_line_magic
# def G(prompt):
#     logging.basicConfig(level=logging.WARN)
#     completions = openai.Completion.create(
#         engine="text-davinci-003",
#         #engine="gpt-3.5-turbo",
#         prompt=prompt,
#         max_tokens=2048,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     message = completions.choices[0].text
#     print(message)

class aGPT:
    """
    a convenient chat gpt assistant:
    1. keep conversation in record and maintain the context of the chat.
    2. switch between engines including the latest: "gpt-3.5-turbo", "text-davinci-003", ""code-davinci-002"
    3. add customized prompt as you wish. 
    
    g=aGPT()
    g.ask("tell me somthingg")
    g.ask("a quick questin...", fresh=True) #clear past conversation
    """
    def __init__(self,
                 needs="helpful and precise",
                 conversational=True):
        self.conversations = []
        self.system_message = f"You are a {needs} assistant."
        #self.system_message = "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: {knowledge_cutoff} Current date: {current_date}"
        self.conversational = conversational
        self.model = "gpt-3.5-turbo" #"text-davinci-003"
        self.default_language = "Python3"

    def ask(self, prompt, fresh=False, style='coder'):
        if fresh: 
            self.clear()
        prompt = self.create_prompt(style)
        self.messages =  self._conv_messages() if self.conversational else [] 
        self.messages.append({"role": "user", "content": prompt})
        self.completion = self._complete(prompt)
        response = self.completion['choices'][0]['message']['content']
        self.conversations.append((prompt, response))
        print(response)
        
    def _complete(self, prompt):
        """
        send to chatapt api and fill self.completion
        """
        if self.model== "gpt-3.5-turbo":
            self.completion = openai.ChatCompletion.create(
                model=self.model,
                messages=self.messages,
            )
        elif self.model == "text-davinci-003": 
            self.completion = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=2048,
                n=1,
                stop=None,
                temperature=0.5,
            )

    def _conv_messages(self):
        messages = [{ 'role': 'system', 'content': self.system_message}]
        for p, r in self.conversations:
            # add past prompt and response
            messages.append( {"role": "user", "content": p })
            messages.append( {"role": "assistant", "content": r }
            )
        return messages

    def _parse_result(self, response):
        return response['choices'][0]['message']['content']

    def clear(self):
        self.conversations = []
    
    def debug(self):
        print(self.messages)
        print(self.completion)
        
        
    # def code(self, prompt): 
    #    response = openai.Completion.create(
    #         model="code-davinci-002",
    #         prompt=f"# Python 3 \{prompt}# Explanation of what the code does\n\n#",
    #         temperature=0,
    #         max_tokens=64,
    #         top_p=1.0,
    #         frequency_penalty=0.0,
    #         presence_penalty=0.0
    #         )
    #    print(self._parse_result(response))
       
    def create_prompt(self,prompt, style='coder'):
        if style =='code_explain': 
            prompt=f"# Python 3 \n{prompt}\n\n# Explanation of what the code does\n\n#"
        elif style == 'debug': 
            prompt=f"# Python 3 \n{prompt}\n\n# please find what wrong with this code\n\n#" 
        elif style== 'coder': 
            prompt=f"# Python 3 \n{prompt}" 
        return prompt
        

