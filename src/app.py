import streamlit as st
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(BASE_DIR, ".."))
model_path = os.path.join(project_root, "models", "house_price_model_compressed.pkl")
model = joblib.load(model_path)

st.title("🏠 House Price Prediction App")

st.write("Enter the details below to predict the house price:")

bedrooms = st.number_input("1. Number of Bedrooms", min_value=1, value=3, step=1)
bathrooms = st.number_input("2. Number of Bathrooms", min_value=0.0, value=2.5, step=0.5)
floors = st.number_input("3. Number of Floors", min_value=1.0, value=2.0, step=0.5)
living_area = st.number_input("4. Living Area (sqft)", min_value=500, value=2500, step=100)
lot_area = st.number_input("5. Lot Area (sqft)", min_value=1000, value=7500, step=500)
area_excl_basement = st.number_input("6. Area of the house (excluding basement, sqft)", min_value=0, value=2000, step=50)
area_basement = st.number_input("7. Area of the basement (sqft)", min_value=0, value=500, step=50)
living_area_renov = st.number_input("8. Renovated Living Area (sqft)", min_value=0, value=2500, step=100)
lot_area_renov = st.number_input("9. Renovated Lot Area (sqft)", min_value=0, value=7500, step=500)
waterfront_present = st.selectbox("10. Waterfront Present (0=No, 1=Yes)", options=[0, 1], index=0)
number_of_views = st.slider("11. Number of Views (0-4)", min_value=0, max_value=4, value=0, step=1)
condition_house = st.slider("12. Condition of the house (1-5)", min_value=1, max_value=5, value=3, step=1)
grade_house = st.slider("13. Grade of the house (1-13)", min_value=1, max_value=13, value=7, step=1)
built_year = st.number_input("14. Built Year", min_value=1800, max_value=2025, value=1980, step=1)
renovation_year = st.number_input("15. Renovation Year (0 if none)", min_value=0, max_value=2025, value=0, step=1)
postal_code = st.number_input("16. Postal Code", min_value=0, value=98001, step=1)
latitude = st.number_input("17. Lattitude", value=47.6, format="%.4f")
longitude = st.number_input("18. Longitude", value=-122.2, format="%.4f")
num_schools = st.number_input("19. Number of schools nearby", min_value=0, value=2, step=1)
distance_airport = st.number_input("20. Distance from the airport (km)", min_value=0, value=20, step=1)

if st.button("Predict Price"):
    data = pd.DataFrame([{
        "number of bedrooms": bedrooms,
        "number of bathrooms": bathrooms,
        "living area": living_area,
        "lot area": lot_area,
        "number of floors": floors,
        "waterfront present": waterfront_present,
        "number of views": number_of_views,
        "condition of the house": condition_house,
        "grade of the house": grade_house,
        "Area of the house(excluding basement)": area_excl_basement,
        "Area of the basement": area_basement,
        "Built Year": built_year,
        "Renovation Year": renovation_year,
        "Postal Code": postal_code,
        "Lattitude": latitude,
        "Longitude": longitude,
        "living_area_renov": living_area_renov,
        "lot_area_renov": lot_area_renov,
        "Number of schools nearby": num_schools,
        "Distance from the airport": distance_airport
    }])

    prediction = model.predict(data)[0]

    st.success(f"Estimated House Price: ${prediction:,.2f}")