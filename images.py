import aiohttp
import asyncio
import time
import os

# ฟังก์ชันสำหรับ MWN
async def fetch_and_save_mwn(session, i, sem):
    url = f"https://mwn.sis4school.com/files/images/students/{i}.jpg"
    save_path = f"students_MWN/{i}.jpg"

    async with sem:
        try:
            async with session.get(url) as resp:
                if resp.status == 200 and resp.headers.get("Content-Type", "").startswith("image"):
                    data = await resp.read()
                    with open(save_path, "wb") as f:
                        f.write(data)
                    print(f"[✓] {i}.jpg โหลดสำเร็จ")
                else:
                    print(f"[x] {i}.jpg ไม่มีไฟล์ (สถานะ {resp.status})")
        except Exception as e:
            print(f"[!] Error {i}: {e}")

async def main_mwn(ids=None):
    sem = asyncio.Semaphore(1000)
    async with aiohttp.ClientSession() as session:
        if ids is None:
            tasks = [fetch_and_save_mwn(session, i, sem) for i in range(00000, 99999)]
        else:
            tasks = [fetch_and_save_mwn(session, i, sem) for i in ids]
        await asyncio.gather(*tasks)

# ฟังก์ชันสำหรับ ASA
async def fetch_and_save_asa(session, i, sem):
    url = f"https://asa.sis4school.com/files/images/students/{i}.jpg"
    save_path = f"students_ASA/{i}.jpg"

    async with sem:
        try:
            async with session.get(url) as resp:
                if resp.status == 200 and resp.headers.get("Content-Type", "").startswith("image"):
                    data = await resp.read()
                    with open(save_path, "wb") as f:
                        f.write(data)
                    print(f"[✓] {i}.jpg โหลดสำเร็จ")
                else:
                    print(f"[x] {i}.jpg ไม่มีไฟล์ (สถานะ {resp.status})")
        except Exception as e:
            print(f"[!] Error {i}: {e}")

async def main_asa(ids=None):
    sem = asyncio.Semaphore(1000)
    async with aiohttp.ClientSession() as session:
        if ids is None:
            tasks = [fetch_and_save_asa(session, i, sem) for i in range(00000, 99999)]
        else:
            tasks = [fetch_and_save_asa(session, i, sem) for i in ids]
        await asyncio.gather(*tasks)

# ฟังก์ชันสำหรับ PWK
async def fetch_and_save_pwk(session, i, sem):
    url = f"https://pwk.sis4school.com/files/images/students/{i}.jpg"
    save_path = f"students_PWK/{i}.jpg"

    async with sem:
        try:
            async with session.get(url) as resp:
                if resp.status == 200 and resp.headers.get("Content-Type", "").startswith("image"):
                    data = await resp.read()
                    with open(save_path, "wb") as f:
                        f.write(data)
                    print(f"[✓] {i}.jpg โหลดสำเร็จ")
                else:
                    print(f"[x] {i}.jpg ไม่มีไฟล์ (สถานะ {resp.status})")
        except Exception as e:
            print(f"[!] Error {i}: {e}")

async def main_pwk(ids=None):
    sem = asyncio.Semaphore(1000)
    async with aiohttp.ClientSession() as session:
        if ids is None:
            tasks = [fetch_and_save_pwk(session, i, sem) for i in range(00000, 99999)]
        else:
            tasks = [fetch_and_save_pwk(session, i, sem) for i in ids]
        await asyncio.gather(*tasks)

# ฟังก์ชันสำหรับ PTW
async def fetch_and_save_ptw(session, i, sem):
    url = f"https://ptw.sis4school.com/files/images/students/{i}.jpg"
    save_path = f"students_PTW/{i}.jpg"

    async with sem:
        try:
            async with session.get(url) as resp:
                if resp.status == 200 and resp.headers.get("Content-Type", "").startswith("image"):
                    data = await resp.read()
                    with open(save_path, "wb") as f:
                        f.write(data)
                    print(f"[✓] {i}.jpg โหลดสำเร็จ")
                else:
                    print(f"[x] {i}.jpg ไม่มีไฟล์ (สถานะ {resp.status})")
        except Exception as e:
            print(f"[!] Error {i}: {e}")

async def main_ptw(ids=None):
    sem = asyncio.Semaphore(1000)
    async with aiohttp.ClientSession() as session:
        if ids is None:
            tasks = [fetch_and_save_ptw(session, i, sem) for i in range(00000, 99999)]
        else:
            tasks = [fetch_and_save_ptw(session, i, sem) for i in ids]
        await asyncio.gather(*tasks)

