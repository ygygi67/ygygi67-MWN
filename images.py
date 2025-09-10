import aiohttp
import asyncio
import os

# โฟลเดอร์เก็บภาพ
os.makedirs("students_images", exist_ok=True)

async def fetch_and_save(session, i, sem):
    url = f"https://mwn.sis4school.com/files/images/students/{i}.jpg"
    save_path = f"students_images/{i}.jpg"

    async with sem:  # จำกัดจำนวน request พร้อมกัน
        try:
            async with session.get(url) as resp:
                if resp.status == 200 and resp.headers.get("Content-Type", "").startswith("image"):
                    data = await resp.read()
                    with open(save_path, "wb") as f:
                        f.write(data)
                    print(f"[✓] {i}.jpg โหลดสำเร็จ")
                else:
                    print(f"[x] {i}.jpg ไม่มีไฟล์ (status {resp.status})")
        except Exception as e:
            print(f"[!] Error {i}: {e}")

async def main():
    sem = asyncio.Semaphore(1000)  # โหลดพร้อมกันสูงสุด 200
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_save(session, i, sem) for i in range(00000, 99999)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
