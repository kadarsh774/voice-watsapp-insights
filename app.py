import streamlit as st
from collections import Counter

st.set_page_config(page_title="Voice AI Insights", page_icon="🎙️")
st.title("🎙️ Voice & WhatsApp Insights")
st.write("Upload WhatsApp chat, get AI insights")

file = st.file_uploader("Upload .txt chat file", type=["txt"])

def get_intent(text):
    t=text.lower()
    intents=[]
    if "price" in t or "cost" in t: intents.append("Price Enquiry")
    if "refund" in t or "return" in t: intents.append("Refund")
    if "buy" in t or "order" in t: intents.append("Buy Intent")
    if "delivery" in t: intents.append("Delivery Issue")
    return intents

if file:
    text=file.read().decode()
    lines=text.split("\n")
    all_intents=[]
    for l in lines[:2000]:
        all_intents.extend(get_intent(l))
    st.metric("Total Messages", len(lines))
    st.write("Top Intents:", Counter(all_intents).most_common(5))
    st.success("Analysis done! This logic extends to Whisper for voice calls.")
else:
    st.info("Export WhatsApp chat (without media) and upload here to test")
