import streamlit as st
import math
def Resonance(R, L, C):
    FR = 1 / (2 * math.pi * math.sqrt(L * C))
    BW = R / (2 * math.pi * L)
    Q = FR / BW  
    FL = FR - (BW / 2)
    FU = FR + (BW / 2)
    return FR, BW, Q, FL, FU
st.title("2205a21039-PS3")
st.header("Enter Circuit Parameters")
R = st.number_input("Resistance (R) in Ohms", min_value=0.01, step=1.0, format="%.2f")
L = st.number_input("Inductance (L) in Henry", min_value=0.000001, step=0.000001, format="%.6f")
C = st.number_input("Capacitance (C) in Farads", min_value=0.00000001, step=0.00000001, format="%.8f")
if st.button("Compute"):
    if R > 0 and L > 0 and C > 0:
        FR, BW, Q, FL, FU = Resonance(R, L, C)

        st.header("Results")
        st.write(f"**Resonance Frequency (FR):** {FR:.2f} Hz")
        st.write(f"**Bandwidth (BW):** {BW:.2f} Hz")
        st.write(f"**Quality Factor (Q):** {Q:.2f}")
        st.write(f"**Lower Cutoff Frequency (FL):** {FL:.2f} Hz")
        st.write(f"**Upper Cutoff Frequency (FU):** {FU:.2f} Hz")
    else:
        st.warning("Please enter positive values for R, L, and C.")
