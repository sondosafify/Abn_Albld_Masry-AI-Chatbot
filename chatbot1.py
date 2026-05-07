import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
import os
from dotenv import load_dotenv

# سحب المفتاح من خزنة كولاب
load_dotenv()

# استخدامه في مشروعك
api_key = os.getenv("GROQ_API_KEY")
class MasryChatbot:
    def __init__(self):
        # تم تحديث الموديل لـ llama-3.3-70b-versatile عشان يتجنب خطأ الـ decommissioned
        self.llm = ChatGroq(
            model_name="llama-3.3-70b-versatile", 
            temperature=0.6
        )

        self.store = {}

        # 2. هندسة الرد المصري
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", (
                "أنت مساعد ذكي ولطيف اسمك 'صاحبي'. "
                "1. إذا كتب المستخدم أي كلمة إنجليزية للمرة الأولى، يجب أن يكون ردك هو هذا النص فقط: "
                "'ايه يا صاحبي هنخيب ولا ايه ,كلمني عربي عشان نعرف نتفاهم' "
                "2. إذا استمر المستخدم في الكتابة بالإنجليزية للمرة الثانية، يجب أن يكون ردك هو هذا النص فقط: "
                "'لا ده انت تروح تشوف botغيري عشان معوركش' "
                "تتحدث اللهجة العامية المصرية بطلاقة وخفة دم. "
                "ردودك لازم تكون بالمصري، ودودة، ومحترمة. "
                "لو حد سألك عن حاجة متعرفهاش، قوله بصراحة بس بلطافة."
                "ابتعد تماماً عن المصطلحات الخليجية مثل'زين'منيح' 'يا أخي' أو 'إيش'. "
                "استخدم كلمات مصرية مية في المية مثل: 'يا باشا'، 'يا زميلي'، 'إيه الأخبار'، 'من عينيا'. "
                "ردودك لازم تكون خفيفة دم ومصرية أصيلة."
                "أنت اسمك 'صاحبي'. مساعد ذكي بيفهم في كل حاجة بس لسانك مصري صميم. "
                "ممنوع تماماً تستخدم كلمات خليجية زي 'إيش' أو 'يا أخي' أو 'طال عمرك'. "
                "اتكلم زي ما المصريين بيتكلموا في الشارع: 'يا باشا'، 'يا صاحبي'، 'يا زميلي'، 'زي الفل'، 'منور'. "
                "خليك فرفوش وبلاش رسميات زيادة عن اللزوم. "
            )),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ])

        # 3. بناء الهيكل
        self.chain = self.prompt | self.llm

    def get_session_history(self, session_id: str):
        if session_id not in self.store:
            self.store[session_id] = ChatMessageHistory()
        return self.store[session_id]

    def ask(self, user_input: str, session_id: str = "user_1"):
        try:
            if not user_input.strip():
                return "مبعتليش حاجة ليه يا غالي؟"

            # استخدام الكلاس ده بيضمن إن الذاكرة تفضل شغالة طول ما البرنامج مفتوح
            with_message_history = RunnableWithMessageHistory(
                self.chain,
                self.get_session_history,
                input_messages_key="input",
                history_messages_key="history",
            )

            response = with_message_history.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}}
            )
            return response.content
        except Exception as e:
            # لو الـ API Key فيه مشكلة أو الموديل مش متاح هيظهرلك هنا
            if "model_decommissioned" in str(e):
                return "الموديل ده قديم، غيرتلك الموديل لواحد أحدث، جرب تاني!"
            print(f"Error details: {e}")
            return "حصلت لخبطة بسيطة، ممكن تجرب تبعت تاني؟"
