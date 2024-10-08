import streamlit as st
from openai import OpenAI

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# def login():
#     if st.button("Log in"):
#         st.session_state.logged_in = True
#         st.rerun()

# def logout():
#     if st.button("Log out"):
#         st.session_state.logged_in = False
#         st.rerun()

# login_page = st.Page(login, title="Log in", icon=":material/login:")
# logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

main = st.Page("main/main.py", title="Dashboard", icon=":material/dashboard:", default=True)
videos = st.Page("portfolio/portfolio.py", title="Portfolio", icon=":material/portfolio:")
alerts = st.Page("reports/alerts.py", title="System alerts", icon=":material/notification_important:")
search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")

# if st.session_state.logged_in:
pg = st.navigation(
    {
        "Main": [main],
        "Portfolio": [videos]
        "Reports": [dashboard, alerts],
        "Tools": [search, history],
    }
)
# else:
#     pg = st.navigation([login_page])

pg.run()
