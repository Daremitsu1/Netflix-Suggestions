import streamlit as st
import pandas as pd
import pandas_profiling
import rpy2.robjects as robjects

# Load the exported R predictive model
model_file = "netflix_recommender.rds"
model = robjects.r['readRDS'](model_file)

def main():
    st.title("Netflix Recommender")

    # Allow user to upload a CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        # Use pandas to read the CSV file
        df = pd.read_csv(uploaded_file)

        # Use pandas-profiling to generate a report on the data
        st.write(pandas_profiling.ProfileReport(df))

        # Use the R predictive model to make recommendations
        recommendations = model.predict(df)

        # Display the recommendations
        st.write(recommendations)

        # Add an export button to download the recommendations as a CSV file
        if st.button("Export recommendations"):
            df['recommendations'] = recommendations
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/csv;base64,{b64}" download="recommendations.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
