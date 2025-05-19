from pynput.keyboard import Key,Controller
import pynput
import time
import pyautogui
class edgeTask:
    def __init__(self):
        self.keyboard = Controller()
        self.mouse = pynput.mouse.Controller()
    def open_edge(self):
        self.keyboard.press(Key.cmd)  # press cmd key
        self.keyboard.press('1')
        self.keyboard.release('1')
        self.keyboard.release(Key.cmd)
    def new_tab(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('t')
        self.keyboard.release('t')
        self.keyboard.release(Key.ctrl)
    def type(self,text):
        self.keyboard.type(text)
    def click_enter(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
    def scroll(self):
        self.keyboard.press(Key.page_down)
        self.keyboard.release(Key.page_down)
        self.keyboard.press(Key.page_down)
        self.keyboard.release(Key.page_down)
        self.mouse.click(pynput.mouse.Button.left,1)
object = edgeTask()
object.open_edge()

topics = [
    "Ancient civilizations' trade routes",
    "Sustainable fashion practices",
    "The benefits of meditation",
    "Space exploration missions",
    "Famous historical figures' love letters",
    "DIY home improvement projects",
    "Traditional healing practices around the world",
    "Cryptocurrency trends and analysis",
    "Endangered species conservation efforts",
    "Unexplained mysteries of the ocean",
    "Urban gardening techniques",
    "Artificial intelligence in healthcare",
    "Indigenous cultures' storytelling traditions",
    "Innovative renewable energy technologies",
    "World-famous street food dishes",
    "Impact of social media on mental health",
    "Evolution of language over time",
    "Historical landmarks undergoing restoration",
    "Mindfulness practices for stress relief",
    "Folklore and mythology from different cultures",
    "Emerging trends in virtual reality gaming",
    "Iconic architectural wonders of the world",
    "Culinary traditions of different regions",
    "Ethical considerations in artificial intelligence development",
    "Alternative forms of transportation",
    "Role of music therapy in mental health treatment",
    "DIY sustainable living projects",
    "Famous unsolved crimes and mysteries",
    "Cultural significance of traditional clothing",
    "Innovations in renewable materials for construction"
]

start = time.time()
for topic in topics:
    object.new_tab()
    time.sleep(.5)
    object.type(topic)
    time.sleep(.5)
    object.click_enter()
    time.sleep(1) #g
    object.scroll()
    time.sleep(.5)
    
    end = time.time() - start
    if  end > 280 and end < 289:
        pyautogui.moveRel(1600,0)
    elif end > 210 and end < 219:
        pyautogui.moveRel(-1600,0)
    elif end > 140 and end < 149:
        pyautogui.moveRel(1600,0)
    elif end > 70 and end < 79:
        pyautogui.moveRel(-1600,0)
    time.sleep(9.5)
print(time.time()-start)

