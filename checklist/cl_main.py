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


def inject_checklist_ui() -> None:
    st.markdown(
        """
        <style>
        div[data-testid="stAlert"] {
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.96), rgba(243, 244, 246, 0.98)) !important;
            border: 1px solid rgba(156, 163, 175, 0.26) !important;
            border-radius: 18px !important;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06) !important;
        }

        div[data-testid="stAlert"] * {
            color: #334155 !important;
        }

        div[data-testid="stAlert"] svg {
            fill: #64748b !important;
        }

        .stDownloadButton > button {
            background: linear-gradient(145deg, #f8fafc, #dbe4ee) !important;
            color: #0f172a !important;
            box-shadow: 0 10px 24px rgba(148, 163, 184, 0.2) !important;
            border: 1px solid rgba(148, 163, 184, 0.32) !important;
            border-radius: 14px !important;
        }

        .stDownloadButton > button:hover,
        .stDownloadButton > button:focus,
        .stDownloadButton > button:active {
            background: linear-gradient(145deg, #eef2f7, #cbd5e1) !important;
            color: #0f172a !important;
            box-shadow: 0 14px 28px rgba(100, 116, 139, 0.22) !important;
            border: 1px solid rgba(100, 116, 139, 0.34) !important;
            transform: translateY(-2px) !important;
        }

        .stDownloadButton > button *,
        .stDownloadButton > button:hover *,
        .stDownloadButton > button:focus *,
        .stDownloadButton > button:active * {
            color: #111827 !important;
            fill: #111827 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


inject_checklist_ui()

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
