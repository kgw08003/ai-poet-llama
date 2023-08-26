import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.llms import CTransformers

# chat_model = ChatOpenAI()
llm = CTransformers(
    model="llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
)

st.title('인공지능 시인')

content = st.text_input('시의 주제를 제시해주세요.')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = llm.predict("write a poem about " + content + ": ")
        st.write(result)

# streamlit run main.py 명령어 실행
# llama를 이용해서 rocal 에서만 사용가능
