# 建立新專案

1. 在 GitHub 使用此 repo 的 Use this template 建立新 repo。
2. 填寫 `docs/init.md`，確認語言、契約與服務責任。
3. 替換 Python 範例時，同步更新 Dockerfile、測試、架構檢查與契約。
4. 執行 `./scripts/validate.sh`。
5. 人工審查機敏資訊、FP 邊界及實際驗收結果，再發布。

模板不會自動強制所有既有 repo 遵守規範。既有專案須明確導入 AGENTS 與本機 Docker 檢查。不得宣稱只新增 AGENTS 就無法繞過規範。

本 repo 不提供 CI/CD，GitHub Actions 維持停用。由範本建立的新 repo 不保證繼承 GitHub 的 repository 設定，需自行確認 Actions 狀態；沒有 workflow 也不等於設定已停用。沒有當次明確授權，不得新增任何遠端或本機自動化。驗證、提交、推送與部署各自獨立。

此 repo 內的 `skills/sepia-ste` 可直接作為專案技能參考。全域安裝是另一項明確操作；範本不自動覆寫任何 `~/.codex/AGENTS.md` 或已安裝技能。摘要會隨 repo 版本固定，只有明確要求更新來源才刷新。

`0.0.0` 固定標記首次發布的 commit。`latest` 首次指向相同 commit；後續更新需要明確授權，不自動 force push。範本變更不會自動傳入由它建立的 repo，需要審查後自行同步。

本次移除 workflow 的變更只更新 `main`，沒有移動或重建 `0.0.0` 與 `latest`。這兩個歷史標籤仍包含初始版本的 workflow；要使用無 workflow 的範本，請使用目前的 `main`，不要用這兩個舊標籤。

公開 repo 不等於所有內含來源都有相同授權。ASD-STE100 完整標準與字典未包含在此 repo，也未重新授權。Sepia 摘要來源及版本記錄於技能來源檔。
