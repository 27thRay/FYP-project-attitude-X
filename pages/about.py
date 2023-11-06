import streamlit as st
from login import authenticator
from streamlit_extras.switch_page_button import switch_page

authenticator.logout('Logout', 'sidebar', key='unique_key')
if st.session_state["authentication_status"] is None:
    switch_page('login')

st.sidebar.success("Select a Page above")

st.write("# Welcome to Attitude-X! 👋")

st.markdown(
    """
    Attitude-X, an AI solution, optimizes hiring processes by analyzing resumes. 
    It integrates cutting-edge NLP technologies and LLMs (Language Model Models) for this purpose.
    
    **Done by group 3A62 from Singapore Polytechnic DAAA FYP Year 2023**
    
    ### More about us:
    - Check out our [GitHub](https://github.com/27thRay/FYP-project-attitude-X)
    - Jump into our [Documentation](https://docs.streamlit.io)
    
    #### Contributors:
    - Raymond Loong Ng
    - Darryl Lim
    - Shaun Ho
"""
)