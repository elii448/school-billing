import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from CTkToolTip import CTkToolTip

class PaymentTrackingApp:
    def __init__(self):
        # Set appearance and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Financial Management Dashboard")
        self.root.geometry("1600x900")
        self.root.minsize(1400, 800)

        # Configure grid layout
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)


        self.sidebar = ctk.CTkFrame(
            self.root, 
            width=280, 
            corner_radius=0,
            fg_color="#1E1E2E"
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.sidebar.grid_propagate(False)

        # Company Logo and Title Section
        self.logo_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.logo_frame.pack(pady=(30, 20), padx=20, fill="x")

        self.app_title = ctk.CTkLabel(
            self.logo_frame,
            text="FINANCE HUB",
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        self.app_title.pack(side="top", pady=(0, 10))

        # Divider
        ctk.CTkFrame(self.sidebar, height=2, fg_color="gray50").pack(fill="x", pady=10, padx=20)

        # Sidebar Navigation
        self.nav_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.nav_frame.pack(pady=10, padx=20, fill="x")

        self.enrollment_btn = self._create_nav_button(
            "Enrollment Costs", 
            self.show_enrollment_module
        )
        self.payment_btn = self._create_nav_button(
            "Payment Breakdown", 
            self.show_payment_module
        )

        # Main content frame
        self.content_frame = ctk.CTkFrame(
            self.root, 
            corner_radius=0,
            fg_color="#2C2C3E"
        )
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        # Data storage
        self.enrollment_costs = {}
        self.total_payable = 0.0
        self.total_paid = 0.0

        # Initial module
        self.show_enrollment_module()

    def _create_nav_button(self, text, command):
        btn = ctk.CTkButton(
            self.nav_frame, 
            text=text, 
            command=command,
            corner_radius=5,
            fg_color="#3498DB",
            hover_color="#2980B9",
            font=("Arial", 16),
            height=40
        )
        btn.pack(pady=10, fill="x")
        CTkToolTip(btn, message=f"Navigate to {text} section")
        return btn

    def show_enrollment_module(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        frame = ctk.CTkFrame(
            self.content_frame,
            corner_radius=0,
            fg_color="#2C2C3E"
        )
        frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        frame.grid_columnconfigure((0, 1), weight=1)

        title = ctk.CTkLabel(
            frame, 
            text="Enrollment Cost Management",
            font=("Arial", 22, "bold"),
            text_color="white"
        )
        title.grid(row=0, column=0, columnspan=2, pady=(20, 30), padx=20, sticky="w")

        # Inputs Column
        input_frame = ctk.CTkFrame(frame, fg_color="transparent")
        input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Label Entry
        ctk.CTkLabel(input_frame, text="Cost Description").pack(pady=(10,5))
        label_entry = ctk.CTkEntry(input_frame, width=300)
        label_entry.pack(pady=5)

        # Value Entry
        ctk.CTkLabel(input_frame, text="Cost Value").pack(pady=(10,5))
        value_entry = ctk.CTkEntry(input_frame, width=300)
        value_entry.pack(pady=5)

        # Total Payable Display
        total_label = ctk.CTkLabel(
            input_frame,
            text=f"Total Payable: ${self.total_payable:.2f}",
            font=("Arial", 14, "bold")
        )
        total_label.pack(pady=10)

        # Breakdown Textbox
        breakdown_text = ctk.CTkTextbox(
            frame,
            height=300,
            width=500,
            state="normal"
        )
        breakdown_text.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        def add_cost():
            try:
                label = label_entry.get().strip()
                value = float(value_entry.get())
                
                if label and value > 0:
                    self.enrollment_costs[label] = value
                    self.total_payable = sum(self.enrollment_costs.values())
                    total_label.configure(text=f"Total Payable: ${self.total_payable:.2f}")
                    
                    # Update breakdown
                    self.breakdown_listing(breakdown_text)
                    
                    # Clear entries
                    label_entry.delete(0, 'end')
                    value_entry.delete(0, 'end')
            except ValueError:
                CTkMessagebox(
                    title="Input Error", 
                    message="Please enter valid cost details", 
                    icon="warning"
                )

        add_btn = ctk.CTkButton(
            input_frame, 
            text="Add Cost", 
            command=add_cost,
            corner_radius=8
        )
        add_btn.pack(pady=10)

        self.breakdown_listing(breakdown_text)

    def show_payment_module(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        frame = ctk.CTkFrame(
            self.content_frame, 
            corner_radius=0, 
            fg_color="#2C2C3E"
        )
        frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        frame.grid_columnconfigure((0, 1), weight=1)

        title = ctk.CTkLabel(
            frame, 
            text="Payment Management", 
            font=("Arial", 22, "bold"),
            text_color="white"
        )
        title.grid(row=0, column=0, columnspan=2, pady=(20, 30), padx=20, sticky="w")

        breakdown_text = ctk.CTkTextbox(
            frame,
            height=300,
            width=500,
            state="normal"
        )
        breakdown_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Payment Input Column
        payment_frame = ctk.CTkFrame(frame, fg_color="transparent")
        payment_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Payment Amount Entry
        ctk.CTkLabel(payment_frame, text="Payment Amount").pack(pady=(10,5))
        payment_entry = ctk.CTkEntry(payment_frame, width=300)
        payment_entry.pack(pady=5)

        # Total Payable and Paid Labels
        total_payable_label = ctk.CTkLabel(
            payment_frame, 
            text=f"Total Payable: ${self.total_payable:.2f}",
            font=("Arial", 14, "bold")
        )
        total_payable_label.pack(pady=10)

        total_paid_label = ctk.CTkLabel(
            payment_frame, 
            text=f"Total Paid: ${self.total_paid:.2f}",
            font=("Arial", 14, "bold")
        )
        total_paid_label.pack(pady=10)

        # Remaining Balance Label
        remaining_label = ctk.CTkLabel(
            payment_frame, 
            text=f"Remaining Balance: ${self.total_payable - self.total_paid:.2f}",
            font=("Arial", 14, "bold")
        )
        remaining_label.pack(pady=10)

        # Payment History Textbox
        payment_history_label = ctk.CTkLabel(payment_frame, text="Payment History")
        payment_history_label.pack(pady=(10,5))
        payment_history_text = ctk.CTkTextbox(payment_frame, height=150, width=300)
        payment_history_text.pack(pady=5)
        payment_history_text.configure(state="disabled")

        def process_payment():
            try:
                payment = float(payment_entry.get())
                
                if 0 < payment <= (self.total_payable - self.total_paid):
                    self.total_paid += payment
                    remaining = self.total_payable - self.total_paid
                    
                    # Update labels
                    total_paid_label.configure(
                        text=f"Total Paid: ${self.total_paid:.2f}"
                    )
                    remaining_label.configure(
                        text=f"Remaining Balance: ${remaining:.2f}"
                    )
                    
                    # Update payment history
                    payment_history_text.configure(state="normal")
                    payment_history_text.insert("end", f"Payment: ${payment:.2f}\n")
                    payment_history_text.configure(state="disabled")
                    
                    # Clear payment entry
                    payment_entry.delete(0, 'end')

                    # Update breakdown
                    self.breakdown_listing(breakdown_text)

                    CTkMessagebox(
                        title="Payment Successful", 
                        message=f"Payment of ${payment:.2f} processed.", 
                        icon="check"
                    )
                else:
                    CTkMessagebox(
                        title="Payment Error", 
                        message="Invalid payment amount", 
                        icon="warning"
                    )
            except ValueError:
                CTkMessagebox(
                    title="Input Error", 
                    message="Please enter a valid payment amount", 
                    icon="warning"
                )

        pay_btn = ctk.CTkButton(
            payment_frame, 
            text="Make Payment", 
            command=process_payment,
            corner_radius=8
        )
        pay_btn.pack(pady=10)

        # Initial population of breakdown
        self.breakdown_listing(breakdown_text)

    def breakdown_listing(self, breakdown_text):
        breakdown_text.configure(
            state="normal",
            fg_color="#34495E",
            text_color="white",
            font=("Consolas", 14)
        )
        breakdown_text.delete("0.0", "end")
        for label, value in self.enrollment_costs.items():
            breakdown_text.insert("end", f"{label}: ${value:.2f}\n")
        breakdown_text.insert("end", f"\nTotal Payable: ${self.total_payable:.2f}")
        breakdown_text.configure(state="disabled")

        return breakdown_text


    def run(self):
        self.root.mainloop()

def main():
    app = PaymentTrackingApp()
    app.run()

if __name__ == "__main__":
    main()