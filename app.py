import streamlit as st 
import helper

st.title("Restaurant Name And Menu Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine",("Italian", "Japanese", "Mexican", "Indian", "French", "Chinese", "Thai"))


if cuisine:
    response = helper.generateRestaurantNameAndMenu(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    st.write("**MENU ITEMS**")
    i = 1
    for item in menu_items:
        st.write(i,".",item)
        i+=1    