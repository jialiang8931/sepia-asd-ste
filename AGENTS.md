# 專案協作規範

本檔適用整個 repository。這是跨語言的最低要求，不是某一語言的框架。新專案先填寫 `docs/init.md`，再核准契約與語言實作。不得從其他專案推定需求。

## 指令與需求優先順序

遵守系統與開發者指令層級。在其允許範圍內，以使用者明確要求、核准需求及契約為準。若需求、契約與實作矛盾，提出衝突，不擅自改契約讓測試通過。不以縮減程式碼為由犧牲安全、正確性、可讀性、可維護性、可觀測性或測試覆蓋。

部署、基礎設施異動、commit、tag、push 與公開發布，需要當次任務的明確授權。不得自動修改其他專案、全域設定或憑證。保留使用者既有修改，不把無關內容放進提交。

## 目錄與相依方向

- `contracts/`：API、事件、資料格式、架構與操作入口契約。
- `services/<service>/core/`：純業務規則與不可變資料。
- `services/<service>/shell/`：輸入輸出、流程協調及外部資源存取。
- `infra/`：Docker、部署與基礎設施設定。不放業務邏輯。
- `scripts/`：人類直接使用的單一用途入口。不放業務規則或通用 dispatcher。
- `docs/`：需求、架構說明、操作方式與決策。
- `tests/`：unit、contract、integration 與必要的 E2E 測試。
- `tools/`：範本的驗證器及其他已核准開發工具，不是共用業務框架。
- `skills/`：可攜式 agent 技能，不包含使用者全域設定或執行紀錄。

相依方向是 `shell -> core`。core 不得依賴 shell、infra、CLI、HTTP、資料庫或雲端 SDK。跨服務透過核准契約整合，不直接 import 其他服務內部模組。新增頂層目錄或改變責任前，先取得允許並更新契約。

## Functional core, imperative shell

所有語言都採用函數式核心、命令式外殼。imperative shell 是架構邊界，不限定使用 Shell Script。

核心以純函數表達規則，相同輸入產生相同結果。不修改輸入或外部狀態。優先使用不可變資料、顯式輸入輸出與錯誤，避免共享可變狀態。時間、隨機數、識別碼與環境設定由外殼取得後顯式傳入。不要為符合形式增加不必要抽象。

外殼驗證外部資料，再交給核心。HTTP、檔案、資料庫、AWS、log、時鐘及其他副作用集中在外殼或其 adapter。把資源清理、錯誤轉換、timeout、重試與冪等性放在真正需要的邊界。不得用 catch-all 隱藏失敗。

共享程式只有出現真實重複需求後才抽取。不要預先建立框架、包裝層或一個 caller 的無用途轉接函數。

## 單一用途 scripts

公開入口以 `contracts/scripts.json` 為準。每個腳本名稱就是其完整目的。不接受位置參數、旗標、子命令或任意參數轉傳。即使是 `--help`，未獲允許前也不新增。收到參數必須在任何建置、網路或部署副作用之前失敗。

允許完成該目的所需的前置驗證。例如 production 部署可以先確認設定、目標帳號與核准狀態，驗證失敗就停止。不得以參數增加測試、環境切換、清理或其他獨立行為。

禁止 `deploy_to_production.sh --run-tests`、`prod.env deploy_to_production.sh`、`ENV=prod deploy.sh`、`deploy.sh production` 與隱藏的行為選擇環境變數。production 與 staging 使用不同、經核准的明確入口。必要設定讀取固定且公開記錄的位置；設定不得成為未經核准的功能調度器。

腳本只保留必要函數。禁止 `eval`、通用 dispatcher 與任意命令執行介面。明確使用 repo root、Dockerfile 及 build context，不依賴呼叫目錄。保留失敗 exit code，不用 `|| true` 隱藏錯誤。

HOME 與 PATH 等作業系統定位，以及受管理環境必要的 proxy/CA 設定不是功能調度器；仍不得藉此偷偷切換部署目標。上述限制適用專案公開腳本，不禁止腳本內固定的 Docker 工具選項。

## Docker 驗證

