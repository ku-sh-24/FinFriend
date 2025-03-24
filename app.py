import streamlit as st
from auth_functions import *
# from user_options.profile_entry import main_profile


initialize_firebase_once()

def rate_us_button():
    @st.dialog("How do you rate our app?")
    def rate():
        sentiment_mapping = ["one", "two", "three", "four", "five"]
        selected = st.feedback("stars")
        if selected is not None:
            st.session_state.rate = {"item": sentiment_mapping[selected]}
            # st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
            # st.rerun()
    rate()
    return


# Set up the page config
st.set_page_config(page_title="Financial Agent", page_icon="💰", layout="wide")

if check_login_status():
    # if 'user_info' in st.session_state:
    # Define the pages for logged-in users

    st.title("Welcome to Financial Agent")
    # Sidebar with buttons for account selection
    initialize_firebase()
    user_info = st.session_state.user_info
    user_id = user_info['localId']  # Get the user ID from session state

    nav_login = []
    # if st.session_state.first_login:

    nav_login = st.navigation(
        [
            st.Page("user_pages/dashboard.py", title="Dashboard"),
            st.Page("user_pages/money_tracker.py", title="Finanace Tracker"),
            st.Page("user_pages/lessons.py", title=" Finance Lessons"),
            st.Page("user_pages/advisor.py", title="Finanace Advisor"),
            st.Page("user_pages/fraud_detector.py", title="Fraud Alert"),
            st.Page("user_pages/quiz.py", title="Quiz"),
            st.Page("user_pages/news.py", title="News"),
            st.Page("user_pages/govt_schemes.py", title="Govt Schemes"),
            st.Page("user_pages/dictionary.py", title="Dictionary"),
            st.Page("user_pages/chatbot.py", title="Chatbot"),
            st.Page('account_settings/user_controls.py', title="Profile", default=True),
            # st.Page("user_pages/dashboard.py", title="Dashboard"),
            st.Page(sign_out, title="Sign Out"),
            # st.Page("user_pages/money_tracker.py", title="Finanace Tracker"),
            # st.Page("user_pages/chatbot.py", title="Chatbot"),
            # st.Page("user_options/profile_entry.py", title="Set Profile"),
        ]
    )
    nav_login.run()
else:
    # Sidebar with buttons for account selection
    
    initialize_firebase()

    nav = st.navigation(
        [
            # st.Page(entry_point, title="Introduction", default=True),
            st.Page("user_options/login_pg.py", title="Log In"),  
            st.Page("user_options/signup_pg.py", title="Sign Up"), 
            st.Page("user_options/forgot_password_pg.py", title="Reset Password"),
        ]
    )
    nav.run()

    # with st.sidebar:
    #     nav_login = st.navigation(
    #         [
    #             # st.Page('account_settings/user_controls.py', title="Profile"),  # Magic works
    #             st.Page("user_pages/dashboard.py", title="Dashboard", default=True),
    #             # st.Page(sign_out, title="Sign Out"),  # Magic works
    #             # st.Page("user_options/profile_entry.py", title="Set Profile"),
    #             st.Page("user_pages/money_tracker.py", title="Finanace Tracker"),
    #             st.Page("user_pages/lessons.py", title=" Finance Lessons"),
    #             st.Page("user_pages/advisor.py", title="Finanace Advisor"),
    #             st.Page("user_pages/fraud_detector.py", title="Fraud Alert"),
    #             st.Page("user_pages/quiz.py", title="Quiz"),
    #             st.Page("user_pages/news.py", title="News"),
    #             st.Page("user_pages/govt_schemes.py", title="Govt Schemes"),
    #             st.Page("user_pages/dictionary.py", title="Dictionary"),
    #             st.Page("user_pages/chatbot.py", title="Chatbot"),
    #         ]
    #     )

    #     # # Add empty space to push buttons to the bottom
    #     # for _ in range(23):  # Adjust the number of empty lines as needed
    #     #     st.write("")

    #     # Add buttons at the bottom
    #     col1, col2, col3 = st.columns([1, 1, 1])
    #     with col1:
    #         if st.button("Profile", key="profile_button"):
    #             main_profile()  # Trigger the profile function when the button is pressed
    #     with col2:
    #         if st.button("Sign Out", key="sign_out_button"):
    #             sign_out()  # Trigger the sign_out function when the button is pressed
    #     with col3:
    #         if st.button("Rate Us", key="rate_us_button"):
    #             # rate_us_button()
    #             if "rate" not in st.session_state:
    #                 rate_us_button()  # Trigger the sign_out function when the button is pressed
    #             else:
    #                 f"You gave us {st.session_state.rate['item']} stars!"


        
    #     # if st.button("Sign Out", key="sign_out_button"):
    #     #     sign_out()  # Trigger the sign_out function when the button is pressed

    #     # if st.button("Profile", key="profile_button"):
    #     #     main_profile()  # Trigger the sign_out function when the button is pressed

    # nav_login.run()

# else:
#     st.title("Welcome to Financial Agent")
#     # Sidebar with buttons for account selection

#     nav = st.navigation(
#         [
#             st.Page(entry_point, title="Introduction", default=True),  # Magic works
#             st.Page("user_options/login_pg.py", title="Log In"),  # Magic does not work
#             st.Page("user_options/signup_pg.py", title="Sign Up"),  # Magic works
#             # st.Page("user_options/forgot_password_pg.py", title="Reset Password"),  # Magic works
#         ]
#     )
#     nav.run()