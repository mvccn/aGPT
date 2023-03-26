# aGPT
### A super convenient way to call chatgpt in notebook and unix shell:
    1. keep conversation in record and maintain the context of the chat.
    2. switch between engines including the latest: "gpt-3.5-turbo", "text-davinci-003", ""code-davinci-002"
    3. keep a template(style) for your chatgpt prompt, for exmaple as a coder in python, simply 
    choose 'coder' style, you can also add customized prompt template as you wish. 
    
    Example: 
    g=aGPT()
    g.ask("tell me somthing")
    Note: 
    you need to get your own openai key and put it in key.py file like this: 
    import openai
    openai.api_key = "you key"
    It is more convenient to use this in a jupyter notebook, it can improve your work flow dramatically. 
    Checkout test_aGPT.ipynb for more comprehensive examples. 
    Install: 
    git clone https://github.com/mvccn/aGPT.git
    cd aGPT
    pip install -e ./
    python aGPT.py
    #you can also do an alias for convenient access
    in your .zshrc(or .bashrc)
    alias agpt='python aGPT.py'
    
## Update: use aGPT in unix shell 
Support shell access and keep the conversation, support rich print out!
![alt text](https://github.com/mvccn/aGPT/blob/main/images/shell.png?raw=true)

## Jupyter Notebook:
![alt text](https://github.com/mvccn/aGPT/blob/main/images/conversation.png?raw=true)

## Styles:
These are really prompt templates created for different needs. You can easily define your own style.

### Coder Style(with your default language)

this will embed your default language tag in your prompt. The default is python 3, but you can change it:
g.default_language="javascript" etc.

![alt text](https://github.com/mvccn/aGPT/blob/main/images/coder.png?raw=true)

### Explain Style

![alt text](https://github.com/mvccn/aGPT/blob/main/images/explain.png?raw=true)

### Debug Style

 ![alt text](https://github.com/mvccn/aGPT/blob/main/images/debug.png?raw=true)

 

