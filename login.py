from pathlib import Path
from tkinter import messagebox

import customtkinter as ctk
from PIL import Image


# ============================================================
# MÀU SẮC
# ============================================================

PRIMARY = "#2563EB"
PRIMARY_HOVER = "#1D4ED8"

BACKGROUND = "#F8FAFC"
LEFT_BACKGROUND = "#E8F1FF"
WHITE = "#FFFFFF"

TEXT_MAIN = "#071333"
TEXT_SECONDARY = "#64748B"

BORDER = "#CBD5E1"
INPUT_BG = "#FFFFFF"


# ============================================================
# CỬA SỔ ĐĂNG NHẬP
# ============================================================

class LoginWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ----------------------------------------------------
        # Cấu hình cửa sổ
        # ----------------------------------------------------

        self.title("Quản Lý Thu Chi Cá Nhân")

        self.geometry("1400x800")
        self.minsize(1100, 650)

        self.configure(fg_color=BACKGROUND)

        # Đưa cửa sổ ra giữa màn hình
        self.center_window(1400, 800)

        # Chia cửa sổ thành 2 cột
        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(
            0,
            weight=1,
            uniform="login"
        )

        self.grid_columnconfigure(
            1,
            weight=1,
            uniform="login"
        )

        # Biến ghi nhớ đăng nhập
        self.remember_var = ctk.BooleanVar(value=True)

        # Biến kiểm tra hiện mật khẩu
        self.password_visible = False

        # Tạo giao diện
        self.create_left_panel()
        self.create_right_panel()

        # Enter = đăng nhập
        self.bind(
            "<Return>",
            lambda event: self.login()
        )

        # Focus vào username
        self.after(
            300,
            self.username_entry.focus_set
        )

    # ========================================================
    # ĐƯA WINDOW RA GIỮA
    # ========================================================

    def center_window(self, width, height):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(
            f"{width}x{height}+{x}+{y}"
        )

    # ========================================================
    # PHẦN BÊN TRÁI
    # ========================================================

    def create_left_panel(self):

        self.left_panel = ctk.CTkFrame(
            self,
            fg_color=LEFT_BACKGROUND,
            corner_radius=0
        )

        self.left_panel.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.left_panel.grid_columnconfigure(
            0,
            weight=1
        )

        # ====================================================
        # LOGO + TÊN PHẦN MỀM
        # ====================================================

        logo_area = ctk.CTkFrame(
            self.left_panel,
            fg_color="transparent"
        )

        logo_area.pack(
            pady=(75, 0)
        )

        # Logo màu xanh
        logo = ctk.CTkLabel(
            logo_area,

            text="💳",

            width=90,
            height=90,

            fg_color=PRIMARY,

            corner_radius=22,

            text_color=WHITE,

            font=ctk.CTkFont(
                size=42
            )
        )

        logo.pack(
            side="left",
            padx=(0, 25)
        )

        # Tên app
        app_name = ctk.CTkLabel(
            logo_area,

            text="Quản Lý Thu Chi\nCá Nhân",

            justify="left",

            text_color=TEXT_MAIN,

            font=ctk.CTkFont(
                size=36,
                weight="bold"
            )
        )

        app_name.pack(
            side="left"
        )

        # ====================================================
        # MÔ TẢ
        # ====================================================

        description = ctk.CTkLabel(
            self.left_panel,

            text=(
                "Theo dõi tài chính – Kiểm soát chi tiêu – "
                "Lập kế hoạch thông minh"
            ),

            text_color=TEXT_MAIN,

            font=ctk.CTkFont(
                size=16
            )
        )

        description.pack(
            pady=(25, 30)
        )

        # ====================================================
        # ẢNH
        # ====================================================

        # login.py nằm trong ui/
        # nên parent.parent chính là thư mục project
        project_path = Path(__file__).resolve().parent.parent

        image_path = (
            project_path
            / "assets"
            / "image"
            / "login_finance.png"
        )

        if image_path.exists():

            image = Image.open(image_path)

            # CTkImage tự scale ảnh
            self.finance_image = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=(520, 400)
            )

            image_label = ctk.CTkLabel(
                self.left_panel,
                text="",
                image=self.finance_image
            )

            image_label.pack(
                pady=(0, 20)
            )

        else:

            # Nếu sai đường dẫn ảnh
            error_label = ctk.CTkLabel(
                self.left_panel,

                text=(
                    "Không tìm thấy ảnh\n\n"
                    f"{image_path}"
                ),

                text_color="#DC2626",

                font=ctk.CTkFont(
                    size=16
                )
            )

            error_label.pack(
                pady=100
            )

    # ========================================================
    # PHẦN BÊN PHẢI
    # ========================================================

    def create_right_panel(self):

        self.right_panel = ctk.CTkFrame(
            self,
            fg_color=BACKGROUND,
            corner_radius=0
        )

        self.right_panel.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.right_panel.grid_rowconfigure(
            0,
            weight=1
        )

        self.right_panel.grid_rowconfigure(
            2,
            weight=1
        )

        self.right_panel.grid_columnconfigure(
            0,
            weight=1
        )

        # ====================================================
        # CARD LOGIN
        # ====================================================

        self.login_card = ctk.CTkFrame(
            self.right_panel,

            width=560,
            height=620,

            fg_color=WHITE,

            corner_radius=22,

            border_width=1,
            border_color="#E2E8F0"
        )

        self.login_card.grid(
            row=1,
            column=0,

            padx=60,
            pady=20
        )

        # Giữ đúng kích thước card
        self.login_card.grid_propagate(False)

        self.login_card.grid_columnconfigure(
            0,
            weight=1
        )

        # ====================================================
        # TIÊU ĐỀ
        # ====================================================

        title = ctk.CTkLabel(
            self.login_card,

            text="Đăng nhập",

            text_color=TEXT_MAIN,

            font=ctk.CTkFont(
                size=38,
                weight="bold"
            )
        )

        title.grid(
            row=0,
            column=0,

            padx=50,

            pady=(55, 5)
        )

        welcome = ctk.CTkLabel(
            self.login_card,

            text="Chào mừng bạn quay lại",

            text_color=TEXT_SECONDARY,

            font=ctk.CTkFont(
                size=18
            )
        )

        welcome.grid(
            row=1,
            column=0,

            pady=(0, 35)
        )

        # ====================================================
        # USERNAME
        # ====================================================

        username_label = ctk.CTkLabel(
            self.login_card,

            text="Tên đăng nhập hoặc Email",

            anchor="w",

            text_color=TEXT_MAIN,

            font=ctk.CTkFont(
                size=15,
                weight="bold"
            )
        )

        username_label.grid(
            row=2,
            column=0,

            padx=50,

            pady=(0, 8),

            sticky="ew"
        )

        self.username_entry = ctk.CTkEntry(
            self.login_card,

            height=58,

            placeholder_text="👤    Nhập tên đăng nhập hoặc email",

            fg_color=INPUT_BG,

            border_color=BORDER,
            border_width=1,

            corner_radius=9,

            text_color=TEXT_MAIN,

            placeholder_text_color="#94A3B8",

            font=ctk.CTkFont(
                size=15
            )
        )

        self.username_entry.grid(
            row=3,
            column=0,

            padx=50,

            sticky="ew"
        )

        # ====================================================
        # PASSWORD LABEL
        # ====================================================

        password_label = ctk.CTkLabel(
            self.login_card,

            text="Mật khẩu",

            anchor="w",

            text_color=TEXT_MAIN,

            font=ctk.CTkFont(
                size=15,
                weight="bold"
            )
        )

        password_label.grid(
            row=4,
            column=0,

            padx=50,

            pady=(25, 8),

            sticky="ew"
        )

        # ====================================================
        # FRAME PASSWORD
        # ====================================================

        password_frame = ctk.CTkFrame(
            self.login_card,

            height=58,

            fg_color=WHITE,

            corner_radius=9,

            border_width=1,
            border_color=BORDER
        )

        password_frame.grid(
            row=5,
            column=0,

            padx=50,

            sticky="ew"
        )

        password_frame.grid_columnconfigure(
            0,
            weight=1
        )

        password_frame.grid_propagate(False)

        # Entry mật khẩu
        self.password_entry = ctk.CTkEntry(
            password_frame,

            placeholder_text="🔒    Nhập mật khẩu",

            show="●",

            fg_color="transparent",

            border_width=0,

            text_color=TEXT_MAIN,

            placeholder_text_color="#94A3B8",

            font=ctk.CTkFont(
                size=15
            )
        )

        self.password_entry.grid(
            row=0,
            column=0,

            padx=(10, 0),

            pady=6,

            sticky="nsew"
        )

        # Nút con mắt
        self.eye_button = ctk.CTkButton(
            password_frame,

            text="👁",

            width=45,
            height=45,

            fg_color="transparent",

            hover_color="#F1F5F9",

            text_color=TEXT_SECONDARY,

            font=ctk.CTkFont(
                size=18
            ),

            command=self.toggle_password
        )

        self.eye_button.grid(
            row=0,
            column=1,

            padx=(0, 5),

            pady=5
        )

        # ====================================================
        # GHI NHỚ + QUÊN MẬT KHẨU
        # ====================================================

        options = ctk.CTkFrame(
            self.login_card,
            fg_color="transparent"
        )

        options.grid(
            row=6,
            column=0,

            padx=50,

            pady=(20, 25),

            sticky="ew"
        )

        remember_checkbox = ctk.CTkCheckBox(
            options,

            text="Ghi nhớ đăng nhập",

            variable=self.remember_var,

            width=180,

            checkbox_width=22,
            checkbox_height=22,

            corner_radius=4,

            fg_color=PRIMARY,
            hover_color=PRIMARY_HOVER,

            border_color=BORDER,

            text_color=TEXT_MAIN,

            font=ctk.CTkFont(
                size=14
            )
        )

        remember_checkbox.pack(
            side="left"
        )

        forgot_button = ctk.CTkButton(
            options,

            text="Quên mật khẩu?",

            width=130,

            fg_color="transparent",

            hover_color="#EFF6FF",

            text_color=PRIMARY,

            font=ctk.CTkFont(
                size=14
            ),

            command=self.forgot_password
        )

        forgot_button.pack(
            side="right"
        )

        # ====================================================
        # BUTTON ĐĂNG NHẬP
        # ====================================================

        login_button = ctk.CTkButton(
            self.login_card,

            text="Đăng nhập",

            height=58,

            fg_color=PRIMARY,

            hover_color=PRIMARY_HOVER,

            text_color=WHITE,

            corner_radius=9,

            font=ctk.CTkFont(
                size=17,
                weight="bold"
            ),

            command=self.login
        )

        login_button.grid(
            row=7,
            column=0,

            padx=50,

            sticky="ew"
        )

        # ====================================================
        # BUTTON TẠO TÀI KHOẢN
        # ====================================================

        register_button = ctk.CTkButton(
            self.login_card,

            text="Tạo tài khoản",

            height=58,

            fg_color=WHITE,

            hover_color="#EFF6FF",

            border_width=1,
            border_color=PRIMARY,

            text_color=PRIMARY,

            corner_radius=9,

            font=ctk.CTkFont(
                size=17,
                weight="bold"
            ),

            command=self.register
        )

        register_button.grid(
            row=8,
            column=0,

            padx=50,

            pady=(12, 25),

            sticky="ew"
        )

        # ====================================================
        # BẢO MẬT
        # ====================================================

        security = ctk.CTkLabel(
            self.login_card,

            text="🛡   Dữ liệu được lưu an toàn trên hệ thống",

            text_color="#94A3B8",

            font=ctk.CTkFont(
                size=13
            )
        )

        security.grid(
            row=9,
            column=0,

            pady=(0, 30)
        )

        # ====================================================
        # VERSION
        # ====================================================

        version = ctk.CTkLabel(
            self.right_panel,

            text="Phiên bản desktop app - Python",

            text_color="#94A3B8",

            font=ctk.CTkFont(
                size=13
            )
        )

        version.grid(
            row=2,
            column=0,

            pady=(0, 25),

            sticky="s"
        )

    # ========================================================
    # HIỆN / ẨN PASSWORD
    # ========================================================

    def toggle_password(self):

        self.password_visible = not self.password_visible

        if self.password_visible:

            self.password_entry.configure(
                show=""
            )

            self.eye_button.configure(
                text="🙈"
            )

        else:

            self.password_entry.configure(
                show="●"
            )

            self.eye_button.configure(
                text="👁"
            )

    # ========================================================
    # LOGIN
    # ========================================================

    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        # Kiểm tra tài khoản
        if username == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên đăng nhập hoặc Email."
            )

            self.username_entry.focus_set()

            return

        # Kiểm tra mật khẩu
        if password == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập mật khẩu."
            )

            self.password_entry.focus_set()

            return

        # ====================================================
        # TÀI KHOẢN TEST
        # Sau này chúng ta sẽ thay bằng SQLite
        # ====================================================

        if username == "admin" and password == "123456":

            messagebox.showinfo(
                "Đăng nhập thành công",
                "Chào mừng bạn đến với Quản Lý Thu Chi Cá Nhân!"
            )

            # Sau này mở Dashboard tại đây
            print("Đăng nhập thành công")

        else:

            messagebox.showerror(
                "Đăng nhập thất bại",
                "Tên đăng nhập hoặc mật khẩu không chính xác."
            )

            # Xóa mật khẩu
            self.password_entry.delete(
                0,
                "end"
            )

            self.password_entry.focus_set()

    # ========================================================
    # QUÊN MẬT KHẨU
    # ========================================================

    def forgot_password(self):

        messagebox.showinfo(
            "Quên mật khẩu",
            "Chức năng quên mật khẩu sẽ được phát triển sau."
        )

    # ========================================================
    # ĐĂNG KÝ
    # ========================================================

    def register(self):

        messagebox.showinfo(
            "Tạo tài khoản",
            "Chức năng tạo tài khoản sẽ được phát triển sau."
        )


# ============================================================
# CHẠY CHƯƠNG TRÌNH
# ============================================================

if __name__ == "__main__":

    # Giao diện sáng
    ctk.set_appearance_mode("light")

    # Theme xanh
    ctk.set_default_color_theme("blue")

    # Khởi tạo app
    app = LoginWindow()

    # Chạy chương trình
    app.mainloop()