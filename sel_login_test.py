from test import Test

if __name__ == "__main__":
    tester = Test("http://127.0.0.1:8003")
    
    tester.test_login("baris@gmail.com", "asdasdasd")
    
    tester.test_login("baris@gmail.com", "test123")
    
    tester.test_login("baris@gmail.com", "test1234")