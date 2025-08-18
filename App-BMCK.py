import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import webbrowser
import random
import time
from datetime import datetime

def create_window(title, width, height, bg_color="lightblue"):
    window = tk.Toplevel()
    window.title(title)
    window.geometry(f"{width}x{height}+100+200")
    window.resizable(0, 0)
    window.configure(bg=bg_color)
    return window




def create_button(parent, text, command, row, column, width=20, height=2, bg="light gray", fg="blue"):
    button = tk.Button(
        parent,
        text=text,
        command=command,
        width=width,
        height=height,
        bg=bg,
        fg=fg,
        font=("Helvetica", 11, "bold")
    )
    button.grid(row=row, column=column, padx=10, pady=10)
    return button

def add_mouseover_effect(widget):
    widget.bind("<Enter>", lambda event, w=widget: w.config(bg='lightcyan'))
    widget.bind("<Leave>", lambda event, w=widget: w.config(bg='light gray'))
    
def open_link(url):
    webbrowser.open(url)




def open_second_window():  
    #second_window = create_window("THỜI KHÓA BIỂU", 300, 250, "darkkhaki")
    second_window = tk.Toplevel()
    second_window.title("THỜI KHÓA BIỂU")
    second_window.geometry("210x200") 
    second_window.resizable(0, 0)
    second_window.config(bg="darkkhaki")



    # Cập nhật vị trí cửa sổ con khi cửa sổ chính di chuyển
    def update_position(event=None):
        x = window.winfo_x()-200  # Dịch chuyển cửa sổ con so với cửa sổ chính
        y = window.winfo_y() 
        second_window.geometry(f"+{x}+{y}")
    # Gọi update_position ngay khi mở cửa sổ
    update_position()
    # Liên kết sự kiện di chuyển cửa sổ chính
    window.bind("<Configure>", update_position)





    def close_and_open_link(url):
        second_window.destroy()  # Đóng cửa sổ
        open_link(url)  # Mở liên kết



    label = tk.Label(second_window, text="THỜI KHÓA BIỂU", font=("Arial", 12, "bold"), fg="indigo")
    label.pack()
    label.configure(bg="darkkhaki") # màu nền của label
    label.place(x=30, y=1)

    label1 = create_button(second_window, "Thời khóa biểu - BMCK", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/1-GLufHecoWHBHYRRDjm78WnaKhigvyeO/edit?usp=sharing&ouid=115226777419629233366&rtpof=true&sd=true"), 1, 1)
    label2 = create_button(second_window, "Thời khóa biểu - Học sinh", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/11HJjkBye2CTxxnxbl-nNuq07JIZLgePX/edit#gid=2003349223"), 2, 1)
    label3 = create_button(second_window, "TKB - Các Bộ môn", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/1_6gCrtLA_1VQjnnRJ4jF0oZWp939YL_EYVSbUzgbbRE/edit?gid=0#gid=0"), 2, 1)
   
    label1.place(x=10, y=30)
    label2.place(x=10, y=85)
    label3.place(x=10, y=140)
    add_mouseover_effect(label1)
    add_mouseover_effect(label2)
    add_mouseover_effect(label3)
    return second_window




def open_third_window():
    #third_window = create_window("THÔNG TƯ - CÁC MẪU", 220, 250, "rosybrown")
    third_window = tk.Toplevel()
    third_window.title("THÔNG TƯ - CÁC MẪU")
    third_window.geometry("210x200") 
    third_window.resizable(0, 0)
    third_window.config(bg="rosybrown")


    # Cập nhật vị trí cửa sổ con khi cửa sổ chính di chuyển
    def update_position(event=None):
        x = window.winfo_x()-200  # Dịch chuyển cửa sổ con so với cửa sổ chính
        y = window.winfo_y() 
        third_window.geometry(f"+{x}+{y}")
    # Gọi update_position ngay khi mở cửa sổ
    update_position()
    # Liên kết sự kiện di chuyển cửa sổ chính
    window.bind("<Configure>", update_position)


    def close_and_open_link(url):
        third_window.destroy()  # Đóng cửa sổ
        open_link(url)  # Mở liên kết


    label = tk.Label(third_window, text="VĂN BẢN-THÔNG TƯ-CÁC MẪU", font=("Arial", 10, "bold"))
    label.pack()
    label.configure(bg="rosybrown") # màu nền của label
    label.place(x=5, y=1)
    label3 = create_button(third_window, "VĂN BẢN \nTHÔNG TƯ", lambda: close_and_open_link("https://drive.google.com/drive/folders/1tatWfHeSqBpwLA8DgM-YYEw7okp_BqSs?usp=sharing"), 1, 1)
    label4 = create_button(third_window, "CÁC MẪU", lambda: close_and_open_link("https://drive.google.com/drive/folders/1UTem6O1MEhg_d4J46XLxckp_QdnbEcPQ?usp=sharing"), 2, 1)
    label5 = create_button(third_window, "LINH TINH", lambda: close_and_open_link("https://drive.google.com/drive/folders/17YTOY56EQ5ZvyS4WFNob9Rs9JlSiiQzS?usp=sharing"), 3, 1)
    label3.place(x=15, y=30)
    label4.place(x=15, y=85)
    label5.place(x=15, y=140)
    add_mouseover_effect(label3)
    add_mouseover_effect(label4)
    add_mouseover_effect(label5)
    return third_window

def open_ei_window():
    ei_window = tk.Toplevel()
    ei_window.title("GIẢNG VIÊN")
    ei_window.geometry("210x200+170+10") 
    ei_window.resizable(0, 0)
    ei_window.config(bg="darkturquoise")
    def update_position(event=None):
        x = window.winfo_x()-200  # Dịch chuyển cửa sổ con so với cửa sổ chính
        y = window.winfo_y() 
        ei_window.geometry(f"+{x}+{y}")
    # Gọi update_position ngay khi mở cửa sổ
    update_position()
    # Liên kết sự kiện di chuyển cửa sổ chính
    window.bind("<Configure>", update_position)

    def close_and_open_link(url):
        ei_window.destroy()  # Đóng cửa sổ
        open_link(url)  # Mở liên kết


    label = tk.Label(ei_window, text="TIẾN ĐỘ - GIẢNG VIÊN", font=("Arial", 12, "bold", ), fg="firebrick") # có mục thay đổi màu chữ cho label
    label.pack()
    label.place(x=15, y=1)
    label.configure(bg="darkturquoise") # màu nền của label
    labe25 = create_button(ei_window, "TIẾN ĐỘ ", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/10jnf-pPUCI3PqNQZ2ve-w2zVx3RHf9i7DPe3M_XODvQ/edit?usp=sharing"), 1, 1,)
    labe26 = create_button(ei_window, "GIẢNG VIÊN", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/1sT7TP1Vc_tEs4WOelE7D4NFa34fOh0TiasBw6iBoso0/edit?usp=sharing"), 2, 1)
    labe27 = create_button(ei_window, "GIÁO ÁN", lambda: close_and_open_link("https://drive.google.com/drive/folders/1p6zAio5hwgFsS0lKsVNNTUgA21lDaBdE?usp=drive_link"), 3, 1)

    labe25.place(x=10, y=30)
    labe26.place(x=10, y=85)
    labe27.place(x=10, y=140)
    add_mouseover_effect(labe25)
    add_mouseover_effect(labe26) 
    add_mouseover_effect(labe27) 
    return ei_window

def open_fo_window():
    #fo_window = create_window("HỌC SINH-SINH VIÊN", 300, 360, "burlywood")
    fo_window = tk.Toplevel()
    fo_window.title("HỌC SINH-SINH VIÊN")
    fo_window.geometry("210x320+1050+10")
    fo_window.resizable(0, 0)
    fo_window.config(bg="burlywood")
    def update_position(event=None):
        x = window.winfo_x()+630  # Dịch chuyển cửa sổ con so với cửa sổ chính
        y = window.winfo_y() 
        fo_window.geometry(f"+{x}+{y}")
    # Gọi update_position ngay khi mở cửa sổ
    update_position()
    # Liên kết sự kiện di chuyển cửa sổ chính
    window.bind("<Configure>", update_position)


    def close_and_open_link(url):
        fo_window.destroy()  # Đóng cửa sổ
        open_link(url)  # Mở liên kết


    label = tk.Label(fo_window, text="HỌC SINH-SINH VIÊN", font=("Arial", 12, "bold"), fg="darkred")
    label.pack()
    label.place(x=20, y=5)
    label.configure(bg="burlywood") # màu nền của label
    label6 = create_button(fo_window, "TỔ CHỨC HỌC LẠI và\nNHẬP ĐIỂM PHẦN MỀM", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/1EWR6hQ8dm6djX1p1_JTpKocdA8LLdCR_TYXw66V19ws/edit?gid=0#gid=0"), 1, 1,)
    label7 = create_button(fo_window, "NHẬP DANH SÁCH \nHỌC SINH HỌC LẠI", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/1ZkZUlHxq1PzJEdymRBhdf3CLRzrNfTgLiWFHz3n-Neg/edit?usp=sharing"), 2, 1)
    label8 = create_button(fo_window, "HỌC BỔNG", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/1rnRYmZekGWg1FjdOyxKF4eNKp4klke2X3_UR9mWku9w/edit?gid=2020826915#gid=2020826915"), 2, 1)
    label9 = create_button(fo_window, "GIẤY BÁO NGHỈ", lambda: close_and_open_link("https://drive.google.com/drive/folders/14aBHBJGNHFx-lQQwwPsapa7ecUuSj-or?usp=drive_link"), 2, 1)
    labe20 = create_button(fo_window, "KHEN THƯỞNG-KỸ LUẬT", lambda: close_and_open_link("https://drive.google.com/drive/folders/1IybIl87KyofBtK8JDclt5gtSMUEUvWWJ?usp=sharing"), 2, 1)

    label6.place(x=10, y=40)
    label7.place(x=10, y=95)
    label8.place(x=10, y=150)
    label9.place(x=10, y=205)
    labe20.place(x=10, y=260)
    add_mouseover_effect(label6)
    add_mouseover_effect(label7) 
    add_mouseover_effect(label8)   
    add_mouseover_effect(label9)       
    add_mouseover_effect(labe20)      
    return fo_window



def open_fi_window():
    #fi_window = create_window("CÁC KẾ HOẠCH", 300, 320, "lightslategray")
    fi_window = tk.Toplevel()
    fi_window.title("CÁC KẾ HOẠCH")
    fi_window.geometry("210x270")
    fi_window.resizable(0, 0)
    fi_window.config(bg="lightslategray")

    def update_position(event=None):
        x = window.winfo_x()+630  # Dịch chuyển cửa sổ con so với cửa sổ chính
        y = window.winfo_y() 
        fi_window.geometry(f"+{x}+{y}")
    # Gọi update_position ngay khi mở cửa sổ
    update_position()
    # Liên kết sự kiện di chuyển cửa sổ chính
    window.bind("<Configure>", update_position)



    def close_and_open_link(url):
        fi_window.destroy()  # Đóng cửa sổ
        open_link(url)  # Mở liên kết
    label = tk.Label(fi_window, text="CÁC KẾ HOẠCH THI", font=("Arial", 12, "bold"), fg="indigo")
    label.pack()
    label.place(x=20, y=5)
    label.configure(bg="lightslategray") # màu nền của label
    label1 = create_button(fi_window, "KẾ HOẠCH \nLỊCH THI - CHẤM THI", lambda: close_and_open_link("https://drive.google.com/drive/folders/1kAZs1vFC5oMCtVYQmr-CX64STp5KbQtq?usp=drive_link"), 1, 1)
    label2 = create_button(fi_window, "ĐĂNG KÝ THI HỌC KỲ", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/1jg2QTOCaRIGonJZkR4GZGF54wYgJWLzd-L9s4u0Qh0E/edit?usp=sharing"), 2, 1)
    label3 = create_button(fi_window, "NHẬP DANH SÁCH THI \nLẦN 2", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/18yStCMHSz1DPWtu5LllSvLMSzDjMB9CnwGdI8vbYO9A/edit?gid=0#gid=0"), 2, 1)
    label4 = create_button(fi_window, "NHẬP ĐIỂM THI LẠI \n PHẦN MỀM", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/1Wi78CdKYcF_-21H3EUpwTc-Dm3WwIuDcplyepxCmEYE/edit?gid=1782914929#gid=1782914929"), 2, 1)

    label1.place(x=10, y=40)
    label2.place(x=10, y=95)
    label3.place(x=10, y=150)
    label4.place(x=10, y=205)
    add_mouseover_effect(label1)
    add_mouseover_effect(label2)    
    add_mouseover_effect(label3)    
    add_mouseover_effect(label4) 
    return fi_window
def open_six_window():
    six_window = tk.Toplevel()
    six_window.title("HỢP ĐỒNG")
    six_window.geometry("230x160+730+525")
    six_window.resizable(0, 0)
    six_window.config(bg="teal")

    def update_position(event=None):
        x = window.winfo_x()+630  # Dịch chuyển cửa sổ con so với cửa sổ chính
        y = window.winfo_y() 
        six_window.geometry(f"+{x}+{y}")
    # Gọi update_position ngay khi mở cửa sổ
    update_position()
    # Liên kết sự kiện di chuyển cửa sổ chính
    window.bind("<Configure>", update_position)

    def close_and_open_link(url):
        six_window.destroy()  # Đóng cửa sổ
        open_link(url)  # Mở liên kết   


    label = tk.Label(six_window, text="HỢP ĐỒNG", font=("Arial", 16, "bold"), fg="#ffffff")
    label.pack()
    label.place(x=60, y=5)
    label.configure(bg="teal") # màu nền của label
    labe21 = create_button(six_window, "THÔNG TIN HỢP ĐỒNG \n ĐÃ GỬI ĐÀO TẠO", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/1jXcTNumkATOTiVL6m4lDp92831KxLLMP/edit?usp=sharing&ouid=113986693805597278554&rtpof=true&sd=true"), 1, 1,)
    labe22 = create_button(six_window, "GVBM CẬP NHẬT \nTHÔNG TIN HỢP ĐỒNG", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/1LulXtbfdPJvK2iIT9qY0t_1q-9mx4L9Ys3tiaJ5aKN0/edit?gid=0#gid=0"), 2, 1)

    labe21.place(x=20, y=40)
    labe22.place(x=20, y=100)
 
    add_mouseover_effect(labe21)
    add_mouseover_effect(labe22) 
    return six_window
def open_sev_window():
    sev_window = tk.Toplevel()
    sev_window.title("KẾ HOẠCH GIÁO VIÊN")
    sev_window.geometry("205x160")  
    sev_window.resizable(0, 0)
    sev_window.config(bg="seagreen")
    # Cập nhật vị trí cửa sổ con khi cửa sổ chính di chuyển
    def update_position(event=None):
        x = window.winfo_x()-200  # Dịch chuyển cửa sổ con so với cửa sổ chính
        y = window.winfo_y() 
        sev_window.geometry(f"+{x}+{y}")
    # Gọi update_position ngay khi mở cửa sổ
    update_position()
    # Liên kết sự kiện di chuyển cửa sổ chính
    window.bind("<Configure>", update_position)
    def close_and_open_link(url):
        sev_window.destroy()  # Đóng cửa sổ
        open_link(url)  # Mở liên kết   

    label = tk.Label(sev_window, text="KẾ HOẠCH GIÁO VIÊN", font=("Arial", 12, "bold"))
    label.pack()
    label.place(x=20, y=5)
    label.configure(bg="seagreen") # màu nền của label
    labe23 = create_button(sev_window, "KẾ HOẠCH GIÁO VIÊN", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/1oBvNUbxI2O5Cl-FSrLBpP2HSV5GB8Fwc/edit?gid=2118481048#gid=2118481048&fvid=960532466"), 1, 1,)
    labe24 = create_button(sev_window, "KẾ HOẠCH GIÁO VIÊN \nNỘP ĐÀO TẠO", lambda: close_and_open_link("https://docs.google.com/spreadsheets/d/1VolZ5qfg9o5NVd_LihUFBgjH_y2G7vQ4W0srK_L0Up4/edit?gid=0#gid=0"), 2, 1)

    labe23.place(x=10, y=40)
    labe24.place(x=10, y=100)
 
    add_mouseover_effect(labe23)
    add_mouseover_effect(labe24) 

    return sev_window



def create_link_button(parent, label, url, row, column, button_fg_color):
    button = create_button(parent, label, lambda: open_link(url), row, column, fg=button_fg_color)
    button.bind("<Enter>", lambda event, b=button: b.config(bg='lightcyan'))
    button.bind("<Leave>", lambda event, b=button: b.config(bg='light gray'))

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    window.after(1000, update_clock)

def update_date():
    current_date = time.strftime("%d/%m/%Y")
    date_label.config(text=current_date)
    window.after(1000, update_date)
# Từ điển để theo dõi trạng thái của cửa sổ con
windows_state = {}


# Các hàm mở cửa sổ con (có thể thay bằng logic cụ thể của bạn)
def toggle_window(window_name, create_window_func):
    global windows_state
    
    if windows_state.get(window_name, False):  # Nếu cửa sổ đã mở
        # Đóng cửa sổ con
        windows_state[window_name].destroy()
        windows_state[window_name] = False
    else:  # Nếu cửa sổ chưa mở
        # Tạo cửa sổ con
        new_window = create_window_func()
        windows_state[window_name] = new_window



def center_window(window, width=630, height=485):
    screen_width = window.winfo_screenwidth()  # Lấy chiều rộng màn hình
    screen_height = window.winfo_screenheight()  # Lấy chiều cao màn hình

    x = (screen_width - width) // 2  # Vị trí X để căn giữa
    y = (screen_height - height) // 2  # Vị trí Y để căn giữa

    window.geometry(f"{width}x{height}+{x}+{y}")  # Đặt lại vị trí cửa sổ

    # Đảm bảo bố cục hiển thị đều
    window.update_idletasks()

window = tk.Tk()
window.title("TRƯỜNG CAO ĐẲNG LONG AN - CƠ SỞ ĐỨC HÒA ")
window.geometry("630x485+400+10")
window.resizable(0, 0)
window.configure(bg="lightblue")
# thay đổi icon của cửa sổ window
icon = tk.PhotoImage(file=r"icon.png")
# Set it as the window icon.



window.iconphoto(True, icon)
links = [
    #{"label": "TIẾN ĐỘ - GIẢNG VIÊN", "command": open_ei_window},
    
    {"label": "TIẾN ĐỘ - GIẢNG VIÊN", "command": lambda: toggle_window("TIẾN ĐỘ - GIẢNG VIÊN", open_ei_window)},

    #{"label": "TIẾN ĐỘ - GIẢNG VIÊN", "command":  open_ei_window},
    {"label": "Thời khóa biểu", "command": lambda: toggle_window("Thời khóa biểu", open_second_window)},
    #{"label": "HỌC SINH - SINH VIÊN", "command": open_fo_window},

    {"label": "HỌC SINH-SINH VIÊN", "command": lambda: toggle_window("HỌC SINH-SINH VIÊN", open_fo_window)},
    {"label": "WEB CĐ Long An", "url": "https://www.lac.edu.vn"},





    #{"label": "Kế hoạch giáo viên", "command": open_sev_window},
    {"label": "Kế hoạch giáo viên", "command":lambda: toggle_window("Kế hoạch giáo viên", open_sev_window)},



    #{"label": "CÁC KẾ HOẠCH THI", "command": open_fi_window},
    {"label": "CÁC KẾ HOẠCH THI",  "command":lambda: toggle_window("CÁC KẾ HOẠCH THI", open_fi_window)},
   
    {"label": "Đăng nhập \nNhập điểm trên WEB", "url": "https://giangvien.lac.edu.vn/login.html"},
    {"label": "Phiếu điểm", "url": "https://drive.google.com/drive/folders/1csXvguAUp_r_wcoLQZppTGEuC-72jWqY?usp=sharing"},
    #{"label": "Hợp Đồng", "command": open_six_window},
    {"label": "Hợp Đồng",  "command":lambda: toggle_window("Hợp Đồng", open_six_window)},
   
    {"label": "Hộp thư góp ý \n BỘ MÔN CƠ KHÍ", "url": "https://forms.gle/rpT7yfBwWVVLURp56"},
    {"label": "TIẾN ĐỘ \n HỒ SƠ SỔ SÁCH", "url": "https://docs.google.com/spreadsheets/d/1Hpm9s-WUNYQK2phw4a5Norp5zBOMxUGhE2Qa4ON9kfg/edit?usp=sharing"},
    {"label": "Tài sản CCDC \n BMCK", "url": "https://drive.google.com/drive/folders/12q6HsgYL7fq5zR7Pe8_ACzaqCtkqehpI?usp=sharing"},
   
    {"label": "Nhiệm Vụ \n Trưởng-Phó BMCK", "url": "https://docs.google.com/spreadsheets/d/1GqpWX_Z_cUGRGdwzhyCoWy-N9l6xXJ9l/edit?usp=share_link&ouid=113986693805597278554&rtpof=true&sd=true",},
    #{"label": "VĂN BẢN - CÁC MẪU \n THÔNG TƯ ", "command": open_third_window},
    {"label": "VĂN BẢN - CÁC MẪU \n THÔNG TƯ ",  "command":lambda: toggle_window("VĂN BẢN - CÁC MẪU \n THÔNG TƯ", open_third_window)},


    {"label": "Báo cáo \n Máy móc thiết bị", "url": "https://drive.google.com/drive/folders/1aCzF7LaQyGEr_8dKRm0H15y5A410kpl4?usp=sharing"},
  
   
]

# Màu chữ cho từng nút liên kết
button_fg_colors = [
    "red", "green", "blue", "maroon", "green", "blue", "maroon", "green", "blue", "maroon", "green", "blue", "maroon", "green", "blue", 
]


background_image = Image.open(r"Bg.PNG")
photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(window, image=photo)
background_label.place(relwidth=1, relheight=0.5)

title_label = tk.Label(window, text="LIÊN KẾT CÔNG VIỆC \nBỘ MÔN CƠ KHÍ", font=(("Old Style", 28,)))
title_label.pack(pady=20)
title_label.configure(bg="light blue")



title_label = tk.Label(window, text="Version 09.25", font=(("Old Style", 8,)))
title_label.place(x=557, y=110)
title_label.configure(bg="lightblue")



button_grid = tk.Frame(window)
button_grid.pack()
button_grid.configure(bg="lightblue")

num_columns = 3

for i, item in enumerate(links):
    label = item["label"]
    url = item.get("url")
    command = item.get("command")

    row = i // num_columns
    col = i % num_columns

    if url:
        create_link_button(button_grid, label, url, row, col, button_fg_colors[i])
    elif command:
        create_button(button_grid, label, command, row, col, fg=button_fg_colors[i])


clock_frame = tk.Frame(window)
clock_frame.pack()
clock_frame.place(x=2, y=0)

date_frame = tk.Frame(window)
date_frame.pack()
date_frame.place(x=540, y=0)

clock_label = tk.Label(clock_frame, text="", font=("Times New Roman", 14, "bold"))
clock_label.pack()

date_label = tk.Label(date_frame, text="", font=("Times New Roman", 13, "bold"))
date_label.pack()

update_clock()
update_date()

center_window(window)

window.mainloop()
