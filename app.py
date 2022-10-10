# ===========================================================================================================
#                                               DIGITAL RESUME
# ===========================================================================================================


# ================================================= IMPORTS =================================================
from pathlib import Path
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


# ============================================== PATH SETTINGS ==============================================
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
# resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# ============================================ GENERAL SETTINGS =============================================

# The title and icon showed on the browser tab
PAGE_TITLE = "Irene Burresi | CV"
PAGE_ICON = ":wave:"

# Personal infos on the top of the page
NAME = "Irene Burresi"
DESCRIPTION = """
Computer Science student at the University of Pisa.

Aspiring Data Scientist.
"""
EMAIL = "burresi.irene@icloud.com"
PHONE = "+39 346 9558740"

# Social media
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ireneburresi",
    "GitHub": "https://github.com/IreneBurresi",
}

github_link = 'https://github.com/IreneBurresi'
github_image = 'https://img.icons8.com/ios-glyphs/30/000000/github.png'

linkedin_link = "https://www.linkedin.com/in/ireneburresi"
linkedin_image = "https://img.icons8.com/ios/30/000000/linkedin-2--v1.png"


# Method to show social media links as clickable images
def add_social_media_links():
    st.write('[![Github](' + github_image + ')](' + github_link + ')'
             + ' [![Linkedin](' + linkedin_image + ')](' + linkedin_link + ')')


# Projects
PROJECTS = {
    "🎮 Videogames sales": "https://ireneburresi-videogames-sales-analysis-app-755m1w.streamlitapp.com/",
}

# ================================================ WEBSITE =================================================
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Loading css
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
# PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# ---------------------------------------------- HERO SECTION ----------------------------------------------
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
#    st.download_button(
 #       label=" 📄 Download EN Resume",
        # data=PDFbyte,
        # file_name=resume_file.name,
  #      mime="application/octet-stream",
    # )
    # st.download_button(
   #     label=" 📄 Download IT Resume",
        # data=PDFbyte,
        # file_name=resume_file.name,
     #   mime="application/octet-stream",
    # )
    st.write("📫 ", EMAIL)
    st.write("📞 ", PHONE)
    add_social_media_links()


# -------------------------------------------- NAVIGATION MENU ---------------------------------------------
selected = option_menu(
    menu_title=None,
    options=["About me", "Education", "Skills", "Projects"],
    icons=["emoji-smile", "mortarboard", "code-slash", "paperclip"],
    orientation="horizontal",
)


# ------------------------------------------------ ABOUT ME ------------------------------------------------
if selected == "About me":
    st.subheader("👋🏻 Hi, I'm Irene!")
    st.markdown("#### I'm an italian computer science student and aspiring data scientist")
    st.write("Actually I'm pursuing a bachelor degree in Computer Science at the University of Pisa (just 2 exams left)")
    st.write("I'm looking for a curricula stage (300 hours), possibly in the data science field.")
#
# ------------------------------------------------- SKILLS -------------------------------------------------
elif selected == "Skills":
    st.write("#")
    st.subheader("Techincal Skills")
    st.write(
        """
        - 👩‍💻 Programming: Python (Numpy, Scikit-learn, Pandas), SQL, Javascript, Java, C
        - 📊 Data Visulization: PowerBi, MS Excel, Plotly
        - 📚 Modelling: linear regression, SVM, decision trees, concept learning, KNN, K-means
        - 🗄️ Databases: MongoDB (basics), MySQL
        """
    )
#
# ------------------------------------------------ PROJECTS ------------------------------------------------
elif selected == "Projects":
    # --- Projects & Accomplishments ---
    st.write("#")
    st.subheader("Projects")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")
#
# ------------------------------------------------ EDUCATION ------------------------------------------------
if selected == "Education":
    st.write("#")
    st.subheader("Education")
    st.write("---")
    
    
