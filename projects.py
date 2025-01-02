import streamlit as st 

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

# pg = st.navigation([st.Page(), st.Page("pages/2_urop_projects.py")])
# pg.run()

class_page = st.Page("pages/1_class_projects.py", title="Class Projects", icon=":material/school:")
urop_page = st.Page("pages/2_urop_projects.py", title="Research Projects", icon=":material/devices:")
club_page = st.Page("pages/3_club_projects.py", title="Club Projects", icon=":material/groups:")

pg = st.navigation([class_page, urop_page, club_page])
st.set_page_config(page_title="Projects", page_icon=":material/edit:")
st.title("Projects")
pg.run()

# st.sidebar.success("Select a demo above.")

# st.title("Projects")

# Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'Project Type',
#     ('Class', 'Club', 'Research (UROP)')
# )

# if add_selectbox == 'Class':
#     st.subheader('6.104 - Software Design')
