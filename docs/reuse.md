# 建立新專案

1. 在 GitHub 使用此 repo 的 Use this template 建立新 repo。
2. 填寫 `docs/init.md`，確認語言、契約與服務責任。
3. 替換 Python 範例時，同步更新 Dockerfile、測試、架構檢查與契約。
4. 執行 `./scripts/validate.sh`。
5. 人工審查機敏資訊、FP 邊界及實際驗收結果，再發布。

模板不會自動強制所有既有 repo 遵守規範。既有專案須明確導入 AGENTS、檢查與 CI；分支保護需要 repository 管理員另外啟用 required checks。不得宣稱只新增 AGENTS 就無法繞過規範。

此 repo 內的 `skills/sepia-ste` 可直接作為專案技能參考。全域安裝是另一項明確操作；範本不自動覆寫任何 `~/.codex/AGENTS.md` 或已安裝技能。摘要會隨 repo 版本固定，只有明確要求更新來源才刷新。

`0.0.0` 固定標記首次發布的 commit。`latest` 首次指向相同 commit；後續更新需要明確授權，不自動 force push。範本變更不會自動傳入由它建立的 repo，需要審查後自行同步。

公開 repo 不等於所有內含來源都有相同授權。ASD-STE100 完整標準與字典未包含在此 repo，也未重新授權。Sepia 摘要來源及版本記錄於技能來源檔。
