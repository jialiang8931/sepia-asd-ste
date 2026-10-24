# AWS 存取邊界

範本沒有 AWS 操作入口，不會讀取或掛載你的憑證。

正式加入本機 AWS 入口前，先確認 profile、region、account ID、role、資源範圍與操作目的。把非機敏目標設定放在該用途固定的設定檔，不讓使用者透過臨時環境變數或參數選擇 production。

AWS 工具在 Docker 執行。只有必要 AWS 操作才把主機 `~/.aws` 唯讀掛載到工具使用者的 home 對應位置。不要把它放進 build context、Dockerfile COPY、repo、測試或 log。工具鏈若需要 SSO 刷新寫入，請使用者先在容器外完成，不自行改成可寫掛載。

資源異動前，透過固定 profile 檢查 caller identity 是否符合核准 account 與 role，再執行唯一目的。驗證失敗即停止。不得沿用不明的 default 身份，也不得用 CLI flags 或環境變數偷偷切換目標。

CI 不具有你的本機 `~/.aws`。需要存取 AWS 時，另行核准 workload identity、OIDC 或 execution role 方案。不要把本機 access key 複製成 repository secret，也不要假裝本機 profile 已可在 CI 使用。

GitHub 發布不得包含憑證、真實環境檔、私鑰、state、plan、客戶資料或原始 log。範本的機敏資訊掃描只是常見模式檢查，不能保證識別所有秘密。
