import streamlit as st
import pandas as pd

# Cấu hình giao diện trang web
st.set_page_config(
    page_title="Global Logistics Space & Rate Portal",
    page_icon="🚢",
    layout="wide"
)

# 1. DANH MỤC CẢNG BIỂN QUỐC TẾ MỞ RỘNG (POL & POD)
POL_LIST = [
    "VN SGN - Cảng Cát Lái, TP. Hồ Chí Minh, Việt Nam",
    "VN VUT - Cảng Cái Mép - Thị Vải, Bà Rịa - Vũng Tàu, Việt Nam",
    "VN HPG - Cảng Hải Phòng, Việt Nam",
    "VN DAD - Cảng Đà Nẵng, Việt Nam",
    "CN SHA - Cảng Thượng Hải (Shanghai), Trung Quốc",
    "CN NGB - Cảng Ninh Ba (Ningbo), Trung Quốc",
    "SGSIN - Cảng Singapore",
    "MYPKG - Cảng Port Klang, Malaysia",
    "THLCH - Cảng Laem Chabang, Thái Lan",
    "VNHPH - Cảng Hải Phòng, Việt Nam"
]

POD_LIST = [
    "US LAX - Cảng Los Angeles, California, Mỹ",
    "US LGB - Cảng Long Beach, California, Mỹ",
    "US OAK - Cảng Oakland, California, Mỹ",
    "US NYC - Cảng New York & New Jersey, Mỹ",
    "US SEA - Cảng Seattle, Washington, Mỹ",
    "NLRTM - Cảng Rotterdam, Hà Lan",
    "DEHAM - Cảng Hamburg, Đức",
    "FRLEH - Cảng Le Havre, Pháp",
    "JPTKO - Cảng Tokyo, Nhật Bản",
    "KRBUS - Cảng Busan, Hàn Quốc"
]

# 2. DANH SÁCH HÃNG TÀU QUỐC TẾ (OCEAN CARRIERS)
CARRIER_LIST = [
    "Tất cả các hãng tàu",
    "Wan Hai Lines",
    "Maersk Line",
    "CMA CGM",
    "Evergreen Line",
    "Hapag-Lloyd",
    "Mediterranean Shipping Company (MSC)",
    "Ocean Network Express (ONE)",
    "Yang Ming Marine Transport"
]

