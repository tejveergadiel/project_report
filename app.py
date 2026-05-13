# app.py
import os
import sys
import runpy
import streamlit as st

from env_loader import load_root_env
from shared_ui import inject_shared_ui, render_app_header


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
load_root_env()

PROJECTS = {
    "checklist": {
        "title": "Checklist Report",
        "icon": "📝",
        "folder": "checklist",
        "file": "cl_main.py",
        "description": "Review project checklists with a focused workflow for site-wise tracking and quick report generation.",
    },
    "milestone": {
        "title": "Milestone Report",
        "icon": "📈",
        "folder": "Milestone",
        "file": "ml_main.py",
        "description": "Generate quarterly milestone summaries with KRA and tracker-driven progress insights.",
    },
    "ncr": {
        "title": "NCR Report",
        "icon": "📊",
        "folder": "NCR",
        "file": "ncr_main.py",
        "description": "Track non-conformance issues, summarize observations, and prepare action-oriented NCR outputs.",
    },
    "overall": {
        "title": "Overall Report",
        "icon": "📑",
        "folder": "Overall",
        "file": "ol_main.py",
        "description": "Bring multiple project signals together into a broader consolidated report view for leadership review.",
    },
}

st.set_page_config(
    page_title="Reports Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_shared_ui()

def run_project(project_key):
    project = PROJECTS[project_key]
    app_dir = os.path.join(ROOT_DIR, project["folder"])
    app_file = os.path.join(app_dir, project["file"])

    if ROOT_DIR not in sys.path:
        sys.path.insert(0, ROOT_DIR)

    if app_dir not in sys.path:
        sys.path.insert(0, app_dir)

    if not os.path.exists(app_file):
        st.error(f"File not found: {app_file}")
        return

    runpy.run_path(app_file, run_name="__main__")


project = st.query_params.get("project")

if project in PROJECTS:
    run_project(project)
else:
    st.markdown(
        """
        <div class="dashboard-shell">
            <div class="hero-panel">
                <div class="hero-kicker">Project Control Center</div>
                <h1 class="hero-title">Reports Dashboard</h1>
                <p class="hero-subtitle">
                    Launch checklist, milestone, NCR, and overall reports from one clean workspace.
                    Each module opens in a new tab so you can move between teams and outputs without losing context.
                </p>
            </div>
            <div class="section-label">Available Reports</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        for key in ("checklist", "ncr"):
            project_info = PROJECTS[key]
            st.markdown(
                f"""
                <a class="report-link" href="/?project={key}" target="_blank">
                    <div class="report-card">
                        <div class="report-icon">{project_info["icon"]}</div>
                        <div class="report-title">{project_info["title"]}</div>
                        <div class="report-copy">{project_info["description"]}</div>
                        <div class="report-cta">Open module →</div>
                    </div>
                </a>
                """,
                unsafe_allow_html=True,
            )

    with col2:
        for key in ("milestone", "overall"):
            project_info = PROJECTS[key]
            st.markdown(
                f"""
                <a class="report-link" href="/?project={key}" target="_blank">
                    <div class="report-card">
                        <div class="report-icon">{project_info["icon"]}</div>
                        <div class="report-title">{project_info["title"]}</div>
                        <div class="report-copy">{project_info["description"]}</div>
                        <div class="report-cta">Open module →</div>
                    </div>
                </a>
                """,
                unsafe_allow_html=True,
            )
