import streamlit as st
from src.text_summarizer_app.pipeline.prediction import PredictionPipeline 
from src.text_summarizer_app.logging import logger
from src.text_summarizer_app.utils.thompson_sampling import ts
import numpy as np

# Streamlit app
def main():
    pipeline = PredictionPipeline()

    st.title("Text Summarization App")
    text = st.text_area("Enter your text here:", height = 300)

    # Define initial alpha and beta values for Thompson sampling
    alpha_bullet, beta_bullet = 1, 1
    alpha_paragraph, beta_paragraph = 1, 1

    # Perform Thompson sampling to determine default format
    default_format = ts(alpha_bullet, beta_bullet + beta_paragraph)

    # Determine default format based on Thompson sampling
    if default_format == 0:
        default_summary_format = "Bullet Points"
    else:
        default_summary_format = "Paragraph"

    # Allow user to choose summary format
    summarization_format = st.radio("Select Summary Format:", ["Bullet Points", "Paragraph"], index=0 if default_summary_format == "Bullet Points" else 1)

    if st.button("Summarize"):
        summary = pipeline.summarize_text(text)
        
        if summarization_format == "Bullet Points":
            summary_text = summary.replace(". ", ".\n- ")
            summary_text = "- " + summary_text
            # Update alpha and beta values for bullet points
            alpha_bullet += 1
        else:
            summary_text = summary
            # Update alpha and beta values for paragraphs
            alpha_paragraph += 1

        # Display summary
        st.subheader("Summary:")
        st.write(summary_text)

if __name__ == "__main__":
    main()