# Thanh menu điều hướng bên trái (Sidebar)
st.sidebar.title("Logistics Management Portal")
menu = st.sidebar.selectbox(
    "Chọn phân hệ chức năng:",
    [
        "1. Tra cứu Cước & Space (Marketplace)",
        "2. Chợ Phái Sinh Space (Slot Reselling)",
        "3. Dashboard Quản trị Rủi ro & Lợi nhuận"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("System Version: 2.6.4 | Enterprise Edition")

# ==========================================
# MÀN HÌNH 1: TRA CỨU CƯỚC & SPACE (PHAATA-STYLE)
# ==========================================
if menu == "1. Tra cứu Cước & Space (Marketplace)":
    st.title("Sàn Giao Dịch Cước & Chỗ Trống (Space Marketplace)")
    st.markdown("Tra cứu lịch trình, giá mua (Buying Rate) và đánh giá độ uy tín chỗ trống từ hệ thống hãng tàu toàn cầu.")

    col1, col2 = st.columns(2)
    with col1:
        pol = st.selectbox("Cảng đi (POL)", POL_LIST)
    with col2:
        pod = st.selectbox("Cảng đến (POD)", POD_LIST)

    col3, col4, col5 = st.columns(3)
    with col3:
        carrier_filter = st.selectbox("Lọc theo Hãng tàu", CARRIER_LIST)
    with col4:
        container_type = st.selectbox("Loại Container", ["40'HC", "20'GP", "40'GP", "45'HC", "Reefer"])
    with col5:
        etd_date = st.date_input("Ngày dự kiến khởi hành (ETD)")

    if st.button("Tìm kiếm Space & Cước toàn cầu", type="primary"):
        st.success(f"Đã tổng hợp các phương án vận chuyển từ mạng lưới hãng tàu cho tuyến: {pol} ➔ {pod}")
        
        # Dữ liệu mẫu động mở rộng nhiều hãng tàu
        data = {
            "Hãng tàu": ["Wan Hai Lines", "Maersk Line", "CMA CGM", "Evergreen Line", "Hapag-Lloyd", "MSC"],
            "Tên tàu / Chuyến": ["WAN HAI A01 E012", "MAERSK EINDHOVEN V.204", "CMA CGM ADONIS", "EVER GIVEN V.088", "HAPAG BERLIN EXPRESS", "MSC OSCAR V.402"],
            "Hành trình (ETD - ETA)": ["08/06 - 30/06", "10/06 - 03/07", "12/06 - 05/07", "14/06 - 07/07", "16/06 - 10/07", "20/06 - 13/07"],
            "Trạng thái Space": ["Sắp hết chỗ (Mùa cao điểm)", "Còn trống", "Sắp đầy", "Còn trống", "Sắp hết chỗ", "Còn trống"],
            "Giá mua (Buying Rate)": ["$5,230 / cont", "$5,350 / cont", "$5,180 / cont", "$5,290 / cont", "$5,400 / cont", "$5,100 / cont"],
            "Thao tác": ["Chọn & Booking", "Chọn & Booking", "Chọn & Booking", "Chọn & Booking", "Chọn & Booking", "Chọn & Booking"]
        }
        df = pd.DataFrame(data)
        
        if carrier_filter != "Tất cả các hãng tàu":
            df = df[df["Hãng tàu"] == carrier_filter]
            
        st.table(df)

# ==========================================
# MÀN HÌNH 2: CHỢ PHÁI SINH SPACE (SLOT RESELLING)
# ==========================================
elif menu == "2. Chợ Phái Sinh Space (Slot Reselling)":
    st.title("Sàn Phái Sinh & Sang Nhượng Space (Bursa Space)")
    st.markdown("Nơi các doanh nghiệp logistics thanh lý slot dư thừa hoặc tìm nguồn cung ứng thay thế khi thị trường biến động.")

    tab1, tab2 = st.tabs(["Bảng tin rao bán / Thanh lý Slot toàn cầu", "Tạo yêu cầu Săn Space Khẩn Cấp"])

    with tab1:
        st.subheader("Danh sách Slot dư thừa từ cộng đồng nhà vận chuyển")
        market_data = {
            "Mã GD": ["SLOT-901", "SLOT-902", "SLOT-903", "SLOT-904", "SLOT-905"],
            "Tuyến vận chuyển": [
                "Cái Mép (VN) → Long Beach (US)", 
                "Cát Lái (VN) → Oakland (US)", 
                "Thượng Hải (CN) → Los Angeles (US)", 
                "Port Klang (MY) → Rotterdam (NL)",
                "Singapore (SG) → New York (US)"
            ],
            "SL Slot": ["3 x 40'HC", "2 x 40'HC", "5 x 40'HC", "4 x 40'HC", "6 x 40'HC"],
            "Hãng tàu & ETD": ["Wan Hai (10/06)", "Maersk (12/06)", "CMA CGM (15/06)", "Evergreen (18/06)", "MSC (22/06)"],
            "Giá nhượng lại": ["$5,150 / cont", "$5,200 / cont", "$5,250 / cont", "$4,900 / cont", "$5,300 / cont"],
            "Hành động": ["Mua ngay", "Mua ngay", "Mua ngay", "Mua ngay", "Mua ngay"]
        }
        st.table(pd.DataFrame(market_data))

    with tab2:
        st.subheader("Tạo lệnh tìm Space khẩn cấp cho lô hàng gấp")
        st.info("Sử dụng khi gặp sự cố thiếu chỗ đột xuất hoặc cần giải phóng hàng hóa theo tiến độ cam kết với khách hàng.")
        
        with st.form("emergency_form"):
            f_name = st.text_input("Tên hàng / Mô tả lô hàng", "General Cargo / Commercial Goods (5 x 40'HC)")
            f_route = st.selectbox("Tuyến yêu cầu khẩn cấp", [
                "Cái Mép (VN) → Los Angeles (US)",
                "Cát Lái (VN) → Long Beach (US)",
                "Thượng Hải (CN) → New York (US)",
                "Port Klang (MY) → Rotterdam (NL)"
            ])
            f_price = st.number_input("Mức giá mua chấp nhận tối đa ($/cont)", value=5400)
            submitted = st.form_submit_button("Phát tín hiệu tìm Space trên Sàn")
            
            if submitted:
                st.success(f"Đã phát lệnh thành công! Hệ thống đang tự động kết nối với các đối tác cung ứng trên tuyến {f_route}.")

# ==========================================
# MÀN HÌNH 3: DASHBOARD QUẢN TRỊ RỦI RO & LỢI NHUẬN
# ==========================================
elif menu == "3. Dashboard Quản trị Rủi ro & Lợi nhuận":
    st.title("Kiểm Soát Biên Lợi Nhuận & Cảnh Báo Rủi Ro")
    st.markdown("Phân tích độ nhạy tài chính và biên lợi nhuận của lô hàng trước biến động chi phí vận hành.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Thông tin lô hàng")
        shipper = st.text_input("Shipper", "Enterprise Shipper Co., Ltd")
        consignee = st.text_input("Consignee", "Global Importer LLC")
        qty = st.number_input("Số lượng container (40'HC)", value=5)
        
        selling_rate = st.number_input("Giá bán cho khách ($/cont)", value=5438)
        buying_rate = st.number_input("Giá mua từ hãng tàu ($/cont)", value=5230)

    with col2:
        st.subheader("Phân tích tài chính thời gian thực")
        profit_per_cont = selling_rate - buying_rate
        total_profit = profit_per_cont * qty
        margin_percent = (profit_per_cont / selling_rate) * 100

        st.metric(label="Lợi nhuận gộp / Container", value=f"${profit_per_cont}", delta=f"{margin_percent:.2f}%")
        st.metric(label="Tổng lợi nhuận lô hàng", value=f"${total_profit}")

        if margin_percent < 5:
            st.warning("CẢNH BÁO ĐỎ: Biên lợi nhuận dưới mức an toàn (5%). Lô hàng nhạy cảm trước biến động chi phí phát sinh hoặc biến động giá mua từ hãng tàu!")
        else:
            st.success("Biên lợi nhuận ở mức an toàn.")

    st.markdown("---")
    st.subheader("Mô phỏng độ nhạy khi chi phí phát sinh")
    sim_cost = st.slider("Giả định chi phí phát sinh thêm (phí lưu bãi, điều vỏ, đổi tàu) ($/cont):", 0, 500, 100)
    
    net_result = total_profit - (sim_cost * qty)
    if net_result < 0:
        st.error(f"KẾT QUẢ THỰC TẾ: LỖ ${abs(net_result)} cho toàn lô hàng do chi phí phát sinh vượt quá biên lợi nhuận dự kiến!")
    else:
        st.success(f"Lợi nhuận ròng sau khi trừ chi phí phát sinh: ${net_result}")
