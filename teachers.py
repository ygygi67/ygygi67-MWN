import asyncio
import aiohttp
import os

# โฟลเดอร์เก็บภาพ
os.makedirs("teachers_images", exist_ok=True)

async def fetch_and_save(session, i, sem):
    url = f"https://mwn.sis4school.com/files/images/teachers/{i}.png"
    save_path = f"teachers_images/{i}.png"

    async with sem:  # จำกัดจำนวน request พร้อมกัน
        try:
            async with session.get(url) as resp:
                if resp.status == 200 and resp.headers.get("Content-Type", "").startswith("image/"):
                    data = await resp.read()
                    with open(save_path, "wb") as f:
                        f.write(data)
                    print(f"[✓] {i}.png โหลดสำเร็จ")
                else:
                    print(f"[x] {i}.png ไม่มีไฟล์ (status {resp.status})")
        except Exception as e:
            print(f"[!] Error {i}: {e}")

async def main():
    sem = asyncio.Semaphore(1000)  # 🔥 เพิ่มเป็น 500 พร้อมกัน
    async with aiohttp.ClientSession() as session:
        # เปลี่ยน range ได้ตามที่ต้องการ เช่น 999 ถึง 9999
        tasks = [fetch_and_save(session, i, sem) for i in range(00000, 99999)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
