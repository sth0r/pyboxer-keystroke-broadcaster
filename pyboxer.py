
import time
time.sleep(5)
import sys
import win32api
import win32gui as wgui
import win32process as wproc
import win32con as wcon

import ctypes as ct
from ctypes import wintypes as wt
import keyboard


WM_KEYDOWN = 0x100
WM_KEYUP = 0x101


class GUITHREADINFO(ct.Structure):
    _fields_ = [
        ("cbSize", wt.DWORD),
        ("flags", wt.DWORD),
        ("hwndActive", wt.HWND),
        ("hwndFocus", wt.HWND),
        ("hwndCapture", wt.HWND),
        ("hwndMenuOwner", wt.HWND),
        ("hwndMoveSize", wt.HWND),
        ("hwndCaret", wt.HWND),
        ("rcCaret", wt.RECT),

    ]

    def __str__(self):
        ret = "\n" + self.__repr__()
        start_format = "\n  {0:s}: "
        for field_name, _ in self. _fields_[:-1]:
            field_value = getattr(self, field_name)
            field_format = start_format + ("0x{1:016X}" if field_value else "{1:}")
            ret += field_format.format(field_name, field_value)
        rc_caret = getattr(self, self. _fields_[-1][0])
        ret += (start_format + "({1:d}, {2:d}, {3:d}, {4:d})").format(self. _fields_[-1][0], rc_caret.top, rc_caret.left, rc_caret.right, rc_caret.bottom)
        return ret


def findWindowWithName(window_name):
    hwnd = wgui.FindWindowEx(wcon.NULL, 0, wcon.NULL, window_name) #Finds window handle (hwnd)
    return hwnd

def scanToVirtualKey(scan):
    scankey = (57,41,11,2,3,4,5,6,7,8,9,10,12,13,23,59,60,61,62,63,64,65,66,67,68,87,88)
    virtuelkey = (32,220,48,49,50,51,52,53,54,55,56,57,187,219,73,112,113,114,115,116,117,118,119,120,121,122,123)
    if scan==scankey[0]:return virtuelkey[0]
    if scan==scankey[1]:return virtuelkey[1]
    if scan==scankey[2]:return virtuelkey[2]
    if scan==scankey[3]:return virtuelkey[3]
    if scan==scankey[4]:return virtuelkey[4]
    if scan==scankey[5]:return virtuelkey[5]
    if scan==scankey[6]:return virtuelkey[6]
    if scan==scankey[7]:return virtuelkey[7]
    if scan==scankey[8]:return virtuelkey[7]
    if scan==scankey[9]:return virtuelkey[9]
    if scan==scankey[10]:return virtuelkey[10]
    if scan==scankey[11]:return virtuelkey[11]
    if scan==scankey[12]:return virtuelkey[12]
    if scan==scankey[13]:return virtuelkey[13]
    if scan==scankey[14]:return virtuelkey[14]
    if scan==scankey[15]:return virtuelkey[15]
    if scan==scankey[16]:return virtuelkey[16]
    if scan==scankey[17]:return virtuelkey[17]
    if scan==scankey[18]:return virtuelkey[18]
    if scan==scankey[19]:return virtuelkey[19]
    if scan==scankey[20]:return virtuelkey[20]
    if scan==scankey[21]:return virtuelkey[21]
    if scan==scankey[22]:return virtuelkey[22]
    if scan==scankey[23]:return virtuelkey[23]
    if scan==scankey[24]:return virtuelkey[24]
    if scan==scankey[25]:return virtuelkey[25]
    if scan==scankey[26]:return virtuelkey[26]
    return 666
	

	
def gethwndFocus(hwnd):
    tid, pid = wproc.GetWindowThreadProcessId(hwnd) #gets treathId and ProcessId from window handle (hwnd)
    user32_dll = ct.WinDLL("user32.dll") #Does this make user32.dll interactable? question 1
    GetGUIThreadInfo = getattr(user32_dll, "GetGUIThreadInfo") #what does this do? question 2
    GetGUIThreadInfo.argtypes = [wt.DWORD, ct.POINTER(GUITHREADINFO)] #what does this do? question 3
    GetGUIThreadInfo.restype = wt.BOOL #what does this do? question 4
    gti = GUITHREADINFO() 
    gti.cbSize = ct.sizeof(GUITHREADINFO)
    res = GetGUIThreadInfo(tid, ct.byref(gti))
    #print("{0:s} returned: {1:d}".format(GetGUIThreadInfo.__name__, res))
    if res:
        print("hwndFocus found")
    win32api.PostMessage(gti.hwndFocus,WM_KEYDOWN,32,0) #sends space keey stroke to indicade hwndFocus has been found
    return gti.hwndFocus

print("Trying to find " + sys.argv[1] + " window")	
hwnd = findWindowWithName(sys.argv[1])

print("Trying to find hwndFocus")
hwndFocus = gethwndFocus(hwnd)

print ("starting broadcasting keys to " + sys.argv[1] + " window")
print("press ctrl + c to stop broadcasting")
while 1:
    event1 = keyboard.read_event(suppress=False)
    #print ("step 1")
    if event1.event_type == "down":
        key = scanToVirtualKey(event1.scan_code)
        #print ("step 2 key = " + str(key))
        if key != 666:
            #print ("step 3")
            win32api.PostMessage(hwndFocus,0x100,key,0)
            win32api.PostMessage(hwndFocus,0x101,key,0)
