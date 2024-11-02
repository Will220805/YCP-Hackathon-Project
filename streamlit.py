import streamlit as st
import Person as p
import Scenario as s
import scenarioLib as lib


if 'page' not in st.session_state:
    st.session_state.page = 'menu'
if 'score' not in st.session_state:
    st.session_state.score = 0

def go_to_page(page_name):
    st.session_state.page = page_name

def reset_game():
    st.session_state.page = 'menu'
    st.session_state.score = 0

# Menu page
if st.session_state.page == 'menu':
    st.title("Welcome to the Questionnaire Game!")
    st.write("Select an option to start.")
    if st.button("Start Game"):
        go_to_page('question_1')
    if st.button("Instructions"):
        go_to_page('instructions')

# Instructions page
if st.session_state.page == 'instructions':
    st.title("Instructions")
    st.write("You are in a silumation. You have to make the correct choices to escape the simulation")
    if st.button("Back to Menu"):
        go_to_page('menu')

a = st.button("Choice 1")
b = st.button("Choice 2")
c = st.button("Choice 3")

if a:
    st.write("Choice 1 chosen")
if b:
    st.write("Choice 2")
if c:
    st.write("Choice 3")