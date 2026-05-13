import streamlit as st


def inject_shared_ui() -> None:
    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&display=swap');

:root {
    --bg-start: #f8fbff;
    --bg-end: #e8f2ff;
    --panel: rgba(255, 255, 255, 0.82);
    --panel-border: rgba(44, 126, 199, 0.12);
    --text-main: #0f2d4a;
    --text-soft: #5c7c99;
    --accent: #2563eb;
    --accent-hover: #1d4ed8;
    --accent-glow: rgba(37, 99, 235, 0.2);
    --success: #059669;
    --warning: #d97706;
    --danger: #dc2626;
    --shadow: 0 20px 40px rgba(15, 45, 74, 0.08);
}

html, body, [class*="css"] {
    font-family: 'Manrope', sans-serif;
    color: var(--text-main);
}

body {
    background: linear-gradient(135deg, var(--bg-start) 0%, var(--bg-end) 100%);
    background-attachment: fixed;
}

.stApp {
    background: transparent;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

#MainMenu, footer, div[data-testid="stToolbar"], .stDeployButton, div[data-testid="stDecoration"] {
    visibility: hidden;
    display: none;
}

div[data-testid="stAppViewContainer"] > .main {
    padding-top: 2rem;
}

section[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.45) !important;
    backdrop-filter: blur(20px);
    border-right: 1px solid var(--panel-border) !important;
}

/* Ensure all text in sidebar is visible */
section[data-testid="stSidebar"] * {
    color: #0f2d4a !important; 
    opacity: 1 !important;
}

section[data-testid="stSidebar"] [data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] p {
    color: #0f2d4a !important;
    font-weight: 600 !important;
    opacity: 1 !important;
}

section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: var(--accent-glow) !important;
    border-radius: 8px;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: var(--text-main) !important;
    font-weight: 800 !important;
}

/* Fix for the download button and general buttons */
.stButton > button,
.stDownloadButton > button {
    background: var(--accent) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.6rem 1.5rem !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 12px var(--accent-glow) !important;
    width: auto !important;
    min-width: 160px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background: var(--accent-hover) !important;
    color: #ffffff !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px var(--accent-glow) !important;
    border: none !important;
}

.stButton > button:focus,
.stDownloadButton > button:focus,
.stButton > button:active,
.stDownloadButton > button:active {
    background: var(--accent-hover) !important;
    color: #ffffff !important;
    box-shadow: 0 0 0 3px var(--accent-glow) !important;
    outline: none !important;
    border: none !important;
}

/* Ensure text and icons inside buttons are white */
.stButton > button *,
.stDownloadButton > button * {
    color: #ffffff !important;
    fill: #ffffff !important;
}

.app-shell, .main-container, .dashboard-shell {
    max-width: 1200px;
    margin: 0 auto 2.5rem;
    background: var(--panel);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid var(--panel-border);
    border-radius: 32px;
    padding: 2.5rem;
    box-shadow: var(--shadow);
}

.section-label {
    font-size: 0.85rem;
    font-weight: 800;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent);
    margin: 2rem 0 1.25rem;
    padding-left: 0.5rem;
    border-left: 4px solid var(--accent);
}

.report-link {
    text-decoration: none !important;
    display: block;
    color: inherit !important;
}

.report-card {
    position: relative;
    overflow: hidden;
    min-height: 200px;
    padding: 2rem;
    border-radius: 24px;
    border: 1px solid var(--panel-border);
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.9), rgba(240, 247, 255, 0.7));
    box-shadow: 0 10px 30px rgba(15, 45, 74, 0.05);
    transition: all 0.3s ease;
    margin-bottom: 1.5rem;
}

.report-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(15, 45, 74, 0.12);
    border-color: var(--accent);
}

.report-card::after {
    content: "";
    position: absolute;
    right: -30px;
    bottom: -30px;
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background: radial-gradient(circle, var(--accent-glow), transparent 70%);
    opacity: 0.5;
}

.report-icon {
    font-size: 2.5rem;
    margin-bottom: 1.2rem;
    display: block;
}

.report-title {
    font-size: 1.4rem;
    font-weight: 800;
    color: var(--text-main);
    margin-bottom: 0.6rem;
}

.report-copy {
    color: var(--text-soft);
    line-height: 1.6;
    font-size: 1rem;
    margin-bottom: 1.5rem;
}

.report-cta {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    border-radius: 999px;
    background: var(--accent-glow);
    color: var(--accent);
    font-size: 0.9rem;
    font-weight: 700;
    transition: all 0.2s ease;
}

.report-card:hover .report-cta {
    background: var(--accent);
    color: white;
}

