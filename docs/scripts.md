# 本 repo 的操作入口

現有入口以 `contracts/scripts.json` 為準，只操作本 repo 的驗證及既有示範，不調度其他專案。

| 指令 | 唯一目的 | 接受參數 |
| --- | --- | --- |
| `./scripts/validate.sh` | 在本機 Docker 掃描、檢查及驗證本 repo | 無 |
| `./scripts/test.sh` | 在本機 Docker 執行既有測試 | 無 |

兩個入口在任何副作用前拒絕參數，不依賴呼叫工作目錄。沒有 MODE、ENV、RUN_TESTS 等行為選擇器，也沒有任意命令轉傳。

單一用途允許必要的前置驗證，但不允許以 `deploy_to_production.sh --run-tests`、`deploy.sh production`、`ENV=prod deploy.sh` 或 `prod.env deploy_to_production.sh` 混合或隱藏行為。這些部署名稱只是規則示例，本 repo 沒有部署入口。

固定的 Docker 工具選項不是可切換的公開模式。Dockerfile 與專用 ignore 檔均在 infra/docker/，build context 明確指定為 repo root。

執行入口需要 Docker daemon 與首次下載映像的權限。本機允許安裝 Docker、AWS CLI、Git，Python、Terraform、Gitleaks 及其他開發工具走容器。腳本不自動安裝工具、不執行 sudo、不關閉 TLS，也不把失敗隱藏成成功。

現有腳本與檢查不代表其他專案必須採用。不為完整性增加新入口、dispatcher、Git hook 或背景自動化。沒有明確需求與授權時不新增流程。
