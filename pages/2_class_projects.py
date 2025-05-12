import streamlit as st

st.title("Projects")
# Tabs for navigation
tab1, tab2, tab3 = st.tabs(["2024-2025", "2023-2024", "2022-2023"])

with tab1:

    st.subheader("6.c35 - Interactive Data Visualization & Society")

    st.markdown("### [Housing4All](https://hap196.github.io/Housing4All2/)")

    st.image("assets/Housing4All.png",
             caption="Housing4All text visualization page")

    st.markdown(
        """
Boston faces a severe affordable housing crisis. _Half of all renters are rent-burdened_, and only one-third of residents own their homes. 
While the Boston Zoning Code aims to promote appropriate land use and resident welfare, it's widely criticized as _bloated, outdated, and inequitable_. 

Our __Housing4All__ project analyzes how Boston’s zoning policies impact affordable housing access by making the Boston Redevelopment Authority’s amendments transparent and analyzable. 
Currently, these critical policy changes exist only as scattered PDFs, making it nearly impossible to track patterns or impacts.

Our interactive visualization tool allows you to:
- Filter amendments by housing and zoning topics to see which areas are most affected
- Examine how specific amendments impact housing construction in targeted districts
- View demographic data to understand who is most affected by these policy changes

By connecting zoning amendments with housing outcomes and demographics, we aim to support advocacy groups who want to _track_ policy changes and _visualize_ 
the real-world impacts of zoning on Boston’s communities.
"""
    )

    st.subheader("6.1040 - Software Design 1")

    st.markdown("### [TrueTide](https://truetide-frontend.vercel.app/)")

    st.image("assets/Truetide.png", caption="TrueTide main page")

    st.markdown(
        """
        __TrueTide__ is designed for _international students_ navigating new environments and cultures. 
        Adjusting to life in a new country can be overwhelming, and students often struggle to find accurate, culturally relevant information. 
        __TrueTide__ helps bridge that gap by providing a diverse range of perspectives on everything from national policies to local slang and customs.

        The app's key feature is its ___DualView___, which allows users to see opposing viewpoints on controversial topics, fostering critical thinking. 
        To support responsible information-sharing, TrueTide offers easy-to-use __fact-checking__ tools and recommends relevant _Citations_ to users as they post content,
        making it simple to back up information. TrueTide offers a trusted and culturally aware platform, easing the transition for students as they learn more about their new surroundings.
    """
    )

    st.subheader("6.1040 - Software Design 2")

    st.markdown("### [Craftfolio](https://craft-folio.vercel.app/)")

    st.image("assets/Craftfolio.png", caption="Craftfolio main page")

    st.markdown(
        "[Demo Video](https://drive.google.com/file/d/1camVrlaDj6gnJt0DmCCHpwG-ir39snW0/view)")

    st.markdown(
        """
        __Craftfolio__ is a web app designed for beginner crafters looking to confidently _start_ and _complete_ creative fiber projects. 
        Our app targets a unique, underserved audience of new crafters who often feel overwhelmed by the complexity of project planning and lack of accessible resources. 
        __Craftfolio__ empowers users by providing an intuitive project tracker and resource management tools tailored specifically to beginners working with different fibers. 
        Unlike existing crafting communities that focus mainly on showcasing finished projects, __Craftfolio__ offers a _collaborative_ space for planning, sharing, and discussing project materials.

        Key features include personalized _project filters_ based on _available_ sources, _ratings_ to simplify finding useful guides, 
        and _sepcial comments_ fostering a supportive and interactive environment. 
        Craftfolio's value lies in bridging the gap between inspiration and execution, helping users efficiently manage crafting resources and build confidence through shared expertise.
    """
    )

    # https://jennet-zamanova.github.io/portfolio-6104/assignments.html

    st.subheader("6.073 - Creating Video Games")

    st.markdown(
        "### [Trash Bandits](https://ashketchmm.itch.io/trash-bandits)")

    st.image("assets/TrashBandits.png", caption="Trash Bandits main page")

    st.markdown(
        """
        A _lighthearted_, _chaotically comedic_ game with a _cute_ aesthetic where you work
        together with your friend as a raccoon and a cat to distract people and steal as
        much trash as possible without getting caught by the humans.
    """
    )

    st.subheader("6.S093 - How to ship almost anything with AI")

    st.markdown("### [DishIQ](https://dish-iq.streamlit.app/)")

    st.image("assets/DishIQ.png", caption="DishIQ example with menu")

    st.markdown(
        """
__DishIQ__ is an innovative app that transforms how you navigate menus. Here's what it does:

__Extract Key Details__
Using advanced AI, DishIQ scans restaurant menus to extract:
- _Ingredients_: Know exactly what's in each dish.  
- _Prices_: Stay within your budget effortlessly.  
- _Dish Images_: If unavailable, it generates mouthwatering, realistic dish visuals to help you decide.  

__Tailored Recommendations__
DishIQ takes dietary restrictions seriously. Whether you're gluten-free, vegan, allergic to nuts, or simply avoiding certain ingredients, the app:

- _Flags_ potential allergens and cross-contamination risks.  
- Provides _questions to ask_ the waiter for clarity on preparation methods.  
- _Highlights_ dishes that fit your preferences while warning you about risky ones.  
"""
    )

    st.subheader("CMS.590 - Computer Games")

    st.markdown(
        "### Tinker Tales")

    st.image("assets/TinkerTales.png", caption="Tinker Tales main page")

    st.markdown(
        """
        __Tinker Tales__ is a digital creative writing game powered by Large Language Models (LLMs) where students solve challenges by 
        writing their own _creative_ and _descriptive_ solutions. The game is targeted towards 5th-7th grade students and is intended to teach students how to
          write _compelling_ narratives using __descriptive details, vivid sensory details, and clear event sequences__. Players type into an open text box to describe actions, 
          spawn items, and describe their solutions, which will influence the game world around them. Students can have fun building their own solutions while practicing 
          improvisation, critical thinking skills, and learning how to write a story from a bottom-up approach.
    """
    )

    st.subheader("More To Come...")

with tab2:

    st.subheader("17.835 - Machine Learning and Data Science in Politics")

    st.markdown(
        """
        The Legitimacy of Representation: Evaluating the Strength of Local-State Proportional
Representation in the US.  Combine constituent level (raw) data with representative level (final) data and create alignment indices for CA and WA. 
Get district-level characteristics for CA and do matching on districts to find the effect of income on how aligned representatives' and constituents' votes are.  
        [Final Report](https://drive.google.com/file/d/1RPG1M6YIGvl3iNcBGwS-uirDC-yUKnsE/view?usp=sharing)  
        [Repo](https://github.com/farinliani/17.853)
    """
    )

    st.subheader("6.9620 - WebLab")

    st.markdown(
        "### [Ancient Adventures](https://ancient-adventures.onrender.com)")

    st.image("assets/AncientAdventures.png",
             caption="Ancient Adventures main page")

    st.markdown(
        """__Ancient Adventures__ is a vibrant and engaging website designed to help travelers explore the historic sites of Central Asia. 
    The platform features detailed guides to ancient landmarks, practical travel tips, and curated insights into the region’s rich culinary traditions.
    """
    )

    # st.subheader("6.1020 - Software Construction")

    st.subheader("6.2000 - Circuits and Electronics")

    st.markdown(
        "Digital to Analog converter, Moth-car, Bass Boost, Morse Code Transmitter/Detector"
    )

with tab3:

    st.subheader("6.S092 - The Art and Science of PCB Design")

    st.image("https://pcb.mit.edu/static/gallery/0006.jpg",
             caption="Bluetooth speaker!!!")
