from langchain_core.prompts import PromptTemplate
template=PromptTemplate(
    template="""
You are an expert educational recommendation assistant that helps learners discover the most suitable online courses.

Given the following inputs:
- Subject: {subject}
- Learner Level: {level}
- Preferred Duration: {duration}
- Course Type: {course_type}

Your task is to suggest **3 high-quality online courses** that match these preferences.

For each recommended course, provide:
1. **Title** — a clear, engaging course title.
2. **Platform** — mention whether it’s on Coursera, YouTube, edX, Udemy, etc.
3. **Short Summary** — describe what the course covers in 2–3 concise lines, focusing on practical value.
4. **Why it suits this level** — explain briefly why it’s appropriate for the learner’s level and type.

Output should be:
- Well-structured and easy to read.
- Formatted in Markdown.
- Avoid generic or repeated titles.
- If unsure, make logical and realistic recommendations based on known online learning patterns.
""",
input_variables=["subject", "level", "duration", "course_type"],
validate_template=True
)
template.save("template.json")