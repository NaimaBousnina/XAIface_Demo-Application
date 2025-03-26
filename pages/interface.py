import streamlit as st
from PIL import Image
import pandas as pd
import streamlit_pandas as sp

st.set_page_config(layout="wide")
st.markdown("""
<style>
/*.st-emotion-cache-zt5igj.e1nzilvr4 /* Gallery image and FV set up boxes*/
{
margin-top: 70px;
}*/
.st-emotion-cache-keje6w.e1f1d6gn3 /* cotainer of gallery image and FV tools*/
{
#background-color: red;
margin-top: -70px;
}
.st-emotion-cache-1nm2qww.eczjsme2
{
visibility: hidden;
}

.st-emotion-cache-16idsys.e1nzilvr5 p /* Labels in the sidebar box*/
{
font-size:18px;
}

.row-widget.stSelectbox/* select boxes: label + select text*/
{
margin-bottom: 32px;
}
.st-emotion-cache-79elbk.eczjsme10 /* the hidden part aboce settings*/
{
visibility: hidden;
margin-top:-100px; 
}

.st-emotion-cache-1v0mbdj.e115fcil1 /* logo in the sidebar*/
{
margin-left: auto;
margin-right: auto;
margin-top: -72px;
margin-bottom: 10px;
}

.css-164nlkn.egzxvld1
{
visibility: hidden;
}
.st-emotion-cache-18ni7ap.ezrtsby2
{
visibility: hidden;
}

.css-1xtoq5p.e1fqkh3o2
{
visibility: hidden;  
}

.css-wjbhl0.e1fqkh3o9
{
margin-top: -100px;
visibility: hidden;  
}

.css-1s3y5qe.e1fqkh3o8
{
visibility: hidden;  
}

.css-1629p8f.e16nr0p31
{
 margin-top: -120px;   
}

.block-container.st-emotion-cache-z5fcl4.ea3mdgi2
{
height:100%;
}


.element-container.css-1ble31s.e1tzin5v3
{
margin-top: 20px; 
#background-color: red;
}
</style>

""", unsafe_allow_html = True)

def jarab():
    if st.session_state['face beautification or face coding'] == "Face Beautification":
        st.session_state['face coding tool'] = "Select"

    if st.session_state['face beautification or face coding'] == "Face Coding":
        st.session_state['face beautification tool'] = "Select"

    if st.session_state['face beautification or face coding'] == "Select":
        st.session_state['face beautification tool'] = "Select"
        st.session_state['face coding tool'] = "Select"

    

@st.cache_data
def load_data():
    df = pd.read_csv("DATASET/Book.csv", dtype=str)
    return df

df = load_data()
#st.write(df)

create_data = {"Probe-gallery Pair ID": "select",
                "Face Beautification or Face Coding": "select",
                "Face Beautification Tool": "select",
                "Face Coding Tool": "select",
                "Face Verification Tool": "select",
                "Face Verification Explainability Tool": "select"}

# Creat the sidebar with the desired widgets
all_widgets = sp.create_widgets(df, create_data, ignore_columns=["Probe_img_path", "Gallery_img_path", 
                                                                 "Comparison Type", "Original Score", 
                                                                 "Decision Threshold", "Original Decision",
                                                                 "Filtred_probe_img_path", 
                                                                 "Decision After Beautification", 
                                                                 "Decoded_probe_img_path", "Score After Coding",
                                                                 "Similar_region_HM_path", "Score After Beautification",
                                                                 "Decision After Coding", "Decision Type", "PSNR-YUV", "MS-SSIM", 
                                                                 "Probe Age", "Gallery Age", "Probe Gender", "Gallery Gender", 
                                                                 "Probe Weight", "Gallery Weight"], on_change=jarab)

# Filter the dataframe according to the user's selections
res = sp.filter_df(df, all_widgets)
#st.write(res)


####
# Containers generation
st.markdown(""" """)
st.markdown(""" """)
first_container = st.container()
st.markdown("""<hr style="height:1px;color:#F8F8F8; margin-top: -5px" /> """, unsafe_allow_html=True)
second_container = st.container()


