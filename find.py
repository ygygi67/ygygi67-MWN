#!/usr/bin/env python3
"""
อ่าน Google Sheet แบบ public โดยไม่ต้องใช้ service account
ติดตั้ง pandas ก่อนใช้งาน:
    pip install pandas requests

วิธีใช้:
    python find.py --sheet <Google Sheet URL> [คำค้นหา]
    หรือรันแล้วตอบคำถาม
"""

import argparse
import pandas as pd
import requests
import sys
import os
import re
import time
import threading
from google.oauth2.service_account import Credentials
import gspread

# Configuration
SPREADSHEET_ID_OR_URL = "1RoG2P3JaDOYwdbbEQllJZPt3H8lHv0o2LOMP8f9I1ac"
SHEET_NAME = "Sheet1"

def typewriter_print(text, delay=0.05):
    """พิมพ์ข้อความแบบ typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def loading_animation(duration=7):
    """แสดง loading animation"""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    messages = [
        "กำลังเชื่อมต่อกับฐานข้อมูล",
        "กำลังโหลดข้อมูล",
        "กำลังประมวลผลข้อมูล",
        "เตรียมข้อมูลให้พร้อมใช้งาน"
    ]
    
    start_time = time.time()
    frame_index = 0
    message_index = 0
    
    while time.time() - start_time < duration:
        elapsed = time.time() - start_time
        
        # เปลี่ยนข้อความตามเวลา
        if elapsed < 2:
            current_message = messages[0]
        elif elapsed < 4:
            current_message = messages[1]
        elif elapsed < 6:
            current_message = messages[2]
        else:
            current_message = messages[3]
        
        print(f"\r{frames[frame_index]} {current_message}...", end='', flush=True)
        frame_index = (frame_index + 1) % len(frames)
        time.sleep(0.1)
    
    print(f"\r✅ เชื่อมต่อสำเร็จ!" + " " * 50)
    time.sleep(0.5)

def sheet_url_to_csv(sheet_url):
    m = re.search(r'/d/([a-zA-Z0-9-_]+)', sheet_url)
    if m:
        sheet_id = m.group(1)
    else:
        sheet_id = sheet_url
    return f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

def display_student_info(row_data, columns):
    """แสดงข้อมูลนักเรียนในรูปแบบที่กำหนด"""
    code_col = None
    for col in columns:
        if any(keyword in col.lower() for keyword in ['id', 'code', 'รหัส', 'เลขที่']):
            code_col = col
            break
    code_value = ""
    if code_col:
        code_value = str(row_data[code_col]) if pd.notna(row_data[code_col]) else ""

    # ถ้ารหัสเป็น NO ไม่แสดงผลอะไรเลย
    if code_col and code_value.strip().upper() == "NO":
        return

    # หาคอลัมน์ชื่อ
    name_value = ""
    for col in columns:
        if any(keyword in col.lower() for keyword in ['name', 'ชื่อ', 'นาม']):
            name_value = str(row_data[col]) if pd.notna(row_data[col]) else "ไม่ระบุ"
            break

    print(f"ชื่อ : {name_value}")
    if code_col:
        print(f"รหัส : {code_value}")

def search_data(df, query):
    """ค้นหาข้อมูลใน DataFrame"""
    if query.lower() in ['all', 'ทั้งหมด', 'all data', 'show all']:
        return df
    
    query_norm = str(query).strip().lower()
    results = []
    
    for idx, row in df.iterrows():
        if any(query_norm in str(val).lower() for val in row if pd.notna(val)):
            results.append(row)
    
    if results:
        return pd.DataFrame(results)
    else:
        return pd.DataFrame()

def main():
    # แสดง header
    print("\n" + "="*60)
    typewriter_print("🔍 ระบบค้นหารหัส", 0.08)
    print("="*60)
    
    # โหลด loading animation
    loading_animation(7)
    
    # โหลดข้อมูล
    sheet_url = SPREADSHEET_ID_OR_URL
    csv_url = sheet_url_to_csv(sheet_url)
    
    try:
        df = pd.read_csv(csv_url)
        typewriter_print("📊 โหลดข้อมูลสำเร็จ!", 0.05)
    except Exception as e:
        typewriter_print(f"❌ เกิดข้อผิดพลาด: {e}", 0.03)
        typewriter_print("กรุณาตรวจสอบว่า Google Sheet เปิด public แล้ว", 0.03)
        sys.exit(1)
    
    time.sleep(1)
    
    # Loop สำหรับค้นหาต่อเนื่อง
    while True:
        print("\n" + "-"*40)
        typewriter_print("💡 ทำโดย ygygi6 ถ้าอยากได้ข้อมูลเพิ่งแบบหนัก ๆ ต้องจ่ายเงินเพิ่มนะจ้ะ", 0.02)
        typewriter_print("          กด Ctrl+C เพื่อออกจากโปรแกรม", 0.02)
        print("-"*40)
        
        try:
            query = input("\n🔎 กรุณาใส่ชื่อหรือรหัสที่ต้องการค้นหา: ").strip()
            
            if not query:
                typewriter_print("⚠️  กรุณาใส่คำค้นหา", 0.03)
                continue
            
            # แสดง searching animation
            search_frames = ["🔍", "🔎", "🔍", "🔎"]
            for i in range(8):
                print(f"\r{search_frames[i % len(search_frames)]} กำลังค้นหา...", end='', flush=True)
                time.sleep(0.2)
            print("\r" + " "*20 + "\r", end='')
            
            results = search_data(df, query)

            if len(results) > 0:
                if query.lower() in ['all', 'ทั้งหมด', 'all data', 'show all']:
                    typewriter_print("="*60, 0.002)
                    for idx, row in results.iterrows():
                        # แสดง searching animation ก่อนแต่ละรายการ
                        for i in range(4):
                            print(f"\r🔎 กำลังแสดงข้อมูล...", end='', flush=True)
                            time.sleep(0.1)
                        print("\r" + " "*20 + "\r", end='')
                        display_student_info(row, df.columns)
                    typewriter_print("="*60, 0.002)
                else:
                    if len(results) == 1:
                        typewriter_print("✅ พบข้อมูลที่ตรงกัน!", 0.03)
                        time.sleep(0.5)
                        display_student_info(results.iloc[0], df.columns)
                    else:
                        typewriter_print(f"✅ พบข้อมูลที่ตรงกัน {len(results)} รายการ:", 0.03)
                        typewriter_print("="*60, 0.002)
                        time.sleep(0.5)
                        for idx, row in results.iterrows():
                            # ถ้ารหัสเป็น NO จะไม่แสดงอะไรเลย
                            code_col = None
                            for col in df.columns:
                                if any(keyword in col.lower() for keyword in ['id', 'code', 'รหัส', 'เลขที่']):
                                    code_col = col
                                    break
                            code_value = str(row[code_col]) if code_col and pd.notna(row[code_col]) else ""
                            if code_value.strip().upper() == "NO":
                                continue
                            display_student_info(row, df.columns)
                        typewriter_print("="*60, 0.002)
            else:
                typewriter_print("❌ ยังไม่มีรหัสนี้ โปรดลองใหม่อีกครั้ง", 0.04)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            print("\n")
            typewriter_print("👋 ขอบคุณที่ใช้บริการ!", 0.05)
            typewriter_print("🚪 กำลังออกจากโปรแกรม...", 0.05)
            time.sleep(1)
            break
        except Exception as e:
            typewriter_print(f"❌ เกิดข้อผิดพลาด: {e}", 0.03)
            time.sleep(1)

if __name__ == "__main__":
    main()