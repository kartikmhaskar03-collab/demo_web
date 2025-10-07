import streamlit as st 


name = st.text_input("ENTER YOU NAME")
fname = st.text_input("ENTER FATHER'S NAME")
adr = st.text_input("ENTER YOUR TEXT : ")
classdata = st.selectbox("ENTER YOUR CLASS :",(1,2,3,4,5,6,7,8,9,10))

button = st.button("done")
if button :
    st.markdown(f"""
    NAME : {name}
    FATHER NAME : {fname}
    address : {adr}
    class : {classdata}""")
