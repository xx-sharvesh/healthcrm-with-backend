import streamlit as st
import pandas as pd
import os

# Function to check if the user exists in the Excel file
def check_user(username, password, df):
    user_row = df[(df['Username'] == username) & (df['Password'].str.strip() == password.strip())]
    if user_row.empty:
        return False
    else:
        return True

# Function to create a new Excel file if it doesn't exist
def create_excel():
    if not os.path.exists('credentials.xlsx'):
        df = pd.DataFrame(columns=['Name', 'Username', 'Password', 'Age', 'Phone No.', 'Email', 'Height', 'Weight', 'Blood Pressure', 'Vaccine', 'Allergies', 'Medication History', 'Surgeries', 'Appointment'])
        df.to_excel('credentials.xlsx', index=False)

# Function to sign up new users
def sign_up(name, username, password, df):
    new_user = pd.DataFrame({'Name': [name], 'Username': [username], 'Password': [password]})
    df = df._append(new_user, ignore_index=True)
    df.to_excel('credentials.xlsx', index=False)

# Function to load existing user credentials from Excel
def load_credentials():
    create_excel()
    return pd.read_excel('credentials.xlsx')

# Function to update health record
def update_health_record(username, df, health_record):
    user_index = df.index[df['Username'] == username].tolist()
    if user_index:
        user_index = user_index[0]
        df.at[user_index, 'Age'] = health_record['Age']
        df.at[user_index, 'Phone No.'] = health_record['Phone No.']
        df.at[user_index, 'Email'] = health_record['Email']
        df.at[user_index, 'Height'] = health_record['Height']
        df.at[user_index, 'Weight'] = health_record['Weight']
        df.at[user_index, 'Blood Pressure'] = health_record['Blood Pressure']
        df.at[user_index, 'Vaccine'] = health_record['Vaccine']
        df.at[user_index, 'Allergies'] = health_record['Allergies']
        df.at[user_index, 'Medication History'] = health_record['Medication History']
        df.at[user_index, 'Surgeries'] = health_record['Surgeries']
        
        df.to_excel('credentials.xlsx', index=False)
        return True
    else:
        return False


# Function to book appointments
def book_appointment(username, df, day, date, reason):
    appointment_info = f"{day}: {date}, Reason: {reason}"
    user_index = df.index[df['Username'] == username].tolist()
    if user_index:
        user_index = user_index[0]
        df.loc[user_index, 'Appointment'] = appointment_info
        df.to_excel('credentials.xlsx', index=False)
        return True
    else:
        return False

# Main function for login page
def login_page():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        df = load_credentials()
        if check_user(username, password, df):
            st.success(f"Hi, {username}!")
            return username
        else:
            st.error("Invalid username or password.")
            return None

# Main function for sign up page
def sign_up_page():
    st.subheader("Sign Up")
    name = st.text_input("Full Name")
    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")
    if st.button("Sign Up"):
        df = load_credentials()
        if username in df['Username'].values:
            st.error("Username already exists. Please choose a different one.")
        else:
            sign_up(name, username, password, df)
            st.success("You have successfully signed up! Please login.")

