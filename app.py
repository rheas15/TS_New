import streamlit as st
from src.text_summarizer_app.pipeline.prediction import PredictionPipeline 
from src.text_summarizer_app.logging import logger
from src.text_summarizer_app.utils.thompson_sampling import ThompsonSampling
import emoji

# Streamlit app
def main():
    # Initialize Thompson Sampling
    thompson_sampling = ThompsonSampling()

    pipeline = PredictionPipeline()
    
    st.title("SummarEase: " + emoji.emojize(":pen:"))
    st.header("Read Faster, Understand Better")
    text = st.text_area("Enter text to summarize:", height=300)

    # Determine default summary format based on Thompson sampling
    default_summary_format = thompson_sampling.sample_format()

    # Allow user to choose summary format
    summarization_format = st.radio("Select Summary Format:", ["Bullet Points", "Paragraph"], index=0 if default_summary_format == "Bullet Points" else 1)

    if st.button("Summarize"):
        summary = pipeline.summarize_text(text)
        
        if summarization_format == "Bullet Points":
            summary_text = summary.replace(". ", ".\n- ")
            summary_text = "- " + summary_text
        else:
            summary_text = summary

        # Display summary
        st.subheader("Summary:")
        st.write(summary_text)

        # Update Thompson Sampling with user feedback
        thompson_sampling.update_format_feedback(summarization_format)

if __name__ == "__main__":
    main()
