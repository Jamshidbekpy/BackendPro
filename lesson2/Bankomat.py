# Jamshidbek
# Homework
# 2)
from abc import ABC, abstractmethod
from dataclasses import dataclass

# ------------------ Ma'lumotlar bazasi (dict) ----------------------------------------
USERS_DB = {
    "998901234567": {"pin": "1234", "balance": 1000},
    "998909876543": {"pin": "4321", "balance": 5000},
}


# ----------------- Foydalanuvchi modeli --------------------------------------------------
@dataclass
class User:
    phone: str
    pin: str
    balance: int


# ----------------- Abstract class (Strategy interfeysi) ------------------------------
class ATMOperation(ABC):
    @abstractmethod
    def execute(self, user: User):
        pass


# ---------------- Strategy pattern: Operatsiyalar ---------------------------------
class BalanceCheck(ATMOperation):
    def execute(self, user: User):
        print(f"Sizning balansingiz: {user.balance} so'm")


class Withdraw(ATMOperation):
    def execute(self, user: User):
        amount = int(input("Yechmoqchi bo‘lgan summani kiriting: "))
        if amount <= user.balance:
            user.balance -= amount
            print(f"{amount} so‘m yechildi. Qolgan: {user.balance} so‘m")
        else:
            print("Mablag' yetarli emas.")


class Deposit(ATMOperation):
    def execute(self, user: User):
        amount = int(input("Qo‘yiladigan summani kiriting: "))
        user.balance += amount
        print(f"{amount} so‘m qo‘shildi. Yangi balans: {user.balance} so‘m")


# ---------------- ATM klassi (Dependency Injection) --------------------------------
class ATM:
    def __init__(self, strategy: ATMOperation):
        self.strategy = strategy

    def run(self, user: User):
        self.strategy.execute(user)


# ----------------- Login funksiyasi --------------------------------------------
def login(users_db: dict) -> User | None:
    phone = input("Telefon raqam (998901234567): ")
    pin = input(" PIN kod: ")

    user_data = users_db.get(phone)
    if user_data and user_data['pin'] == pin:
        print("Muvaffaqiyatli kirdingiz!")
        return User(phone=phone, pin=pin, balance=user_data["balance"])
    else:
        print("Login yoki PIN noto‘g‘ri!")
        return None


# ===================== Asosiy menyu =====================
def main():
    user = login(USERS_DB)
    if not user:
        return

    while True:
        print("\n MENYU:")
        print("1. Balansni ko‘rish")
        print("2. Pul yechish")
        print("3. Pul qo‘yish")
        print("4. Chiqish")

        choice = input("Tanlov (1-4): ")

        if choice == "1":
            atm = ATM(BalanceCheck())
        elif choice == "2":
            atm = ATM(Withdraw())
        elif choice == "3":
            atm = ATM(Deposit())
        elif choice == "4":
            USERS_DB[user.phone]["balance"] = user.balance
            print("Amliyot uchun katta rahmat!. Xayr!")
            break
        else:
            print("Noto‘g‘ri tanlov!")
            continue

        atm.run(user)


# ----------------------------- Dastur boshlanishi ---------------------------
main()







