import dateutil.utils
import streamlit as st
from streamlit_option_menu import option_menu

def calculator():
    st.title("Arithmetic Calculator")
    st.write("-----")

    num1 = st.number_input("Enter First Number: ")
    num2 = st.number_input("Enter Second Number: ")
    operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = num1 / num2
    st.write("Result: ", result)

def discount():
    st.title("Discount Calculator")
    price = st.number_input("Enter Original Price")
    discount_percentage = st.number_input("Enter Discount Percentage")

    discount_calculate = (discount_percentage*price)/100
    discounted_price = (price - discount_calculate)

    st.subheader("Discounted Price -")
    st.success(discounted_price)

    saved = price - discounted_price
    with st.expander ( "Saved" ):
        st.success ( saved )

def age():
    st.title("Age Calculator")
    birth_date = st.date_input("Your Date Of Birth")
    today = dateutil.utils.today()
    age = today.year - birth_date.year - ((today.month, today.day)<(birth_date.month, birth_date.day))
    st.subheader("Age -")
    st.success(age)

def loan():
    st.title("Loan Calculator")

    amount = st.number_input ( "Loan Amount" )
    rate = st.number_input ( "Interest Rate (%)" )
    years = st.number_input ( "Loan Term (years)" )
    r = rate / 100 / 12
    n = years * 12
    payment = (r * amount) / (1 - ((1 + r) ** (-n)))
    st.write ( "Monthly Payment: ", payment )

#----------------------------------------------------

st.sidebar.title("CALCULATOR")
with st.sidebar:
    choice = option_menu(menu_title="Menu",
                         options=["Arithmetic Calculator", "Discount Calculator", "Age Calculator", "Loan Calculator"],
                         icons=["calculator", "tag", "calendar2", "coin"],
                         menu_icon="cast",
                         default_index=0)

if choice == "Arithmetic Calculator":
    calculator()
elif choice == "Discount Calculator":
    discount()
elif choice == "Age Calculator":
    age()
elif choice == "Loan Calculator":
    loan()