.hero-panel {
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.95), rgba(240, 249, 255, 0.85));
    border: 1px solid var(--panel-border);
    border-radius: 28px;
    padding: 2.5rem;
    margin-bottom: 2rem;
    box-shadow: 0 15px 35px rgba(15, 45, 74, 0.06);
}

.hero-kicker {
    display: inline-block;
    padding: 0.5rem 1rem;
    border-radius: 999px;
    background: var(--accent-glow);
    color: var(--accent);
    font-size: 0.85rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
}

.hero-title, .main-title {
    margin: 0;
    color: var(--text-main) !important;
    font-size: clamp(2.2rem, 4.5vw, 3.5rem);
    line-height: 1.1;
    font-weight: 800;
}

.hero-subtitle, .subtitle {
    margin: 1.2rem 0 0;
    max-width: 800px;
    color: var(--text-soft) !important;
    font-size: 1.1rem;
    line-height: 1.6;
    font-weight: 500;
}

.section-card, .project-selection {
    background: rgba(255, 255, 255, 0.6);
    border: 1px solid var(--panel-border);
    border-radius: 24px;
    padding: 1.8rem;
    margin: 1.5rem 0;
    box-shadow: 0 10px 25px rgba(15, 45, 74, 0.04);
    transition: all 0.3s ease;
}

.section-card:hover {
    background: rgba(255, 255, 255, 0.8);
    border-color: var(--accent);
}

.section-card h3, .project-selection h3 {
    margin: 0 0 0.8rem;
    color: var(--text-main) !important;
    font-size: 1.35rem;
    font-weight: 800;
}

.section-card p {
    margin: 0;
    color: var(--text-soft);
    line-height: 1.65;
}

.status-container, .success-container, .error-container, .system-info {
    border-radius: 20px;
    padding: 1.5rem;
    margin: 1.2rem 0;
    border: 1px solid transparent;
}

.status-container {
    background: #fffbeb;
    border-color: #fef3c7;
    color: #92400e;
}

.success-container, .system-info {
    background: #ecfdf5;
    border-color: #d1fae5;
    color: #065f46;
}

.error-container {
    background: #fef2f2;
    border-color: #fee2e2;
    color: #991b1b;
}

.status-container h4, .success-container h4, .error-container h4 {
    margin: 0 0 0.45rem;
    font-size: 1.15rem;
    font-weight: 800;
}

.status-container h4 { color: #9c6804; }
.success-container h4, .system-info { color: #136b49; }
.error-container h4 { color: #ac2f42; }

.status-container p, .success-container p, .error-container p {
    margin: 0;
    color: var(--text-main);
}

.chat-message {
    padding: 1.25rem;
    border-radius: 18px;
    margin-bottom: 1rem;
    display: flex;
    align-items: flex-start;
    box-shadow: 0 10px 24px rgba(23, 72, 116, 0.08);
}

.chat-message.bot {
    background: linear-gradient(145deg, #f5fbff, #e6f2ff);
    border-left: 4px solid var(--accent);
}

.chat-message.user {
    background: linear-gradient(145deg, #edf8ff, #e8f7ef);
    border-right: 4px solid var(--success);
}

.chat-message .avatar {
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.25rem;
    margin: 0 0.9rem;
    background: linear-gradient(145deg, var(--accent), #69a9de);
    color: white;
}

.chat-message.user .avatar {
    background: linear-gradient(145deg, var(--success), #4bbd8c);
}

.chat-message .message {
    flex: 1;
    color: var(--text-main) !important;
    font-weight: 600;
    line-height: 1.65;
}

.footer {
    text-align: center;
    color: var(--text-soft);
    margin-top: 2.5rem;
    padding: 1.5rem;
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.4);
    border: 1px solid var(--panel-border);
}

.stProgress > div > div > div > div {
    background: linear-gradient(90deg, var(--accent), #60a5fa) !important;
}

[data-testid="stDataFrame"], .stAlert, [data-testid="stExpander"] {
    border-radius: 18px;
}

hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(44, 126, 199, 0.32), transparent);
    margin: 1.6rem 0;
}

@media (max-width: 768px) {
    .app-shell, .main-container {
        padding: 1rem;
        margin: 0 auto 1.2rem;
        border-radius: 20px;
    }

    .hero-panel {
        padding: 1.2rem;
    }
}
</style>
""",
        unsafe_allow_html=True,
    )


def render_app_header(title: str, subtitle: str, badge: str) -> None:
    st.markdown(
        f"""
<div class="hero-panel">
    <div class="hero-kicker">{badge}</div>
    <h1 class="hero-title">{title}</h1>
    <p class="hero-subtitle">{subtitle}</p>
</div>
""",
        unsafe_allow_html=True,
    )
