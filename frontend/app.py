import streamlit as st
from api_client import query_financial_assistant

st.set_page_config(
    page_title="Financial RAG Assistant",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Financial Document Assistant")
st.caption("Ask questions about SEC 10-K Filings (Apple, Microsoft, NVIDIA)")

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثات السابقة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "sources" in msg and msg["sources"]:
            with st.expander("📚 Cited Sources"):
                for src in msg["sources"]:
                    st.markdown(f"- `{src}`")

# استقبال سؤال المستخدم
if user_query := st.chat_input("Ask a financial question..."):
    # عرض سؤال المستخدم وإضافته للسجل
    st.chat_message("user").markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # معالجة الطلب والتواصل مع الباك إند
    with st.chat_message("assistant"):
        with st.spinner("Analyzing SEC filings and generating answer..."):
            result = query_financial_assistant(user_query)

        if "error" in result:
            st.error(result["error"])
        else:
            answer = result["answer"]
            sources = result.get("sources", [])

            st.markdown(answer)
            if sources:
                with st.expander("📚 Cited Sources"):
                    for src in sources:
                        st.markdown(f"- `{src}`")

            # حفظ الرد والمصادر في السجل
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": sources
            })