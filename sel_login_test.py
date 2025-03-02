from test import Test

if __name__ == "__main__":
    tester = Test("https://127.0.0.1:5000")
    
    # Regular login Tests Cases

    tester.test_login("", "")  #Test Case 1: No e-mail & password.
    
    tester.test_login("", "12345") #Test Case 2: No e-mail.
    
    tester.test_login("duru.solakoglu@ug.bilkent", "") #Test Case 3: No password. Warning: Invalid credentials

    tester.test_login("duru.solakoglu@ug.bilkent", "12345") #Test Case 4: Invalid password. Warning: Invalid credentials

    tester.test_login("duru.solakoglu@ug.bilkent", "12345678") #Test Case 5: Valid mail & password

    # This test would not work in a realistic scenario
    # since SSO login procedure cannot be automized.

    tester.test_sso_login() #Test Case 6: Testing Google SSO 
