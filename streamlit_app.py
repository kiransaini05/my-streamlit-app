import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Student Performance Predictor 🎓",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Sidebar Navigation
# ----------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📊 Predictor", "📈 Insights"])

# ----------------------------
# HOME PAGE
# ----------------------------
if page == "🏠 Home":
    st.title("🎓 AI-powered tool to forecast student performance")
    st.markdown(
        """
        Welcome to the Student Performance Predictor 🚀  
        This tool helps to:
        - 🔮 Predict grades based on study patterns  
        - 📈 Visualize learning insights  
        - 🎯 Help teachers & students take better decisions  
        """
    )

# ----------------------------
# PREDICTOR PAGE
# ----------------------------
elif page == "📊 Predictor":
    st.header("📊 Student Performance Predictor")

    # Input sliders
    study_hours = st.slider("📖 Daily Study Hours", 0, 12, 4)
    assignments = st.slider("📝 Assignments Completed (%)", 0, 100, 80)
    attendance = st.slider("🏫 Attendance (%)", 0, 100, 75)
    prev_score = st.number_input("📊 Previous Exam Score (out of 100)", 0, 100, 69)

    if st.button("🚀 Predict Performance"):
        # Simple formula (you can replace with ML model later)
        performance_score = (0.4 * study_hours * 8 +
                             0.2 * assignments +
                             0.2 * attendance +
                             0.2 * prev_score)

        performance_score = min(100, round(performance_score, 2))

        st.success(f"🎯 Predicted Performance Score: {performance_score} / 100")

        if performance_score > 85:
            st.balloons()
            st.info("🌟 Excellent! Keep up the hard work.")
        elif performance_score > 60:
            st.warning("📘 Good! But there’s still room to improve.")
        else:
            st.error("⚠ Needs Improvement. Focus more on study and attendance.")

# ----------------------------
# INSIGHTS PAGE
# ----------------------------
elif page == "📈 Insights":
    st.header("📈 Learning Insights")

    # Fake dataset for visualization
    factors = ["Study Hours", "Assignments", "Attendance", "Previous Score"]
    values = [6, 70, 85, 65]  # example values

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(factors, values, color=["#4CAF50", "#2196F3", "#FF9800", "#9C27B0"])
    ax.set_ylim(0, 100)
    ax.set_ylabel("Score / %")
    ax.set_title("Impact of Different Factors on Performance")

    # Add values on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 2, str(height),
                ha='center', va='bottom')

    st.pyplot(fig)
