# sepia-asd-ste

跨語言專案範本，採 Functional Core, Imperative Shell。主機只需 Git、Docker 及 POSIX shell。內附 Python 最小範例，示範架構，不限定正式專案語言。

## 驗證範本

```sh
./scripts/validate.sh
```

此入口先使用鎖定映像的 Gitleaks 掃描機敏資訊，再在本機 Docker 內檢查目錄、腳本契約及範例相依方向，最後執行測試。掃描結果不代表可保證識別所有秘密。只執行測試：

```sh
./scripts/test.sh
```

兩個入口均不接受任何參數。第一次執行需取得鎖定的官方 Python 與 Gitleaks Docker 映像。主機不需要安裝 Python 或 Gitleaks。

此 repo 僅保留手動啟動的本機 Docker 驗證。GitHub Actions 已停用，沒有 CI/CD workflow。未經當次明確核准，不得新增或啟用 CI/CD，也不得在 push、tag 或本機 Git hook 中自動觸發驗證或部署。

## 架構

```text
AGENTS.md
contracts/
  architecture.json
  scripts.json
  sample-request.schema.json
services/sample/
  core/
  shell/
infra/
  docker/Dockerfile
  deployments/production/README.md
scripts/
  validate.sh
  test.sh
tools/validate_repository.py
tests/
docs/
  init.md
  architecture.md
  scripts.md
  aws.md
  reuse.md
skills/sepia-ste/
```

先讀 `AGENTS.md`，再填寫 `docs/init.md`。相依方向固定為 shell 到 core。規範跨語言，現有自動檢查只覆蓋列出的結構、Shell 規則與 Python 範例；新增語言需要補齊檢查。

## 重複使用

可透過 GitHub 的 Use this template 建立自己的 repo。每個新專案都會得到獨立歷史，不會自動同步後續範本變更。詳見 `docs/reuse.md`。

內附 `skills/sepia-ste`，不需要連回作者機器。一般回答使用 Sepia 摘要，技術文件按需加入 STE；嚴格模式必須明確要求。沒有完整標準與字典，不宣稱 ASD-STE100 合規。

範本沒有真實部署、AWS 帳號、憑證或客戶資料。production 部署尚未實作，不存在假成功的部署入口。`0.0.0` 與 `latest` 是 Git 標籤，與部署狀態無關。
