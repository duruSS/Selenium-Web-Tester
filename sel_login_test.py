from test import Test

if __name__ == "__main__":
    tester = Test("https://127.0.0.1:5000")
    
    # Regular login Tests
    tester.test_login("baris@gmail.com", "asdasdasd")
    
    tester.test_login("baris@gmail.com", "test123")
    
    tester.test_login("baris@gmail.com", "test1234")

    tester.test_login("baris@gmail.com", "' 1==1--")

    # This test would not work in a realistic scenario
    # since SSO login procedure cannot be automized.
    tester.test_sso_login()

    tester.test_login("", "")  #No e-mail & password. Pop-Up: Lütfen bu alanı doldurunuz (points email box)
    
    tester.test_login("", "12345") #No e-mail. Pop-Up: Lütfen bu alanı doldurunuz (points email box)
    
    tester.test_login("duru.solakoglu@ug.bilkent", "") #No password. Warning: Invalid credentials

    tester.test_login("duru.solakoglu@ug.bilkent", "12345") #Invalid password. Warning: Invalid credentials

    tester.test_login("duru.solakoglu@ug.bilkent", "12345678") # Valid mail & password
