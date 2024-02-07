import streamlit as st
from sim_score import sim_score, text_preprocessing
import sys
import os

# Append the directory containing sim_score.py to sys.path
module_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(module_directory)

def main():
    st.title("Text Similarity Comparison")

    # Text input widgets
    s1 = st.text_area("Enter text 1:")
    s2 = st.text_area("Enter text 2:")

    # Radio button for selecting text processing option
    text_processing_option = st.radio("Select text processing option:", ("Clean Text", "Use Text As It Is"))

    if st.button("Submit"):
        if s1.strip() == "" or s2.strip() == "":
            st.warning("Please enter both texts before submitting.")
        else:
            # Perform text preprocessing based on user selection
            if text_processing_option == "Clean Text":
                s1_clean = text_preprocessing(s1)
                s2_clean = text_preprocessing(s2)
                st.write(f"Text1 After Cleaning : {s1_clean}")
                st.write(f"Text2 After Cleaning : {s2_clean}")
            else:  # Use text as it is
                s1_clean = s1
                s2_clean = s2
            
            # Calculate similarity score
            similarity_score = sim_score(s1_clean, s2_clean)

            # Display result
            st.write(f"Similarity Score: {similarity_score}")

if __name__ == "__main__":
    main()
