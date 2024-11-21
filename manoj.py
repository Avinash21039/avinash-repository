import streamlit as st
def output(vth, rth, rl):
    il = vth / (rth + rl)  
    pl = il * il * rl  
    return il, pl
def thevenins_theorem():
    st.title("Thevenin's Theorem 1039")
    col1, col2 = st.columns(2)
    with col1:
        vth = st.number_input("Vth (V)", value=10)
        rth = st.number_input("Rth (Ohms)", value=100)
        rl = st.number_input("Rl (Ohms)", value=100)
        compute = st.button("Compute")
    with col2:
        if compute:
            il, pl = output(vth, rth, rl)
            st.write(f"Load Current = {il:.2f} A")
            st.write(f"Load Power = {pl:.2f} Watts")
def another_page():
    st.title("Another Page")
    st.write("This is another page where you can add more content, explanations, or topics.")
def home():
    st.write("This is the home page")
    st.title("Streamlit Workshop - SRU")
    page = st.sidebar.radio("Select a page", ("Theorems", "Circuits"))
    if page == "Theorems":
        st.write("You selected Thevenin's Theorem")
        thevenins_theorem() 
    elif page == "Circuits":
        st.write("You selected Another Page")
        another_page() 

if __name__ == "__main__":
    home()
