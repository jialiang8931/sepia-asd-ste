# 初始版本驗證

日期：2026-10-24。以下是初始範本的本機 Docker 驗證，不代表正式部署驗收。

- `./scripts/validate.sh` 通過。包含 Gitleaks 掃描、結構與入口契約檢查、Python 範例相依方向檢查及 15 個測試。
- `./scripts/test.sh` 從非 repo 工作目錄執行通過。
- 完整驗證映像可在沒有主機來源掛載的容器中執行測試與結構檢查。
- 兩個入口實際收到 `--run-tests`、`production`、`--help` 時，均回傳 exit code 2，沒有呼叫 Docker。
- 測試包含不可變輸入、空值、負數業務錯誤、無效 JSON、錯誤型別、禁止的 core import、機敏路徑與掃描輸出不回顯秘密。
- Gitleaks 版本為 8.30.1，映像依 digest 鎖定。掃描未發現機敏資訊，但任何掃描器都無法保證識別所有秘密。

未執行 AWS 操作、真實部署、Terraform apply、其他程式語言測試或完整 ASD-STE100 合規審查。範本未提供這些功能。初始版本曾加入 GitHub workflow；其後依使用者要求停用 Actions 並從 main 移除 workflow，只保留本機 Docker 驗證。這不修改兩個既有版本標籤的歷史內容。

公開來源不含本機 AWS 設定、環境檔、原始日誌、客戶資料、ESG 服務實作或使用者全域 AGENTS。Git 提交身份使用 GitHub noreply email。
