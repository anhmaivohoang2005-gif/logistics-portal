import streamlit as st
import pandas as pd

# Cấu hình trang
st.set_page_config(
    page_title="LogiSpace Sentinel - Quản trị Rủi ro Space & Cước",
    page_icon="",
    layout="wide"
)

# Tiêu đề ứng dụng
st.title(" LogiSpace Sentinel: Smart Booking & Risk Management Dashboard")
st.markdown("Hệ thống hỗ trợ Sales/Ops kiểm soát rủi ro thiếu chỗ (Space), mô phỏng biên lợi nhuận và tối ưu hóa thời điểm chốt booking dựa trên dữ liệu thị trường thực tế.")

st.markdown("---")

# --- PHẦN 1: KHUNG NHẬP LIỆU (SEARCH & INPUT FORM - CHUẨN PHAATA + CASE STUDY) ---
st.header("1. Tra cứu tuyến đường & Khai báo thông tin lô hàng")

with st.form("booking_form"):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        pol = st.selectbox(
            "Nơi đi (POL)", 
            ["Cái Mép (VN)", "Hải Phòng (VN)", "Cát Lái (VN)", "Đà Nẵng (VN)"],
            index=0
        )
    with col2:
        pod = st.selectbox(
            "Nơi đến (POD)", 
            ["Los Angeles (US)", "Long Beach (US)", "New York (US)", "Rotterdam (NL)", "Singapore (SG)"],
            index=0
        )
    with col3:
        carrier = st.selectbox(
            "Hãng tàu (Carrier)", 
            ["Wan Hai", "Maersk", "Evergreen", "MSC", "CMA CGM", "Tất cả các hãng"],
            index=0
        )
    with col4:
        container_type = st.selectbox(
            "Loại container", 
            ["40'HC", "20'DC", "40'GP", "45'HC"],
            index=0
        )

    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        container_qty = st.number_input("Số lượng container", min_value=1, max_value=50, value=5)
    with col6:
        commodity = st.text_input("Mặt hàng / HS Code", value="Wooden kitchen cabinets, HS 940340")
    with col7:
        booking_date = st.date_input("Ngày dự kiến Booking", value=pd.to_datetime("2025-05-30").date())
    with col8:
        target_etd = st.date_input("Ngày dự kiến Xuất tàu (ETD)", value=pd.to_datetime("2025-06-08").date())

    st.markdown("#####  Thông tin Tài chính & Báo giá")
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        buy_rate = st.number_input("Cước mua dự kiến (Buy Rate - USD/cont)", min_value=0.0, value=5230.0, step=10.0)
    with col_f2:
        sell_rate = st.number_input("Cước bán cho khách (Sell Rate - USD/cont)", min_value=0.0, value=5438.0, step=10.0)
    with col_f3:
        other_cost = st.number_input("Chi phí phát sinh dự trù (Lưu bãi, tách lô...) (USD)", min_value=0.0, value=0.0, step=50.0)

    submitted = st.form_submit_button(" Kiểm tra & Phân tích Rủi ro Space", use_container_width=True)

if submitted:
    st.markdown("---")
    st.header("2. Kết quả Phân tích Rủi ro & Bảng điều khiển (Risk Dashboard)")

    # Tính toán tài chính
    total_revenue = sell_rate * container_qty
    total_buy = buy_rate * container_qty
    profit_per_cont = sell_rate - buy_rate
    total_profit_initial = profit_per_cont * container_qty
    margin_pct = (profit_per_cont / sell_rate) * 100 if sell_rate > 0 else 0

    # Hiển thị các chỉ số tổng quan (Metrics)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Lợi nhuận gộp / Cont", f"${profit_per_cont:,.0f}", f"{margin_pct:.2f}% biên LN")
    m2.metric("Tổng lợi nhuận lô hàng", f"${total_profit_initial:,.0f}", f"{container_qty} containers")
    
    # Đánh giá rủi ro tuyến đường và số lượng
    risk_score = "TRUNG BÌNH"
    risk_color = "orange"
    if container_qty >= 4 and "Los Angeles" in pod:
        risk_score = "CAO (Lô lớn tuyến cao điểm)"
        risk_color = "red"
    
    m3.metric("Mức độ Rủi ro Space", risk_score)
    m4.metric("Ngưỡng cước mua chịu đựng", f"${buy_rate + profit_per_cont:,.0f}", "Trước khi âm vốn")

    # Cảnh báo chi tiết
    col_alert1, col_alert2 = st.columns(2)

    with col_alert1:
        st.subheader(" Cảnh báo Thị trường & Vận hành")
        if risk_score.startswith("CAO"):
            st.error(f"**CẢNH BÁO ĐỎ:** Lô hàng yêu cầu giữ chỗ đồng thời **{container_qty} containers** trên tuyến **{pol} → {pod}** trong giai đoạn cao điểm thị trường. Yêu cầu space lớn làm giảm độ linh hoạt, nguy cơ rớt tàu hoặc trễ lịch (giống case thực tế trễ 2 ngày) là rất cao.")
        else:
            st.warning("**CẢNH BÁO VÀNG:** Thị trường đang có biến động cung ứng space. Cần xác nhận booking sớm trước ít nhất 2-3 tuần.")
        
        st.info(" **Gợi ý Giải pháp thông minh (Smart Recommendations):**
"
                "- **Phương án Tách lô (Split Shipment):** Nên chia 5 container thành 2 đợt (ví dụ 3 và 2 cont) đi trên 2 chuyến tàu khác nhau để dễ xin space từ hãng tàu.
"
                "- **Cam kết sản lượng:** Làm việc trước với hãng tàu để ký cam kết volume nhằm ưu tiên phân bổ chỗ.")

    with col_alert2:
        st.subheader(" Mô phỏng Độ nhạy cảm Lợi nhuận (Sensitivity Analysis)")
        st.markdown(f"Biên lợi nhuận hiện tại khá mỏng (**{margin_pct:.1f}%**, tương ứng **${profit_per_cont} USD/container**).")
        
        # Tạo bảng mô phỏng biến động giá cước mua
        sim_data = []
        for delta in [-200, -100, 0, 100, 200, 300, 500]:
            sim_buy = buy_rate + delta
            sim_profit = (sell_rate - sim_buy) * container_qty - other_cost
            status = "Lãi " if sim_profit > 0 else ("Hòa vốn " if sim_profit == 0 else "LỖ ")
            sim_data.append({
                "Biến động cước mua": f"{'+$' if delta>0 else ''}{delta} USD",
                "Cước mua thực tế": f"${sim_buy:,.0f}",
                "Tổng lợi nhuận lô": f"${sim_profit:,.0f}",
                "Trạng thái": status
            })
        
        df_sim = pd.DataFrame(sim_data)
        st.dataframe(df_sim, use_container_width=True)

else:
    st.info(" Vui lòng điền thông tin lô hàng ở phía trên và nhấn nút **'Kiểm tra & Phân tích Rủi ro Space'** để hiển thị bảng điều khiển.")
