# AWS 存取參考

本 repo 沒有 AWS 操作入口，既有驗證不讀取或掛載憑證。以下是經核准有 AWS 需求時的存取原則，不是要求其他專案新增 AWS 整合。

本機允許安裝 AWS CLI，身份與設定使用 `~/.aws`。容器需要 AWS 存取時才唯讀掛載，不複製進 build context、映像、repo、測試或 log。

操作前確認核准的 profile、region、account、role、資源範圍與唯一目的。資源異動前驗證 caller identity 與目標，資訊不足就停止，不猜測 default，不用臨時參數或環境變數偷偷切換部署目標。

SSO 刷新由使用者透過核准方式處理，不自行把憑證掛載改成可寫。不得索取或保存 access key，也不把本機憑證上傳到 GitHub。

Terraform 必須在 Docker 執行，本機 AWS CLI 的安裝許可不擴及 Terraform 或其他開發工具。

本 repo 不提供 CI/CD，不因 AWS 文件存在而新增遠端身份、部署或自動化流程。公開內容不得含憑證、私鑰、真實環境檔、state、plan、客戶資料或原始 log；掃描結果不是絕對安全保證。
