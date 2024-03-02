import streamlit as st
import pandas as pd
import random

# Function to load quotes from CSV file
def load_quotes():
    try:
        df = pd.read_csv("quotes.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Quote", "Genre"])
    return df

# Function to save quotes to CSV file
def save_quotes(df):
    df.to_csv("quotes.csv", index=False)

def signup():
    st.title("Signup")
    name = st.text_input("Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        # Here you can save the signup data to your data source
        st.success("Signup Successful!")

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Dummy authentication (no actual authentication)
        if username == "dummyuser" and password == "dummypassword":
            st.success("Login Successful!")
            return True
        else:
            st.error("Invalid Username or Password")
            return False

def add_quote(df):
    st.title("Add or Show Quotes")
    quote = st.text_area("Enter Quote")
    genre = st.selectbox("Select Genre", ["Literature", "Philosophy", "Funny", "Motivational", "Happy", "Humour", "Self-Improvement"])
    if st.button("Submit"):
        # Create a DataFrame if df is None or not a pandas DataFrame
        if df is None or not isinstance(df, pd.DataFrame):
            df = pd.DataFrame(columns=["Quote", "Genre"])
        # Create a new row for the DataFrame
        new_row = {"Quote": quote, "Genre": genre}
        # Append the new row to the DataFrame
        df = df.append(new_row, ignore_index=True)
        # Save the DataFrame to CSV
        save_quotes(df)
        st.success("Quote added successfully!")

    if not df.empty:
        st.title("All Quotes")
        st.write("Quotes and their genres:")
        st.table(df)
    else:
        st.write("No quotes available.")

def main():
    st.title("QuizQuest")
    df = load_quotes()

    page = st.sidebar.radio("Navigation", ["Login", "Signup", "Add or Show Quotes", "Random Quote"])

    if page == "Login":
        if login():
            pass  # Redirect to other pages after successful login

    elif page == "Signup":
        signup()

    elif page == "Add or Show Quotes":
        add_quote(df)

    elif page == "Random Quote":
        st.title("Random Quote Generator")
        selected_genre = st.selectbox("Select Genre", ["Select the genre"] + df['Genre'].unique().tolist())
        if selected_genre != "Select the genre":
            if st.button("Hit me a quote"):
                genre_df = df[df['Genre'] == selected_genre]
                if not genre_df.empty:
                    random_quote = genre_df.sample(n=1)['Quote'].values[0]
                    st.header("Random Quote")
                    st.subheader(random_quote)
                else:
                    st.warning("No quotes available for selected genre.")

if __name__ == "__main__":
    main()
