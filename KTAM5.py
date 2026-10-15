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

html_code = """<!DOCTYPE html>
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
                       <i class="fa-solid fa-chart-line mr-1"></i> Biến Động Cung – Cầu Space
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
                       <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-medium">Đã nạp dữ liệu chuẩn (U&I Logistics Network)</span>
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
                                   <option v-for="p in polOptions" :key="p" :value="p">{{ p }}</option>
                               </select>
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Cảng Đến (POD)</label>
                               <select v-model="tempShipment.pod" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                   <option v-for="d in podOptions" :key="d" :value="d">{{ d }}</option>
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
                   <div class="flex flex-col md:flex-row md:justify-between md:items-center gap-1 pb-3 border-b border-slate-700/60">
                       <h3 class="text-sm font-bold text-blue-400 flex items-center gap-2">
                           <i class="fa-solid fa-file-invoice-dollar"></i> Báo Giá & Kiểm Soát Biên Lợi Nhuận
                       </h3>
                       <span class="text-xs text-slate-400">Lô hàng: <strong class="text-slate-200">{{ shipment.volume }} x {{ shipment.containerType }}</strong> | {{ shipment.pol }} → {{ shipment.pod }}</span>
                   </div>

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
                                   <tr v-for="r in dynamicRouteStress" :key="r.code" class="border-b border-slate-800/60" :class="r.code === podCode ? 'bg-blue-500/20 font-semibold text-blue-200' : ''">
                                       <td class="p-2">{{ r.name }}</td>
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

            <!-- TAB 6: SÀN RAO BÁN & CHUYỂN NHƯỢNG SPACE (MARKETPLACE) -->
            <div v-if="currentTab === 'marketplace'" class="space-y-6 w-full">
               <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-5 w-full">
                   <div class="flex flex-col md:flex-row justify-between items-center gap-3 pb-3 border-b border-slate-700/60">
                       <h3 class="text-sm font-bold text-emerald-400 flex items-center gap-2">
                           <i class="fa-solid fa-store"></i> Sàn Rao Bán & Chuyển Nhượng Space (LogiSpace Exchange)
                       </h3>
                       <button @click="showPostModal = !showPostModal" class="bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-2 shadow-lg">
                           <i class="fa-solid fa-plus"></i> {{ showPostModal ? 'Đóng Form Rao Bán' : 'Đăng Bán / Rao Mua Slot' }}
                       </button>
                   </div>

                   <!-- FORM ĐĂNG TIN MỚI -->
                   <div v-if="showPostModal" class="bg-slate-900 border border-emerald-500/40 rounded-xl p-4 space-y-4 text-xs animate-fadeIn">
                       <div class="font-bold text-slate-200 text-sm border-b border-slate-800 pb-2 flex items-center gap-2">
                           <i class="fa-solid fa-bullhorn text-emerald-400"></i> Tạo Tin Đăng Mới Lên Sàn
                       </div>
                       <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3">
                           <div>
                               <label class="text-slate-400 block mb-1">Loại tin đăng</label>
                               <select v-model="newPost.type" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100 font-semibold">
                                   <option value="SELL">Bán / Nhượng Space (Có sẵn slot)</option>
                                   <option value="BUY">Cần Mua Space (Đang tìm slot gấp)</option>
                               </select>
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Công ty / Đơn vị đăng</label>
                               <input type="text" v-model="newPost.provider" placeholder="VD: U&I Logistics" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Cảng đi (POL)</label>
                               <select v-model="newPost.pol" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                   <option v-for="p in polOptions" :key="p" :value="p">{{ p }}</option>
                               </select>
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Cảng đến (POD)</label>
                               <select v-model="newPost.pod" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                   <option v-for="d in podOptions" :key="d" :value="d">{{ d }}</option>
                               </select>
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Hãng tàu</label>
                               <select v-model="newPost.carrier" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                   <option value="Wan Hai Lines">Wan Hai Lines</option>
                                   <option value="Evergreen Line">Evergreen Line</option>
                                   <option value="COSCO Shipping">COSCO Shipping</option>
                                   <option value="Maersk Line">Maersk Line</option>
                                   <option value="MSC">MSC</option>
                                   <option value="CMA CGM">CMA CGM</option>
                               </select>
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Số lượng Slot & Cont</label>
                               <div class="flex gap-2">
                                   <input type="number" min="1" v-model.number="newPost.slots" class="w-16 bg-slate-800 border border-slate-700 rounded-lg p-2 text-amber-400 font-bold text-center">
                                   <select v-model="newPost.containerType" class="flex-1 bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                       <option value="40'HC">40'HC</option>
                                       <option value="40'GP">40'GP</option>
                                       <option value="20'GP">20'GP</option>
                                       <option value="45'HC">45'HC</option>
                                   </select>
                               </div>
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Giá chào (USD / Cont)</label>
                               <input type="number" v-model.number="newPost.price" placeholder="VD: 5250" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-emerald-400 font-bold">
                           </div>
                           <div>
                               <label class="text-slate-400 block mb-1">Ngày tàu chạy (ETD)</label>
                               <input type="date" v-model="newPost.etd" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                           </div>
                       </div>
                       <div class="flex justify-end gap-2 pt-2 border-t border-slate-800">
                           <button @click="showPostModal = false" class="bg-slate-800 hover:bg-slate-700 text-slate-300 px-4 py-2 rounded-lg transition">Hủy</button>
                           <button @click="submitMarketplacePost" class="bg-emerald-600 hover:bg-emerald-500 text-white px-5 py-2 rounded-lg font-bold shadow transition">
                               <i class="fa-solid fa-check mr-1"></i> Đăng Tin Lên Sàn
                           </button>
                       </div>
                   </div>

                   <!-- BỘ LỌC TÌM KIẾM TRÊN SÀN -->
                   <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
                       <div>
                           <label class="text-slate-400 block mb-1">Lọc theo loại giao dịch</label>
                           <select v-model="marketFilter.type" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                               <option value="ALL">Tất cả tin đăng (Bán & Mua)</option>
                               <option value="SELL">Tin Rao Bán / Nhượng Space</option>
                               <option value="BUY">Tin Cần Mua Space Gấp</option>
                           </select>
                       </div>
                       <div>
                           <label class="text-slate-400 block mb-1">Lọc theo Cảng đến (POD)</label>
                           <select v-model="marketFilter.pod" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                               <option value="ALL">Tất cả cảng đến</option>
                               <option v-for="d in podOptions" :key="'f' + d" :value="d">{{ d }}</option>
                           </select>
                       </div>
                       <div>
                           <label class="text-slate-400 block mb-1">Tìm kiếm nhanh hãng tàu / đơn vị</label>
                           <input type="text" v-model="marketFilter.keyword" placeholder="Nhập tên hãng tàu, công ty..." class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                       </div>
                   </div>

                   <!-- DANH SÁCH TIN ĐĂNG TRÊN SÀN -->
                   <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
                       <div v-for="slot in filteredMarketplaceExchange" :key="slot.id" class="bg-slate-900/70 border rounded-xl p-4 flex flex-col justify-between gap-3 text-xs transition hover:border-slate-500"
                            :class="slot.type === 'SELL' ? 'border-emerald-500/40 shadow-emerald-950/20' : 'border-blue-500/40 shadow-blue-950/20'">
                           <div class="flex justify-between items-start">
                                <div>
                                    <div class="flex items-center gap-2 mb-1">
                                        <span class="px-2 py-0.5 rounded font-bold text-[10px]" :class="slot.type === 'SELL' ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30' : 'bg-blue-500/20 text-blue-300 border border-blue-500/30'">
                                            {{ slot.type === 'SELL' ? 'BÁN NHƯỢNG SPACE' : 'CẦU MUA SPACE' }}
                                        </span>
                                        <span class="text-slate-400 text-[11px]"><i class="fa-regular fa-building mr-1"></i>{{ slot.provider }}</span>
                                    </div>
                                    <div class="font-bold text-slate-100 text-sm mt-1">Hãng tàu: <span class="text-blue-400">{{ slot.carrier }}</span></div>
                                    <div class="text-slate-300 mt-0.5">Tuyến: <strong>{{ slot.pol }} → {{ slot.pod }}</strong></div>
                                    <div class="text-slate-400 mt-1">ETD: <strong class="text-slate-200">{{ slot.etd }}</strong></div>
                                </div>
                                <div class="text-right">
                                    <div class="text-slate-400">Giá chào giao dịch</div>
                                    <div class="text-base font-bold text-emerald-400">${{ slot.price.toLocaleString() }} <span class="text-[10px] text-slate-400">USD</span></div>
                                </div>
                           </div>
                           <div class="flex justify-between items-center pt-3 border-t border-slate-800">
                                <span class="text-slate-300">Khả dụng: <strong class="text-amber-400">{{ slot.slots }} slot {{ slot.containerType }}</strong></span>
                                <button @click="claimSlot(slot)" class="px-4 py-2 rounded-lg font-bold transition shadow"
                                        :class="slot.type === 'SELL' ? 'bg-emerald-600 hover:bg-emerald-500 text-white' : 'bg-blue-600 hover:bg-blue-500 text-white'">
                                    <i class="fa-solid fa-handshake mr-1"></i> {{ slot.type === 'SELL' ? 'Nhận Giữ Slot Này' : 'Cung Cấp Slot Match' }}
                                </button>
                           </div>
                       </div>
                   </div>
                   
                   <div v-if="filteredMarketplaceExchange.length === 0" class="text-center py-10 text-slate-500 text-xs">
                       Không tìm thấy tin đăng phù hợp với bộ lọc hiện tại.
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
                    forecastMonth: 10,
                    sellRateOverride: null,
                    showPostModal: false,
                    marketFilter: {
                        type: 'ALL',
                        pod: 'ALL',
                        keyword: ''
                    },
                    newPost: {
                        type: 'SELL',
                        provider: 'U&I Logistics Corp',
                        pol: 'Cái Mép TCIT (VNVUT)',
                        pod: 'Los Angeles, CA (USLAX)',
                        carrier: 'Wan Hai Lines',
                        slots: 2,
                        containerType: "40'HC",
                        price: 5250,
                        etd: '2026-10-20'
                    },
                    polOptions: [
                        'Cái Mép TCIT (VNVUT)',
                        'Cát Lái (VNCLI)',
                        'Sài Gòn (VNSGN)',
                        'Hải Phòng (VNHPH)',
                        'Đà Nẵng (VNDAD)',
                        'Quy Nhơn (VNUIH)'
                    ],
                    podOptions: [
                        'Los Angeles, CA (USLAX)',
                        'Long Beach, CA (USLGB)',
                        'New York, NY/NJ (USNYC)',
                        'Savannah, GA (USSAV)',
                        'Seattle, WA (USSEA)',
                        'Rotterdam, NLD (NLRTM)',
                        'Hamburg, DEU (DEHAM)',
                        'Singapore, SGP (SGSIN)',
                        'Incheon, KOR (KRINC)',
                        'Tokyo, JPN (JPTKO)'
                    ],
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
                    rateConfig: {
                        perCont: { thcBuy: 200, thcSell: 200, sealBuy: 10, sealSell: 10 },
                        perBill: [
                            { name: 'AMS', buy: 35, sell: 35 },
                            { name: 'Telex release', buy: 35, sell: 35 },
                            { name: 'Docs', buy: 38, sell: 38 },
                            { name: 'Handling fee (POL)', buy: 25, sell: 25 }
                        ],
                        handlingPodBuy: 90,
                        podFactor: {
                            'USLAX': { f: 1.00, src: 'dữ liệu R02' },
                            'USLGB': { f: 0.996, src: 'ước tính' },
                            'USNYC': { f: 1.45, src: 'ước tính' },
                            'USSAV': { f: 1.40, src: 'ước tính' },
                            'USSEA': { f: 1.35, src: 'ước tính' },
                            'NLRTM': { f: 1.60, src: 'ước tính' },
                            'DEHAM': { f: 1.65, src: 'ước tính' },
                            'SGSIN': { f: 0.45, src: 'ước tính' },
                            'KRINC': { f: 0.55, src: 'ước tính' },
                            'JPTKO': { f: 0.50, src: 'ước tính' }
                        },
                        polAddon: {
                            'VNVUT': { usd: 0, src: 'dữ liệu R02' },
                            'VNCLI': { usd: 100, src: 'ước tính' },
                            'VNSGN': { usd: 120, src: 'ước tính' },
                            'VNHPH': { usd: 300, src: 'ước tính' },
                            'VNDAD': { usd: 200, src: 'ước tính' },
                            'VNUIH': { usd: 220, src: 'ước tính' }
                        },
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
                    allCarriersData: {
                        'Wan Hai Lines': { name: 'Wan Hai Lines', code: 'WHL', vessel: 'WAN HAI A01 E012', oceanFreight: 5230, thc: 200, sealDoc: 48, handlingPod: 90, reserveFee: 0, currentSellRate: 5438, delayDays: 2 },
                        'Evergreen Line': { name: 'Evergreen Line', code: 'EMC', vessel: 'EVER GIVEN V.088E', oceanFreight: 5150, thc: 200, sealDoc: 45, handlingPod: 90, reserveFee: 0, currentSellRate: 5350, delayDays: 1 },
                        'COSCO Shipping': { name: 'COSCO Shipping', code: 'COS', vessel: 'COSCO SHIPPING APEX', oceanFreight: 5100, thc: 200, sealDoc: 50, handlingPod: 90, reserveFee: 0, currentSellRate: 5300, delayDays: 3 },
                        'ONE (Ocean Network Express)': { name: 'ONE (Ocean Network Express)', code: 'ONE', vessel: 'ONE INNOVATION V.012', oceanFreight: 5300, thc: 200, sealDoc: 50, handlingPod: 90, reserveFee: 0, currentSellRate: 5550, delayDays: 1 },
                        'Maersk Line': { name: 'Maersk Line', code: 'MSK', vessel: 'MAERSK MC-KINNEY', oceanFreight: 5400, thc: 200, sealDoc: 50, handlingPod: 90, reserveFee: 0, currentSellRate: 5700, delayDays: 0 },
                        'MSC': { name: 'MSC', code: 'MSC', vessel: 'MSC IRINA V.021', oceanFreight: 5050, thc: 200, sealDoc: 45, handlingPod: 90, reserveFee: 0, currentSellRate: 5280, delayDays: 2 },
                        'CMA CGM': { name: 'CMA CGM', code: 'CMA', vessel: 'CMA CGM JACQUES SAADE', oceanFreight: 5250, thc: 200, sealDoc: 48, handlingPod: 90, reserveFee: 0, currentSellRate: 5490, delayDays: 1 }
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
                    marketplaceExchangeList: [
                        { id: 301, type: 'SELL', provider: 'VinaFreighter Partner', carrier: 'Evergreen Line', pol: 'Cái Mép TCIT (VNVUT)', pod: 'Los Angeles, CA (USLAX)', etd: '2026-10-14', slots: 3, containerType: "40'HC", price: 5200 },
                        { id: 302, type: 'SELL', provider: 'Global Logistics Corp', carrier: 'COSCO Shipping', pol: 'Cái Mép TCIT (VNVUT)', pod: 'Long Beach, CA (USLGB)', etd: '2026-10-16', slots: 2, containerType: "40'HC", price: 5180 },
                        { id: 303, type: 'BUY', provider: 'U&I Export Co.', carrier: 'Wan Hai Lines', pol: 'Cái Mép TCIT (VNVUT)', pod: 'New York, NY/NJ (USNYC)', etd: '2026-10-18', slots: 4, containerType: "40'HC", price: 7400 },
                        { id: 304, type: 'SELL', provider: 'TransOcean Vietnam', carrier: 'Maersk Line', pol: 'Cát Lái (VNCLI)', pod: 'Rotterdam, NLD (NLRTM)', etd: '2026-10-22', slots: 2, containerType: "40'HC", price: 8200 }
                    ],
                    monthlyStress: [
                        { m: 1, idx: 65, prem: 15 },
                        { m: 2, idx: 75, prem: 22 },
                        { m: 3, idx: 45, prem: 5 },
                        { m: 4, idx: 35, prem: 0 },
                        { m: 5, idx: 40, prem: 5 },
                        { m: 6, idx: 55, prem: 10 },
                        { m: 7, idx: 68, prem: 15 },
                        { m: 8, idx: 82, prem: 25 },
                        { m: 9, idx: 88, prem: 30 },
                        { m: 10, idx: 80, prem: 25 },
                        { m: 11, idx: 72, prem: 20 },
                        { m: 12, idx: 70, prem: 18 }
                    ],
                    seasons: [
                        { key: 'shopping', name: 'Mùa Mua Sắm Cuối Năm (Black Friday / Giáng Sinh)', time: 'Tháng 8 – 11', color: 'blue',
                          premium: '+18% đến +30%', lead: '4 – 6 tuần',
                          trait: 'Hàng tiêu dùng, bán lẻ và thương mại điện tử dồn về Mỹ trước mùa lễ. Chủ hàng đặt chỗ sớm khiến nguồn cung tàu không đủ đáp ứng.',
                          action: 'Chốt booking sớm, thương lượng allocation với hãng tàu, chuẩn bị ngân sách mua slot.',
                          source: 'Xeneta, DHL; chu kỳ mùa cao điểm quý 3' },
                        { key: 'tet', name: 'Trước Tết Nguyên Đán (Pre-Lunar New Year)', time: 'Tháng 12 – 2', color: 'amber',
                          premium: '+10% đến +25%', lead: '4 – 5 tuần',
                          trait: 'Nhà máy dồn hàng trước kỳ nghỉ Tết, hãng tàu tăng phụ phí mùa cao điểm (PSS), dễ thiếu vỏ container và nghẽn cảng.',
                          action: 'Đẩy lịch xuất sớm hơn kỳ nghỉ, giữ vỏ cont từ sớm, dự phòng chi phí lưu bãi.',
                          source: 'VASEP (PSS tăng 150 – 450 USD cuối 2020)' },
                        { key: 'tariff', name: 'Gom Hàng "Chạy" Mốc Thuế Quan', time: 'Theo sự kiện', color: 'rose',
                          premium: '+15% đến +40%', lead: '2 – 3 tuần',
                          trait: 'Chủ hàng đồng loạt xuất sớm trước mốc áp thuế mới của Mỹ, cầu tăng đột ngột, hút vỏ container và chỗ tàu, khó dự báo trước.',
                          action: 'Theo dõi tin chính sách, đặt trước mốc áp thuế, cân nhắc mua slot trên sàn.',
                          source: 'Cục Hàng hải VN (mốc 1/8/2024); Diễn đàn Doanh nghiệp (mốc 24/7/2026)' },
                        { key: 'route', name: 'Gián Đoạn Tuyến Tàu & Thiếu Vỏ Container Rỗng', time: 'Theo sự kiện', color: 'emerald',
                          premium: '+10% đến +30%', lead: '3 – 4 tuần',
                          trait: 'Khủng hoảng Biển Đỏ khiến tàu đi vòng, nguồn cung tàu thu hẹp. Hãng tàu bỏ cảng hoặc rút ngắn thời gian neo, vỏ cont rỗng bị hút về Trung Quốc.',
                          action: 'Đặt vỏ cont sớm, chấp nhận lịch tàu linh hoạt, chuẩn bị phương án rolling.',
                          source: 'Bertling/Xeneta; vnreview; Cục Hàng hải VN' },
                        { key: 'fuel', name: 'Biến Động Nhiên Liệu & Quy Định Môi Trường', time: 'Quanh năm', color: 'slate',
                          premium: 'Phụ phí BAF thay đổi', lead: 'Theo kỳ công bố của hãng',
                          trait: 'Điều chỉnh BAF và các quy định môi trường tác động trực tiếp đến chi phí vận hành, ảnh hưởng gián tiếp đến giá slot.',
                          action: 'Ghi rõ điều khoản điều chỉnh phụ phí trong báo giá cho khách.',
                          source: 'Thông lệ ngành' }
                    ]
                }
            },
            computed: {
                polCode() {
                    const s = this.shipment.pol || '';
                    return s.slice(s.lastIndexOf('(') + 1, s.lastIndexOf(')'));
                },
                podCode() {
                    const s = this.shipment.pod || '';
                    return s.slice(s.lastIndexOf('(') + 1, s.lastIndexOf(')'));
                },
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
                        const baseBuy = c.oceanFreight;
                        const markup = c.currentSellRate / c.oceanFreight;
                        const oceanBuy = Math.round((baseBuy * b.podFactor + b.polAddon) * b.contOf);
                        const oceanSellAuto = Math.round(oceanBuy * markup);
                        const oceanSell = (this.sellRateOverride !== null && this.sellRateOverride >= 0) ? this.sellRateOverride : oceanSellAuto;

                        const thcBuy = Math.round(cfg.perCont.thcBuy * b.contThc);
                        const thcSell = Math.round(cfg.perCont.thcSell * b.contThc);
                        const seal = cfg.perCont.sealBuy;
                        const sealSell = cfg.perCont.sealSell;

                        const billFeesBuy = cfg.perBill.reduce((s, f) => s + f.buy, 0);
                        const billFeesSell = cfg.perBill.reduce((s, f) => s + f.sell, 0);
                        const handlingPod = cfg.handlingPodBuy;
                        const reserveFee = c.reserveFee || 0;

                        const totalCostShipment = n * (oceanBuy + thcBuy + seal) + billFeesBuy + handlingPod + reserveFee;
                        const totalRevenue = n * (oceanSell + thcSell + sealSell) + billFeesSell;
                        const totalProfit = totalRevenue - totalCostShipment;
                        const marginPercent = totalRevenue > 0 ? parseFloat(((totalProfit / totalRevenue) * 100).toFixed(1)) : 0;

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
                    return this.marketplaceExchangeList.filter(s => s.pol.includes(this.shipment.pol.split(' ')[0]));
                },
                filteredMarketplaceExchange() {
                    return this.marketplaceExchangeList.filter(item => {
                        const matchType = (this.marketFilter.type === 'ALL' || item.type === this.marketFilter.type);
                        const matchPod = (this.marketFilter.pod === 'ALL' || item.pod === this.marketFilter.pod);
                        const kw = this.marketFilter.keyword.toLowerCase();
                        const matchKw = (!kw || item.carrier.toLowerCase().includes(kw) || item.provider.toLowerCase().includes(kw) || item.pod.toLowerCase().includes(kw));
                        return matchType && matchPod && matchKw;
                    });
                },
                stressNow() {
                    const item = this.monthlyStress.find(d => d.m === this.forecastMonth);
                    return item ? item.idx : 50;
                },
                premiumNow() {
                    const item = this.monthlyStress.find(d => d.m === this.forecastMonth);
                    return item ? item.prem : 10;
                },
                levelNow() {
                    return this.levelOf(this.stressNow);
                },
                supplyDemand() {
                    const high = this.stressNow >= 70;
                    return {
                        supply: high ? '3 slot' : '8 slot',
                        demand: high ? '7 slot' : '4 slot',
                        short: high,
                        gap: high ? 4 : 0
                    };
                },
                marginImpact() {
                    const extra = Math.round(this.stressNow * 15 * (this.shipment.volume || 1));
                    const baseCost = this.evaluatedCarriers[0] ? this.evaluatedCarriers[0].totalCostShipment : 50000;
                    const newCost = baseCost + extra;
                    const rev = this.evaluatedCarriers[0] ? this.evaluatedCarriers[0].totalRevenue : 55000;
                    const newMargin = rev > 0 ? parseFloat((((rev - newCost) / rev) * 100).toFixed(1)) : 0;
                    const baseMargin = this.evaluatedCarriers[0] ? this.evaluatedCarriers[0].marginPercent : 10;
                    return { base: baseMargin, newMargin, extra };
                },
                dynamicRouteStress() {
                    return [
                        { code: 'USLAX', name: 'Los Angeles, CA', score: Math.min(98, this.stressNow + 5), prem: this.premiumNow + 5, level: this.levelOf(this.stressNow + 5) },
                        { code: 'USLGB', name: 'Long Beach, CA', score: this.stressNow, prem: this.premiumNow, level: this.levelOf(this.stressNow) },
                        { code: 'USNYC', name: 'New York, NY/NJ', score: Math.max(20, this.stressNow - 10), prem: Math.max(0, this.premiumNow - 5), level: this.levelOf(this.stressNow - 10) },
                        { code: 'USSAV', name: 'Savannah, GA', score: Math.max(20, this.stressNow - 15), prem: Math.max(0, this.premiumNow - 8), level: this.levelOf(this.stressNow - 15) },
                        { code: 'USSEA', name: 'Seattle, WA', score: Math.max(25, this.stressNow - 8), prem: Math.max(0, this.premiumNow - 4), level: this.levelOf(this.stressNow - 8) },
                        { code: 'NLRTM', name: 'Rotterdam, NLD', score: Math.max(30, this.stressNow - 5), prem: Math.max(0, this.premiumNow - 2), level: this.levelOf(this.stressNow - 5) },
                        { code: 'DEHAM', name: 'Hamburg, DEU', score: Math.max(30, this.stressNow - 6), prem: Math.max(0, this.premiumNow - 3), level: this.levelOf(this.stressNow - 6) },
                        { code: 'SGSIN', name: 'Singapore, SGP', score: Math.max(15, this.stressNow - 25), prem: Math.max(0, this.premiumNow - 15), level: this.levelOf(this.stressNow - 25) },
                        { code: 'KRINC', name: 'Incheon, KOR', score: Math.max(20, this.stressNow - 20), prem: Math.max(0, this.premiumNow - 12), level: this.levelOf(this.stressNow - 20) },
                        { code: 'JPTKO', name: 'Tokyo, JPN', score: Math.max(18, this.stressNow - 22), prem: Math.max(0, this.premiumNow - 14), level: this.levelOf(this.stressNow - 22) }
                    ];
                }
            },
            methods: {
                levelOf(idx) {
                    if (idx >= 70) return { label: 'Cao', text: 'text-rose-400', badge: 'bg-rose-500/20 text-rose-300 border-rose-500/30', bar: 'bg-rose-500' };
                    if (idx >= 40) return { label: 'Trung bình', text: 'text-amber-400', badge: 'bg-amber-500/20 text-amber-300 border-amber-500/30', bar: 'bg-amber-500' };
                    return { label: 'Thấp', text: 'text-emerald-400', badge: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30', bar: 'bg-emerald-500' };
                },
                seasonOfMonth(m) {
                    if ([8, 9, 10, 11].includes(m)) return 'bg-blue-500/20 border-blue-500/40 text-blue-300';
                    if ([12, 1, 2].includes(m)) return 'bg-amber-500/20 border-amber-500/40 text-amber-300';
                    return 'bg-slate-800 border-slate-700 text-slate-400';
                },
                onSellRateInput(e) {
                    const v = parseFloat(e.target.value);
                    this.sellRateOverride = isNaN(v) ? null : v;
                },
                isValidDate(s) {
                    return !!s && !isNaN(Date.parse(s));
                },
                commitShipmentUpdate() {
                    this.shipment = JSON.parse(JSON.stringify(this.tempShipment));
                    this.sellRateOverride = null;
                    
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
                    this.forecastMonth = 10;
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
                submitMarketplacePost() {
                    if (!this.newPost.provider || !this.newPost.price) {
                        alert('Vui lòng điền đầy đủ tên đơn vị và giá chào!');
                        return;
                    }
                    const newEntry = {
                        id: Date.now(),
                        type: this.newPost.type,
                        provider: this.newPost.provider,
                        carrier: this.newPost.carrier,
                        pol: this.newPost.pol,
                        pod: this.newPost.pod,
                        etd: this.newPost.etd || '2026-10-25',
                        slots: this.newPost.slots,
                        containerType: this.newPost.containerType,
                        price: this.newPost.price
                    };
                    this.marketplaceExchangeList.unshift(newEntry);
                    this.showPostModal = false;
                    alert('Đã đăng tin thành công lên Sàn giao dịch LogiSpace Exchange!');
                },
                claimSlot(slot) {
                    if (slot.type === 'SELL') {
                        alert(`Thành công! Đã kết nối giao dịch nhận giữ ${slot.slots} slot (${slot.containerType}) từ ${slot.provider} với giá $${slot.price.toLocaleString()} USD.`);
                    } else {
                        alert(`Thành công! Đã gửi chào giá cung cấp slot cho yêu cầu của ${slot.provider}.`);
                    }
                }
            }
        }).mount('#app');
    </script>
</body>
</html>"""

st.components.v1.html(html_code, height=980, scrolling=True)
