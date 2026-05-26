import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E2F3EA;

        background-image:
            linear-gradient(to right, rgba(46, 204, 113, 0.22) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(46, 204, 113, 0.22) 1px, transparent 1px);

        background-size: 38px 38px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("محاسبه مساحت چندضلعی های شبکه ای توسط فرمول پيک")
st.subheader(" آذین احمدی")

st.write("فرمول: S = I + B/2 - 1")

# INPUTS
I = st.number_input("تعداد نقاط داخلی (I)", min_value=0, step=1)
B = st.number_input("تعداد نقاط مرزی (B)", min_value=0, step=1)

# CALC
if st.button("محاسبه مساحت"):
    S = I + (B / 2) - 1

    st.success(f"مساحت چندضلعی: {S}")

    st.markdown("### توضیح")
    st.write("طبق قضیه پیک، مساحت از ترکیب نقاط داخلی و مرزی محاسبه می‌شود.")

st.markdown("---")
st.caption("Azin Ahmadi - 102")
