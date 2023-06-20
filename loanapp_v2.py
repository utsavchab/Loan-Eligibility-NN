import pandas as pd
import streamlit as st
import pickle
pickle_in = open('classifier.pkl', 'rb') 
model = pickle.load(pickle_in)
def main():
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Check your Loan Eligibility</h1> 
    </div> 
    """
    st.markdown(html_temp, unsafe_allow_html = True) 
    
    Gender = st.selectbox('Gender',("Male","Female","Other"))
    Married = st.selectbox('Marital Status',("Unmarried","Married","Other")) 
    ApplicantIncome = st.number_input("Monthly Income in Rupees") 
    LoanAmount = st.number_input("Loan Amount in Rupees")
    result =""
    
    if st.button("Check"): 
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount) 
    st.success('Your loan is {}'.format(result))
    
def prediction(Gender, Married, ApplicantIncome, LoanAmount):
    # ApplicantIncome = (ApplicantIncome - aIncome_min)/(aIncome_max)
    # LoanAmount  = (LoanAmount - loanAmount_min)/ (loanAmount_max)
    
    X = [Gender,Married,ApplicantIncome, LoanAmount]
    X = pd.DataFrame(X)
    y_pred = model.fit(X)
    if(y_pred):
        pred = "Approved"
        return pred
    else:
        pred = "Not Approved"
        return pred
    
if __name__=='__main__': 
    main()
        
        
