import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide")
st.markdown("""
<style>
.st-emotion-cache-ztfqz8.ef3psqc5
{
 visibility: hidden;
}
.eyeqlp51 st-emotion-cache-fblp2m ex0cdmw0
{
visibility: hidden;
}
.css-18ni7ap.e8zbici2  /*default menu of streamlit library*/
{
    visibility: hidden;
}
.st-emotion-cache-vk3wp9.eczjsme11/*sidebar of MultipageApp*/
{
    visibility: hidden;
    margin-left: -350px;
}
.st-emotion-cache-14rvwma.eczjsme11
{
    visibility: hidden;
}


.appview-container.css-1wrcr25.egzxvld6  /*Whole page*/
{
    background-color:Beige;
    margin-bottom:-150px;
}
    
.st-emotion-cache-1v0mbdj.e115fcil1 /* XAIface logo */
{
    text-align: center;
    display: block;
    margin-top: -5px;
    width: 100%;
    margin-left: 100px;
    margin-right: 100px;

}

.css-1kyxreq.etr89bj2
{
margin-left: 100px;
}

div.stButton > button:first-child 
{ 
    background-color: #D3D3D3;
    border-radius: 20%;
    height: 3.5em;
    width: 180px; 
    margin-top: 70px;
    margin-left:800px; 
}

div[data-testid="stMarkdownContainer"] p {
    font-size: 34px;
    font-family: Arial; 
    font-weight: bold;
}

</style>
""", unsafe_allow_html = True)

st.markdown("<h1 style='margin-left:45px;text-align: center;  color: Grey; font-size:54px; margin-top: 20px; font-family: Sans-Serif;'>Welcome to the XAIface Face Verification Explainability Demo</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='margin-top: 55px;'></h1>", unsafe_allow_html=True)
image = Image.open("xaiface_logo_PNG.png")
image = image.resize((500, 300))
st.image(image)

st.markdown("<h5 style='margin-left:45px; text-align: center;  color: red; font-size:30px; margin-top: 60px; margin-bottom: -10px; font-family: Sans-Serif; '>Please press F11 on your keyboard to enter the full screen mode</h5>", unsafe_allow_html=True)

st.markdown("<h5 style='margin-left:45px; text-align: center;  color: black; font-size:20px; margin-top: 40px; margin-bottom: -50px; font-family: Sans-Serif; '>If the screen components are misplaced, please adjust the screen scaling to 100% or 125% </h5>", unsafe_allow_html=True)

naima ="Start"
strat_button = st.button(label=naima)

if strat_button:
    switch_page("interface")
