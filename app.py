import streamlit as st
from resume_parser import extract_text_from_pdf
from matcher import calculate_match_score
from utils import clean_text

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening Agent")
st.markdown("### Smart Resume Screening using Python and NLP")

st.sidebar.header("Instructions")
st.sidebar.write("""
1. Upload a candidate's resume (PDF).
2. Enter the job description.
3. Click **Analyze Resume**.
4. View the matching score and recommendation.
""")

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Enter Job Description",
    height=250,
    placeholder="Paste the job description here..."
)

if st.button("Analyze Resume"):

    if uploaded_resume is None:
        st.error("Please upload a resume.")
        st.stop()

    if job_description.strip() == "":
        st.error("Please enter the job description.")
        st.stop()

    with st.spinner("Analyzing Resume..."):

        resume_text = extract_text_from_pdf(uploaded_resume)

        resume_text = clean_text(resume_text)
        job_description = clean_text(job_description)

        score = calculate_match_score(
            resume_text,
            job_description
        )

    st.success("Analysis Completed!")

    st.subheader("Matching Score")

    st.progress(int(score))

    st.metric(
        label="Resume Match",
        value=f"{score:.2f}%"
    )

    if score >= 80:
        st.success("Highly Recommended Candidate")
    elif score >= 60:
        st.warning("Recommended Candidate")
    else:
        st.error("Not Recommended")

    st.subheader("Resume Preview")

    st.text_area(
        "",
        resume_text[:3000],
        height=250
    )
