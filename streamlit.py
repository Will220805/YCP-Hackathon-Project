import streamlit as st
import Person as p
import Scenario as s
import scenarioLib as lib
import time
import inkle

# Function to display text with a typing effect
def type_text(text, delay=0.1):
    typed_text = ""
    text_placeholder = st.empty()  # Placeholder for updating text

    for char in text:
        typed_text += char
        text_placeholder.markdown(f"**{typed_text}**")  # Update placeholder with each character
        time.sleep(delay)

# Function to display title with a typing effect
def type_title(text, delay=0.1):
    typed_text = ""
    title_placeholder = st.empty()  # Placeholder for updating the title

    for char in text:
        typed_text += char
        title_placeholder.title(typed_text)  # Update placeholder with each character as a title
        time.sleep(delay)


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
    type_title("Welcome to the Matrix!", delay=0.05)
    type_text("Press to start.", delay=0.05)
    if st.button("Start Game"):
        st.session_state.page = 'question_1'
    if st.button("Instructions"):
        st.session_state.page = 'instructions'

# Instructions page
if st.session_state.page == 'instructions':
    st.title("Instructions")
    st.write("You are in an abusive relationship. You have to make the correct choices to break out of it")
    if st.button("Back to Menu"):
        st.session_state.page = 'menu'

if st.session_state.page == 'question_1':
    st.title("Question 1")
    st.write("What's your favorite food?")
    if st.button("sandwich"):
        st.session_state.score += 1
        st.session_state.page = 'question_2.1'
    if st.button("noodles"):
        st.session_state.score += 2
        st.session_state.page = 'question_2.2'

# Question 2
if st.session_state.page == 'question_2.1':
    st.title("Question 2")
    st.write("Do you prefer Banh Mi or Hamburger?")
    if st.button("Banh Mi"):
        st.session_state.score += 1
        st.session_state.page = 'ending'
    if st.button("Hamburger"):
        st.session_state.score += 2
        st.session_state.page = 'ending'

# Question 2
if st.session_state.page == 'question_2.2':
    st.title("Question 3")
    st.write("Do you prefer Ramen or Spaghetti?")
    if st.button("Ramen"):
        st.session_state.score += 1
        st.session_state.page = 'ending'
    if st.button("Spaghetti"):
        st.session_state.score += 2
        st.session_state.page = 'ending'

# Ending page
if st.session_state.page == 'ending':
    st.title("The End")
    st.write(f"Your final score is: {st.session_state.score}")
    if st.button("Play Again"):
        reset_game()