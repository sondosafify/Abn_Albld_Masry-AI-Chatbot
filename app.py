#streamlit run app.py
#pip install ipynb
import streamlit as st
from chatbot1 import MasryChatbot
import streamlit as st

# إضافة صورة في نص الصفحة
# تقسيم الصفحة لـ 3 أعمدة عشان نوسطن الصورة
col1, col2, col3 = st.columns([1, 2, 1]) 

with col2:
    # استخدمنا حرف r قبل المسار عشان نهرب من مشاكل الويندوز والصورة تطلع في النص
    st.image("D:/bot/images.jpg", width=300)

st.set_page_config(page_title="صاحبي AI", page_icon="🤖")
st.title("🤖 شات بوت 'صاحبي'")

if "bot" not in st.session_state:
    st.session_state.bot = MasryChatbot()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# عرض المحادثة
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

user_query = st.chat_input("قول يا صاحبي عايز تسأل عن إيه؟")

if user_query:
    st.session_state.chat_history.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        # بنادي على ask اللي في ملف الـ logic
        response = st.session_state.bot.ask(user_query)
        st.markdown(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
