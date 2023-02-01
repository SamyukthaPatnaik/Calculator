import streamlit as st
import pandas as pd
from datetime import datetime, date
import dateutil.utils
from streamlit_option_menu import option_menu
from forex_python.converter import CurrencyRates

def calculator():
    st.title("Arithmetic Calculator")
    st.write("-----") #seperator

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
    # st.title("Age Calculator")
    # birth_date = st.date_input("Enter your birthdate")
    # today = dateutil.utils.today()
    # age = today.year - birth_date.year - ((today.month, today.day)<(birth_date.month, birth_date.day))
    #
    # st.subheader("Age -")
    # st.success(age)
    def calculate_age(born):
        today = date.today ()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def exact_age(born):
        today = datetime.now ()
        years_diff = today.year - born.year
        months_diff = today.month - born.month
        days_diff = today.day - born.day
        if days_diff < 0:
            months_diff -= 1
        if months_diff < 0:
            months_diff += 12
            years_diff -= 1
        return years_diff, months_diff, days_diff

    def main():
        st.title ( "Age Calculator" )
        born = st.date_input ( "Enter your birthdate (YYYY-MM-DD):" )
        if st.button ( "Calculate" ):
            age_years = calculate_age ( born )
            exact_age_years, exact_age_months, exact_age_days = exact_age ( born )
            st.write ( f"You are {age_years} years, {exact_age_months} months, and {exact_age_days} days old" )

    if __name__ == '__main__':
        main ()

def loan():
    st.title("Loan Calculator")
    amount = st.number_input ( "Loan Amount" )
    rate = st.number_input ( "Interest Rate (%)" )
    years = st.number_input ( "Loan Term (years)" )
    r = rate / 100 / 12
    n = years * 12
    payment = (r * amount) / (1 - ((1 + r) ** (-n)))
    st.write ( "Monthly EMI: ", payment )
    # interest = (amount * rate * years) / 100
    # total = interest * rate
    # st.write("Total Interest Amount ", total)

def currency():
    st.title("Currency Calculator")
    c = CurrencyRates()
    amount = st.number_input( "Enter the amount: " )
    currency = pd.read_excel('Currency_Data.xls')
    # currency_name = currency['Currency Name']
    # currency_symbol = currency['Currency Symbol']
    currency_code = currency['ISO code']
    currency_from = st.selectbox( "Enter or select the currency code to convert from: ", currency_code)
    currency_to = st.selectbox ( "Enter or select the currency code to convert to: ", currency_code )
    if st.button ( "Convert" ):
        result = c.convert ( currency_from, currency_to, float ( amount ) )
        st.write ( "Result: ", result )

#----------------------------------------------------

st.sidebar.title("CALCULATOR")
with st.sidebar:
    choice = option_menu(menu_title="Menu",
                         options=["Arithmetic Calculator", "Discount Calculator", "Age Calculator", "Loan Calculator", "Currency Calculator"],
                         icons=["calculator", "tag", "calendar2", "coin", "arrow-left-right"],
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
elif choice == "Currency Calculator":
    currency()
