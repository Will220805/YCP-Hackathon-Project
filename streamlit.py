import streamlit as st
import Person as p
import Scenario as s
import scenarioLib as lib

st.write('hello world!')

a = st.button("Choice 1")
b = st.button("Choice 2")
c = st.button("Choice 3")

if a:
    st.write("Choice 1 chosen")
if b:
    st.write("Choice 2")
if c:
    st.write("Choice 3")
