import streamlit as st

st.title("Projects")
# Tabs for navigation
tab1, tab2, tab3 = st.tabs(["2024-2025", "2023-2024", "2022-2023"])

with tab1:
    st.subheader("[RTC](https://ai2-student-tests.uc.r.appspot.com/)")

    st.image("assets/RTC.png", caption="Share Project Wizard", width=600)

    st.markdown("Implemented allowing to share App Inventor projects in read-only mode with other users")

    st.subheader("Light/Dark Mode")

    st.image("assets/DarkMode.png", caption="Dark Mode main page", width=600)

    st.markdown("Implemented light/dark mode per Material Design standards, followed by user testing to optimize experience.")

    st.subheader("Multiple Screens for Aptly")

    st.markdown("[Research Paper](https://www.semanticscholar.org/paper/Aptly%3A-Making-Mobile-Apps-from-Natural-Language-Patton-Kim/c659d7187c8d8a18ff3e2846046fcde6a942df57#citing-papers)")

    st.markdown("Evan W Patton, David Y Kim, Ashley M Granquist, Robin Liu, Arianna Scott, Jennet Zamanova, and Harold Abelson. 2025. Aptly: Making Mobile Apps from Natural Language. In Proceedings of the Extended Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI EA '25). Association for Computing Machinery, New York, NY, USA, Article 73, 1–6. [https://doi.org/10.1145/3706599.3720081](https://doi.org/10.1145/3706599.3720081)")
    
    st.subheader("Any Component for Aptly")


with tab2:
    st.subheader("Dynamic switching between multiple styles")

    st.image("assets/StyleSwitching.png", caption="Style Switching Dialog", width=400)

    st.markdown("Built a dynamic style-switching feature for App Inventor, allowing users to customize their experience.")

    st.subheader("Make the GWT panel collapsable")

    # Create columns
    col1, col2 = st.columns(2)

    # Add images to columns
    with st.container():
        with col1:
            st.image("assets/CollapsedPanel.png", caption="Collapsed collapsable panel", use_container_width=True)

        with col2:
            st.image("assets/OpenedPanel.png", caption="Uncollapsed collapsable panel", use_container_width=True)

    st.markdown("Create a collapsable panel out of multiple GWT disclosure panels.")


with tab3:
    st.subheader("Updated “New Project” dialog")

    st.image("assets/NewProject.png", caption="New Project Dialog", width=400)

    st.markdown("Updated New Project Dialog to customize the toolkit and the app theme to increase exposure to the new features.")
    