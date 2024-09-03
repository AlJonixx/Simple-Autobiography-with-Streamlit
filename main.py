import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
        page_title="My Autobiography and Portfolio",
        page_icon="🤍",
    )

tab1, tab2, tab3 = st.tabs(["Home", "Portfolio", "About Me"])

with tab1:
    col1, col2 = st.columns(2, vertical_alignment="center")

    with col1:
        st.image("static/Sleep.png")

    with col2:
        st.markdown("""
            ### Hey I'm                 
            # :rainbow[Aljon Rey Alipin]
            ***BSIT Student/Digital Artist***

        """)

with tab2:
    st.markdown("""
        #### Full-Stack Development of an AppDev Project using Python Django Framework
        ##### CIT - University
        ###### October 2020 - December 2020
        - Project Title: Human Resource Information System 
        - Developed a web application for Uni-Orient Travel Incorporated (Cebu) with a fully functional CRUD operation using Django Framework 
        - Implemented the database using MySQL 
        - Used HTML, CSS, Bootstrap, and JavaScript in creating the user interface design. 

        #### Full-Stack Development of an Information Management Project using Python Django Framework
        ##### CIT - University
        ###### August 2020 - October 2020

        - Project Title: GetVaxxed 
        - Developed a web application with a fully functional CRUD operation using Django Framework 
        - Implemented the database using MySQL 
        - Used HTML, CSS, and Bootstrap in creating the user interface design.

        #### Full-Stack Development of an OOP Project using Java and MySQL
        ##### CIT - University
        ###### November 2019 - February 2020

        - Project Title: WeCare Medical Booking Appointment System 
        - Developed a simple doctor appointment booking system with fully functional CRUD operations with Java's Object-Oriented Programming concepts. 
        - Implemented the database using MySQL. 
        - Created and design the user interface using Java GUI frameworks

        ---
        ## Artwork Portfolio 
    """)
    
    art1, art2 = st.columns(2)
    with art1:
        st.image("static/1.png")
        st.image("static/seulgiii.png")
    with art2:
        st.image("static/chrollo.png")
        st.image("static/kurapika.png")

with tab3:
    st.markdown("""
        My name is Aljon Rey Alipin, and I'm 24 years old. I was born on October 18, 1999, in Cebu City. I am currently pursuing a Bachelor of Science in Information Technology at the Cebu Institute of Technology University.

I stopped for a couple of years because of the pandemic that happened in 2020 and tried to work with my passion in digital art. While doing digital art, I also accepted commissions to earn extra income. I'm still doing digital art and hope to one day turn it into a full-time career. I want to continue sharing my artworks with the world and inspire others to pursue their passions as well.

I'm taking my last year as a BSIT student to get my degree and start working towards my dream. It may have taken me a while to get back to school, but I am determined to make it happen. It's never too late to chase your dreams and make them a reality. I have always had a passion for art, and pursuing a career in digital art has been a dream of mine since I was young. I am grateful for the opportunities that have come my way and for the support of my family and friends. With hard work and dedication, I believe that I can turn my passion into a successful career. I am excited for what the future holds and am confident that I can achieve my goals with perseverance and determination.
    """)