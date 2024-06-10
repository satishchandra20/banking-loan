import streamlit as st
st.title('BANK LOAN')
a=st.text_input('Enter the type of loan')
st.write("Welcome to Bank Loan Prediction!")
account_no = st.text_input('Account number')
fn = st.text_input('Full Name')
emp_display = ('Job', 'Business')
# Applicant Monthly Income
mon_income = st.number_input("Applicant's Monthly Income", 25000)
# Loan Amount
loan_amt = st.number_input("Loan Amount", 500000)
# Loan Duration
dur = st.selectbox("Loan Duration", "123456")
loan_rate = st.number_input("rate of loan")
if mon_income>=30000:
    st.write("provide a loan in 10%")
else:
    st.write("provide a loan in 15%")
if dur == 0:
    st.error(f"Hello:  Account number: {account_no}  "
                "According to our calculations, you will not get the loan from the bank.")

else:
    st.success(f"Hello:  Account number: {account_no}  "
                "Congratulations! You will get the loan from the bank.")