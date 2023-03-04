# aGPT
    A convenient chat gpt assistant:
    1. keep conversation in record and maintain the context of the chat.
    2. switch between engines including the latest: "gpt-3.5-turbo", "text-davinci-003", ""code-davinci-002"
    3. add customized prompt template as you wish. 
    
    Example: 
    g=aGPT()
    g.ask("tell me somthing")
    g.ask("a quick question...", fresh=True) #clear past conversation
    g.ask("how to use F.CrossEntropy?", style="coder")
    
    It is more convenient to use this in a jupyter notebook, it can improve your work flow dramatically. 
    Checkout test_aGPT.ipynb for more comprehensive examples. 
    
    Note: 
    you need to get your own openai key and put it in key.py file like this: 
    import openai
    openai.api_key = "you key"
