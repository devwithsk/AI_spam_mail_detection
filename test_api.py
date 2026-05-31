#!/usr/bin/env python3
"""
Spam Detection API - Test Script
Tests all API endpoints to ensure everything is working correctly
"""

import requests
import json
from datetime import datetime
import sys

# Configuration
BASE_URL = "http://localhost:5000"
TIMEOUT = 10

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

class APITester:
    def __init__(self, base_url):
        self.base_url = base_url
        self.passed = 0
        self.failed = 0
        self.test_data = {
            "spam_messages": [
                "Congratulations! You won a free iPhone. Click here now.",
                "URGENT: Your account has been suspended. Click here to verify.",
                "Get rich quick! Earn $5000/day from home.",
                "You have been selected for a special prize!",
            ],
            "ham_messages": [
                "Hi, how are you doing today?",
                "Meeting at 3 PM tomorrow in the conference room.",
                "Thanks for your email, I'll get back to you soon.",
                "The project deadline has been extended to next month.",
            ]
        }

    def print_header(self, text):
        print(f"\n{BLUE}{'='*50}")
        print(f"  {text}")
        print(f"{'='*50}{RESET}\n")

    def print_success(self, message):
        print(f"{GREEN}✓ {message}{RESET}")
        self.passed += 1

    def print_error(self, message):
        print(f"{RED}✗ {message}{RESET}")
        self.failed += 1

    def print_info(self, message):
        print(f"{YELLOW}ℹ {message}{RESET}")

    def test_connection(self):
        """Test if API server is running"""
        self.print_header("Testing Connection")
        try:
            response = requests.get(f"{self.base_url}/", timeout=TIMEOUT)
            if response.status_code == 200:
                self.print_success(f"Server is running on {self.base_url}")
                data = response.json()
                self.print_info(f"API Version: {data.get('version', 'N/A')}")
                return True
            else:
                self.print_error(f"Server returned status code {response.status_code}")
                return False
        except requests.exceptions.ConnectionError:
            self.print_error(f"Cannot connect to {self.base_url}")
            self.print_info("Make sure Flask backend is running: python app.py")
            return False
        except Exception as e:
            self.print_error(f"Connection failed: {str(e)}")
            return False

    def test_health_check(self):
        """Test health check endpoint"""
        self.print_header("Testing Health Check")
        try:
            response = requests.get(f"{self.base_url}/api/health", timeout=TIMEOUT)
            if response.status_code == 200:
                data = response.json()
                if data.get("model_loaded"):
                    self.print_success("Model is loaded and ready")
                else:
                    self.print_error("Model is not loaded. Run: python main.py")
                return True
            else:
                self.print_error(f"Health check failed with status {response.status_code}")
                return False
        except Exception as e:
            self.print_error(f"Health check error: {str(e)}")
            return False

    def test_single_prediction(self):
        """Test single message prediction"""
        self.print_header("Testing Single Predictions")
        
        # Test SPAM message
        spam_msg = self.test_data["spam_messages"][0]
        try:
            response = requests.post(
                f"{self.base_url}/api/predict",
                json={"message": spam_msg},
                timeout=TIMEOUT
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("prediction") == "spam":
                    self.print_success(f"Correctly identified SPAM message")
                    self.print_info(f"  Confidence: {data.get('confidence', 'N/A')}%")
                else:
                    self.print_error("Failed to identify spam message")
            else:
                self.print_error(f"Request failed with status {response.status_code}")
        except Exception as e:
            self.print_error(f"SPAM prediction error: {str(e)}")

        # Test HAM message
        ham_msg = self.test_data["ham_messages"][0]
        try:
            response = requests.post(
                f"{self.base_url}/api/predict",
                json={"message": ham_msg},
                timeout=TIMEOUT
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("prediction") == "ham":
                    self.print_success(f"Correctly identified SAFE message")
                    self.print_info(f"  Confidence: {data.get('confidence', 'N/A')}%")
                else:
                    self.print_error("Failed to identify safe message")
            else:
                self.print_error(f"Request failed with status {response.status_code}")
        except Exception as e:
            self.print_error(f"HAM prediction error: {str(e)}")

    def test_batch_prediction(self):
        """Test batch prediction"""
        self.print_header("Testing Batch Predictions")
        
        test_messages = [
            self.test_data["spam_messages"][1],
            self.test_data["ham_messages"][1],
            self.test_data["spam_messages"][2],
        ]
        
        try:
            response = requests.post(
                f"{self.base_url}/api/batch-predict",
                json={"messages": test_messages},
                timeout=TIMEOUT
            )
            
            if response.status_code == 200:
                data = response.json()
                count = data.get("count", 0)
                if count == 3:
                    self.print_success(f"Batch prediction successful for {count} messages")
                    results = data.get("results", [])
                    for i, result in enumerate(results, 1):
                        pred_type = "SPAM" if result.get("prediction") == "spam" else "SAFE"
                        conf = result.get("confidence", "N/A")
                        self.print_info(f"  Message {i}: {pred_type} ({conf}%)")
                else:
                    self.print_error(f"Expected 3 results, got {count}")
            else:
                self.print_error(f"Batch prediction failed with status {response.status_code}")
        except Exception as e:
            self.print_error(f"Batch prediction error: {str(e)}")

    def test_error_handling(self):
        """Test error handling"""
        self.print_header("Testing Error Handling")
        
        # Test empty message
        try:
            response = requests.post(
                f"{self.base_url}/api/predict",
                json={"message": ""},
                timeout=TIMEOUT
            )
            if response.status_code == 400:
                self.print_success("Empty message validation works")
            else:
                self.print_error("Empty message validation failed")
        except Exception as e:
            self.print_error(f"Empty message test error: {str(e)}")
        
        # Test missing message
        try:
            response = requests.post(
                f"{self.base_url}/api/predict",
                json={},
                timeout=TIMEOUT
            )
            if response.status_code == 400:
                self.print_success("Missing message validation works")
            else:
                self.print_error("Missing message validation failed")
        except Exception as e:
            self.print_error(f"Missing message test error: {str(e)}")

    def run_all_tests(self):
        """Run all tests"""
        print(f"\n{BLUE}")
        print("=" * 50)
        print("  Spam Detection API - Test Suite")
        print("=" * 50)
        print(f"{RESET}")
        print(f"Testing: {self.base_url}")
        print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Run tests in sequence
        if not self.test_connection():
            self.print_error("Cannot connect to API. Skipping remaining tests.")
            return
        
        self.test_health_check()
        self.test_single_prediction()
        self.test_batch_prediction()
        self.test_error_handling()
        
        # Print summary
        self.print_summary()

    def print_summary(self):
        """Print test summary"""
        total = self.passed + self.failed
        
        print(f"\n{BLUE}{'='*50}")
        print(f"  Test Summary")
        print(f"{'='*50}{RESET}\n")
        
        print(f"{GREEN}Passed: {self.passed}/{total}{RESET}")
        print(f"{RED}Failed: {self.failed}/{total}{RESET}")
        
        if self.failed == 0:
            print(f"\n{GREEN}✓ All tests passed! API is working correctly.{RESET}")
            return True
        else:
            print(f"\n{RED}✗ Some tests failed. Please check the errors above.{RESET}")
            return False


if __name__ == "__main__":
    print("\nSpam Detection API - Test Script\n")
    
    # Allow custom base URL
    base_url = sys.argv[1] if len(sys.argv) > 1 else BASE_URL
    
    tester = APITester(base_url)
    success = tester.run_all_tests()
    
    sys.exit(0 if success else 1)
