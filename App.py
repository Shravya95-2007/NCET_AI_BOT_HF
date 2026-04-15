import streamlit as st
from transformers import pipeline
# loard the summerization model
est.cache_resource
def load_summarizer():
  return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
#calling the function
summerizer = load_summerzier()
#streamlit UI
st.title(" AI Text Summerizer")
st.write("Enter a long text below, and get a concise summary")
#text input
long_text=st.text_area("Enter text to summerize:",height=200)
#summary parameters 
max_length=st.slider("Max Summary Length", min_value=50,max_value=300,value=130)
min_length=st.slider("Min Summary Length", min_value=20,max_value=100,value=30)
if st.button("Summarize"):
  if long_text.strip():
    with st.spinner("Generating summary..."):
      summary = summarizer(long_text,max_length=max_length,
                           min_length=min_length,do_sample=False)
      st.subheader("Summary:")
      st.success(summary[0]['summary_text'])
  else:
    st.write("please enter some text to summarizer.")
