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
                       <i class="fa-solid fa-triangle-exclamation mr-1"></i> Mùa Cao Điểm Thuế
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
                       <strong class="text-white">Trạng thái đồng bộ:</strong>
                       <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-medium">Đã nạp dữ liệu chuẩn (QA Furniture - Cái Mép / LAX)</span>
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
                       <div class="text-2xl font-bold text-amber-400">3.8%</div>
                       <div class="text-[11px] text-slate-400 mt-2">Mục tiêu chuẩn: {{ targetMargin }}% (Nhạy cảm chi phí)</div>
                   </div>
                   <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                       <div class="text-xs text-slate-400 mb-1">Rủi Ro Trễ Tàu (Rolling Risk)</div>
                       <div class="text-2xl font-bold text-rose-400">+2 Ngày Chậm</div>
                       <div class="text-[11px] text-slate-400 mt-2">ETD kế hoạch: 2025-10-15</div>
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
                           <div><strong>Booking / MBL:</strong> 039FX49604 | <strong>Vessel:</strong> {{ carriers[0].vessel }}</div>
                           <div><strong>Ngày Book (Booking Date):</strong> {{ shipment.bookingDate }}</div>
                           <div class="p-3 mt-2 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300">
                               <i class="fa-solid fa-triangle-exclamation mr-1"></i> 
                               Cảnh báo: Yêu cầu giữ chỗ đồng thời số lượng lớn đối mặt rủi ro thiếu space trầm trọng do làn sóng đẩy hàng trước chính sách thuế quan.
                           </div>
                       </div>
                   </div>

                   <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4">
                       <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                           <i class="fa-solid fa-circle-info text-blue-400"></i> Hướng Dẫn Sử Dụng Nút Cập Nhật
                       </h3>
                       <p class="text-xs text-slate-300 leading-relaxed">
                           Truy cập tab <strong>Thông Tin Lô Hàng</strong> để thay đổi cảng, loại container hoặc số lượng. Sau đó nhấn nút <strong>“Hoàn thành và cập nhật dữ liệu”</strong> để toàn bộ hệ thống tính toán lại giá mua, giá bán, biên lãi và rủi ro theo đúng quy trình kiểm thử nghiệp vụ Sales Forwarding.
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

            <!-- TAB 3: BÁO GIÁ & BIÊN LÃI (tính động theo tuyến / loại cont / số lượng) -->
            <div v-if="currentTab === 'quotation'" class="space-y-6 w-full">
               <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                   <div class="flex flex-col md:flex-row md:justify-between md:items-center gap-1 pb-3 border-b border-slate-700/60">
                       <h3 class="text-sm font-bold text-blue-400 flex items-center gap-2">
                           <i class="fa-solid fa-file-invoice-dollar"></i> Báo Giá & Kiểm Soát Biên Lợi Nhuận
                       </h3>
                       <span class="text-xs text-slate-400">Lô hàng: <strong class="text-slate-200">{{ shipment.volume }} x {{ shipment.containerType }}</strong> | {{ shipment.pol }} → {{ shipment.pod }}</span>
                   </div>

                   <!-- CƠ SỞ TÍNH GIÁ (thu gọn, bấm để xem chi tiết) -->
                   <details class="rounded-xl border border-slate-700 bg-slate-900/50 text-xs">
                       <summary class="cursor-pointer select-none p-3 flex flex-wrap items-center gap-2">
                           <span v-if="quoteBasis.isFullData" class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold">Dữ liệu thực</span>
                           <span v-else class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30 font-semibold">Giá ước tính</span>
                           <span class="text-slate-400">
                               {{ quoteBasis.isFullData ? 'Lấy đúng từ báo giá R02 (Cái Mép → LAX, 40HC)' : 'Điều chỉnh từ báo giá R02 theo tuyến và loại cont' }} — bấm để xem hệ số
                           </span>
                       </summary>
                       <div class="px-3 pb-3 grid grid-cols-1 md:grid-cols-3 gap-2">
                           <div class="bg-slate-950/50 rounded-lg p-2 border border-slate-800">
                               <div class="text-slate-500">Cảng đến (POD)</div>
                               <div class="text-slate-200 font-semibold">x{{ quoteBasis.podFactor }} <span class="font-normal text-slate-500">({{ quoteBasis.podSrc }})</span></div>
                           </div>
                           <div class="bg-slate-950/50 rounded-lg p-2 border border-slate-800">
                               <div class="text-slate-500">Cảng đi (POL)</div>
                               <div class="text-slate-200 font-semibold">+${{ quoteBasis.polAddon }} / 40' <span class="font-normal text-slate-500">({{ quoteBasis.polSrc }})</span></div>
                           </div>
                           <div class="bg-slate-950/50 rounded-lg p-2 border border-slate-800">
                               <div class="text-slate-500">Loại cont {{ shipment.containerType }}</div>
                               <div class="text-slate-200 font-semibold">Cước x{{ quoteBasis.contOf }} · THC x{{ quoteBasis.contThc }} <span class="font-normal text-slate-500">({{ quoteBasis.contSrc }})</span></div>
                           </div>
                       </div>
                   </details>

                   <div class="space-y-4 w-full">
                       <div v-for="carrier in evaluatedCarriers" :key="carrier.id" class="bg-slate-900/70 border border-slate-700/80 rounded-xl p-4 space-y-4 w-full">

                           <!-- Dòng 1: hãng tàu + trạng thái -->
                           <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 rounded-lg bg-slate-800 flex items-center justify-center font-bold text-slate-200 border border-slate-700 text-xs">
                                        {{ carrier.code }}
                                    </div>
                                    <div>
                                        <div class="font-semibold text-slate-100 flex flex-wrap items-center gap-2">
                                            {{ carrier.name }}
                                           <span class="text-[10px] bg-blue-500/20 text-blue-300 px-2 py-0.5 rounded border border-blue-500/30">{{ carrier.vessel }}</span>
                                        </div>
                                        <div class="text-xs text-slate-400 mt-0.5">
                                            ETD: <strong class="text-slate-200">{{ carrier.etd }}</strong> | Biến động: <span class="text-rose-400 font-semibold">+{{ carrier.delayDays }} ngày trễ</span>
                                        </div>
                                    </div>
                                </div>
                                <div>
                                    <span v-if="carrier.marginPercent < 0" class="px-3 py-1.5 rounded-lg bg-rose-500/20 text-rose-300 border border-rose-500/30 text-xs font-semibold inline-flex items-center gap-1.5">
                                        <i class="fa-solid fa-circle-xmark"></i> Lô hàng đang lỗ
                                    </span>
                                    <span v-else-if="carrier.marginPercent < targetMargin" class="px-3 py-1.5 rounded-lg bg-amber-500/20 text-amber-300 border border-amber-500/30 text-xs font-semibold inline-flex items-center gap-1.5">
                                        <i class="fa-solid fa-triangle-exclamation"></i> Biên lãi dưới mục tiêu {{ targetMargin }}%
                                    </span>
                                    <span v-else class="px-3 py-1.5 rounded-lg bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-semibold inline-flex items-center gap-1.5">
                                        <i class="fa-solid fa-circle-check"></i> Đạt biên lãi mục tiêu
                                    </span>
                                </div>
                           </div>

                           <!-- Dòng 2: bảng chi phí (giá vốn) -->
                           <div class="overflow-x-auto rounded-lg border border-slate-800 bg-slate-950/60">
                               <table class="w-full text-xs">
                                   <thead>
                                       <tr class="text-slate-500 text-left border-b border-slate-800">
                                           <th class="p-2 font-medium">Khoản chi phí (giá vốn)</th>
                                           <th class="p-2 font-medium text-right">Đơn giá</th>
                                           <th class="p-2 font-medium text-right">Tính theo</th>
                                           <th class="p-2 font-medium text-right">Thành tiền</th>
                                       </tr>
                                   </thead>
                                   <tbody class="text-slate-300">
                                       <tr class="border-b border-slate-800/60">
                                           <td class="p-2">Cước biển (O/F)</td>
                                           <td class="p-2 text-right">${{ carrier.oceanFreight.toLocaleString() }}</td>
                                           <td class="p-2 text-right text-slate-500">{{ shipment.volume }} cont</td>
                                           <td class="p-2 text-right font-semibold text-slate-100">${{ (carrier.oceanFreight * shipment.volume).toLocaleString() }}</td>
                                       </tr>
                                       <tr class="border-b border-slate-800/60">
                                           <td class="p-2">THC (xếp dỡ tại cảng đi)</td>
                                           <td class="p-2 text-right">${{ carrier.thc }}</td>
                                           <td class="p-2 text-right text-slate-500">{{ shipment.volume }} cont</td>
                                           <td class="p-2 text-right font-semibold text-slate-100">${{ (carrier.thc * shipment.volume).toLocaleString() }}</td>
                                       </tr>
                                       <tr class="border-b border-slate-800/60">
                                           <td class="p-2">Seal (niêm phong)</td>
                                           <td class="p-2 text-right">${{ carrier.seal }}</td>
                                           <td class="p-2 text-right text-slate-500">{{ shipment.volume }} cont</td>
                                           <td class="p-2 text-right font-semibold text-slate-100">${{ (carrier.seal * shipment.volume).toLocaleString() }}</td>
                                       </tr>
                                       <tr class="border-b border-slate-800/60">
                                           <td class="p-2">Chứng từ & handling tại POL <span class="text-slate-500">(AMS, Telex, Docs, Handling)</span></td>
                                           <td class="p-2 text-right">${{ carrier.billFeesBuy }}</td>
                                           <td class="p-2 text-right text-slate-500">1 lô</td>
                                           <td class="p-2 text-right font-semibold text-slate-100">${{ carrier.billFeesBuy }}</td>
                                       </tr>
                                       <tr class="border-b border-slate-800/60">
                                           <td class="p-2">Handling tại POD</td>
                                           <td class="p-2 text-right">${{ carrier.handlingPod }}</td>
                                           <td class="p-2 text-right text-slate-500">1 lô</td>
                                           <td class="p-2 text-right font-semibold text-slate-100">${{ carrier.handlingPod }}</td>
                                       </tr>
                                       <tr class="border-b border-slate-800/60">
                                           <td class="p-2">Dự phòng rủi ro</td>
                                           <td class="p-2 text-right">${{ carrier.reserveFee }}</td>
                                           <td class="p-2 text-right text-slate-500">1 lô</td>
                                           <td class="p-2 text-right font-semibold text-slate-100">${{ carrier.reserveFee }}</td>
                                       </tr>
                                   </tbody>
                                   <tfoot>
                                       <tr class="bg-slate-900/80">
                                           <td class="p-2 font-bold text-slate-200" colspan="3">
                                               Tổng giá vốn toàn lô <span class="font-normal text-slate-500">(≈ ${{ carrier.avgCostPerCont.toLocaleString() }} / cont)</span>
                                           </td>
                                           <td class="p-2 text-right font-bold text-blue-400 text-sm">${{ carrier.totalCostShipment.toLocaleString() }}</td>
                                       </tr>
                                   </tfoot>
                               </table>
                           </div>

                           <!-- Dòng 3: 4 chỉ số chính -->
                           <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
                                <div class="bg-slate-950/60 border border-slate-800 rounded-lg p-3">
                                   <span class="text-slate-400 block mb-1">Giá bán cước ($/cont)</span>
                                   <input type="number" :value="carrier.currentSellRate" @input="onSellRateInput($event)" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-slate-100 font-bold">
                                </div>
                                <div class="bg-slate-950/60 border border-slate-800 rounded-lg p-3">
                                   <span class="text-slate-400 block mb-1">Giá bán tối thiểu (đạt {{ targetMargin }}%)</span>
                                   <span class="font-bold text-emerald-400 text-base">${{ carrier.minSellRateRequired.toLocaleString() }}</span>
                                   <span class="text-slate-500"> /cont</span>
                                </div>
                                <div class="bg-slate-950/60 border border-slate-800 rounded-lg p-3">
                                   <span class="text-slate-400 block mb-1">Biên lợi nhuận gộp</span>
                                   <span class="font-bold text-base" :class="carrier.marginPercent < 0 ? 'text-rose-400' : (carrier.marginPercent < targetMargin ? 'text-amber-400' : 'text-emerald-400')">{{ carrier.marginPercent }}%</span>
                                </div>
                                <div class="bg-slate-950/60 border border-slate-800 rounded-lg p-3">
                                   <span class="text-slate-400 block mb-1">Tổng lãi toàn lô</span>
                                   <span class="font-bold text-base" :class="carrier.totalProfit < 0 ? 'text-rose-400' : 'text-emerald-400'">{{ carrier.totalProfit < 0 ? '-' : '' }}${{ Math.abs(carrier.totalProfit).toLocaleString() }}</span>
                                   <span class="text-slate-500 block">Doanh thu: ${{ carrier.totalRevenue.toLocaleString() }}</span>
                                </div>
                           </div>
                       </div>
                   </div>
               </div>
            </div>
