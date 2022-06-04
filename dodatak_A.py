import getpass
import math
import hashlib

class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        if (self.b == 0):
            return float('nan')

        return self.a / self.b

    def perform_root(self) -> float:
        """Gets the bth root of a. If any value is invalid returns NaN."""
        if (self.a == 0):
            return 0
            
        if (self.a < 0) or (self.b == 0):
            return float('nan')

        return math.pow(self.a, 1/self.b)

if __name__ == "__main__":
    user = input("Username: ")
    password = getpass.getpass("Password: ")

    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

    pass_file = open("safe_pass.txt", "r")
    safe_pass = pass_file.read()
    pass_file.close()

    if user != "root" or password_hash != safe_pass:
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        a = float(input("A = "))
        b = float(input("B = "))

        print("Division:")
        ops_manager = OperationsManager(a, b)
        print(ops_manager.perform_division())

        print("Root:")
        ops_manager = OperationsManager(a, b)
        print(ops_manager.perform_root())

