import os
from datetime import datetime
from selenium import webdriver

def takeScreenshot(test_case: str, driver: webdriver) -> str:

    # Directory structure
    parent_dir = 'results'
    base_dir = os.path.join(parent_dir, 'screenshots')
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_name = f"{test_case}_{timestamp}.png"
    screenshot_path = os.path.join(base_dir, screenshot_name)

    # Ensure directory exists
    os.makedirs(base_dir, exist_ok=True)

    # Capture and save the screenshot
    driver.maximize_window()
    driver.save_screenshot(screenshot_path)