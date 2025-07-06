import streamlit as st
import pandas as pd
import os
import plotly.express as px

# --- Login Check ---
def login():
    st.title("🔐 Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username == "MJW" and password == "withoutayesha":
            st.session_state["authenticated"] = True
            st.success("Login successful! Access granted.")
            st.rerun()  # Refresh the page after successful login
        else:
            st.error("Invalid username or password.")

# --- Admin Dashboard ---
def show_dashboard():
    st.set_page_config(page_title="Admin Dashboard", layout="wide")
    st.title("🛠️ Admin Dashboard - Resume Uploads")

    if os.path.exists("admin_log.csv"):
        df = pd.read_csv("admin_log.csv")

        st.subheader("📋 Uploaded Resume Data")
        st.dataframe(df, use_container_width=True)

        st.download_button(
            "⬇️ Download Resume Data as CSV",
            data=df.to_csv(index=False),
            file_name="admin_log.csv",
            mime="text/csv"
        )

        # --- Visualizations ---
        st.markdown("---")
        st.subheader("📊 Data Insights")

        # Match Score Distribution (Histogram)
        if "Match Score" in df.columns:
            df["Match Score"] = pd.to_numeric(df["Match Score"], errors="coerce")
            df = df[df["Match Score"].notnull()]  # Drop rows with missing/invalid score

            fig1 = px.histogram(df, x="Match Score", nbins=20, title="Distribution of Match Scores")
            st.plotly_chart(fig1, use_container_width=True)

            # Bin scores for pie chart
            score_bins = [0, 10, 20, 40, 60, 80, 100]
            score_labels = ['0-10', '10-20', '20-40', '40-60', '60-80', '80-100']
            df['Match Score Binned'] = pd.cut(df['Match Score'], bins=score_bins, labels=score_labels, right=False)

            score_binned_counts = df['Match Score Binned'].value_counts(dropna=True).reset_index()
            score_binned_counts.columns = ["Score Range", "Count"]

            if not score_binned_counts.empty:
                fig2 = px.pie(score_binned_counts, names="Score Range", values="Count", title="Match Score Distribution (Pie Chart)")
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.info("No scores in defined ranges to plot pie chart.")

        # Suggested Profession Count (Bar Chart)
        if "Suggested Profession" in df.columns:
            profession_counts = df["Suggested Profession"].value_counts().reset_index()
            profession_counts.columns = ["Suggested Profession", "Count"]
            fig3 = px.bar(profession_counts, x="Suggested Profession", y="Count", title="Count of Resumes per Suggested Profession")
            st.plotly_chart(fig3, use_container_width=True)

    else:
        st.info("No resumes have been analyzed yet.")

# --- Main ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    show_dashboard()
