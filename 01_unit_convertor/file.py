import streamlit as st 

def unit_conversion(value, unit_from , unit_to):
    
    conversions = {
        "metre_kilometre": 0.001,
        "kilometre_metre": 1000,

        "metre_centimetre": 100,
        "centimetre_metre": 0.01,

        "metre_yard": 1.09361,
        "yard_metre": 0.9144,

        "metre_foot": 3.28084,
        "foot_metre": 0.3048,

        "metre_inch": 39.3701,
        "inch_metre": 0.0254,

        "metre_mile": 0.000621371,
        "mile_metre": 1609.34,

        "metre_nauticalmile": 0.000539957,
        "nauticalmile_metre": 1852,

        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
        "inch_foot": 1 / 12,        
        "foot_inch": 12,

        "yard_foot": 3,             
        "foot_yard": 1 / 3,

        "nauticalmile_mile": 1.15078,      
        "mile_nauticalmile": 1 / 1.15078,

        "kilometre_nauticalmile": 0.539957,
        "nauticalmile_kilometre": 1.852
         
      }
    key = f"{unit_from}_{unit_to}"
      
    if key in conversions:
          converion = conversions[key]
          return value * converion
    else:
          return 'Invalid Conversion'
st.title('Unit Converter')
value = st.number_input('Enter a Value to Convert', min_value=0.0)
unit_from = st.selectbox('Convert From', ["metre", "kilometre", "gram", "kilogram","centimetre", "foot", "inch", "mile", "nauticalmile", "yard"])
unit_to = st.selectbox("Convert To", ["metre", "kilometre", "gram", "kilogram","centimetre", "foot", "inch", "mile", "nauticalmile", "yard"])

if st.button("Convert"):
    result = unit_conversion(value, unit_from , unit_to)
    st.success(f"Converted Value {result}")