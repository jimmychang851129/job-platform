Preparation:
1. MySQL 設置密碼(如果記得則略過)
2. 執行 mysql -u root -p
3. 輸入密碼
4. CREATE DATABASE Positions;
5. 回去app/databasse.py 修改密碼（root:password）
6. 正常執行 'uvicorn app.main:app --reload'

Usage:
1. 一開始 DB為空，所以先post 一筆資料上去，我這邊使用Post man 
 POST  http://127.0.0.1:8000/positions
 body(raw-json):{
    "title": "machine learning engineer",
    "company": "google",
    "full_or_part": "part-time",
    "site": "Taipei",
    "position_level": "L1",
    "sitemap":"",
    "pay":  "50k~80K/ Month",
    "url": "https://www.google.com/?client=safari",
    "skills": "C++/C/Python"
  }
2. list all data:
 GET http://127.0.0.1:8000/positions/all

3. 刪除：
 DELETE http://127.0.0.1:8000/positions/1

過程可以用 mysq底下指令確認  SELECT * FROM ML_Engineer;

