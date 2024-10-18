import streamlit as st

st.write("Hello World")
st.title("welcome to the jungle ")
animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'

number = st.slider('pick a number',0,100)
if st.button("Say hello"):
    st.write("whey hello there")
genre = st.radio(
    "whar is your favorite move genre",
("comedy","Drama","Documentary"))
option = st.selectbox(
    'how would you like to be contaced',
('Email','Home phone','Mobile phone'))
option1 = st.sidebar.selectbox(
    'How would you like to be contaced',
("Email",'Hone Phone','Mobile phone'))
st.text_input("Enter you whatsapp number")
uploaded_file = st.sidebar.file_uploader("choose a csv file",type="csv")

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

if st.session_state.button:
    # The message and nested widget will remain on the page
    st.write('Button is on!')
    st.slider('Select a value')
else:
    st.write('Button is off!')
import streamlit as st

# Adding custom CSS for background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ADD8E6;  /* Light blue background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Your app content
st.title("Change Background Color in Streamlit")
st.write("The background color has been changed to light blue.")