# Containers building
with first_container:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<h6 style='margin-top: -130px; text-align: center; margin-left: 70px; margin-right: 70px; color: Black; font-size:21px; font-family: Sans-Serif; background-color:#FF5C5C; border-radius: 10px 10px; height: 50px; line-height: 50px; '>Gallery Image</h6>", unsafe_allow_html=True)
        Gallery_img_path = res["Gallery_img_path"]
        Gallery_img_path = Gallery_img_path.tolist()[0]
        image = Image.open(Gallery_img_path.strip('\"'))
        image = image.resize((350, 350))
        st.image(image)

    with col2:
        st.markdown("<h6 style='margin-top: -130px; text-align: center; margin-left: 70px; margin-right: 70px; color: Black; font-size:21px; font-family: Sans-Serif; background-color:#FF5C5C; border-radius: 10px 10px; height: 50px; line-height: 50px;'>Face Verification Setup</h6>", unsafe_allow_html=True)
        recognition_tool = res["Face Verification Tool"]
        recognition_tool = recognition_tool.tolist()[0]

        comparison_type = res["Comparison Type"]
        comparison_type = comparison_type.tolist()[0]

        decision_thresh = res["Decision Threshold"]
        decision_thresh = decision_thresh.tolist()[0]

        contain_1 = st.container()
        contain_3 = st.container()

        with contain_1:
            st.markdown(f"<h6 style='margin-top: 60px; text-align: center;float:left; margin-left: 60px; width: 210px; height: 40px; line-height: 40px; color:white;font-size:18px; font-family: Sans-Serif; background-color:DarkBlue; border-radius: 5px 5px;'> Face Verification Tool </h6> <h6 style='margin-top: 60px; text-align: center; float:right;width: 130px; height: 40px; line-height: 40px; color:Black;font-size:18px; font-family: Sans-Serif; background-color:Aqua; border-radius: 5px 5px; margin-right:50px;'>{recognition_tool}</h6>", unsafe_allow_html=True)
        with contain_3:
            st.markdown(f"<h6 style='margin-top: 30px; text-align: center;float:left; margin-left: 60px; width: 210px; height: 40px; line-height: 40px; color:white;font-size:18px; font-family: Sans-Serif; background-color:DarkBlue; border-radius: 5px 5px;'> Decision Threshold </h6> <h6 style='margin-top: 30px; text-align: center; float:right;width: 130px; height: 40px; line-height: 40px; color:Black;font-size:18px; font-family: Sans-Serif; background-color:Aqua; border-radius: 5px 5px; margin-right:50px;'>{decision_thresh}</h6>", unsafe_allow_html=True)

    with col3:
        st.markdown("<h6 style='margin-top: -130px; text-align: center; margin-left: 70px; margin-right: 70px; color: Black; font-size:21px; font-family: Sans-Serif; background-color:#FF5C5C; border-radius: 10px 10px; height: 50px; line-height: 50px; '>Soft Biometrics (EUR) </h6>", unsafe_allow_html=True)
       
        probe_age = res["Probe Age"]
        probe_age = probe_age.tolist()[0]

        gallery_age = res["Gallery Age"]
        gallery_age = gallery_age.tolist()[0]

        probe_gender = res["Probe Gender"]
        probe_gender = probe_gender.tolist()[0]

        gallery_gender = res["Gallery Gender"]
        gallery_gender = gallery_gender.tolist()[0]

        probe_weight = res["Probe Weight"]
        probe_weight = probe_weight.tolist()[0]

        gallery_weight = res["Gallery Weight"]
        gallery_weight = gallery_weight.tolist()[0]

        contain_3_1 = st.container()
        contain_3_2 = st.container()


        beauti_choix= res["Face Beautification Tool"]
        beauti_choix = beauti_choix.tolist()[0]

        coding_choix= res["Face Coding Tool"]
        coding_choix = coding_choix.tolist()[0]


        if st.session_state['face beautification or face coding'] == "Select":
            
            with contain_3_1:
                st.markdown(f"<h6 style='margin-left: 20px; margin-right: 20px; margin-top: -60px; background-color:#E0FFFF; border-radius: 10px 10px; height: 140px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Probe Image:</p> <p style='margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Gender:   {probe_gender}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Age:  {probe_age}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'> Weight:  {probe_weight}</p></h6>", unsafe_allow_html=True)

            with contain_3_2:
                st.markdown(f"<h6 style='margin-left: 20px; margin-right: 20px; margin-top: 30px; background-color:#E0FFFF; border-radius: 10px 10px; height: 140px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Gallery Image:</p> <p style='margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Gender:   {gallery_gender}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Age:  {gallery_age}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'> Weight:  {gallery_weight}</p></h6>", unsafe_allow_html=True)

        if st.session_state['face beautification or face coding'] == "Face Coding":
            
            if coding_choix != "Select":
                
                with contain_3_1:
                    st.markdown(f"<h6 style='margin-left: 20px; margin-right: 20px; margin-top: -60px; background-color:#E0FFFF; border-radius: 10px 10px; height: 140px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Decoded Probe Image:</p> <p style='margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Gender:   {probe_gender}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Age:  {probe_age}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'> Weight:  {probe_weight}</p></h6>", unsafe_allow_html=True)
                    
                with contain_3_2:
                    st.markdown(f"<h6 style='margin-left: 20px; margin-right: 20px; margin-top: 30px; background-color:#E0FFFF; border-radius: 10px 10px; height: 140px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Gallery Image:</p> <p style='margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Gender:   {gallery_gender}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Age:  {gallery_age}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'> Weight:  {gallery_weight}</p></h6>", unsafe_allow_html=True)
            else:
                
                with contain_3_1:
                    st.markdown(f"<h6 style='margin-left: 20px; margin-right: 20px; margin-top: -60px; background-color:#E0FFFF; border-radius: 10px 10px; height: 140px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Probe Image:</p> <p style='margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Gender:   {probe_gender}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Age:  {probe_age}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'> Weight:  {probe_weight}</p></h6>", unsafe_allow_html=True)
                    
                with contain_3_2:
                    st.markdown(f"<h6 style='margin-left: 20px; margin-right: 20px; margin-top: 30px; background-color:#E0FFFF; border-radius: 10px 10px; height: 140px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Gallery Image:</p> <p style='margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Gender:   {gallery_gender}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Age:  {gallery_age}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'> Weight:  {gallery_weight}</p></h6>", unsafe_allow_html=True)


        if st.session_state['face beautification or face coding'] == "Face Beautification":
            
            if beauti_choix != "Select":
                
                with contain_3_1:
                    st.markdown(f"<h6 style='margin-left: 20px; margin-right: 20px; margin-top: -60px; background-color:#E0FFFF; border-radius: 10px 10px; height: 140px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Filtered Probe Image:</p> <p style='margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Gender:   {probe_gender}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Age:  {probe_age}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'> Weight:  {probe_weight}</p></h6>", unsafe_allow_html=True)

                with contain_3_2:
                    st.markdown(f"<h6 style='margin-left: 20px; margin-right: 20px; margin-top: 30px; background-color:#E0FFFF; border-radius: 10px 10px; height: 140px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Gallery Image:</p> <p style='margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Gender:   {gallery_gender}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Age:  {gallery_age}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'> Weight:  {gallery_weight}</p></h6>", unsafe_allow_html=True)

            else:
                
                with contain_3_1:
                    st.markdown(f"<h6 style='margin-left: 20px; margin-right: 20px; margin-top: -60px; background-color:#E0FFFF; border-radius: 10px 10px; height: 140px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Probe Image:</p> <p style='margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Gender:   {probe_gender}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Age:  {probe_age}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'> Weight:  {probe_weight}</p></h6>", unsafe_allow_html=True)
                    
                with contain_3_2:
                    st.markdown(f"<h6 style='margin-left: 20px; margin-right: 20px; margin-top: 30px; background-color:#E0FFFF; border-radius: 10px 10px; height: 140px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Gallery Image:</p> <p style='margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Gender:   {gallery_gender}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'>Age:  {gallery_age}</p> <p style='margin-top: -10px; margin-left: 30px; font-size:18px; color: DarkBlue; font-weight: bold;'> Weight:  {gallery_weight}</p></h6>", unsafe_allow_html=True)

 
 
