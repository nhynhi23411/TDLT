def khau_hao_duong_thang(gia_mua, chi_phi_van_chuyen, so_nam_khau_hao):
  nguyen_gia = gia_mua + chi_phi_van_chuyen
  khau_hao_nam = nguyen_gia / so_nam_khau_hao
  khau_hao_thang = khau_hao_nam / 12
  khau_hao_luy_ke = 0
  print("Bảng kê khai khấu hao")
  print("-----------------------")
  print("Năm\tKhấu hao năm\tKhấu hao lũy kế\tGiá trị còn lại")
  for nam in range(1, so_nam_khau_hao + 1):
    khau_hao_luy_ke += khau_hao_nam
    gia_tri_con_lai = nguyen_gia - khau_hao_luy_ke
    if gia_tri_con_lai < 0:
      gia_tri_con_lai = 0
      khau_hao_luy_ke = nguyen_gia
    print(f"{nam}\t{khau_hao_nam:.2f}\t\t{khau_hao_luy_ke:.2f}\t\t{gia_tri_con_lai:.2f}")

gia_mua = float(input("Nhập giá mua tài sản: "))
chi_phi_van_chuyen = float(input("Nhập chi phí vận chuyển, lắp đặt: "))
so_nam_khau_hao = int(input("Nhập số năm khấu hao: "))

khau_hao_duong_thang(gia_mua, chi_phi_van_chuyen, so_nam_khau_hao)