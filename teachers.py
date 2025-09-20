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
                    print(f"[x] {i}.png ไม่มีรูป (สถานะ {resp.status})")
        except Exception as e:
            print(f"[!] Error {i}: {e}")

async def main(ids=None):
    sem = asyncio.Semaphore(1000)  # 🔥 เพิ่มเป็น 500 พร้อมกัน
    async with aiohttp.ClientSession() as session:
        if ids is None:
            tasks = [fetch_and_save(session, i, sem) for i in range(00000, 99999)]
        else:
            tasks = [fetch_and_save(session, i, sem) for i in ids]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    choice = input("พิมพ์รหัสครู หรือ Enter เพื่อโหลดทั้งหมด: ").strip()
    if choice:
        ids = [int(i) for i in choice.split(",") if i.strip().isdigit()]
        asyncio.run(main(ids))
    else:
        asyncio.run(main())