with second_container:
    col1, col2, col3 = st.columns(3)

    with col1:

        ori_score = res["Original Score"]
        ori_score = ori_score.tolist()[0]

        ori_decision = res["Original Decision"]
        ori_decision = ori_decision.tolist()[0]

        st.markdown("<h6 style='text-align: center; margin-left: 70px; margin-right: 70px; color: Black; font-size:21px; font-family: Sans-Serif; margin-top: -20px; background-color:#FF5C5C; border-radius: 10px 10px; height: 50px; line-height: 50px; '>Probe Image</h6>", unsafe_allow_html=True)
        
        container_2 = st.container()
        container_4 = st.container()
        container_5 = st.container()

        with container_2:
            st.markdown(f"<h6 style='margin-top: 40px; text-align: center;float:left; margin-left: 40px; width: 210px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#556B2F; border-radius: 5px 5px;'> Type of Pair </h6> <h6 style='margin-top: 40px; text-align: center; float:right;width: 120px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#808000; border-radius: 5px 5px; margin-right:45px;'> {comparison_type} </h6>", unsafe_allow_html=True)
        with container_4:
            st.markdown(f"<h6 style='margin-top: 20px; text-align: center;float:left; margin-left: 40px; width: 210px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#556B2F; border-radius: 5px 5px;'> Cosine Distance </h6> <h6 style='margin-top: 20px; text-align: center; float:right;width: 120px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#808000; border-radius: 5px 5px; margin-right:45px;'> {ori_score} </h6>", unsafe_allow_html=True)
        with container_5:  
            st.markdown(f"<h6 style='margin-top: 20px; text-align: center;float:left; margin-left: 40px; width: 210px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#556B2F; border-radius: 5px 5px;'> Verification Decision </h6> <h6 style='margin-top: 20px; text-align: center; float:right;width: 120px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#808000; border-radius: 5px 5px; margin-right:45px;'>{ori_decision}</h6>", unsafe_allow_html=True)  

        st.markdown("<h3 style='margin-top: 45px;'></h3>", unsafe_allow_html=True)
        probe_img_path = res["Probe_img_path"]
        probe_img_path = probe_img_path.tolist()[0]
        image = Image.open(probe_img_path.strip('\"'))
        image = image.resize((350, 350))
        st.image(image)


    with col2:   

        choise = res["Face Beautification or Face Coding"]
        choise = choise.tolist()[0]

        select_beautifi = res["Face Beautification Tool"]
        select_beautifi = select_beautifi.tolist()[0]

        select_coding = res["Face Coding Tool"]
        select_coding = select_coding.tolist()[0]

        # if no choise is slecetd
        if choise == "Select":


            st.markdown("<h6 style='text-align: center; margin-left: 30px; margin-right: 30px; color: Black; font-size:21px; font-family: Sans-Serif; margin-top: -20px; background-color:#FF5C5C; border-radius: 10px 10px; height: 50px; line-height: 50px; '>Face Beautification/Face Coding</h6>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; color: Black; font-size:24px; margin-top: 220px; '>No face beautification or face coding is applied</h5>", unsafe_allow_html=True)
            #st.markdown("<h5 style='text-align: center; color: Black; font-size:24px; margin-top: 5px; '>😔</h5>", unsafe_allow_html=True)
        
        # if no beautification filter is selected
        if choise == "Face Beautification" and select_beautifi == "Select" : 

            st.markdown("<h6 style='text-align: center; margin-left: 30px; margin-right: 30px; color: Black; font-size:21px; font-family: Sans-Serif; margin-top: -20px; background-color:#FF5C5C; border-radius: 10px 10px; height: 50px; line-height: 50px; '>Filtered Probe Image</h6>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; color: Black; font-size:24px; margin-top: 220px; '> Please select the face beautification tool</h5>", unsafe_allow_html=True)
            #st.markdown("<h5 style='text-align: center; color: Black; font-size:24px; margin-top: 5px; '>😊</h5>", unsafe_allow_html=True)

        # if a beautification filter is selected
        if choise == "Face Beautification" and select_beautifi != "Select" : 

            st.markdown("<h6 style='text-align: center; margin-left: 30px; margin-right: 30px; color: Black; font-size:21px; font-family: Sans-Serif; margin-top: -20px; background-color:#FF5C5C; border-radius: 10px 10px; height: 50px; line-height: 50px; '>Filtered Probe Image</h6>", unsafe_allow_html=True)

            beauti_score = res["Score After Beautification"]
            beauti_score = beauti_score.tolist()[0]

            beauti_decision = res["Decision After Beautification"]
            beauti_decision = beauti_decision.tolist()[0]

            container_6 = st.container()
            container_7 = st.container()

            with container_6:
                st.markdown(f"<h6 style='margin-top: 70px; text-align: center;float:left; margin-left: 40px; width: 210px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#556B2F; border-radius: 5px 5px;'> Cosine Distance </h6> <h6 style='margin-top: 70px; text-align: center; float:right;width: 120px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#808000; border-radius: 5px 5px; margin-right:40px;'>{beauti_score}</h6>", unsafe_allow_html=True)
            with container_7:
                st.markdown(f"<h6 style='margin-top: 20px; text-align: center;float:left; margin-left: 40px; width: 210px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#556B2F; border-radius: 5px 5px;'> Verification Decision </h6> <h6 style='margin-top: 20px; text-align: center; float:right;width: 120px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#808000; border-radius: 5px 5px; margin-right:40px;'>{beauti_decision}</h6>", unsafe_allow_html=True)  


            st.markdown("<h3 style=' margin-top: 75px;'></h3>", unsafe_allow_html=True)
            beauti_img_path = res["Filtred_probe_img_path"]
            beauti_img_path = beauti_img_path.tolist()[0]
            image = Image.open(beauti_img_path.strip('\"'))
            image = image.resize((350, 350))
            st.image(image)
        
        # If no image coding tool is selected
        if choise == "Face Coding" and select_coding == "Select": 

            st.markdown("<h6 style='text-align: center; margin-left: 30px; margin-right: 30px; color: Black; font-size:21px; font-family: Sans-Serif; margin-top: -20px; background-color:#FF5C5C; border-radius: 10px 10px; height: 50px; line-height: 50px; '>Decoded Probe Image</h6>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; color: Black; font-size:24px; margin-top: 220px; '> Please select the face coding tool</h5>", unsafe_allow_html=True)
            #st.markdown("<h5 style='text-align: center; color: Black; font-size:24px; margin-top: 5px; '>😊</h5>", unsafe_allow_html=True)
         
     
            # if the image coding tool is selected
        if choise == "Face Coding" and select_coding != "Select": 

            coding_score = res["Score After Coding"]
            coding_score = coding_score.tolist()[0]

            coding_decision = res["Decision After Coding"]
            coding_decision = coding_decision.tolist()[0]

            st.markdown("<h6 style='text-align: center; margin-left: 30px; margin-right: 30px; color: Black; font-size:21px; font-family: Sans-Serif; margin-top: -20px; background-color:#FF5C5C; border-radius: 10px 10px; height: 50px; line-height: 50px; '>Decoded Probe Image </h6>", unsafe_allow_html=True)

            PSNR_YUV = res["PSNR-YUV"]
            PSNR_YUV = PSNR_YUV.tolist()[0]

            MS_SSIM = res["MS-SSIM"]
            MS_SSIM = MS_SSIM.tolist()[0]

            container_8 = st.container()
            container_9 = st.container()
            container_12 = st.container()
            container_13 = st.container()
     
            with container_8:
                st.markdown(f"<h6 style='margin-top: 30px; text-align: center;float:left; margin-left: 40px; width: 210px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#556B2F; border-radius: 5px 5px;'> Cosine Distance </h6> <h6 style='margin-top: 30px; text-align: center; float:right;width: 120px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#808000; border-radius: 5px 5px; margin-right:40px;'>{coding_score}</h6>", unsafe_allow_html=True)
            with container_9:
                st.markdown(f"<h6 style='margin-top: 5px; text-align: center;float:left; margin-left: 40px; width: 210px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#556B2F; border-radius: 5px 5px;'> Verification Decision </h6> <h6 style='margin-top: 5px; text-align: center; float:right;width: 120px; height: 40px; line-height: 40px; color:White;font-size:18px; font-family: Sans-Serif; background-color:#808000; border-radius: 5px 5px; margin-right:40px;'>{coding_decision}</h6>", unsafe_allow_html=True)  

            with container_12:
                st.markdown(f"<h6 style='margin-top: 5px; text-align: center;float:left; margin-left: 40px; width: 210px; height: 40px; line-height: 40px; color:black;font-size:18px; font-family: Sans-Serif; background-color:#FFDEAD; border-radius: 5px 5px;'> PSNR-YUV (dB) </h6> <h6 style='margin-top: 5px; text-align: center; float:right;width: 120px; height: 40px; line-height: 40px; color:black;font-size:18px; font-family: Sans-Serif; background-color:#FFEBCD; border-radius: 5px 5px; margin-right:40px;'>{PSNR_YUV}</h6>", unsafe_allow_html=True)
            with container_13:
                st.markdown(f"<h6 style='margin-top: 5px; text-align: center;float:left; margin-left: 40px; width: 210px; height: 40px; line-height: 40px; color:black;font-size:18px; font-family: Sans-Serif; background-color:#FFDEAD; border-radius: 5px 5px;'>  MS-SSIM </h6> <h6 style='margin-top: 5px; text-align: center; float:right;width: 120px; height: 40px; line-height: 40px; color:black;font-size:18px; font-family: Sans-Serif; background-color:#FFEBCD; border-radius: 5px 5px; margin-right:40px;'>{MS_SSIM}</h6>", unsafe_allow_html=True)      

            st.markdown("<h3 style=' margin-top: 40px;'></h3>", unsafe_allow_html=True)
            decoded_img_path = res["Decoded_probe_img_path"]
            decoded_img_path = decoded_img_path.tolist()[0]
            image = Image.open(decoded_img_path.strip('\"'))
            image = image.resize((350, 350))
            st.image(image)


    with col3:

        st.markdown("<h6 style='text-align: center; margin-left: 22px; margin-right: 22px; color: Black; font-size:20px; font-family: Sans-Serif; margin-top: -20px; background-color:#FF5C5C; border-radius: 10px 10px; height: 50px; line-height: 50px; '>Face Verification Explainability Heatmap</h6>", unsafe_allow_html=True)
        
        deci_type = res["Decision Type"]
        deci_type = deci_type.tolist()[0]

        Exception1 = res["Probe-gallery Pair ID"]
        Exception1 = Exception1.tolist()[0]

        Exception2 = res["Face Beautification Tool"]
        Exception2 = Exception2.tolist()[0]

        container_10 = st.container()
        container_11 = st.container()

        if st.session_state['face verification explainability tool'] == "LIBF (JRS)" and st.session_state['probe-gallery pair id'] != '"5"' and  st.session_state['face beautification tool'] != "Relax You Pretty":

            with container_10:
                st.markdown(f"<h6 style='margin-top: 30px; text-align: center;float:left; margin-left: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> Type of Decision </h6><h6 style='margin-top: 30px; text-align: center;float:right; margin-right: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> {deci_type} </h6>", unsafe_allow_html=True)
                    
            st.markdown("<h6 style='margin-left: 20px; margin-right: 20px; margin-top: 5px; background-color:#E0FFFF; border-radius: 10px 10px; height: 90px; outline: 2px solid #AFEEEE;'><p style='margin-top: 8px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Colour coded magnitude of face patch correlations for gallery/probe image in face verification.</p></h6>", unsafe_allow_html=True)
            st.markdown("<h3 style=' margin-top: 90px;'></h3>", unsafe_allow_html=True) #65px
            explai_img_path = res["Similar_region_HM_path"]
            explai_img_path = explai_img_path.tolist()[0]
            image = Image.open(explai_img_path.strip('\"'))
            #image = image.resize((round(image.size[0]*0.5), round(image.size[1]*0.5)))
            image = image.resize((450, 320))
            st.image(image) 

        if st.session_state['face verification explainability tool'] != "LIBF (JRS)" and st.session_state['probe-gallery pair id'] != '"5"' and  st.session_state['face beautification tool'] != "Relax You Pretty":
            
            with container_10:
                
                st.markdown(f"<h6 style='margin-top: 30px; text-align: center;float:left; margin-left: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> Type of Decision </h6><h6 style='margin-top: 30px; text-align: center;float:right; margin-right: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> {deci_type} </h6>", unsafe_allow_html=True)
            
            with container_11:
                
                if deci_type == "True Positive" or deci_type == "False Positive":
                    st.markdown(f"<h6 style='margin-top: 5px; text-align: center;float:left; margin-left: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px; outline: 2px solid #0000FF;'> Similarity Map </h6><h6 style='margin-top: 5px; text-align: center;float:right; margin-right: 30px; width: 180px; height: 40px; line-height: 40px; color:#A9A9A9; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> Dissimilarity Map </h6>", unsafe_allow_html=True)  
                    
                if deci_type == "True Negative" or deci_type == "False Negative":
                    st.markdown(f"<h6 style='margin-top: 5px; text-align: center;float:left; margin-left: 30px; width: 180px; height: 40px; line-height: 40px; color:#A9A9A9; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> Similarity Map </h6><h6 style='margin-top: 5px; text-align: center;float:right; margin-right: 30px; width: 180px; height: 40px; line-height: 40px; color:Black;font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px; outline: 2px solid #0000FF;'> Dissimilarity Map </h6>", unsafe_allow_html=True)  
                    
            st.markdown("<h6 style='margin-left: 20px; margin-right: 20px; margin-top: -5px; background-color:#E0FFFF; border-radius: 10px 10px; height: 80px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Highlights the face regions contributing to the face verification decision.</p></h6>", unsafe_allow_html=True)
            st.markdown("<h3 style=' margin-top: 55px;'></h3>", unsafe_allow_html=True)
            explai_img_path = res["Similar_region_HM_path"]
            explai_img_path = explai_img_path.tolist()[0]
            image = Image.open(explai_img_path.strip('\"'))
            image = image.resize((350, 350))
            st.image(image)    

        if st.session_state['face verification explainability tool'] == "LIBF (JRS)" and st.session_state['probe-gallery pair id'] == '"5"' and  st.session_state['face beautification tool'] != "Relax You Pretty":
            
            with container_10:
                st.markdown(f"<h6 style='margin-top: 30px; text-align: center;float:left; margin-left: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> Type of Decision </h6><h6 style='margin-top: 30px; text-align: center;float:right; margin-right: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> {deci_type} </h6>", unsafe_allow_html=True)
                    
            st.markdown("<h6 style='margin-left: 20px; margin-right: 20px; margin-top: 5px; background-color:#E0FFFF; border-radius: 10px 10px; height: 90px; outline: 2px solid #AFEEEE;'><p style='margin-top: 8px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Colour coded magnitude of face patch correlations for gallery/probe image in face verification.</p></h6>", unsafe_allow_html=True)
            st.markdown("<h3 style=' margin-top: 90px;'></h3>", unsafe_allow_html=True) #65px
            explai_img_path = res["Similar_region_HM_path"]
            explai_img_path = explai_img_path.tolist()[0]
            image = Image.open(explai_img_path.strip('\"'))
            #image = image.resize((round(image.size[0]*0.5), round(image.size[1]*0.5)))
            image = image.resize((450, 320))
            st.image(image) 

        if st.session_state['face verification explainability tool'] != "LIBF (JRS)" and st.session_state['probe-gallery pair id'] == '"5"' and  st.session_state['face beautification tool'] != "Relax You Pretty":
            
            with container_10:
                
                st.markdown(f"<h6 style='margin-top: 30px; text-align: center;float:left; margin-left: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> Type of Decision </h6><h6 style='margin-top: 30px; text-align: center;float:right; margin-right: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> {deci_type} </h6>", unsafe_allow_html=True)
            
            with container_11:
                
                if deci_type == "True Positive" or deci_type == "False Positive":
                    st.markdown(f"<h6 style='margin-top: 5px; text-align: center;float:left; margin-left: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px; outline: 2px solid #0000FF;'> Similarity Map </h6><h6 style='margin-top: 5px; text-align: center;float:right; margin-right: 30px; width: 180px; height: 40px; line-height: 40px; color:#A9A9A9; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> Dissimilarity Map </h6>", unsafe_allow_html=True)  
                    
                if deci_type == "True Negative" or deci_type == "False Negative":
                    st.markdown(f"<h6 style='margin-top: 5px; text-align: center;float:left; margin-left: 30px; width: 180px; height: 40px; line-height: 40px; color:#A9A9A9; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> Similarity Map </h6><h6 style='margin-top: 5px; text-align: center;float:right; margin-right: 30px; width: 180px; height: 40px; line-height: 40px; color:Black;font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px; outline: 2px solid #0000FF;'> Dissimilarity Map </h6>", unsafe_allow_html=True)  
                    
            st.markdown("<h6 style='margin-left: 20px; margin-right: 20px; margin-top: -5px; background-color:#E0FFFF; border-radius: 10px 10px; height: 80px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Highlights the face regions contributing to the face verification decision.</p></h6>", unsafe_allow_html=True)
            st.markdown("<h3 style=' margin-top: 55px;'></h3>", unsafe_allow_html=True)
            explai_img_path = res["Similar_region_HM_path"]
            explai_img_path = explai_img_path.tolist()[0]
            image = Image.open(explai_img_path.strip('\"'))
            image = image.resize((350, 350))
            st.image(image) 
    
        if st.session_state['face verification explainability tool'] == "LIBF (JRS)" and st.session_state['probe-gallery pair id'] != '"5"' and  st.session_state['face beautification tool'] == "Relax You Pretty":
            
            with container_10:
                st.markdown(f"<h6 style='margin-top: 30px; text-align: center;float:left; margin-left: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> Type of Decision </h6><h6 style='margin-top: 30px; text-align: center;float:right; margin-right: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> {deci_type} </h6>", unsafe_allow_html=True)
                    
            st.markdown("<h6 style='margin-left: 20px; margin-right: 20px; margin-top: 5px; background-color:#E0FFFF; border-radius: 10px 10px; height: 90px; outline: 2px solid #AFEEEE;'><p style='margin-top: 8px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Colour coded magnitude of face patch correlations for gallery/probe image in face verification.</p></h6>", unsafe_allow_html=True)
            st.markdown("<h3 style=' margin-top: 90px;'></h3>", unsafe_allow_html=True) #65px
            explai_img_path = res["Similar_region_HM_path"]
            explai_img_path = explai_img_path.tolist()[0]
            image = Image.open(explai_img_path.strip('\"'))
            #image = image.resize((round(image.size[0]*0.5), round(image.size[1]*0.5)))
            image = image.resize((450, 320))
            st.image(image) 

        if st.session_state['face verification explainability tool'] != "LIBF (JRS)" and st.session_state['probe-gallery pair id'] != '"5"' and  st.session_state['face beautification tool'] == "Relax You Pretty":
            
            with container_10:
                
                st.markdown(f"<h6 style='margin-top: 30px; text-align: center;float:left; margin-left: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> Type of Decision </h6><h6 style='margin-top: 30px; text-align: center;float:right; margin-right: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> {deci_type} </h6>", unsafe_allow_html=True)
            
            with container_11:
                
                if deci_type == "True Positive" or deci_type == "False Positive":
                    st.markdown(f"<h6 style='margin-top: 5px; text-align: center;float:left; margin-left: 30px; width: 180px; height: 40px; line-height: 40px; color:Black; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px; outline: 2px solid #0000FF;'> Similarity Map </h6><h6 style='margin-top: 5px; text-align: center;float:right; margin-right: 30px; width: 180px; height: 40px; line-height: 40px; color:#A9A9A9; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> Dissimilarity Map </h6>", unsafe_allow_html=True)  
                    
                if deci_type == "True Negative" or deci_type == "False Negative":
                    st.markdown(f"<h6 style='margin-top: 5px; text-align: center;float:left; margin-left: 30px; width: 180px; height: 40px; line-height: 40px; color:#A9A9A9; font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px;'> Similarity Map </h6><h6 style='margin-top: 5px; text-align: center;float:right; margin-right: 30px; width: 180px; height: 40px; line-height: 40px; color:Black;font-size:18px; font-family: Sans-Serif; background-color:#87CEFA; border-radius: 5px 5px; outline: 2px solid #0000FF;'> Dissimilarity Map </h6>", unsafe_allow_html=True)  
                    
            st.markdown("<h6 style='margin-left: 20px; margin-right: 20px; margin-top: -5px; background-color:#E0FFFF; border-radius: 10px 10px; height: 80px; outline: 2px solid #AFEEEE;'><p style='margin-top: 10px; text-align: justify;margin-left: 15px; margin-right: 15px; font-size:21px; color: Black;'>Highlights the face regions contributing to the face verification decision.</p></h6>", unsafe_allow_html=True)
            st.markdown("<h3 style=' margin-top: 55px;'></h3>", unsafe_allow_html=True)
            explai_img_path = res["Similar_region_HM_path"]
            explai_img_path = explai_img_path.tolist()[0]
            image = Image.open(explai_img_path.strip('\"'))
            image = image.resize((350, 350))
            st.image(image)
      
        if st.session_state['probe-gallery pair id'] == '"5"' and  st.session_state['face beautification tool'] == "Relax You Pretty":
            st.markdown("<h5 style='text-align: center; color: Black; font-size:24px; margin-top: 220px; '> Explainability heatmap is not generated due to face verification failure</h5>", unsafe_allow_html=True)
            #st.markdown("<h5 style='text-align: center; color: Black; font-size:24px; margin-top: 5px; '>😔</h5>", unsafe_allow_html=True)
