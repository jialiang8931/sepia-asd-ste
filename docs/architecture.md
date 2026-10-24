# 架構責任

外殼讀取及驗證輸入，再把明確的值交給核心。核心回傳結果，外殼負責輸出或執行外部操作。相依方向固定為 shell 到 core。

範例的 `services/sample/core/quantities.py` 對不可變 tuple 計算總數，不讀取檔案、環境或網路。負數是業務錯誤。外殼 `services/sample/shell/main.py` 處理 JSON、型別驗證、stdin、stdout、stderr 及 exit code。

輸入與 `contracts/sample-request.schema.json` 對應。整數的邊界解析拒絕布林與小數，核心不重做外部格式驗證。成功回傳 total，無效輸入回傳非零 exit code，不輸出原始敏感 payload。

這個 repo 的架構規範跨語言。新增語言可使用其慣用的 module/package，但仍須保留 core 與 shell 責任、Docker 驗證及相依方向。新增語言時須補上自己的靜態檢查或測試。現有 Python import 檢查不能證明其他語言的架構。

靜態檢查只提供部分保證。沒有 import 的程式仍可能呼叫副作用或修改狀態，因此 review 仍須檢查純度、可變狀態與真正的資料流。例外要由 owner 核准，不允許用規避檢查的方式維持表面通過。
