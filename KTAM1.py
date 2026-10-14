import streamlit as st

st.set_page_config(
    page_title="LogiSpace Simulator — Freight Quotation & Space Intelligence Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === CSS TÙY CHỈNH FULL MÀN HÌNH VÀ ẨN MENU STREAMLIT ===
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        
        .stApp {
            margin: 0px;
            background-color: #0f172a;
        }
    </style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LogiSpace Simulator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
    <style>
        html, body {
            width: 100%; height: 100%; margin: 0; padding: 0; background-color: #0f172a; 
        }
    </style>
</head>
<body class="bg-slate-900 text-slate-100 font-sans min-h-screen">
    <div id="app" class="flex flex-col min-h-screen w-full">
        
        <!-- HEADER -->
        <header class="border-b border-slate-800 bg-slate-950/90 backdrop-blur sticky top-0 z-50 w-full px-6 py-3">
            <div class="w-full flex flex-col md:flex-row justify-between items-center gap-3">
               <div class="flex items-center gap-3">
                   <div class="bg-blue-600 text-white p-2.5 rounded-xl font-bold shadow-lg shadow-blue-600/30">
                       <i class="fa-solid fa-ship"></i>
                   </div>
                   <div>
                       <h1 class="font-bold text-base md:text-lg leading-none text-blue-400">LogiSpace Simulator</h1>
                       <span class="text-xs text-slate-400">Freight Quotation & Space Intelligence Platform</span>
                   </div>
               </div>
               
               <div class="flex flex-wrap items-center gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800">
                   <button @click="currentTab = 'dashboard'" :class="currentTab === 'dashboard' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition">
                       <i class="fa-solid fa-chart-pie mr-1"></i> Dashboard
                   </button>
                   <button @click="currentTab = 'shipmentForm'" :class="currentTab === 'shipmentForm' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition">
                       <i class="fa-solid fa-pen-to-square mr-1"></i> Thông Tin Lô Hàng
                   </button>
                   <button @click="currentTab = 'quotation'" :class="currentTab === 'quotation' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition">
                       <i class="fa-solid fa-calculator mr-1"></i> Báo Giá & Biên Lãi
                   </button>
                   <button @click="currentTab = 'spaceForecast'" :class="currentTab === 'spaceForecast' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition">
                       <i class="fa-solid fa-shield-halved mr-1"></i> Dự Báo Space
                   </button>
                   <button @click="currentTab = 'peakSeason'" :class="currentTab === 'peakSeason' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition">
                       <i class="fa-solid fa-triangle-exclamation mr-1"></i> Mùa Cao Điểm & Thị Trường
                   </button>
                   <button @click="currentTab = 'marketplace'" :class="currentTab === 'marketplace' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition">
                       <i class="fa-solid fa-right-left mr-1"></i> Sàn Slot Marketplace
                   </button>
               </div>
            </div>
        </header>

        <main class="flex-1 w-full p-4 md:p-6 space-y-6">
            <div class="bg-slate-800/80 border border-slate-700 rounded-2xl p-4 flex flex-col md:flex-row items-center justify-between gap-3 text-xs shadow-lg w-full">
               <div class="flex items-center gap-3">
                   <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
                   <div>
                       <strong class="text-white">Trạng thái hệ thống:</strong>
                       <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-medium">Đang mô phỏng tuyến: {{ shipment.pol }} → {{ shipment.pod }}</span>
                       (Cập nhật lúc: <span class="text-slate-300 font-mono">{{ lastUpdatedTime }}</span>).
                   </div>
               </div>
               <div class="flex items-center gap-3">
                   <button @click="resetToDefault" class="bg-slate-700 hover:bg-slate-600 text-slate-200 px-3 py-1 rounded-lg transition font-medium">
                       Đặt Lại Dữ Liệu Chuẩn
                   </button>
               </div>
            </div>

            <!-- TAB 1: DASHBOARD -->
            <div v-if="currentTab === 'dashboard'" class="space-y-6 w-full">
               <div class="grid grid-cols-1 md:grid-cols-4 gap-4 w-full">
                   <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                       <div class="text-xs text-slate-400 mb-1">Quy Mô Lô Hàng</div>
                       <div class="text-2xl font-bold text-white">{{ shipment.volume }} x {{ shipment.containerType }}</div>
                       <div class="text-[11px] text-blue-400 mt-2">Tuyến: {{ shipment.pol }} → {{ shipment.pod }}</div>
                   </div>
                   <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                       <div class="text-xs text-slate-400 mb-1">Biên Lợi Nhuận Gộp Thực Tế</div>
                       <div class="text-2xl font-bold text-amber-400">{{ evaluatedCarriers[0] ? evaluatedCarriers[0].marginPercent : 0 }}%</div>
                       <div class="text-[11px] text-slate-400 mt-2">Mục tiêu chuẩn: {{ targetMargin }}%</div>
                   </div>
                   <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                       <div class="text-xs text-slate-400 mb-1">Rủi Ro Trễ Tàu (Rolling Risk)</div>
                       <div class="text-2xl font-bold text-rose-400">+{{ evaluatedCarriers[0] ? evaluatedCarriers[0].delayDays : 2 }} Ngày Chậm</div>
                       <div class="text-[11px] text-slate-400 mt-2">ETD kế hoạch: {{ shipment.etd }}</div>
                   </div>
                   <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                       <div class="text-xs text-slate-400 mb-1">Slot Sẵn Sàng Trên Sàn</div>
                       <div class="text-2xl font-bold text-emerald-400">{{ filteredMarketplaceList.length }} Tin Đăng</div>
                       <div class="text-[11px] text-slate-400 mt-2">Giải pháp bù đắp thiếu hụt space</div>
                   </div>
               </div>

               <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 w-full">
                   <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4">
                       <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                           <i class="fa-solid fa-bolt text-amber-400"></i> Hồ Sơ Lô Hàng Đang Khảo Sát
                       </h3>
                       <div class="space-y-2 text-xs text-slate-300">
                           <div><strong>Shipper / Consignee:</strong> {{ shipment.shipper }} / {{ shipment.consignee }}</div>
                           <div><strong>Mặt hàng:</strong> {{ shipment.commodity }}</div>
                           <div><strong>Hãng Tàu Lựa Chọn:</strong> <span class="text-blue-400 font-semibold">{{ shipment.preferredCarrier }}</span> | <strong>Vessel:</strong> {{ evaluatedCarriers[0] ? evaluatedCarriers[0].vessel : 'N/A' }}</div>
                           <div><strong>Ngày Book (Booking Date):</strong> {{ shipment.bookingDate }}</div>
                           <div class="p-3 mt-2 rounded-xl bg-blue-500/10 border border-blue-500/30 text-blue-300">
                               <i class="fa-solid fa-circle-info mr-1"></i> 
                               Hệ thống đang mô phỏng linh hoạt theo thông số thực tế bạn nhập tại tab "Thông Tin Lô Hàng".
                           </div>
                       </div>
                   </div>

                   <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4">
                       <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                           <i class="fa-solid fa-circle-info text-blue-400"></i> Hướng Dẫn Vận Hành
                       </h3>
                       <p class="text-xs text-slate-300 leading-relaxed">
                           Bạn có thể thay đổi hãng tàu, cảng đi/đến hoặc loại container ở tab <strong>Thông Tin Lô Hàng</strong>. Mọi chi phí cước biển, phụ phí THC, Seal/Doc và rủi ro sẽ tự động tính toán lại chính xác theo hãng tàu bạn chọn.
                       </p>
                   </div>
               </div>
            </div>

            <!-- TAB 2: FORM THÔNG TIN LÔ HÀNG -->
            <div v-if="currentTab === 'shipmentForm'" class="space-y-6 w-full">
               <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-6 shadow-xl space-y-5 w-full">
                   <div class="flex justify-between items-center pb-3 border-b border-slate-700/60">
                       <h3 class="text-base font-bold text-blue-400 flex items-center gap-2">
                           <i class="fa-solid fa-pen-to-square"></i> Chỉnh Sửa Thông Tin Lô Hàng
                       </h3>
                       <span class="text-xs text-slate-400">Đồng bộ hóa toàn hệ thống sau khi xác nhận</span>
                   </div>

                   <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
                       <div class="space-y-3 bg-slate-900/50 p-3 rounded-xl border border-slate-700/50">
                           <div class="font-semibold text-slate-200 border-b border-slate-700 pb-1">1. Các Bên Liên Quan</div>
                           <div>
                               <label class="text-slate-400 block mb-1">Shipper</label>
                               <input type="text" v-model="tempShipment.shipper" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Consignee</label>
                               <input type="text" v-model="tempShipment.consignee" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Sales Phụ Trách</label>
                               <input type="text" v-model="tempShipment.salesPerson" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                           </div>
                       </div>

                       <div class="space-y-3 bg-slate-900/50 p-3 rounded-xl border border-slate-700/50">
                           <div class="font-semibold text-slate-200 border-b border-slate-700 pb-1">2. Tuyến Vận Tải (POL / POD)</div>
                           <div>
                               <label class="text-slate-400 block mb-1">Cảng Đi (POL)</label>
                               <select v-model="tempShipment.pol" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                   <option value="Cái Mép TCIT (VNVUT)">Cái Mép TCIT (VNVUT)</option>
                                   <option value="Cát Lái (VNCLI)">Cát Lái (VNCLI)</option>
                                   <option value="Hải Phòng (VNHPH)">Hải Phòng (VNHPH)</option>
                                   <option value="Sài Gòn (VNSGN)">Sài Gòn (VNSGN)</option>
                               </select>
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Cảng Đến (POD)</label>
                               <select v-model="tempShipment.pod" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                   <option value="Los Angeles, CA (USLAX)">Los Angeles, CA (USLAX)</option>
                                   <option value="Long Beach, CA (USLGB)">Long Beach, CA (USLGB)</option>
                                   <option value="New York, NY/NJ (USNYC)">New York, NY/NJ (USNYC)</option>
                                   <option value="Norfolk, VA (USORF)">Norfolk, VA (USORF)</option>
                                   <option value="Savannah, GA (USSAV)">Savannah, GA (USSAV)</option> 
                               </select>
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Loại Hàng Hóa</label>
                               <input type="text" v-model="tempShipment.commodity" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                           </div>
                       </div>

                       <div class="space-y-3 bg-slate-900/50 p-3 rounded-xl border border-slate-700/50">
                           <div class="font-semibold text-slate-200 border-b border-slate-700 pb-1">3. Quy Mô & Container</div>
                           <div class="grid grid-cols-2 gap-2">
                               <div>
                                   <label class="text-slate-400 block mb-1">Loại Cont</label>
                                   <select v-model="tempShipment.containerType" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                       <option value="40'HC">40'HC</option>
                                       <option value="40'GP">40'GP</option>
                                       <option value="20'GP">20'GP</option>
                                       <option value="45'HC">45'HC (High Cube)</option>
                                       <option value="40'RF">40'RF (Reefer - Lạnh)</option>
                                       <option value="20'RF">20'RF (Reefer - Lạnh)</option>
                                       <option value="40'OT">40'OT (Open Top)</option>
                                       <option value="20'OT">20'OT (Open Top)</option>
                                       <option value="40'FR">40'FR (Flat Rack)</option>
                                   </select>
                               </div>
                               <div>
                                   <label class="text-slate-400 block mb-1">Số Lượng</label>
                                   <input type="number" min="1" max="100" v-model.number="tempShipment.volume" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-amber-400 font-bold">
                               </div>
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Hãng Tàu</label>
                               <select v-model="tempShipment.preferredCarrier" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                   <option value="Wan Hai Lines">Wan Hai Lines</option>
                                   <option value="Evergreen Line">Evergreen Line</option>
                                   <option value="COSCO Shipping">COSCO Shipping</option>
                                   <option value="Maersk Line">Maersk Line</option>
                                   <option value="MSC (Mediterranean Shipping Company)">MSC</option>
                                   <option value="CMA CGM">CMA CGM</option>
                                   <option value="Hapag-Lloyd">Hapag-Lloyd</option>
                                   <option value="ONE (Ocean Network Express)">ONE</option>
                                   <option value="Yang Ming">Yang Ming</option>
                                   <option value="HMM">HMM (Hyundai Merchant Marine)</option>
                                   <option value="PIL (Pacific International Lines)">PIL</option>
                                   <option value="SITC">SITC</option>
                               </select>
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Mục Tiêu Biên Lãi (%)</label>
                               <input type="number" min="1" max="50" v-model.number="targetMargin" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-blue-400 font-bold">
                           </div>
                       </div>

                       <div class="space-y-3 bg-slate-900/50 p-3 rounded-xl border border-slate-700/50">
                           <div class="font-semibold text-slate-200 border-b border-slate-700 pb-1">4. Lịch Trình (ETD / ETA)</div>
                           <div>
                               <label class="text-slate-400 block mb-1">Ngày Book Chỗ</label>
                               <input type="date" v-model="tempShipment.bookingDate" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">ETD</label>
                               <input type="date" v-model="tempShipment.etd" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">ETA</label>
                               <input type="date" v-model="tempShipment.eta" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                           </div>
                       </div>
                   </div>

                   <div class="pt-4 border-t border-slate-700 flex justify-end gap-3">
                       <button @click="commitShipmentUpdate" class="bg-blue-600 hover:bg-blue-500 text-white px-6 py-2.5 rounded-xl text-xs font-bold shadow-lg transition flex items-center gap-2">
                           <i class="fa-solid fa-check"></i> Hoàn Thành Và Cập Nhật Dữ Liệu
                       </button>
                   </div>
               </div>
            </div>

            <!-- TAB 3: BÁO GIÁ & BIÊN LÃI -->
            <div v-if="currentTab === 'quotation'" class="space-y-6 w-full">
               <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                   <div class="flex justify-between items-center pb-3 border-b border-slate-700/60">
                       <h3 class="text-sm font-bold text-blue-400 flex items-center gap-2">
                           <i class="fa-solid fa-file-invoice-dollar"></i> Phân Hệ B: Báo Giá & Kiểm Soát Biên Lợi Nhuận
                       </h3>
                       <span class="text-xs text-slate-400">Lô hàng: <strong>{{ shipment.volume }} x {{ shipment.containerType }}</strong> ({{ shipment.pol }} → {{ shipment.pod }})</span>
                   </div>

                   <div class="space-y-4 w-full">
                       <div v-for="carrier in evaluatedCarriers" :key="carrier.id" class="bg-slate-900/70 border border-slate-700/80 rounded-xl p-4 space-y-3 w-full">
                           <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 rounded-lg bg-slate-800 flex items-center justify-center font-bold text-slate-200 border border-slate-700">
                                        {{ carrier.code }}
                                    </div>
                                    <div>
                                        <div class="font-semibold text-slate-100 flex items-center gap-2">
                                            {{ carrier.name }}
                                           <span class="text-[10px] bg-blue-500/20 text-blue-300 px-2 py-0.5 rounded border border-blue-500/30">{{ carrier.vessel }}</span>
                                        </div>
                                        <div class="text-xs text-slate-400 mt-0.5">
                                            ETD: <strong class="text-slate-200">{{ carrier.etd }}</strong> | Biến động: <span class="text-rose-400 font-semibold">+{{ carrier.delayDays }} ngày trễ</span>
                                        </div>
                                    </div>
                                </div>

                                <div class="text-right text-xs">
                                    <span class="text-slate-400 block">Tổng Giá Vốn (1 Cont)</span>
                                    <span class="text-base font-bold text-blue-400">${{ carrier.totalCostPerCont.toLocaleString() }} USD</span>
                                </div>
                           </div>

                           <div class="grid grid-cols-2 md:grid-cols-5 gap-2 bg-slate-950/60 p-3 rounded-lg border border-slate-800 text-xs w-full">
                                <div>Cước biển (O/F): <strong class="text-slate-200">${{ carrier.oceanFreight }}</strong></div>
                                <div>THC: <strong class="text-slate-200">${{ carrier.thc }}</strong></div>
                                <div>Seal + Doc: <strong class="text-slate-200">${{ carrier.sealDoc }}</strong></div>
                                <div>Handling (POD): <strong class="text-slate-200 text-rose-400">${{ carrier.handlingPod }}</strong></div>
                                <div>Dự phòng rủi ro: <strong class="text-slate-200">${{ carrier.reserveFee }}</strong></div>
                           </div>
                           <div class="pt-2 border-t border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-3 text-xs">
                                <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                                    <div>
                                       <span class="text-slate-400 block">Giá Bán Cước ($)</span>
                                       <input type="number" v-model.number="carrier.currentSellRate" class="w-28 bg-slate-800 border border-slate-700 rounded p-1 text-slate-100 font-bold mt-1">
                                    </div>
                                    <div>
                                       <span class="text-slate-400 block">Giá Bán Tối Thiểu (Chuẩn {{ targetMargin }}%)</span>
                                       <span class="font-bold text-emerald-400 text-sm">${{ carrier.minSellRateRequired }} USD</span>
                                    </div>
                                    <div>
                                       <span class="text-slate-400 block">Biên Lợi Nhuận Gộp</span>
                                       <span class="font-bold text-amber-400">
                                            {{ carrier.marginPercent }}%
                                       </span>
                                    </div>
                                    <div>
                                       <span class="text-slate-400 block">Tổng Lãi Toàn Lô ({{ shipment.volume }} cont)</span>
                                       <span class="font-bold text-emerald-400">${{ carrier.totalProfit.toLocaleString() }} USD</span>
                                    </div>
                                </div>

                                <div>
                                    <span class="px-3 py-1.5 rounded-lg bg-blue-500/20 text-blue-300 border border-blue-500/30 text-xs font-semibold flex items-center gap-1.5">
                                        <i class="fa-solid fa-calculator"></i> Tính toán tự động theo hãng
                                    </span>
                                </div>
                           </div>
                       </div>
                   </div>
               </div>
            </div>

            <!-- TAB 4: DỰ BÁO SPACE -->
            <div v-if="currentTab === 'spaceForecast'" class="space-y-6 w-full">
               <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                   <h3 class="text-sm font-bold text-amber-400 flex items-center gap-2">
                       <i class="fa-solid fa-shield-halved"></i> Phân Hệ C: Phân Tích Rủi Ro Thiếu Hụt Space & Quản Trị Tải Trọng
                   </h3>
                   <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                       <div class="bg-slate-900/70 p-4 rounded-xl border border-slate-700 space-y-2">
                           <div class="font-bold text-white text-sm">Nguyên Nhân Thiếu Space Theo Mùa Vụ</div>
                           <p class="text-slate-300">• <strong>Mùa cao điểm lễ hội (Black Friday / Giáng Sinh):</strong> Nhu cầu nhập khẩu hàng tiêu dùng tăng vọt từ tháng 8 đến tháng 11.</p>
                           <p class="text-slate-300">• <strong>Mùa cao điểm trước Tết (Lunar New Year Rush):</strong> Các nhà máy dồn dịch đẩy hàng trước kỳ nghỉ dài, gây nghẽn mạch tại cảng xuất.</p>
                       </div>
                       <div class="bg-gradient-to-br from-rose-500/10 to-orange-500/10 p-4 rounded-xl border border-rose-500/30 space-y-2">
                           <div class="font-bold text-rose-400 text-sm"><i class="fa-solid fa-triangle-exclamation mr-1"></i> Giải Pháp Quản Trị Vận Hành</div>
                           <p class="text-slate-300">• Chủ động đặt chỗ trước ít nhất 3-4 tuần đối với các tuyến chính đi bờ Tây/Đông nước Mỹ hoặc châu Âu.</p>
                           <p class="text-slate-300">• Sử dụng nguồn slot dự phòng từ sàn Marketplace để bù đắp khi hãng tàu thông báo ngưng nhận booking (roll over).</p>
                       </div>
                   </div>
               </div>
            </div>

            <!-- TAB 5: MÙA CAO ĐIỂM & THỊ TRƯỜNG -->
            <div v-if="currentTab === 'peakSeason'" class="space-y-6 w-full">
               <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                   <h3 class="text-sm font-bold text-amber-400 flex items-center gap-2">
                       <i class="fa-solid fa-calendar-days"></i> Phân Hệ D: Nhận Diện Các Chu Kỳ Mùa Cao Điểm & Biến Động Thị Trường
                   </h3>
                   <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                       <div class="bg-slate-900/70 p-4 rounded-xl border border-slate-700 space-y-2">
                           <div class="font-bold text-blue-400 text-sm">1. Mùa Mua Sắm Cuối Năm (Black Friday & Giáng Sinh)</div>
                           <p class="text-slate-300"><strong>Thời gian:</strong> Tháng 8 – Tháng 11 hằng năm.</p>
                           <p class="text-slate-300"><strong>Đặc điểm:</strong> Hãng tàu áp dụng phụ phí PSS (Peak Season Surcharge) và cước biển tăng mạnh do nhu cầu tiêu dùng toàn cầu đạt đỉnh.</p>
                       </div>
                       <div class="bg-slate-900/70 p-4 rounded-xl border border-slate-700 space-y-2">
                           <div class="font-bold text-amber-400 text-sm">2. Mùa Trước Tết Nguyên Đán (Pre-LNY Rush)</div>
                           <p class="text-slate-300"><strong>Thời gian:</strong> Tháng 12 – Tháng 2 (tùy năm).</p>
                           <p class="text-slate-300"><strong>Đặc điểm:</strong> Doanh nghiệp đẩy mạnh xuất khẩu trước khi các nhà máy đóng cửa nghỉ Tết, gây hiện tượng thiếu vỏ container và quá tải bãi.</p>
                       </div>
                       <div class="bg-slate-900/70 p-4 rounded-xl border border-slate-700 space-y-2">
                           <div class="font-bold text-emerald-400 text-sm">3. Biến Động Nhiên Liệu & Địa Chính Trị</div>
                           <p class="text-slate-300"><strong>Thời gian quanh năm:</strong></p>
                           <p class="text-slate-300"><strong>Đặc điểm:</strong> Thay đổi tuyến hải trình quốc tế ảnh hưởng trực tiếp đến thời gian vận chuyển (transit time) và chi phí nhiên liệu phụ trội (BAF/CAF).</p>
                       </div>
                   </div>
               </div>
            </div>

            <!-- TAB 6: SÀN GIAO DỊCH SLOT MARKETPLACE -->
            <div v-if="currentTab === 'marketplace'" class="space-y-6 w-full">
               <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                   <div class="flex justify-between items-center pb-3 border-b border-slate-700/60">
                       <h3 class="text-sm font-bold text-emerald-400 flex items-center gap-2">
                           <i class="fa-solid fa-right-left"></i> Phân Hệ E: Sàn Chuyển Nhượng Slot Space (Marketplace)
                       </h3>
                       <span class="text-xs text-slate-400">Tuyến: <strong>{{ shipment.pol }} → {{ shipment.pod }}</strong></span>
                   </div>

                   <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
                       <div v-for="slot in filteredMarketplaceList" :key="slot.id" class="bg-slate-900/70 border border-slate-700/80 rounded-xl p-4 flex flex-col justify-between gap-3 text-xs">
                           <div class="flex justify-between items-start">
                                <div>
                                    <span class="px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20 font-semibold">{{ slot.provider }}</span>
                                    <div class="font-semibold text-slate-100 mt-1.5">Hãng tàu: {{ slot.carrier }} (ETD: {{ slot.etd }})</div>
                                    <div class="text-slate-400">Tuyến: {{ slot.route }}</div>
                                </div>
                                <div class="text-right">
                                    <div class="text-slate-400">Giá chào nhượng</div>
                                    <div class="text-sm font-bold text-emerald-400">${{ slot.price }} USD/Cont</div>
                                </div>
                           </div>
                           <div class="flex justify-between items-center pt-2 border-t border-slate-800">
                                <span class="text-slate-300">Khả dụng: <strong>{{ slot.slots }} slot {{ shipment.containerType }}</strong></span>
                                <button @click="claimSlot(slot)" class="bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-1.5 rounded-lg transition font-medium">
                                    Gửi Yêu Cầu Nhượng Slot
                                </button>
                           </div>
                       </div>
                   </div>
               </div>
            </div>
        </main>
    </div>

    <script>
        const { createApp } = Vue;
        createApp({
            data() {
                return {
                    currentTab: 'dashboard',
                    targetMargin: 10,
                    lastUpdatedTime: new Date().toLocaleTimeString(),
                    shipment: {
                        shipper: 'QA Furniture Co., Ltd (Bình Phước)',
                        consignee: 'MTA Cabinets LLC (Texas)',
                        salesPerson: 'Nhập tên',
                        pol: 'Cái Mép TCIT (VNVUT)',
                        pod: 'Los Angeles, CA (USLAX)',
                        commodity: 'Wooden kitchen cabinets (HS 940340)',
                        containerType: "40'HC",
                        volume: 5,
                        preferredCarrier: 'Wan Hai Lines',
                        bookingDate: '2025-10-13',
                        etd: '2025-10-15',
                        eta: '2025-11-02'
                    },
                    tempShipment: {
                        shipper: 'QA Furniture Co., Ltd (Bình Phước)',
                        consignee: 'MTA Cabinets LLC (Texas)',
                        salesPerson: 'Nhập tên',
                        pol: 'Cái Mép TCIT (VNVUT)',
                        pod: 'Los Angeles, CA (USLAX)',
                        commodity: 'Wooden kitchen cabinets (HS 940340)',
                        containerType: "40'HC",
                        volume: 5,
                        preferredCarrier: 'Wan Hai Lines',
                        bookingDate: '2025-10-13',
                        etd: '2025-10-15',
                        eta: '2025-11-02'
                    },
                    // Kho dữ liệu chuẩn chi tiết cho từng hãng tàu
                    allCarriersData: {
                        'Wan Hai Lines': { name: 'Wan Hai Lines', code: 'WHL', vessel: 'WAN HAI A01 E012', oceanFreight: 5230, thc: 200, sealDoc: 48, handlingPod: 90, reserveFee: 0, currentSellRate: 5438, delayDays: 2 },
                        'Evergreen Line': { name: 'Evergreen Line', code: 'EMC', vessel: 'EVER GIVEN V.088E', oceanFreight: 5150, thc: 200, sealDoc: 45, handlingPod: 90, reserveFee: 0, currentSellRate: 5350, delayDays: 1 },
                        'COSCO Shipping': { name: 'COSCO Shipping', code: 'COS', vessel: 'COSCO SHIPPING APEX', oceanFreight: 5100, thc: 200, sealDoc: 50, handlingPod: 90, reserveFee: 0, currentSellRate: 5300, delayDays: 3 },
                        'ONE (Ocean Network Express)': { name: 'ONE (Ocean Network Express)', code: 'ONE', vessel: 'ONE INNOVATION V.012', oceanFreight: 5300, thc: 200, sealDoc: 50, handlingPod: 90, reserveFee: 0, currentSellRate: 5550, delayDays: 1 },
                        'Maersk Line': { name: 'Maersk Line', code: 'MSK', vessel: 'MAERSK MC-KINNEY', oceanFreight: 5400, thc: 200, sealDoc: 50, handlingPod: 90, reserveFee: 0, currentSellRate: 5700, delayDays: 0 },
                        'MSC (Mediterranean Shipping Company)': { name: 'MSC', code: 'MSC', vessel: 'MSC IRINA V.021', oceanFreight: 5050, thc: 200, sealDoc: 45, handlingPod: 90, reserveFee: 0, currentSellRate: 5280, delayDays: 2 },
                        'CMA CGM': { name: 'CMA CGM', code: 'CMA', vessel: 'CMA CGM JACQUES SAADE', oceanFreight: 5250, thc: 200, sealDoc: 48, handlingPod: 90, reserveFee: 0, currentSellRate: 5490, delayDays: 1 },
                        'Hapag-Lloyd': { name: 'Hapag-Lloyd', code: 'HPL', vessel: 'EXPRESS BERLIN', oceanFreight: 5350, thc: 200, sealDoc: 50, handlingPod: 90, reserveFee: 0, currentSellRate: 5600, delayDays: 1 },
                        'Yang Ming': { name: 'Yang Ming', code: 'YML', vessel: 'YANG MING UNIFORM', oceanFreight: 5120, thc: 200, sealDoc: 45, handlingPod: 90, reserveFee: 0, currentSellRate: 5350, delayDays: 2 },
                        'HMM': { name: 'HMM', code: 'HMM', vessel: 'HMM ALGECIRAS', oceanFreight: 5180, thc: 200, sealDoc: 48, handlingPod: 90, reserveFee: 0, currentSellRate: 5420, delayDays: 2 },
                        'PIL (Pacific International Lines)': { name: 'PIL', code: 'PIL', vessel: 'KOTA TAMADUN', oceanFreight: 5000, thc: 200, sealDoc: 45, handlingPod: 90, reserveFee: 0, currentSellRate: 5250, delayDays: 3 },
                        'SITC': { name: 'SITC', code: 'SITC', vessel: 'SITC WEIHAI', oceanFreight: 4900, thc: 200, sealDoc: 40, handlingPod: 90, reserveFee: 0, currentSellRate: 5150, delayDays: 2 }
                    },
                    carriers: [
                        {
                            id: 1,
                            name: 'Wan Hai Lines',
                            code: 'WHL',
                            vessel: 'WAN HAI A01 E012',
                            etd: '2025-10-15',
                            delayDays: 2,
                            oceanFreight: 5230,
                            thc: 200,
                            sealDoc: 48,
                            handlingPod: 90,
                            reserveFee: 0,
                            currentSellRate: 5438
                        }
                    ],
                    marketplaceList: [
                        { id: 201, provider: 'VinaFreighter Partner', carrier: 'Evergreen', route: 'Cái Mép TCIT → Los Angeles', pol: 'Cái Mép TCIT (VNVUT)', pod: 'Los Angeles, CA (USLAX)', etd: '2026-10-14', slots: 3, price: 5200 },
                        { id: 202, provider: 'Global Logistics Corp', carrier: 'COSCO', route: 'Cái Mép TCIT → Long Beach', pol: 'Cái Mép TCIT (VNVUT)', pod: 'Long Beach, CA (USLGB)', etd: '2026-10-16', slots: 2, price: 5180 }
                    ]
                }
            },
            computed: {
                evaluatedCarriers() {
                    return this.carriers.map(c => {
                        const totalCostPerCont = c.oceanFreight + c.thc + c.sealDoc + c.handlingPod + c.reserveFee;
                        const minSellRateRequired = Math.ceil(totalCostPerCont / (1 - (this.targetMargin / 100)));
                        const profitPerCont = c.currentSellRate - totalCostPerCont;
                        const totalProfit = profitPerCont * this.shipment.volume;
                        const marginPercent = c.currentSellRate > 0 ? ((profitPerCont / c.currentSellRate) * 100).toFixed(1) : 0;
                        return {
                            ...c,
                            totalCostPerCont,
                            minSellRateRequired,
                            profitPerCont,
                            totalProfit,
                            marginPercent: parseFloat(marginPercent)
                        };
                    });
                },
                filteredMarketplaceList() {
                    return this.marketplaceList.filter(s => s.pol.includes(this.shipment.pol.split(' ')[0]));
                }
            },
            methods: {
                commitShipmentUpdate() {
                    this.shipment = JSON.parse(JSON.stringify(this.tempShipment));
                    
                    // LẤY ĐÚNG THÔNG TIN HÃNG TÀU NGƯỜI DÙNG CHỌN ĐỂ CẬP NHẬT CHI PHÍ VÀ THÔNG SỐ RIÊNG
                    const selectedCarrierName = this.shipment.preferredCarrier || 'Wan Hai Lines';
                    const templateData = this.allCarriersData[selectedCarrierName] || this.allCarriersData['Wan Hai Lines'];

                    this.carriers = [{
                        id: 1,
                        name: templateData.name,
                        code: templateData.code,
                        vessel: templateData.vessel,
                        etd: this.shipment.etd,
                        delayDays: templateData.delayDays,
                        oceanFreight: templateData.oceanFreight,
                        thc: templateData.thc,
                        sealDoc: templateData.sealDoc,
                        handlingPod: templateData.handlingPod,
                        reserveFee: templateData.reserveFee,
                        currentSellRate: templateData.currentSellRate
                    }];

                    this.lastUpdatedTime = new Date().toLocaleTimeString();
                    alert('Đã cập nhật thông tin lô hàng và đồng bộ biểu giá theo hãng tàu mới thành công!');
                    this.currentTab = 'quotation';
                },
                resetToDefault() {
                    this.targetMargin = 10;
                    this.shipment = {
                        shipper: 'QA Furniture Co., Ltd (Bình Phước)',
                        consignee: 'MTA Cabinets LLC (Texas)',
                        salesPerson: 'Nhập tên',
                        pol: 'Cái Mép TCIT (VNVUT)',
                        pod: 'Los Angeles, CA (USLAX)',
                        commodity: 'Wooden kitchen cabinets (HS 940340)',
                        containerType: "40'HC",
                        volume: 5,
                        preferredCarrier: 'Wan Hai Lines',
                        bookingDate: '2025-10-13',
                        etd: '2025-10-15',
                        eta: '2025-11-02'
                    };
                    this.tempShipment = JSON.parse(JSON.stringify(this.shipment));
                    this.carriers = [{
                        id: 1,
                        name: 'Wan Hai Lines',
                        code: 'WHL',
                        vessel: 'WAN HAI A01 E012',
                        etd: '2025-10-15',
                        delayDays: 2,
                        oceanFreight: 5230,
                        thc: 200,
                        sealDoc: 48,
                        handlingPod: 90,
                        reserveFee: 0,
                        currentSellRate: 5438
                    }];
                    this.lastUpdatedTime = new Date().toLocaleTimeString();
                    alert('Đã khôi phục dữ liệu mẫu chuẩn.');
                },
                claimSlot(slot) {
                    alert(`Đã gửi yêu cầu giữ ${slot.slots} slot từ ${slot.provider} thành công!`);
                }
            }
        }).mount('#app');
    </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=980, scrolling=True)
