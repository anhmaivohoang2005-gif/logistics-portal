import pandas as pd
import streamlit as st
from calc import load, compute, is_optional, CHOOSE_ONE

st.set_page_config(page_title="U&I Logistics - Chi phí theo tuyến", layout="wide")
routes, rates, dnotes, china = load("data")

st.title("Chi phí vận chuyển theo tuyến")
tab1, tab2, tab3, tab4 = st.tabs(["Báo giá theo tuyến", "Cước biển Trung Quốc → VN", "Hóa đơn thực tế", "Dữ liệu gốc"])

# ---------------- Tab 1 ----------------
with tab1:
    label = {r.route_id: f"{r.route_id} | {r.tuyen} | {r.cont} | {r.mode}" for r in routes.itertuples()}
    rid = st.selectbox("Chọn tuyến", list(label), format_func=label.get)
    info = routes[routes.route_id == rid].iloc[0]
    st.caption(f"Ngày báo giá: {info.ngay_bao_gia if pd.notna(info.ngay_bao_gia) else '-'} | Hiệu lực: {info.het_han if pd.notna(info.het_han) else '-'} | Hãng tàu (giá mua): {info.hang_tau_mua if pd.notna(info.hang_tau_mua) else '-'}")

    c1, c2, c3, c4, c5 = st.columns(5)
    n_cont = c1.number_input("Số container", 1, 100, 1)
    volume = c2.number_input("Khối lượng (TON/CBM, cho hàng lẻ)", 0.0, 1000.0, 1.0, 0.1)
    days = c3.number_input("Số ngày (chassis, storage...)", 0, 30, 2)
    hours = c4.number_input("Số giờ (drop, waiting...)", 0, 48, 0)
    vnd = c5.number_input("Tỷ giá VND/USD", 20000.0, 30000.0, 26000.0, 100.0)
    p = dict(n_cont=n_cont, volume=volume, days=days, hours=hours, pallets=1)

    dest = None
    if rid in CHOOSE_ONE:
        dest = st.radio("Điểm giao hàng", CHOOSE_ONE[rid], horizontal=True)
    r_all = rates[rates.route_id == rid]
    opt_names = [row.khoan_phi for row in r_all.itertuples() if is_optional(r_all.loc[row.Index])]
    optional = st.multiselect("Khoản phí phát sinh / tùy chọn muốn tính thêm", opt_names)

    detail, tot = compute(rates, rid, p, optional, dest, vnd)
    show = detail[["nhom", "khoan_phi", "don_vi", "gia_ban", "gia_mua", "tien_te", "so_luong", "ban_usd", "mua_usd", "ghi_chu"]].rename(columns={
        "nhom": "Nhóm", "khoan_phi": "Khoản phí", "don_vi": "ĐVT", "gia_ban": "Đơn giá bán", "gia_mua": "Đơn giá mua",
        "tien_te": "Tiền tệ", "so_luong": "SL", "ban_usd": "Thành tiền bán (USD)", "mua_usd": "Thành tiền mua (USD)", "ghi_chu": "Ghi chú"})
    st.dataframe(show, use_container_width=True, hide_index=True)

    m1, m2, m3 = st.columns(3)
    m1.metric("Tổng giá bán (USD)", f"{tot['tong_ban']:,.0f}")
    m2.metric("Tổng giá mua (USD)", f"{tot['tong_mua']:,.0f}")
    m3.metric("Lợi nhuận (USD)", f"{tot['loi_nhuan']:,.0f}",
              help="Chỉ tính các khoản có giá mua. Phí hải quan/trucking không có giá mua thì không đưa vào lợi nhuận.")
    if tot["so_khoan_chua_co_gia"]:
        st.info(f"{tot['so_khoan_chua_co_gia']} khoản 'at cost' / theo % giá trị: không có số tiền, cần tính riêng (xem cột Ghi chú).")
    if info.mode and "LCL" in str(info.cont):
        st.warning("Hàng lẻ: cần xác nhận quy tắc tối thiểu (1 CBM / 1 TON) trước khi dùng giá này.")

# ---------------- Tab 2 ----------------
with tab2:
    f1, f2, f3, f4 = st.columns(4)
    pol = f1.multiselect("Cảng đi", sorted(china.pol.unique()))
    pod = f2.multiselect("Cảng đến", sorted(china.pod.unique()))
    carrier = f3.multiselect("Hãng tàu", sorted(china.hang_tau.unique()))
    cont = f4.radio("Loại container", ["20", "40HQ"], horizontal=True)
    markup = st.number_input("Lợi nhuận cộng thêm / container (USD)", 0, 1000, 0)
    d = china.copy()
    if pol: d = d[d.pol.isin(pol)]
    if pod: d = d[d.pod.isin(pod)]
    if carrier: d = d[d.hang_tau.isin(carrier)]
    col = "gia_20" if cont == "20" else "gia_40HQ"
    d = d[d[col].notna()].sort_values(col)
    d["gia_ban_de_xuat"] = d[col] + markup
    st.dataframe(d[["pol", "pod", "hang_tau", col, "gia_ban_de_xuat", "etd", "cls", "tt_ngay", "free_time", "dich_vu", "nguon", "ghi_chu"]],
                 use_container_width=True, hide_index=True)
    st.caption("Lưu ý: bảng giá chưa rõ hiệu lực/năm, và chưa gồm local charge. Kiểm tra lại trước khi báo khách.")

# ---------------- Tab 3 ----------------
with tab3:
    sel = st.multiselect("Lọc theo tuyến", sorted(dnotes.route_id.dropna().unique()))
    dd = dnotes[dnotes.route_id.isin(sel)] if sel else dnotes
    st.dataframe(dd, use_container_width=True, hide_index=True)

# ---------------- Tab 4 ----------------
with tab4:
    st.subheader("Tuyến"); st.dataframe(routes, use_container_width=True, hide_index=True)
    st.subheader("Bảng giá"); st.dataframe(rates.drop(columns=["ban_num", "mua_num"]), use_container_width=True, hide_index=True)