<!-- TAB 4: DỰ BÁO SPACE -->
            <div v-if="currentTab === 'spaceForecast'" class="space-y-6 w-full">
               <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-5 w-full">
                   <div class="flex flex-col md:flex-row md:items-center justify-between gap-3 pb-3 border-b border-slate-700/60">
                       <h3 class="text-sm font-bold text-amber-400 flex items-center gap-2">
                           <i class="fa-solid fa-shield-halved"></i> Dự Báo Rủi Ro Thiếu Space Theo Mùa Vụ
                       </h3>
                       <div class="flex items-center gap-2 text-xs">
                           <span class="text-slate-400">Tuyến: <strong class="text-slate-200">{{ shipment.pol }} → {{ shipment.pod }}</strong></span>
                           <span class="text-slate-400 ml-2">Tháng xuất hàng:</span>
                           <select v-model.number="forecastMonth" class="bg-slate-900 border border-slate-700 rounded-lg p-1.5 text-slate-100">
                               <option v-for="i in 12" :key="i" :value="i">Tháng {{ i }}</option>
                           </select>
                       </div>
                   </div>

                   <!-- 4 chỉ số chính -->
                   <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
                       <div class="bg-slate-900/70 border border-slate-700 rounded-xl p-4">
                           <div class="text-slate-400 mb-1">Chỉ số căng thẳng space</div>
                           <div class="text-2xl font-bold" :class="levelNow.text">{{ stressNow }}<span class="text-sm text-slate-500">/100</span></div>
                           <span class="inline-block mt-2 px-2 py-0.5 rounded border font-semibold" :class="levelNow.badge">Rủi ro {{ levelNow.label }}</span>
                       </div>
                       <div class="bg-slate-900/70 border border-slate-700 rounded-xl p-4">
                           <div class="text-slate-400 mb-1">Giá slot dự kiến tăng</div>
                           <div class="text-2xl font-bold text-amber-400">+{{ premiumNow }}%</div>
                           <div class="text-[11px] text-slate-500 mt-2">So với giá nền ngoài mùa cao điểm</div>
                       </div>
                       <div class="bg-slate-900/70 border border-slate-700 rounded-xl p-4">
                           <div class="text-slate-400 mb-1">Cung / Cầu trên sàn</div>
                           <div class="text-2xl font-bold" :class="supplyDemand.short ? 'text-rose-400' : 'text-emerald-400'">{{ supplyDemand.supply }} / {{ supplyDemand.demand }}</div>
                           <div class="text-[11px] text-slate-500 mt-2">
                               {{ supplyDemand.short ? 'Thiếu ' + supplyDemand.gap + ' slot (cầu lớn hơn cung)' : 'Cung đang đủ cầu' }}
                           </div>
                       </div>
                       <div class="bg-slate-900/70 border border-slate-700 rounded-xl p-4">
                           <div class="text-slate-400 mb-1">Biên lãi nếu mua slot giá cao</div>
                           <div class="text-2xl font-bold" :class="marginImpact.newMargin < 0 ? 'text-rose-400' : (marginImpact.newMargin < targetMargin ? 'text-amber-400' : 'text-emerald-400')">{{ marginImpact.newMargin }}%</div>
                           <div class="text-[11px] text-slate-500 mt-2">Hiện tại {{ marginImpact.base }}% · phát sinh +${{ marginImpact.extra.toLocaleString() }}</div>
                       </div>
                   </div>

                   <!-- Biểu đồ 12 tháng -->
                   <div class="bg-slate-900/70 border border-slate-700 rounded-xl p-4 text-xs">
                       <div class="font-bold text-slate-200 text-sm mb-3">Chỉ số căng thẳng space theo tháng</div>
                       <div class="flex items-end gap-1.5 h-40">
                           <div v-for="d in monthlyStress" :key="d.m" class="flex-1 flex flex-col items-center justify-end h-full cursor-pointer" @click="forecastMonth = d.m">
                               <span class="text-[10px] text-slate-400 mb-1">{{ d.idx }}</span>
                               <div class="w-full rounded-t transition-all" :class="[levelOf(d.idx).bar, d.m === forecastMonth ? 'ring-2 ring-white' : 'opacity-70']" :style="{ height: d.idx + '%' }"></div>
                           </div>
                       </div>
                       <div class="flex gap-1.5 mt-1.5">
                           <div v-for="d in monthlyStress" :key="'l' + d.m" class="flex-1 text-center text-slate-400" :class="d.m === forecastMonth ? 'text-white font-bold' : ''">T{{ d.m }}</div>
                       </div>
                       <div class="flex flex-wrap gap-4 mt-3 text-slate-400">
                           <span><span class="inline-block w-2.5 h-2.5 rounded bg-rose-500 mr-1"></span>Cao (≥70)</span>
                           <span><span class="inline-block w-2.5 h-2.5 rounded bg-amber-500 mr-1"></span>Trung bình (40-69)</span>
                           <span><span class="inline-block w-2.5 h-2.5 rounded bg-emerald-500 mr-1"></span>Thấp (<40)</span>
                           <span class="text-slate-500">Bấm vào cột để chọn tháng. Số liệu giả định phục vụ mô phỏng.</span>
                       </div>
                   </div>

                   <!-- Cảnh báo theo tuyến -->
                   <div class="bg-slate-900/70 border border-slate-700 rounded-xl p-4 text-xs">
                       <div class="font-bold text-slate-200 text-sm mb-3">Cảnh báo theo cảng đến (Tháng {{ forecastMonth }})</div>
                       <div class="overflow-x-auto">
                           <table class="w-full">
                               <thead>
                                   <tr class="text-slate-500 text-left border-b border-slate-800">
                                       <th class="p-2 font-medium">Cảng đến</th>
                                       <th class="p-2 font-medium text-right">Chỉ số</th>
                                       <th class="p-2 font-medium text-right">Giá tăng dự kiến</th>
                                       <th class="p-2 font-medium text-right">Mức rủi ro</th>
                                   </tr>
                               </thead>
                               <tbody class="text-slate-300">
                                   <tr v-for="r in routeStress" :key="r.code" class="border-b border-slate-800/60" :class="r.code === podCode ? 'bg-blue-500/10' : ''">
                                       <td class="p-2">{{ r.name }} <span v-if="r.code === podCode" class="text-blue-400">(lô hàng này)</span></td>
                                       <td class="p-2 text-right font-semibold">{{ r.score }}</td>
                                       <td class="p-2 text-right">+{{ r.prem }}%</td>
                                       <td class="p-2 text-right"><span class="px-2 py-0.5 rounded border font-semibold" :class="r.level.badge">{{ r.level.label }}</span></td>
                                   </tr>
                               </tbody>
                           </table>
                       </div>
                   </div>

                   <!-- Khuyến nghị + chuyển sang sàn -->
                   <div class="p-4 rounded-xl border text-xs flex flex-col md:flex-row md:items-center justify-between gap-3"
                        :class="levelNow.label === 'Cao' ? 'bg-rose-500/10 border-rose-500/30' : 'bg-slate-900/70 border-slate-700'">
                       <div class="text-slate-300 leading-relaxed">
                           <strong :class="levelNow.text">Khuyến nghị:</strong>
                           <span v-if="levelNow.label === 'Cao'"> Rủi ro thiếu space cao. Nên chốt booking sớm hoặc mua slot trên sàn trước khi giá tăng thêm. Chi phí phát sinh ước tính +${{ marginImpact.extra.toLocaleString() }} cho cả lô.</span>
                           <span v-else-if="levelNow.label === 'Trung bình'"> Rủi ro trung bình. Nên đặt trước 2 – 3 tuần và theo dõi tin "Cần space" trên sàn.</span>
                           <span v-else> Rủi ro thấp. Có thể đặt booking theo quy trình thông thường.</span>
                       </div>
                       <button @click="currentTab = 'marketplace'" class="shrink-0 bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded-lg font-medium transition">
                           <i class="fa-solid fa-right-left mr-1"></i> Xem slot khả dụng trên sàn
                       </button>
                   </div>
               </div>
            </div>

            <!-- TAB 5: BIẾN ĐỘNG CUNG – CẦU SPACE -->
            <div v-if="currentTab === 'peakSeason'" class="space-y-6 w-full">
               <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-5 w-full">
                   <h3 class="text-sm font-bold text-amber-400 flex items-center gap-2">
                       <i class="fa-solid fa-chart-line"></i> Các Yếu Tố Gây Biến Động Cung – Cầu & Thiếu Hụt Space
                   </h3>

                   <!-- Lịch 12 tháng -->
                   <div class="bg-slate-900/70 border border-slate-700 rounded-xl p-4 text-xs">
                       <div class="font-bold text-slate-200 text-sm mb-3">Lịch mùa vụ 12 tháng</div>
                       <div class="grid grid-cols-6 md:grid-cols-12 gap-1.5">
                           <div v-for="d in monthlyStress" :key="d.m" class="rounded-lg border p-2 text-center" :class="seasonOfMonth(d.m)">
                               <div class="font-bold">T{{ d.m }}</div>
                               <div class="text-[10px] mt-0.5">+{{ d.prem }}%</div>
                           </div>
                       </div>
                       <div class="flex flex-wrap gap-4 mt-3 text-slate-400">
                           <span><span class="inline-block w-2.5 h-2.5 rounded bg-blue-500 mr-1"></span>Mua sắm cuối năm</span>
                           <span><span class="inline-block w-2.5 h-2.5 rounded bg-amber-500 mr-1"></span>Trước Tết</span>
                           <span><span class="inline-block w-2.5 h-2.5 rounded bg-slate-600 mr-1"></span>Ngoài cao điểm</span>
                       </div>
                   </div>

                   <!-- Các yếu tố -->
                   <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 text-xs">
                       <div v-for="s in seasons" :key="s.key" class="bg-slate-900/70 p-4 rounded-xl border border-slate-700 space-y-2">
                           <div class="font-bold text-sm" :class="{'text-blue-400': s.color==='blue', 'text-amber-400': s.color==='amber', 'text-rose-400': s.color==='rose', 'text-emerald-400': s.color==='emerald', 'text-slate-300': s.color==='slate'}">{{ s.name }}</div>
                           <p class="text-slate-300"><strong>Thời gian:</strong> {{ s.time }}</p>
                           <p class="text-slate-300"><strong>Đặc điểm:</strong> {{ s.trait }}</p>
                           <p class="text-slate-300"><strong>Mức tăng giá:</strong> {{ s.premium }}</p>
                           <p class="text-slate-300"><strong>Nên đặt trước:</strong> {{ s.lead }}</p>
                           <p class="text-slate-400 border-t border-slate-800 pt-2"><i class="fa-solid fa-lightbulb text-amber-400 mr-1"></i>{{ s.action }}</p>
                           <p class="text-[10px] text-slate-500"><i class="fa-solid fa-newspaper mr-1"></i>Nguồn tham khảo: {{ s.source }}</p>
                       </div>
                   </div>
                   <p class="text-[11px] text-slate-500">Mức tăng giá và thời gian đặt trước là số liệu giả định phục vụ mô phỏng, dựa trên xu hướng được báo chí ngành logistics nêu.</p>
               </div>
            </div>

            <!-- TAB 6: SÀN GIAO DỊCH SLOT MARKETPLACE -->
            <div v-if="currentTab === 'marketplace'" class="space-y-6 w-full">
               <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                   <div class="flex justify-between items-center pb-3 border-b border-slate-700/60">
                       <h3 class="text-sm font-bold text-emerald-400 flex items-center gap-2">
                           <i class="fa-solid fa-right-left"></i> Phân Hệ E: Sàn Chuyển Nhượng Slot Space (DEMO Marketplace)
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
                    // Giá bán cước do người dùng gõ tay (null = dùng giá tính tự động)
                    sellRateOverride: null,
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
                        etd: 'yyyy-mm-dd',
                        eta: 'yyyy-mm-dd'
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
                        bookingDate: 'yyyy-mm-dd',
                        etd: 'yyyy-mm-dd',
                        eta: 'yyyy-mm-dd'
                    },

                    // ====== BẢNG GIÁ NỀN (lấy từ rates.csv - tuyến R02: Cái Mép → LAX, 40'HC, Wan Hai) ======
                    // Giá nền chỉ có THẬT cho: Cái Mép → LAX, 40'HC. Các tuyến/cont khác = điều chỉnh bằng hệ số ƯỚC TÍNH
                    // (sửa số ở đây khi có báo giá thật của hãng tàu).
                    rateConfig: {
                        // Phí theo CONT (R02): THC 200/200, Seal 10/10 (giá mua / giá bán)
                        perCont: { thcBuy: 200, thcSell: 200, sealBuy: 10, sealSell: 10 },
                        // Phí theo BILL / LÔ (R02): chỉ tính 1 lần cho cả lô, không nhân số cont
                        perBill: [
                            { name: 'AMS', buy: 35, sell: 35 },
                            { name: 'Telex release', buy: 35, sell: 35 },
                            { name: 'Docs', buy: 38, sell: 38 },
                            { name: 'Handling fee (POL)', buy: 25, sell: 25 }
                        ],
                        // Handling tại POD (R02): chỉ có ở giá mua, 90 USD / lô
                        handlingPodBuy: 90,
                        // Hệ số cước biển theo cảng đến (so với LAX). LGB suy ra từ giá sàn slot trong app (5180/5200)
                        podFactor: {
                            'USLAX': { f: 1.00, src: 'dữ liệu R02' },
                            'USLGB': { f: 0.996, src: 'ước tính' },
                            'USNYC': { f: 1.45, src: 'ước tính' },
                            'USORF': { f: 1.50, src: 'ước tính' },
                            'USSAV': { f: 1.40, src: 'ước tính' }
                        },
                        // Phụ phí cảng đi (USD / cont 40') so với Cái Mép (feeder / chuyển tải)
                        polAddon: {
                            'VNVUT': { usd: 0, src: 'dữ liệu R02' },
                            'VNCLI': { usd: 100, src: 'ước tính' },
                            'VNSGN': { usd: 120, src: 'ước tính' },
                            'VNHPH': { usd: 300, src: 'ước tính' }
                        },
                        // Hệ số theo loại cont (so với 40'HC): of = cước biển, thc = THC
                        contFactor: {
                            "40'HC": { of: 1.00, thc: 1.00, src: 'dữ liệu R02' },
                            "40'GP": { of: 0.95, thc: 1.00, src: 'ước tính' },
                            "20'GP": { of: 0.60, thc: 0.65, src: 'ước tính' },
                            "45'HC": { of: 1.10, thc: 1.10, src: 'ước tính' },
                            "40'RF": { of: 1.90, thc: 1.50, src: 'ước tính' },
                            "20'RF": { of: 1.15, thc: 1.00, src: 'ước tính' },
                            "40'OT": { of: 1.35, thc: 1.30, src: 'ước tính' },
                            "20'OT": { of: 0.85, thc: 0.90, src: 'ước tính' },
                            "40'FR": { of: 1.60, thc: 1.40, src: 'ước tính' }
                        }
                    },

                    // Kho dữ liệu chi tiết cho từng hãng tàu (giúp đổi hãng tàu là đổi đúng chi phí cước & tên tàu)
                    // Lưu ý: oceanFreight / currentSellRate là giá 40'HC Cái Mép → LAX (giá nền), hệ thống sẽ tự điều chỉnh theo tuyến & loại cont.
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
                // Lấy mã cảng trong ngoặc, ví dụ "Cái Mép TCIT (VNVUT)" -> "VNVUT"
                polCode() {
                    const s = this.shipment.pol || '';
                    return s.slice(s.lastIndexOf('(') + 1, s.lastIndexOf(')'));
                },
                podCode() {
                    const s = this.shipment.pod || '';
                    return s.slice(s.lastIndexOf('(') + 1, s.lastIndexOf(')'));
                },
                // Các hệ số đang áp dụng cho lô hàng hiện tại
                quoteBasis() {
                    const cfg = this.rateConfig;
                    const pod = cfg.podFactor[this.podCode] || { f: 1.0, src: 'ước tính' };
                    const pol = cfg.polAddon[this.polCode] || { usd: 0, src: 'ước tính' };
                    const cont = cfg.contFactor[this.shipment.containerType] || { of: 1.0, thc: 1.0, src: 'ước tính' };
                    const isFullData = pod.src.indexOf('dữ liệu') === 0 && pol.src.indexOf('dữ liệu') === 0 && cont.src.indexOf('dữ liệu') === 0;
                    return {
                        podFactor: pod.f, podSrc: pod.src,
                        polAddon: pol.usd, polSrc: pol.src,
                        contOf: cont.of, contThc: cont.thc, contSrc: cont.src,
                        isFullData
                    };
                },
                evaluatedCarriers() {
                    const cfg = this.rateConfig;
                    const b = this.quoteBasis;
                    const n = Math.max(1, Number(this.shipment.volume) || 1);

                    return this.carriers.map(c => {
                        // 1) Cước biển / cont: giá nền 40'HC LAX của hãng tàu -> điều chỉnh theo POD, POL, loại cont
                        const baseBuy = c.oceanFreight;
                        const markup = c.currentSellRate / c.oceanFreight; // tỷ lệ giá bán / giá mua của hãng
                        const oceanBuy = Math.round((baseBuy * b.podFactor + b.polAddon) * b.contOf);
                        const oceanSellAuto = Math.round(oceanBuy * markup);
                        const oceanSell = (this.sellRateOverride !== null && this.sellRateOverride >= 0) ? this.sellRateOverride : oceanSellAuto;

                        // 2) Phí theo cont (nhân số lượng cont)
                        const thcBuy = Math.round(cfg.perCont.thcBuy * b.contThc);
                        const thcSell = Math.round(cfg.perCont.thcSell * b.contThc);
                        const seal = cfg.perCont.sealBuy;
                        const sealSell = cfg.perCont.sealSell;

                        // 3) Phí theo bill / lô (chỉ 1 lần)
                        const billFeesBuy = cfg.perBill.reduce((s, f) => s + f.buy, 0);
                        const billFeesSell = cfg.perBill.reduce((s, f) => s + f.sell, 0);
                        const handlingPod = cfg.handlingPodBuy;
                        const reserveFee = c.reserveFee || 0;

                        // 4) Tổng chi phí & doanh thu TOÀN LÔ
                        const totalCostShipment = n * (oceanBuy + thcBuy + seal) + billFeesBuy + handlingPod + reserveFee;
                        const totalRevenue = n * (oceanSell + thcSell + sealSell) + billFeesSell;
                        const totalProfit = totalRevenue - totalCostShipment;
                        const marginPercent = totalRevenue > 0 ? parseFloat(((totalProfit / totalRevenue) * 100).toFixed(1)) : 0;

                        // 5) Giá bán cước tối thiểu / cont để đạt biên lãi mục tiêu
                        const requiredRevenue = totalCostShipment / (1 - (this.targetMargin / 100));
                        const minSellRateRequired = Math.ceil((requiredRevenue - n * (thcSell + sealSell) - billFeesSell) / n);

                        return {
                            ...c,
                            oceanFreight: oceanBuy,
                            thc: thcBuy,
                            seal,
                            billFeesBuy,
                            handlingPod,
                            reserveFee,
                            currentSellRate: oceanSell,
                            totalCostShipment,
                            avgCostPerCont: Math.round(totalCostShipment / n),
                            totalRevenue,
                            minSellRateRequired,
                            totalProfit,
                            marginPercent
                        };
                    });
                },
                filteredMarketplaceList() {
                    return this.marketplaceList.filter(s => s.pol.includes(this.shipment.pol.split(' ')[0]));
                }
            },
            methods: {
                onSellRateInput(e) {
                    const v = parseFloat(e.target.value);
                    this.sellRateOverride = isNaN(v) ? null : v;
                },
                isValidDate(s) {
                    return !!s && !isNaN(Date.parse(s));
                },
                commitShipmentUpdate() {
                    this.shipment = JSON.parse(JSON.stringify(this.tempShipment));
                    this.sellRateOverride = null; // đổi lô hàng -> bỏ giá bán gõ tay, tính lại từ đầu
                    
                    // CẬP NHẬT CHÍNH XÁC HÃNG TÀU VÀ THÔNG SỐ CHI PHÍ TƯƠNG ƯNG
                    const selectedCarrierName = this.shipment.preferredCarrier || 'Wan Hai Lines';
                    const templateData = this.allCarriersData[selectedCarrierName] || this.allCarriersData['Wan Hai Lines'];

                    this.carriers = [{
                        id: 1,
                        name: templateData.name,
                        code: templateData.code,
                        vessel: templateData.vessel,
                        etd: this.isValidDate(this.shipment.etd) ? this.shipment.etd : '2025-10-15',
                        delayDays: templateData.delayDays,
                        oceanFreight: templateData.oceanFreight,
                        thc: templateData.thc,
                        sealDoc: templateData.sealDoc,
                        handlingPod: templateData.handlingPod,
                        reserveFee: templateData.reserveFee,
                        currentSellRate: templateData.currentSellRate
                    }];

                    this.lastUpdatedTime = new Date().toLocaleTimeString();
                    alert('Đã cập nhật thành công! Biểu giá, hãng tàu và thông tin lô hàng đã đồng bộ.');
                    this.currentTab = 'quotation';
                },
                resetToDefault() {
                    this.targetMargin = 10;
                    this.sellRateOverride = null;
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
                        etd: 'yyyy-mm-dd',
                        eta: 'yyyy-mm-dd'
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
