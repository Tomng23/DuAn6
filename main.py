import streamlit as st
import time

st.title('my_progress')
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1)

if st.button('Click ME!'):
    st.balloons()
