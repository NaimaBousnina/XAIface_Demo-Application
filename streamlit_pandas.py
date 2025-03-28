import streamlit as st
import pandas as pd
from PIL import Image

def filter_string(df, column, selected_list):
    final = []
    df = df[df[column].notna()]
    for idx, row in df.iterrows():
        if row[column] in selected_list:
            final.append(row)
    res = pd.DataFrame(final)
    return res

def number_widget(df, column, ss_name):
    df = df[df[column].notna()]
    max = float(df[column].max())
    min = float(df[column].min())
    temp_input = st.sidebar.slider(f"{column.title()}", min, max, (min, max), key=ss_name)
    all_widgets.append((ss_name, "number", column))

def number_widget_int(df, column, ss_name):
    df = df[df[column].notna()]
    max = int(df[column].max())
    min = int(df[column].min())
    temp_input = st.sidebar.slider(f"{column.title()}", min, max, (min, max), key=ss_name)
    all_widgets.append((ss_name, "number", column))

def create_select(df, column, ss_name, multi=False, on_change_=None):
    df = df[df[column].notna()]
    options = df[column].unique()
    #options.sort()
    if multi==False:
        temp_input = st.sidebar.selectbox(f"**{column}:**", options, index=0, key=ss_name, on_change=on_change_)
        all_widgets.append((ss_name, "select", column))
    else:
        temp_input = st.sidebar.multiselect(f"**{column}:**", options, key=ss_name)
        all_widgets.append((ss_name, "multiselect", column))


def text_widget(df, column, ss_name):
    temp_input = st.sidebar.text_input(f"{column.title()}", key=ss_name)
    all_widgets.append((ss_name, "text", column))

def create_widgets(df, create_data={}, ignore_columns=[], on_change=None):
    """
    This function will create all the widgets from your Pandas DataFrame and return them.
    df => a Pandas DataFrame
    create_data => Optional dictionary whose keys are the Pandas DataFrame columns
        and whose values are the type of widget you wish to make.
        supported: - multiselect, select, text
    ignore_columns => columns to entirely ignore when creating the widgets.
    """
    for column in ignore_columns:
        df = df.drop(column, axis=1)
    global all_widgets
    all_widgets = []
    st.sidebar.image("xaiface_logo_PNG.png", width= 200, use_column_width=False)
    
   
    st.sidebar.markdown("<h3 style='margin-bottom: 25px; text-align: center; color: White; margin-left: -25px; margin-right: -25px; font-size:30px; font-family: Sans-Serif; background-color:Black; height: 60px; line-height: 30px; padding: 10px 10px;'>Settings</h3>", unsafe_allow_html=True)
    #st.sidebar.markdown("About")
    for ctype, column in zip(df.dtypes, df.columns):
        if column in create_data:
            if create_data[column] == "text":
                text_widget(df, column, column.lower())
            elif create_data[column] == "select":
                create_select(df, column, column.lower(), multi=False, on_change_=on_change)
            elif create_data[column] == "multiselect":
                create_select(df, column, column.lower(), multi=True, on_change_=on_change)
        else:
            if ctype == "float64":
                number_widget(df, column, column.lower())
            elif ctype == "int64":
                number_widget_int(df, column, column.lower())
            elif ctype == "object":
                if str(type(df[column].tolist()[0])) == "<class 'str'>":
                    text_widget(df, column, column.lower())
    return all_widgets


def filter_df(df, all_widgets):
    """
    This function will take the input dataframe and all the widgets generated from
    Streamlit Pandas. It will then return a filtered DataFrame based on the changes
    to the input widgets.

    df => the original Pandas DataFrame
    all_widgets => the widgets created by the function create_widgets().
    """
    res = df
    for widget in all_widgets:
        ss_name, ctype, column = widget
        data = st.session_state[ss_name]
        if data:
            if ctype == "text":
                if data != "":
                    res = res.loc[res[column].str.contains(data)]
            elif ctype == "select":
                res = filter_string(res, column, data)
            elif ctype == "multiselect":
                res = filter_string(res, column, data)
            elif ctype == "number":
                min, max = data
                res = res.loc[(res[column] >= min) & (res[column] <= max)]
    return res
