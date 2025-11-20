import os
try: import openai
except ImportError: openai=None


class OpenAIAgent:
def __init__(self,api_key=None):
self.api_key=api_key or os.getenv('OPENAI_API_KEY')
if openai and self.api_key: openai.api_key=self.api_key
def summarize_text(self,text):
if not openai or not self.api_key: return text[:100]+'...'
resp=openai.ChatCompletion.create(model='gpt-5-mini',messages=[{'role':'user','content':f'Summarize this text: {text}'}])
return resp.choices[0].message.content.strip()
