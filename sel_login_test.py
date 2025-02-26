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
