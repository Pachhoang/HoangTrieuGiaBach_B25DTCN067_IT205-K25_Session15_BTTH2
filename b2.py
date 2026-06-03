atm_vault_balance = 50000000
user_account_balance = 10000000


def display_balances():
    """
    Hiển thị số dư tài khoản và tiền mặt trong ATM.
    """
    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    """
    Nạp tiền vào tài khoản.

    Args:
        amount (int): Số tiền muốn nạp.

    Returns:
        bool: True nếu nạp thành công, False nếu không hợp lệ.
    """
    global user_account_balance, atm_vault_balance

    if amount <= 0:
        return False

    user_account_balance += amount
    atm_vault_balance += amount
    return True


def check_withdrawal_rules(amount):
    """
    Kiểm tra điều kiện rút tiền.

    Args:
        amount (int): Số tiền muốn rút.

    Returns:
        tuple: (status, total_deduction)
    """
    fee = 1100
    total_deduction = amount + fee

    if amount % 50000 != 0:
        return ("INVALID_AMOUNT", total_deduction)

    if total_deduction > user_account_balance:
        return ("INSUFFICIENT_FUNDS", total_deduction)

    if amount > atm_vault_balance:
        return ("ATM_OUT_OF_CASH", total_deduction)

    return ("OK", total_deduction)


def execute_withdrawal(total_deduction, amount_to_dispense):
    """
    Thực hiện rút tiền.

    Args:
        total_deduction (int): Tổng tiền bị trừ.
        amount_to_dispense (int): Số tiền ATM trả ra.

    Returns:
        None
    """
    global user_account_balance, atm_vault_balance

    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense

    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")


def main():
    """
    Chương trình chính.
    """
    while True:
        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")

        choice = input("Vui lòng chọn giao dịch (1-4): ")

        if choice == "1":
            display_balances()

        elif choice == "2":
            try:
                amount = int(input("Nhập số tiền muốn nạp: "))

                if deposit_money(amount):
                    print(
                        f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND."
                    )
                else:
                    print("Số tiền không hợp lệ")

            except ValueError:
                print("Số tiền không hợp lệ")

        elif choice == "3":
            try:
                amount = int(input("Nhập số tiền cần rút: "))

                if amount <= 0:
                    print("Số tiền không hợp lệ")
                    continue

                status, total_deduction = check_withdrawal_rules(amount)

                if status == "INVALID_AMOUNT":
                    print("Số tiền rút phải là bội số của 50,000")

                elif status == "INSUFFICIENT_FUNDS":
                    print("Giao dịch thất bại: Số dư tài khoản không đủ.")

                elif status == "ATM_OUT_OF_CASH":
                    print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")

                else:
                    execute_withdrawal(total_deduction, amount)

            except ValueError:
                print("Số tiền không hợp lệ")

        elif choice == "4":
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break

        else:
            print("Lựa chọn không hợp lệ")


main()