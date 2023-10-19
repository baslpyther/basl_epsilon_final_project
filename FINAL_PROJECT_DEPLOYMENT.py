import streamlit as st
import pandas as pd
import joblib
import sklearn

model = joblib.load("Model.pkl")
inputs = joblib.load("inputs3.pkl")

def prediction(Baths, Beds, Dining_Room, Laundry_Room, Store_Rooms, Kitchens, Drawing_Room, Gym, Powder_Room, Steam_Room, Prayer_Rooms, lounge, additional_rooms, area_squared_meter, Total_Rooms, total_amenity_rooms, total_regular_rooms):
    df = pd.DataFrame(columns=inputs)
    df.at[0, "Baths"] = Baths
    df.at[0, "Beds"] = Beds
    df.at[0, "Dining Room"] = Dining_Room
    df.at[0, "Laundry Room"] = Laundry_Room
    df.at[0, "Store Rooms"] = Store_Rooms
    df.at[0, "Kitchens"] = Kitchens
    df.at[0, "Drawing Room"] = Drawing_Room
    df.at[0, "Gym"] = Gym
    df.at[0, "Powder Room"] = Powder_Room
    df.at[0, "Steam Room"] = Steam_Room
    df.at[0, "Prayer Rooms"] = Prayer_Rooms
    df.at[0, "lounge"] = lounge
    df.at[0, "additional rooms"] = additional_rooms
    df.at[0, "area_squared_meter"] = area_squared_meter
    df.at[0, "Total Rooms"] = Total_Rooms
    df.at[0, "total amenity rooms"] = total_amenity_rooms
    df.at[0, "total regular rooms"] = total_regular_rooms
    result = model.predict(df)
    return result[0]



def main():
    st.title("HOUSE PRICE PREDICTION MODEL")
    Baths = st.slider("Baths",min_value= 1.0, max_value = 10.0 , value = 2.0 , step =1.0)
    Beds = st.slider("Beds",min_value= 1.0, max_value = 25.0 , value = 2.0 , step =1.0)
    Dining_Room = st.slider("Dining Room",min_value= 0, max_value = 1 , value = 0 , step =1)
    Laundry_Room = st.slider("Laundry Room",min_value= 0, max_value = 1 , value = 0 , step =1)
    Store_Rooms = st.slider("Store Rooms",min_value= 0, max_value = 22 , value = 2 , step =1)
    Kitchens = st.slider("Kitchens",min_value= 0.0, max_value = 20.0 , value = 2.0 , step =1.0)
    Drawing_Room = st.slider("Drawing Room",min_value= 0.0, max_value = 1.0 , step =1.0)
    Gym = st.slider("Gym", min_value=0.0, max_value=1.0, step=1.0)
    Powder_Room = st.slider("Powder Room",min_value= 0.0, max_value = 1.0  , step =1.0)
    Steam_Room = st.slider("Steam Room",min_value= 0.0, max_value = 1.0  , step =1.0)
    Prayer_Rooms = st.slider("Prayer Rooms",min_value= 0.0, max_value = 1.0  , step =1.0)
    lounge = st.slider("lounge",min_value= 0.0, max_value = 1.0  , step =1.0)
    additional_rooms = st.slider("additional rooms",min_value= 0.0, max_value = 1.0 , step =1.0)
    area_squared_meter = st.slider("area_squared_meter",min_value= 30.0, max_value = 500.0 , value = 2.0 , step =0.25)
    Total_Rooms = st.slider("Total Rooms",min_value= 2.0, max_value = 37.0 , value = 2.0 , step =1.0)
    total_amenity_rooms = st.slider("Total Amenity Rooms", min_value=0.0, max_value=6.0, step=1.0)
    total_regular_rooms = st.slider("total regular rooms",min_value= 2.0, max_value = 37.0 , value = 2.0 , step =1.0)

    if st.button("predict"):
        result = prediction(Baths, Beds, Dining_Room, Laundry_Room, Store_Rooms, Kitchens, Drawing_Room, Gym, Powder_Room, Steam_Room, Prayer_Rooms, lounge, additional_rooms, area_squared_meter, Total_Rooms, total_amenity_rooms, total_regular_rooms)
        st.text(f"Predicted Price: ${result:,.2f}")
main()