# ฟังก์ชันสำหรับ KPK
async def fetch_and_save_kpk(session, i, sem):
    url = f"https://kpk.sis4school.com/files/images/students/{i}.jpg"
    save_path = f"students_KPK/{i}.jpg"

    async with sem:
        try:
            async with session.get(url) as resp:
                if resp.status == 200 and resp.headers.get("Content-Type", "").startswith("image"):
                    data = await resp.read()
                    with open(save_path, "wb") as f:
                        f.write(data)
                    print(f"[✓] {i}.jpg โหลดสำเร็จ")
                else:
                    print(f"[x] {i}.jpg ไม่มีไฟล์ (สถานะ {resp.status})")
        except Exception as e:
            print(f"[!] Error {i}: {e}")

async def main_kpk(ids=None):
    sem = asyncio.Semaphore(1000)
    async with aiohttp.ClientSession() as session:
        if ids is None:
            tasks = [fetch_and_save_kpk(session, i, sem) for i in range(00000, 99999)]
        else:
            tasks = [fetch_and_save_kpk(session, i, sem) for i in ids]
        await asyncio.gather(*tasks)

# เมนูสำหรับ MWN
def menu_01():
    os.makedirs("students_MWN", exist_ok=True)
    choice = input("พิมพ์รหัสนักเรียน หรือ Enter เพื่อโหลดทั้งหมด: ").strip()
    if choice:
        ids = [int(i) for i in choice.split(",") if i.strip().isdigit()]
        asyncio.run(main_mwn(ids))
    else:
        asyncio.run(main_mwn())

# เมนูสำหรับ ASA
def menu_02():
    os.makedirs("students_ASA", exist_ok=True)
    choice = input("พิมพ์รหัสนักเรียน หรือ Enter เพื่อโหลดทั้งหมด: ").strip()
    if choice:
        ids = [int(i) for i in choice.split(",") if i.strip().isdigit()]
        asyncio.run(main_asa(ids))
    else:
        asyncio.run(main_asa())

# เมนูสำหรับ PWK
def menu_03():
    os.makedirs("students_PWK", exist_ok=True)
    choice = input("พิมพ์รหัสนักเรียน หรือ Enter เพื่อโหลดทั้งหมด: ").strip()
    if choice:
        ids = [int(i) for i in choice.split(",") if i.strip().isdigit()]
        asyncio.run(main_pwk(ids))
    else:
        asyncio.run(main_pwk())

# เมนูสำหรับ PTW
def menu_04():
    os.makedirs("students_PTW", exist_ok=True)
    choice = input("พิมพ์รหัสนักเรียน หรือ Enter เพื่อโหลดทั้งหมด: ").strip()
    if choice:
        ids = [int(i) for i in choice.split(",") if i.strip().isdigit()]
        asyncio.run(main_ptw(ids))
    else:
        asyncio.run(main_ptw())

# เมนูสำหรับ KPK
def menu_05():
    os.makedirs("students_KPK", exist_ok=True)
    choice = input("พิมพ์รหัสนักเรียน หรือ Enter เพื่อโหลดทั้งหมด: ").strip()
    if choice:
        ids = [int(i) for i in choice.split(",") if i.strip().isdigit()]
        asyncio.run(main_kpk(ids))
    else:
        asyncio.run(main_kpk())

# เมนูหลัก
def main_menu():
    while True:
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print("======== ระบบดึงภาพนักเรียน ========\n")
        print("1. โหลดภาพนักเรียนของ MWN")
        print("2. โหลดภาพนักเรียนของ ASA")
        print("3. โหลดภาพนักเรียนของ PWK")
        print("4. โหลดภาพนักเรียนของ PTW")
        print("5. โหลดภาพนักเรียนของ KPK")
        print("0. ออกจากโปรแกรม")
        print("===============================")
        choice = input("กรุณาเลือกที่จะทำ: ").strip()

        if choice == "1":
            menu_01()
            input("\nกด Enter เพื่อกลับเมนูหลัก...")
        elif choice == "2":
            menu_02()
            input("\nกด Enter เพื่อกลับเมนูหลัก...")
        elif choice == "3":
            menu_03()
            input("\nกด Enter เพื่อกลับเมนูหลัก...")
        elif choice == "4":
            menu_04()
            input("\nกด Enter เพื่อกลับเมนูหลัก...")
        elif choice == "5":
            menu_05()
            input("\nกด Enter เพื่อกลับเมนูหลัก...")
        elif choice == "0":
            print("ออกจากโปรแกรม...")
            break
        else:
            print("กรุณาเลือกที่ถูกต้อง")
            time.sleep(2)

if __name__ == "__main__":
    main_menu()