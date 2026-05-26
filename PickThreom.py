import streamlit as st

st.title("محاسبه مساحت چندضلعي هاي شبکه اي توسط فرمول پيک")
st.subheader("ساخته شده توسط آذین احمدي")

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