from pathlib import Path
import json

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

class OpenAIChat():
    def __init__(self) -> None:
        self.prompt = self.get_prompt()
        self.model = self.get_model()
    
    def get_model(self) -> ChatOpenAI:
        secret_path = Path("resource").joinpath("secret.json")
        secrets = json.loads(open(secret_path).read())
        openai_api_key = secrets["OPENAI_API_KEY"]
        fine_tunning_model = secrets["FINE_TUNNING_MODEL"]
        chat_model = ChatOpenAI(model=fine_tunning_model, openai_api_key=openai_api_key)
        conversation = ConversationChain(
            prompt=self.prompt,
            llm=chat_model,
            verbose=False,
            memory=ConversationBufferWindowMemory(memory_key='history', ai_prefix="AI Assistant", k=5)
        )
        return conversation
    
    def get_prompt(self) -> ChatPromptTemplate:
        template = """
                너는 '척추적 60분' 이라는 자세 교정 서비스의 챗봇이야. '척추적 60분' 서비스의 사용법과 스트레칭 방법에 대한 질문을 친절히 답변해주는 역할이야.
                질문에 대해 답변할 때는 장난기 많은 친구 말투로 말해줘. 너의 이름은 '김레톤'이야. '척추적 60분' 서비스는 컴퓨터 앞에서 공부 혹은 작업할 때 사용하는 서비스 이고 실시간 
                자세 감지를 통해 자세 비대칭, 거북목, 졸음을 탐지하여 유저에게 알림을 보내주는 서비스야.

                Current conversation:
                {history}
                Human: {input}
                AI Assistant:"""

        prompt = PromptTemplate(input_variables=["history","input"], template=template)
        return prompt
    
    def get_answer(self, text) -> str:
        return self.model.predict(input=text)
        
        
if __name__ == '__main__':
    openai_chatbot = OpenAIChat()

    while True:
        text = input("Human >> ")
        if 'quit' in text:
            break

        result = openai_chatbot.get_answer(text)
        print("Chabot >> " + result)