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
                          <div><strong>Booking / MBL:</strong> 039FX49604 | <strong>Vessel:</strong> WAN HAI A01 E012</div>
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
                          <i class="fa-solid fa-pen-to-square"></i> Cấu Hình & Chỉnh Sửa Thông Tin Lô Hàng (Input Trung Tâm)
                      </h3>
                      <span class="text-xs text-slate-400">Đồng bộ hóa toàn hệ thống sau khi xác nhận</span>
                  </div>

                  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
                      <!-- 1. Các bên liên quan -->
                      <div class="space-y-3 bg-slate-900/50 p-3 rounded-xl border border-slate-700/50">
                          <div class="font-semibold text-slate-200 border-b border-slate-700 pb-1">1. Các Bên Liên Quan</div>
                          <div>
                               <label class="text-slate-400 block mb-1">Shipper <span class="text-rose-400">*</span></label>
                               <input type="text" v-model="tempShipment.shipper" placeholder="Nhập tên doanh nghiệp gửi" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                               <span v-if="formErrors.shipper" class="text-rose-400 text-[10px] mt-1 block">{{ formErrors.shipper }}</span>
                          </div>
                          <div>
                               <label class="text-slate-400 block mb-1">Consignee <span class="text-rose-400">*</span></label>
                               <input type="text" v-model="tempShipment.consignee" placeholder="Nhập tên doanh nghiệp nhận" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                               <span v-if="formErrors.consignee" class="text-rose-400 text-[10px] mt-1 block">{{ formErrors.consignee }}</span>
                          </div>
                          <div>
                               <label class="text-slate-400 block mb-1">Sales Phụ Trách</label>
                               <select v-model="tempShipment.salesPerson" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                   <option value="Bắp (Sales Forwarding)">Bắp (Sales Forwarding)</option>
                                   <option value="An Nguyễn (Sales SCM)">An Nguyễn (Sales SCM)</option>
                                   <option value="Hà Linh (Key Account)">Hà Linh (Key Account)</option>
                               </select>
                          </div>
                      </div>

                      <!-- 2. Tuyến vận tải -->
                      <div class="space-y-3 bg-slate-900/50 p-3 rounded-xl border border-slate-700/50">
                          <div class="font-semibold text-slate-200 border-b border-slate-700 pb-1">2. Tuyến Vận Tải (POL / POD)</div>
                          <div>
                               <label class="text-slate-400 block mb-1">Cảng Đi (POL)</label>
                               <select v-model="tempShipment.pol" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                   <option value="Cái Mép TCIT (VNVUT)">Cái Mép TCIT (VNVUT)</option>
                                   <option value="Cát Lái (VNCLI)">Cát Lái (VNCLI)</option>
                                   <option value="Hải Phòng (VNHPH)">Hải Phòng (VNHPH)</option>
                               </select>
                          </div>
                          <div>
                               <label class="text-slate-400 block mb-1">Cảng Đến (POD)</label>
                               <select v-model="tempShipment.pod" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                   <option value="Los Angeles, CA (USLAX)">Los Angeles, CA (USLAX)</option>
                                   <option value="Long Beach, CA (USLGB)">Long Beach, CA (USLGB)</option>
                               </select>
                          </div>
                          <div>
                               <label class="text-slate-400 block mb-1">Loại Hàng Hóa <span class="text-rose-400">*</span></label>
                               <input type="text" v-model="tempShipment.commodity" placeholder="Ví dụ: Wooden kitchen cabinets (HS 940340)" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                               <span v-if="formErrors.commodity" class="text-rose-400 text-[10px] mt-1 block">{{ formErrors.commodity }}</span>
                          </div>
                      </div>

                      <!-- 3. Quy mô & Container -->
                      <div class="space-y-3 bg-slate-900/50 p-3 rounded-xl border border-slate-700/50">
                          <div class="font-semibold text-slate-200 border-b border-slate-700 pb-1">3. Quy Mô & Container</div>
                          <div class="grid grid-cols-2 gap-2">
                               <div>
                                   <label class="text-slate-400 block mb-1">Loại Cont</label>
                                   <select v-model="tempShipment.containerType" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                       <option value="20'GP">20'GP</option>
                                       <option value="40'GP">40'GP</option>
                                       <option value="40'HC">40'HC</option>
                                       <option value="45'HC">45'HC</option>
                                   </select>
                               </div>
                               <div>
                                   <label class="text-slate-400 block mb-1">Số Lượng <span class="text-rose-400">*</span></label>
                                   <input type="number" min="1" max="100" v-model.number="tempShipment.volume" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-amber-400 font-bold">
                                   <span v-if="formErrors.volume" class="text-rose-400 text-[10px] mt-1 block">{{ formErrors.volume }}</span>
                               </div>
                          </div>
                          <div>
                               <label class="text-slate-400 block mb-1">Hãng Tàu</label>
                               <select v-model="tempShipment.preferredCarrier" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                   <option value="Wan Hai Lines">Wan Hai Lines</option>
                                   <option value="Evergreen Line">Evergreen Line</option>
                                   <option value="COSCO Shipping">COSCO Shipping</option>
                               </select>
                          </div>
                          <div>
                               <label class="text-slate-400 block mb-1">Mục Tiêu Biên Lãi (%) <span class="text-rose-400">*</span></label>
                               <input type="number" step="0.1" min="0" max="100" v-model.number="targetMargin" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-blue-400 font-bold">
                               <span v-if="formErrors.targetMargin" class="text-rose-400 text-[10px] mt-1 block">{{ formErrors.targetMargin }}</span>
                          </div>
                      </div>

                      <!-- 4. Lịch trình (Chuẩn giao diện dd/mm/yyyy kèm icon lịch) -->
                      <div class="space-y-3 bg-slate-900/50 p-3 rounded-xl border border-slate-700/50">
                          <div class="font-semibold text-slate-200 border-b border-slate-700 pb-1">4. Lịch Trình (DD/MM/YYYY)</div>
                          <div>
                               <label class="text-slate-400 block mb-1">Ngày dự kiến đặt booking</label>
                               <div class="relative">
                                    <input type="text" v-model="tempShipment.bookingDate" placeholder="dd/mm/yyyy" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 pr-10 text-slate-100 font-mono text-xs">
                                    <span class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none text-slate-400">
                                        <i class="fa-regular fa-calendar"></i>
                                    </span>
                               </div>
                               <span v-if="formErrors.bookingDate" class="text-rose-400 text-[10px] mt-1 block">{{ formErrors.bookingDate }}</span>
                          </div>
                          <div>
                               <label class="text-slate-400 block mb-1">ETD Thực Tế</label>
                               <div class="relative">
                                    <input type="text" v-model="tempShipment.etd" placeholder="dd/mm/yyyy" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 pr-10 text-slate-100 font-mono text-xs">
                                    <span class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none text-slate-400">
                                        <i class="fa-regular fa-calendar"></i>
                                    </span>
                               </div>
                               <span v-if="formErrors.etd" class="text-rose-400 text-[10px] mt-1 block">{{ formErrors.etd }}</span>
                          </div>
                          <div>
                               <label class="text-slate-400 block mb-1">ETA Los Angeles</label>
                               <div class="relative">
                                    <input type="text" v-model="tempShipment.eta" placeholder="dd/mm/yyyy" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 pr-10 text-slate-100 font-mono text-xs">
                                    <span class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none text-slate-400">
                                        <i class="fa-regular fa-calendar"></i>
                                    </span>
                               </div>
                               <span v-if="formErrors.eta" class="text-rose-400 text-[10px] mt-1 block">{{ formErrors.eta }}</span>
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
                                            {{ carrier.marginPercent }}% (Nhạy cảm)
                                       </span>
                                    </div>
                                    <div>
                                       <span class="text-slate-400 block">Tổng Lãi Toàn Lô ({{ shipment.volume }} cont)</span>
                                       <span class="font-bold text-emerald-400">${{ carrier.totalProfit.toLocaleString() }} USD</span>
                                    </div>
                                </div>

                                <div>
                                    <span class="px-3 py-1.5 rounded-lg bg-amber-500/20 text-amber-300 border border-amber-500/30 text-xs font-semibold flex items-center gap-1.5">
                                        <i class="fa-solid fa-triangle-exclamation"></i> Biên lãi mỏng dưới mục tiêu
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
                      <i class="fa-solid fa-shield-halved"></i> Phân Hệ C: Phân Tích Rủi Ro Thiếu Hụt Space
                  </h3>
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                      <div class="bg-slate-900/70 p-4 rounded-xl border border-slate-700 space-y-2">
                          <div class="font-bold text-white text-sm">Nguyên Nhân Thiếu Space Giai Đoạn Cao Điểm</div>
                          <p class="text-slate-300">• Làn sóng đẩy hàng (front-loading) mạnh mẽ trước thời hạn áp dụng thuế quan hàng hóa xuất khẩu.</p>
                          <p class="text-slate-300">• Yêu cầu giữ chỗ đồng thời số lượng lớn container tạo sức ép tải trọng lên hãng tàu.</p>
                      </div>
                      <div class="bg-gradient-to-br from-rose-500/10 to-orange-500/10 p-4 rounded-xl border border-rose-500/30 space-y-2">
                          <div class="font-bold text-rose-400 text-sm"><i class="fa-solid fa-triangle-exclamation mr-1"></i> Tác Động Tài Chính & Vận Hành</div>
                          <p class="text-slate-300">• Biên lợi nhuận lô hàng mỏng, dễ bị xóa sạch nếu phát sinh chi phí lưu bãi hoặc mua space giá cao.</p>
                          <p class="text-slate-300">• Nguy cơ hàng đến chậm so với yêu cầu của Consignee tại điểm đến.</p>
                      </div>
                  </div>
               </div>
            </div>

            <!-- TAB 5: MÙA CAO ĐIỂM -->
            <div v-if="currentTab === 'peakSeason'" class="space-y-6 w-full">
               <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                  <h3 class="text-sm font-bold text-amber-400 flex items-center gap-2">
                      <i class="fa-solid fa-calendar-days"></i> Phân Hệ D: Nhận Diện Mùa Cao Điểm & Bối Cảnh Chính Sách Thương Mại
                  </h3>
                  <div class="space-y-3 text-xs text-slate-300 leading-relaxed bg-slate-900/70 p-4 rounded-xl border border-slate-700">
                      <div><strong>Sự kiện / Nguyên nhân:</strong> Làn sóng "chạy nước rút" xuất khẩu hàng hóa trước các mốc rà soát và áp thuế đối ứng.</div>
                      <div><strong>Khung thời gian cao điểm:</strong> Giai đoạn thị trường chịu áp lực cung ứng mạnh.</div>
                      <div><strong>Khuyến nghị cho Sales Forwarding:</strong> Cần chủ động khảo sát giá và đặt chỗ trước ít nhất 4 tuần đối với các lô hàng quy mô lớn trong các giai đoạn biến động chính sách thương mại.</div>
                  </div>
               </div>
            </div>

            <!-- TAB 6: SÀN GIAO DỊCH SLOT MARKETPLACE -->
            <div v-if="currentTab === 'marketplace'" class="space-y-6 w-full">
               <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                  <div class="flex justify-between items-center pb-3 border-b border-slate-700/60">
                      <h3 class="text-sm font-bold text-emerald-400 flex items-center gap-2">
                          <i class="fa-solid fa-right-left"></i> Phân Hệ E: Sàn Chuyển Nhượng Slot Space (DEMO Marketplace)
                      </h3>
                      <span class="text-xs text-slate-400">Tuyến: <strong>Cái Mép → Los Angeles</strong></span>
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
                                <span class="text-slate-300">Khả dụng: <strong>{{ slot.slots }} slot 40'HC</strong></span>
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
                   formErrors: {},
                   shipment: {
                       shipper: 'QA Furniture Co., Ltd (Bình Phước)',
                       consignee: 'MTA Cabinets LLC (Texas)',
                       salesPerson: 'Bắp (Sales Forwarding)',
                       pol: 'Cái Mép TCIT (VNVUT)',
                       pod: 'Los Angeles, CA (USLAX)',
                       commodity: 'Wooden kitchen cabinets (HS 940340)',
                       containerType: "40'HC",
                       volume: 5,
                       preferredCarrier: 'Wan Hai Lines',
                       bookingDate: '13/10/2026',
                       etd: '15/10/2026',
                       eta: '30/10/2026'
                   },
                   tempShipment: {
                       shipper: 'Tên doanh nghiệp/cá nhân',
                       consignee: 'Tên doanh nghiệp/cá nhân',
                       salesPerson: 'Tên',
                       pol: '',
                       pod: '',
                       commodity: '',
                       containerType: "",
                       volume: ,
                       preferredCarrier: '',
                       bookingDate: 'dd/mm/yyyy',
                       etd: 'dd/mm/yyyy',
                       eta: 'dd/mm/yyyy'
                   },
                   carriers: [
                       {
                           id: 1,
                           name: 'Wan Hai Lines',
                           code: 'WHL',
                           vessel: 'WAN HAI A01 E012',
                           etd: '15/10/2026',
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
                       { id: 201, provider: 'VinaFreighter Partner', carrier: 'Evergreen', route: 'Cái Mép TCIT → Los Angeles', pol: 'Cái Mép TCIT (VNVUT)', pod: 'Los Angeles, CA (USLAX)', etd: '14/10/2026', slots: 3, price: 5200 },
                       { id: 202, provider: 'Global Logistics Corp', carrier: 'COSCO', route: 'Cái Mép TCIT → Long Beach', pol: 'Cái Mép TCIT (VNVUT)', pod: 'Long Beach, CA (USLGB)', etd: '16/10/2026', slots: 2, price: 5180 }
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
                    return this.marketplaceList.filter(s => s.pol.includes('Cái Mép'));
                }
            },
            methods: {
                isValidDate(dateStr) {
                    const regex = /^(\\d{2})\\/(\\d{2})\\/(\\d{4})$/;
                    if (!regex.test(dateStr)) return false;
                    const parts = dateStr.split('/');
                    const day = parseInt(parts[0], 10);
                    const month = parseInt(parts[1], 10);
                    const year = parseInt(parts[2], 10);
                    if (year < 2000 || year > 2100 || month < 1 || month > 12) return false;
                    const daysInMonth = new Date(year, month, 0).getDate();
                    return day >= 1 && day <= daysInMonth;
                },
                validateForm() {
                    this.formErrors = {};
                    if (!this.tempShipment.shipper || this.tempShipment.shipper.trim() === '') {
                        this.formErrors.shipper = 'Shipper không được để trống.';
                    }
                    if (!this.tempShipment.consignee || this.tempShipment.consignee.trim() === '') {
                        this.formErrors.consignee = 'Consignee không được để trống.';
                    }
                    if (!this.tempShipment.commodity || this.tempShipment.commodity.trim() === '') {
                        this.formErrors.commodity = 'Loại hàng hóa không được để trống.';
                    }
                    if (!this.tempShipment.volume || this.tempShipment.volume <= 0 || !Number.isInteger(this.tempShipment.volume)) {
                        this.formErrors.volume = 'Số lượng phải là số nguyên dương.';
                    }
                    if (this.targetMargin === null || this.targetMargin < 0 || this.targetMargin > 100) {
                        this.formErrors.targetMargin = 'Biên lãi phải từ 0 đến 100%.';
                    }
                    if (!this.isValidDate(this.tempShipment.bookingDate)) {
                        this.formErrors.bookingDate = 'Sai định dạng hoặc ngày không tồn tại (dd/mm/yyyy).';
                    }
                    if (!this.isValidDate(this.tempShipment.etd)) {
                        this.formErrors.etd = 'Sai định dạng hoặc ngày không tồn tại (dd/mm/yyyy).';
                    }
                    if (!this.isValidDate(this.tempShipment.eta)) {
                        this.formErrors.eta = 'Sai định dạng hoặc ngày không tồn tại (dd/mm/yyyy).';
                    }
                    return Object.keys(this.formErrors).length === 0;
                },
                commitShipmentUpdate() {
                    if (!this.validateForm()) {
                        alert('Vui lòng kiểm tra lại các trường thông tin bị lỗi bên dưới.');
                        return;
                    }
                    this.shipment = JSON.parse(JSON.stringify(this.tempShipment));
                    
                    this.carriers.forEach(carrier => {
                        carrier.etd = this.shipment.etd;
                    });

                    this.lastUpdatedTime = new Date().toLocaleTimeString();
                    alert('Đã cập nhật thành công! Ngày ETD và toàn bộ bảng giá đã được đồng bộ.');
                    this.currentTab = 'quotation';
                },
                resetToDefault() {
                    this.targetMargin = 10;
                    this.formErrors = {};
                    this.shipment = {
                        shipper: 'QA Furniture Co., Ltd (Bình Phước)',
                        consignee: 'MTA Cabinets LLC (Texas)',
                        salesPerson: 'Bắp (Sales Forwarding)',
                        pol: 'Cái Mép TCIT (VNVUT)',
                        pod: 'Los Angeles, CA (USLAX)',
                        commodity: 'Wooden kitchen cabinets (HS 940340)',
                        containerType: "40'HC",
                        volume: 5,
                        preferredCarrier: 'Wan Hai Lines',
                        bookingDate: '13/10/2026',
                        etd: '15/10/2026',
                        eta: '30/10/2026'
                    };
                    this.tempShipment = JSON.parse(JSON.stringify(this.shipment));
                    this.carriers.forEach(carrier => {
                        carrier.etd = this.shipment.etd;
                    });
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
