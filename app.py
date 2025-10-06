from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt
load_dotenv()

endpoint=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    temperature=0.7,

)
# Wrapper
model=ChatHuggingFace(llm=endpoint)

# streamlit
st.title("Course Navigator AI (Open-Source-Version)")
st.write("Find your perfect learning path - powered by Hugging Face Models")
# Dropdowns
subject=st.selectbox("Select Subject",["AI", "Machine Learning", "Deep Learning", "Data Science", "Computer Vision", "Maths"])
level=st.selectbox("Select Level", ["Begineer", "Intermediate", "Advanced"])
duration=st.selectbox("Select Duration", ["Short (<10 hrs)", "Medium (10-30 hrs)", "Long (>30 hrs)"])
course_type=st.selectbox("Select Type", ["Code-oriented", "Theory-oriented", "Mixed"])

# Load prompts
template=load_prompt("template.json")

# Fill the placeholder
# prompt=template.invoke({
#     "subject":subject,
#     "level":level,
#     "duration":duration,
#     "course_type":type_
# })

# Button 
if st.button("Find Courses"):
    chain=template | model
    result=chain.invoke({
    "subject":subject,
    "level":level,
    "duration":duration,
    "course_type":course_type
})
    st.write(result)