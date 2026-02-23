import streamlit as st
import json
import os
import pandas as pd

# --- PREDEFINED DATA ---
TUTORS = [
    "Muzayyan Shah", "Hassan Riaz", "Misbah ullah", "Hammad tahir", 
    "ijlal ghani", "Muhammad Haroon", "Abdullah Shah", "Saboor Khattak", "Khadija shah"
]

SUBJECTS = [
    "Software engineering", "Database systems", "physiology", "Computer networks", 
    "Pharmacology", "microbiology", "Programming fundamentals", "criminal law", "Biochemistry"
]

# Mapping Tutors to their specific Expertise
TUTOR_EXPERT_MAP = dict(zip(TUTORS, SUBJECTS))

# --- APP SETUP ---
st.set_page_config(page_title="Vercetii Admin Portal", layout="wide")

# Custom CSS for a professional "Dark Mode" look
st.markdown("""
    <style>
    .main { background-color: #080810; color: #e4e4f0; }
    .stButton>button { background: linear-gradient(135deg,#5b8dee 0%,#a78bfa 100%); color: white; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 Vercetii Student-Tutor Assignment")

# --- DATA STORAGE ---
if 'assignments' not in st.session_state:
    st.session_state.assignments = []

# --- INTERFACE ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("➕ New Assignment")
    student_name = st.text_input("Enter Student Name", placeholder="e.g. Ahmed Khan")
    
    # Select Tutor
    selected_tutor = st.selectbox("Select Tutor", TUTORS)
    
    # Auto-suggest the subject based on the tutor's expertise
    suggested_subject = TUTOR_EXPERT_MAP[selected_tutor]
    st.info(f"Expertise: {suggested_subject}")
    
    if st.button("Assign Student"):
        if student_name:
            new_entry = {
                "Student": student_name,
                "Tutor": selected_tutor,
                "Subject": suggested_subject
            }
            st.session_state.assignments.append(new_entry)
            st.success(f"Assigned {student_name} to {selected_tutor}")
        else:
            st.warning("Please enter a student name.")

with col2:
    st.subheader("📋 Current Assignments")
    if st.session_state.assignments:
        df = pd.DataFrame(st.session_state.assignments)
        st.dataframe(df, use_container_width=True)
        
        # Simple Analytics
        st.divider()
        st.write("📊 **Quick Stats**")
        st.bar_chart(df['Tutor'].value_counts())
    else:
        st.write("No active assignments yet.")