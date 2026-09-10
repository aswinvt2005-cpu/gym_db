import streamlit as st
from gym_db import GymMemberManager

member_instance = GymMemberManager()
tab1,tab2=st.tabs(["ADD","VIEW"])
with tab1:
    st.name = st.text_input("Enter name")
    st.place = st.text_input("Enter place")
    st.mobile = st.text_input("Enter mobile")

    st.plan = st.selectbox(
    "Select your plan",
    ["1 month", "6 month", "1 year"]
    )

    st.fee = st.number_input("Enter fee")

    st.joined_date = st.date_input("Select joining date")


if st.button("Add Member"):
    member_instance.post(
        name=name,
        place=place,
        mobile=mobile,
        plan=plan,
        fee=fee,
        joined_date=joined_date
    )
    st.success("blood donor added successfully")
with tab2:
    st.title("VIEW NEW BLOOD DETAILS")
    records=member_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("no records found!")