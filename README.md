## 🧠 Course Navigator AI

Course Navigator AI is an intelligent Streamlit app that recommends personalized online courses (Coursera, Udemy, YouTube, etc.) based on a learner’s level, subject, and time availability.
It uses LangChain, Hugging Face LLMs, and a custom prompt template to generate useful, beginner-friendly course suggestions.

## 🚀 Features

- 🎓Smart course recommendations using open-source LLMs
- 🧩 Dynamic prompt templates for flexible queries
- 🖥️ Streamlit-based interactive UI
- 🔐 Secure Hugging Face token integration
- 💡Beginner, Intermediate, and Advanced level course filters

## 🧩 How It Works

# Prompt Generator:
- prompt_generator.py defines a reusable prompt using ChatPromptTemplate and saves it as template.json.
# Streamlit Frontend:
- app.py loads that prompt, takes user input (subject, level, duration, type), and invokes the LangChain pipeline.
# Hugging Face Model:
- The model (e.g., mistralai/Mixtral-8x7B-Instruct-v0.1) generates contextual course suggestions.
  
## 🧠 Example Output

# User Input:
- Subject: Machine Learning
- Level: Beginner
- Duration: Short (less than 10 hours)
- Type: Technical

## Model Output

```
1️⃣ Introduction to Machine Learning  
   Platform: Coursera  
   Summary: Covers basic ML concepts and algorithms using Python and scikit-learn.  
   Why: Beginner-friendly, hands-on introduction with practical exercises.

2️⃣ Machine Learning Crash Course  
   Platform: YouTube (Google Developers)  
   Summary: A fast-paced visual and code-based guide to ML basics.  
   Why: Perfect for quick learners with limited time.

3️⃣ AI for Everyone  
   Platform: Coursera (Andrew Ng)  
   Summary: Non-technical overview of AI’s impact and applications.  
   Why: Helps beginners understand AI concepts before diving into coding.
```