def health_record_page(username):
    st.subheader(f"Health Record & Appointments for {username}")

    df = load_credentials()
    user_index = df.index[df['Username'] == username].tolist()
    if user_index:
        user_index = user_index[0]
        
        # Check if 'Age' column exists in DataFrame
        if 'Age' in df.columns:
            age = st.text_input("Age", df.loc[user_index, 'Age'], key=f"age_input_{username}")
        else:
            age = st.text_input("Age", key=f"age_input_{username}")

        # Check if 'Phone No.' column exists in DataFrame
        if 'Phone No.' in df.columns:
            phone = st.text_input("Phone No.", df.loc[user_index, 'Phone No.'], key=f"phone_input_{username}")
        else:
            phone = st.text_input("Phone No.", key=f"phone_input_{username}")

        # Check if 'Email' column exists in DataFrame
        if 'Email' in df.columns:
            email = st.text_input("Email", df.loc[user_index, 'Email'], key=f"email_input_{username}")
        else:
            email = st.text_input("Email", key=f"email_input_{username}")

        # Check if 'Height' column exists in DataFrame
        if 'Height' in df.columns:
            height = st.text_input("Height", df.loc[user_index, 'Height'], key=f"height_input_{username}")
        else:
            height = st.text_input("Height", key=f"height_input_{username}")

        # Check if 'Weight' column exists in DataFrame
        if 'Weight' in df.columns:
            weight = st.text_input("Weight", df.loc[user_index, 'Weight'], key=f"weight_input_{username}")
        else:
            weight = st.text_input("Weight", key=f"weight_input_{username}")

        # Check if 'Blood Pressure' column exists in DataFrame
        if 'Blood Pressure' in df.columns:
            bp = st.text_input("Blood Pressure", df.loc[user_index, 'Blood Pressure'], key=f"bp_input_{username}")
        else:
            bp = st.text_input("Blood Pressure", key=f"bp_input_{username}")

        # Check if 'Vaccine' column exists in DataFrame
        if 'Vaccine' in df.columns:
            vaccine = st.text_input("Vaccine", df.loc[user_index, 'Vaccine'], key=f"vaccine_input_{username}")
        else:
            vaccine = st.text_input("Vaccine", key=f"vaccine_input_{username}")

        # Check if 'Allergies' column exists in DataFrame
        if 'Allergies' in df.columns:
            allergies = st.text_input("Allergies", df.loc[user_index, 'Allergies'], key=f"allergies_input_{username}")
        else:
            allergies = st.text_input("Allergies", key=f"allergies_input_{username}")

        # Check if 'Medication History' column exists in DataFrame
        if 'Medication History' in df.columns:
            medication = st.text_input("Medication History", df.loc[user_index, 'Medication History'], key=f"medication_input_{username}")
        else:
            medication = st.text_input("Medication History", key=f"medication_input_{username}")

        # Check if 'Surgeries' column exists in DataFrame
        if 'Surgeries' in df.columns:
            surgeries = st.text_input("Surgeries", df.loc[user_index, 'Surgeries'], key=f"surgeries_input_{username}")
        else:
            surgeries = st.text_input("Surgeries", key=f"surgeries_input_{username}")
        
        st.subheader("Appointments")
        day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], key=f"day_select_{username}")
        date = st.date_input("Date", key=f"date_input_{username}")
        time = st.time_input("Time", key=f"time_input_{username}")
        reason = st.text_input("Reason", key=f"reason_input_{username}")
        
        if st.button("Book Appointment", key=f"book_button_{username}"):
            appointment_info = f"{day}: {date}, {time}, Reason: {reason}"
            df.at[user_index, 'Appointment'] = appointment_info
            df.to_excel('credentials.xlsx', index=False)
            st.success("Your appointment has been scheduled at " + str(date) + ", " + str(time) + ".")
            
        if st.button("Save", key=f"save_button_{username}"):
            df.loc[user_index, 'Age'] = age
            df.loc[user_index, 'Phone No.'] = phone
            df.loc[user_index, 'Email'] = email
            df.loc[user_index, 'Height'] = height
            df.loc[user_index, 'Weight'] = weight
            df.loc[user_index, 'Blood Pressure'] = bp
            df.loc[user_index, 'Vaccine'] = vaccine
            df.loc[user_index, 'Allergies'] = allergies
            df.loc[user_index, 'Medication History'] = medication
            df.loc[user_index, 'Surgeries'] = surgeries

            df.to_excel('credentials.xlsx', index=False)
            st.success("Your details have been updated successfully!")
    else:
        st.error("User not found.")


# Main function
def main():
    st.title("Health Care Records App")

    choice = st.sidebar.radio("Navigation", ("Login", "Sign Up"), key="nav_choice")

    if choice == "Login":
        username = login_page()
        if username:
            st.sidebar.success("You are logged in!")
            st.sidebar.radio("Navigation", ("Health Record",), key="login_nav")
            health_record_page(username)
    elif choice == "Sign Up":
        sign_up_page()

if __name__ == "__main__":
    main()
