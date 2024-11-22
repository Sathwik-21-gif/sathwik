import streamlit as st

# Define the STAR_DELTA function
def STAR_DELTA(R1, R2, R3):
    denominator = R1 * R2 + R2 * R3 + R3 * R1
    R12 = denominator / R3
    R23 = denominator / R1
    R31 = denominator / R2
    return R12, R23, R31

# Streamlit Application
st.title("02341A0259-PS2")

st.header("Calculate Delta Connection Resistances (R12, R23, R31)")

# Input fields for STAR resistances
R1 = st.number_input("Enter Resistance R1 (Ω):", min_value=0.0, format="%.2f")
R2 = st.number_input("Enter Resistance R2 (Ω):", min_value=0.0, format="%.2f")
R3 = st.number_input("Enter Resistance R3 (Ω):", min_value=0.0, format="%.2f")

# Button to trigger calculation
if st.button("Calculate"):
    # Validate inputs
    if R1 > 0 and R2 > 0 and R3 > 0:
        R12, R23, R31 = STAR_DELTA(R1, R2, R3)
        # Convert the results to ohms (Ω)
        R12_kilo = R12 / 1000
        R23_kilo = R23 / 1000
        R31_kilo = R31 / 1000
        
        st.success(f"Calculated Resistances in kilo-ohms:\nR12 = {R12_kilo:.3f} kΩ\nR23 = {R23_kilo:.3f} kΩ\nR31 = {R31_kilo:.3f} kΩ")
    else:
        st.error("Please enter positive values for R1, R2, and R3.")
