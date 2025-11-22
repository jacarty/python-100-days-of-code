"""
Dinosaur Game Bot
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
from PIL import ImageGrab
import time

url = "https://elgoog.im/dinosaur-game/"

def load_page(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    chrome_options.add_experimental_option("detach", True)
    
    driver = None
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        print("Chrome driver started successfully")
        
        print("Navigating to game page...")
        driver.get(url)
        
        wait = WebDriverWait(driver, 20)
        time.sleep(3)
        
        return driver
        
    except Exception as e:
        print(f"Error during navigation: {e}")
        import traceback
        traceback.print_exc()
        if driver:
            driver.quit()
        return None

def check_obstacle_type(screenshot, threshold=127):
    """
    Returns 'bird' for flying obstacles, 'cactus' for ground obstacles, None for nothing
    Birds appear in upper portion, cacti in lower portion
    """
    pixels = screenshot.load()
    width, height = screenshot.size
    
    # Divide into thirds
    upper_third = height // 3
    
    upper_dark = 0
    lower_dark = 0
    total_dark = 0
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]
            if r < threshold and g < threshold and b < threshold:
                total_dark += 1
                if y < upper_third:
                    upper_dark += 1
                else:
                    lower_dark += 1
    
    # Need minimum darkness to consider it an obstacle
    if total_dark < 3:
        return None
    # If most dark pixels are in upper third, it's a bird
    if upper_dark > lower_dark and upper_dark > 2:
        return 'bird'
    # Otherwise it's a cactus
    elif total_dark > 3:
        return 'cactus'
    
    return None

def play_game(driver):
    print("\nPreparing to play...")
    time.sleep(2)
    
    screen_width, screen_height = pyautogui.size()
    print(f"Screen size: {screen_width}x{screen_height}")
    
    dino_x = 60
    ground_y = 680
    
    # Detection zone
    detect_x1 = dino_x + 80
    detect_y1 = ground_y - 80
    detect_x2 = dino_x + 180
    detect_y2 = ground_y - 5
    
    print(f"Detection zone: ({detect_x1}, {detect_y1}) to ({detect_x2}, {detect_y2})")
    
    # Click and start
    pyautogui.click(400, 500)
    time.sleep(0.5)
    
    pyautogui.press('space')
    print("🎮 Game started!")
    time.sleep(1)
    
    print("\n🦖 Bot is running! Press Ctrl+C to stop\n")
    
    last_action_time = 0
    frame_count = 0
    jumps = 0
    ducks = 0
    min_action_interval = 0.35
    speed_multiplier = 1.0
    
    try:
        while True:
            current_time = time.time()
            
            # Gradually increase detection distance as game speeds up
            if jumps + ducks > 20:
                speed_multiplier = 1.15
            if jumps + ducks > 40:
                speed_multiplier = 1.3
            if jumps + ducks > 60:
                speed_multiplier = 1.5
            
            adjusted_distance = int(80 * speed_multiplier)
            detect_x1 = dino_x + adjusted_distance
            detect_x2 = dino_x + adjusted_distance + 100
            
            screenshot = ImageGrab.grab(bbox=(detect_x1, detect_y1, detect_x2, detect_y2))
            obstacle_type = check_obstacle_type(screenshot, threshold=127)
            
            frame_count += 1
            
            if frame_count % 500 == 0:
                print(f"⏱️  Frame {frame_count} | Jumps: {jumps} | Ducks: {ducks} | Speed: {speed_multiplier:.2f}x")
            
            # React to obstacles
            time_since_last_action = current_time - last_action_time
            
            if obstacle_type and time_since_last_action >= min_action_interval:
                if obstacle_type == 'bird':
                    # Duck for birds
                    pyautogui.keyDown('down')
                    time.sleep(0.3)
                    pyautogui.keyUp('down')
                    ducks += 1
                    last_action_time = current_time
                    print(f"🦆 DUCK #{ducks} (bird)")
                        
                elif obstacle_type == 'cactus':
                    # Jump for cacti
                    pyautogui.press('space')
                    jumps += 1
                    last_action_time = current_time
                    print(f"🦖 JUMP #{jumps} (cactus)")
            
            time.sleep(0.008)
            
    except KeyboardInterrupt:
        print(f"\n\n✅ Bot stopped!")
        print(f"📊 Final Stats:")
        print(f"   Jumps: {jumps}")
        print(f"   Ducks: {ducks}")
        print(f"   Total Actions: {jumps + ducks}")
        print(f"   Frames: {frame_count}")

if __name__ == "__main__":
    driver = load_page(url)
    if driver:
        play_game(driver)