主機只需 Git、Docker 及 POSIX shell。不得要求主機安裝 Python、Node、Go、Java、Terraform 或 AWS CLI。開發、測試、打包及基礎設施工具執行都經本機 Docker，由使用者明確啟動。

依賴鎖版，基礎映像固定 digest，明確指定建置內容。不得把 repo 外的資料當 build context。驗證容器預設非 root、唯讀、無網路、無多餘 capabilities，必要暫存使用短生命週期空間。網路整合測試另訂隔離及權限，不擅自開放。

測試必須包含核心規則、邊界契約與失敗路徑。新增語言時同步提供 Docker 工具鏈、鎖檔、語言相依方向檢查及測試；Python 範例不是其他語言已驗證的證據。不要宣稱結構檢查已證明所有函數純度。

## 禁止擅自新增 CI/CD

本 repo 以單人使用及本機 Docker 驗證為準。GitHub 只保存來源、文件與版本標籤；GitHub Actions 維持停用，不包含 workflow。

未取得使用者當次明確核准，不得新增、啟用或修改任何 CI/CD，包括 GitHub Actions、其他代管平台、self-hosted runner、webhook、排程與背景自動化。不得把 Docker 驗證、commit、push、tag 或建立 repo 的授權解讀為 CI/CD 授權，也不得改用本機常駐程序或 Git hook 自動觸發。

驗證使用 `./scripts/validate.sh`，測試使用 `./scripts/test.sh`。驗證、提交、推送與部署各自獨立，不自動串接。若未來需要 CI/CD，先提出目的、觸發條件、執行位置、資源用量、權限及停止方式，經核准後再實作。

## AWS 與機敏資訊

本機 AWS 設定與身份只由使用者 `~/.aws` 存取，不讀入 agent 上下文、不列印內容、不複製到 repo、映像、測試 fixture、log 或產出檔。不要索取或保存 access key。容器只在必要 AWS 操作中唯讀掛載；一般測試不得掛載。

每個 AWS 入口必須固定並記錄核准 profile、region、預期 account ID、role 與資源範圍。變更資源前驗證實際 caller identity，不接受任意環境變數或 flags 切換目標。若身份或目標未設定，停止而不是猜測 default。

SSO 更新本機快取由使用者在容器外完成。不能為刷新快取而擅自給容器寫入憑證的權限。CI 與部署執行環境沒有使用者的 `~/.aws`，必須另行核准 workload identity/role 等方案；不得把本機憑證上傳到 GitHub 解決。

維持 TLS 驗證及最小權限。禁止提交真實環境檔、token、私鑰、客戶資料、資料庫、Terraform state/plan 或原始 log。ignore 規則不是防洩漏保證；提交前檢查實際追蹤內容及機敏資訊掃描結果。

## 文件與 agent 寫作

預設使用 repo 的 `skills/sepia-ste/SKILL.md`。同一可用上下文只讀一次並重用，不另外讀原始 Sepia。一般回答使用摘要，技術與操作文件才載入 STE principles。小說或明確要求深度 Sepia 分析時依技能路由處理。

嚴格 STE 只有使用者明確要求嚴格或 ASD-STE100 合規時才啟用。提到 STE 或採用其原則不代表嚴格模式。摘要不是完整標準、字典或合規認證。衝突優先順序為正確性與安全、明確要求、明確啟用的嚴格 STE、技術 STE 原則、Sepia 文風，並遵守指令層級。

使用使用者語言。保留命令、路徑、程式、識別碼與引文，不為文風改動它們。不自動下載或更新技能來源。必要的警告、證據及不確定性不能為節省 token 被省略。

## 交付與發布

變更需求或契約時先取得核准。交付須附變更範圍、實際執行的驗證、未執行項目、限制與產出清理情況。不得把尚未實作的部署入口寫成已可執行。

`0.0.0` 是不可變版本標籤；`latest` 初次指向同一 commit，後續移動必須另行授權。Git tag 不是 Docker image tag，也不代表成功部署。禁止 force push 或重寫既有歷史，除非使用者當次明確允許。
