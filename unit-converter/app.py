import streamlit as st

# Custom Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #F8E8EE; /* Soft pastel pink background */
        color: #5D5A6D;
    }
    div[data-testid="stWidgetLabel"] {
        font-weight: bold;
        font-size: 18px;
        color: #A88F8F; /* Muted pastel brown */
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #A3D8F4, #FFB6C1); /* Pastel blue to pink */
        color: white;
        font-size: 16px;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 12px;
        cursor: pointer;
        box-shadow: 2px 2px 10px rgba(163, 216, 244, 0.4);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #FFB6C1, #A3D8F4);
    }
    .result-box {
        background-color: #C1E1C1; /* Soft pastel green */
        color: #5D5A6D;
        font-size: 20px;
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Conversion Functions
def convert_length(value, from_unit, to_unit):
    units = {"Kilometers": 1.0, "Meters": 1000.0, "Miles": 0.621371, "Feet": 3280.84}
    return value * (units[to_unit] / units[from_unit]) if from_unit != to_unit else value

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    return (value * 9/5) + 32 if from_unit == "Celsius" else (value - 32) * 5/9

def convert_weight(value, from_unit, to_unit):
    units = {"Kilograms": 1.0, "Grams": 1000.0, "Pounds": 2.20462, "Ounces": 35.274}
    return value * (units[to_unit] / units[from_unit]) if from_unit != to_unit else value

# App Title
st.markdown("<h1 style='text-align: center; color: #A88F8F;'>⚡ Unit Converter ⚡</h1>", unsafe_allow_html=True)

# Input Fields
col1, col2 = st.columns(2)
with col1:
    conversion_type = st.selectbox("Select Conversion Type:", ["Length", "Temperature", "Weight"])
with col2:
    value = st.number_input("Enter the value:", min_value=0.0, format="%.2f")

# Unit Selection
if conversion_type == "Length":
    from_unit = st.selectbox("From:", ["Kilometers", "Meters", "Miles", "Feet"])
    to_unit = st.selectbox("To:", ["Kilometers", "Meters", "Miles", "Feet"])
elif conversion_type == "Temperature":
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit"])
elif conversion_type == "Weight":
    from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Pounds", "Ounces"])

# Convert Button & Result
if st.button("Convert"):
    result = None
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    
    if result is not None:
        st.markdown(f'<div class="result-box">{value} {from_unit} = {result:.2f} {to_unit}</div>', unsafe_allow_html=True)
