# checklist/cl_main.py
import os
import sys
import runpy
import streamlit as st

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)

if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from env_loader import load_root_env
from shared_ui import inject_shared_ui, render_app_header

load_root_env()

try:
    st.set_page_config(
        page_title="Checklist Report",
        page_icon="📝",
        layout="wide",
        initial_sidebar_state="expanded",
    )
except Exception:
    pass

inject_shared_ui()

CHECKLIST_PAGES = {
    "EDEN": "eden.py",
    "EWS Checklist": "checklistews.py",
    "Wave City Checklist": "Wave City.py",
    "Eligo Checklist": "CheckEligo.py",
    "Veridia": "veridia.py",
}

st.sidebar.markdown(
    "<h2>Checklist Modules</h2>",
    unsafe_allow_html=True,
)

selected_page = st.sidebar.radio(
    "Select Checklist Project",
    list(CHECKLIST_PAGES.keys()),
    key="checklist_project_selector"
)

render_app_header(
    "Checklist Report",
    "Move between checklist modules from one consistent workspace and keep the project review flow simple.",
    "Checklist Control",
)

st.markdown(
    f"""
    <div class="section-card">
        <h3>Active Module</h3>
        <p><strong>{selected_page}</strong> is loaded below. Use the left sidebar to switch between checklist report flows.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

file_name = CHECKLIST_PAGES[selected_page]
file_path = os.path.join(CURRENT_DIR, file_name)

if not os.path.exists(file_path):
    st.error(f"File not found: {file_path}")
else:
    runpy.run_path(file_path, run_name="__main__")
