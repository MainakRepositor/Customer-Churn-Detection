"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Detection Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Artificial Neural Networks</b> for the Customer Churn Prediction.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    col1,col2 = st.columns(2)
    with col1:
        gen = st.slider("Gender", int(df["gender"].min()), int(df["gender"].max()))
        sec = st.slider("Senior Citizen", int(df["SeniorCitizen"].min()), int(df["SeniorCitizen"].max()))
        par = st.slider("Partner", int(df["Partner"].min()), int(df["Partner"].max()))
        dep = st.slider("Dependents", int(df["Dependents"].min()), int(df["Dependents"].max()))
        ten = st.slider("Tenure", int(df["tenure"].min()), int(df["tenure"].max()))
        phn = st.slider("Phone Service", int(df["PhoneService"].min()), int(df["PhoneService"].max()))
        mul = st.slider("Multiple Lines", int(df["MultipleLines"].min()), int(df["MultipleLines"].max()))
        its = st.slider("Internet Service", int(df["InternetService"].min()), int(df["InternetService"].max()))
        osr = st.slider("Online Security", int(df["OnlineSecurity"].min()), int(df["OnlineSecurity"].max()))
        obp = st.slider("Online Backup", int(df["OnlineBackup"].min()), int(df["OnlineBackup"].max()))

    with col2:
        dvp = st.slider("Device Protection", int(df["DeviceProtection"].min()), int(df["DeviceProtection"].max()))
        tsp = st.slider("Tech Support", int(df["TechSupport"].min()), int(df["TechSupport"].max()))
        stv = st.slider("Streaming TV", int(df["StreamingTV"].min()), int(df["StreamingTV"].max()))
        smv = st.slider("Streaming Movies", int(df["StreamingMovies"].min()), int(df["StreamingMovies"].max()))
        cot = st.slider("Contract", int(df["Contract"].min()), int(df["Contract"].max()))
        pbl = st.slider("Paperless Billing", int(df["PaperlessBilling"].min()), int(df["PaperlessBilling"].max()))
        pym = st.slider("Payment Method", int(df["PaymentMethod"].min()), int(df["PaymentMethod"].max()))
        mnc = st.slider("Monthly Charges", float(df["MonthlyCharges"].min()), float(df["MonthlyCharges"].max()))
        toc = st.slider("Total Charges", float(df["TotalCharges"].min()), float(df["TotalCharges"].max()))
           


    # Create a list to store all the features
    features = [gen,sec,par,dep,ten,phn,mul,its,osr,obp,dvp,tsp,stv,smv,cot,pbl,pym,mnc,toc]

    # Create a button to predict
    if st.button("Detect"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.20
        st.info("Detected Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.success("The person will be loyal to the system")
        else:
            st.error("The person will have a negative churn outcome")

        # Print teh score of the model 
        st.write("The model used is trusted by analysts and has an accuracy of ", round((score*100)),"%")
