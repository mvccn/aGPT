import openai
from key import *

class aGPT:
    """
    A convenient chat gpt assistant:
    1. keep conversation in record and maintain the context of the chat.
    2. switch between engines including the latest: "gpt-3.5-turbo", "text-davinci-003", ""code-davinci-002"
    3. add customized prompt as you wish. 
    
    Example: 
    g=aGPT()
    g.ask("tell me somthing")
    g.ask("a quick question...", fresh=True) #clear past conversation
    g.ask("how to use F.CrossEntropy?", style="coder")
    
    get your own open ai key and put it in key.py file like this: 
    import openai
    openai.api_key = "you key"
    
    """
    def __init__(self,
                 needs="helpful and concise", #message to set context for gpt 3.5 turbo
                 model= "gpt-3.5-turbo", #"text-davinci-003"
                 conversational=True, # keep this true to keep conversation 
                 ):
        self.conversations = []
        self.system_message = f"You are a {needs} assistant."
        #self.system_message = "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: {knowledge_cutoff} Current date: {current_date}"
        self.conversational = conversational
        self.model = model
        self.default_language = "Python3"

    def ask(self, prompt, fresh=False, style=None):
        if fresh: 
            self.clear()
        prompt = self.create_prompt(prompt, style)
        self.messages =  self._conv_messages() if self.conversational else [] 
        self.messages.append({"role": "user", "content": prompt})
        self.completion=self._complete(prompt)
        response = self.completion['choices'][0]['message']['content']
        self.conversations.append((prompt, response))
        print(response)
        
    def _complete(self, prompt):
        """
        send to chatapt api and fill self.completion
        """

        if self.model == "text-davinci-003": 
            completion = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=2048,
                n=1,
                stop=None,
                temperature=0.5,
            )
        elif self.model== "gpt-3.5-turbo":
            completion = openai.ChatCompletion.create(
                model=self.model,
                messages=self.messages,
            )
        return completion

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
        print(f"messages: \n{self.messages}\n")
        print(f"response: \n{self.completion}\n")
        
       
    def create_prompt(self,prompt, style):
        if style =='explain': 
            prompt=f"#{self.default_language} \n{prompt}\n\n# Explanation of what the code does\n\n#"
        elif style == 'debug': 
            prompt=f"#{self.default_language} \n{prompt}\n\n# please find what wrong with this code\n\n#" 
        elif style== 'coder': 
            prompt=f"#{self.default_language}  \n{prompt}" 
        return prompt
        

