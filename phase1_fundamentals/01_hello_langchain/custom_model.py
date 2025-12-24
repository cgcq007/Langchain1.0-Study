from langchain_core.language_models import BaseChatModel

#自定义调用大模型类
class CustomModel(BaseChatModel):
    model_name="deepseek-v3.2"
    api_key=""
    api_secret=""
    base_url=""
    enable_thinking:bool=True
    temperature:float=1.0
    max_tokens:int=2048


