![compdf-github-banner 1](assets/ComPDF-Comprehensive%20PDF%20Solutions.png)
[English](README.md) | [繁體中文](README_繁中.md) | [日本語](README_JA.md) | [简体中文](README_CN.md)

# ComPDF MCP

ComPDF MCP 專為 MCP 用戶端與 AI Agent 平台，提供 PDF/圖片剖析與資料擷取、PDF 格式轉換、PDF 編輯、圖片格式轉換等能力。它可協助使用者先處理原始文件，再將更輕量、更乾淨、更結構化的結果交給 AI，進而降低 AI Token 消耗並節省營運成本，並提升整體處理效率。

> * 如果你覺得 ComPDF MCP 對你有幫助，歡迎在 GitHub 給我們一個 ⭐ **Star**，這會幫助我們持續優化產品。
> * 如果你有問題或想法，歡迎加入我們的 [Discussions](https://github.com/ComPDFKit/compdf-mcp/discussions) 一起交流。

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/docker-supported-blue" alt="Docker"></a>
  <a href="#"><img src="https://img.shields.io/github/stars/ComPDFKit/compdf-mcp" alt="GitHub Stars"></a>
  <a href="#"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs Welcome"></a>
</p>

<p align="center">
  <a href="#為什麼選擇-compdf-mcp"><b>為什麼選擇 ComPDF MCP</b></a> •
  <a href="#功能支援"><b>功能支援</b></a> •
  <a href="#技術架構"><b>技術架構</b></a> •
  <a href="#快速開始"><b>快速開始</b></a> •
  <a href="#部署與維運"><b>部署與維運</b></a> •
  <a href="#license-與免費使用"><b>License 與免費使用</b></a> •
  <a href="#適用情境與範例提問"><b>適用情境與範例提問</b></a> •
  <a href="#支援"><b>支援</b></a>
</p>

## 為什麼選擇 ComPDF MCP

使用者採用 ComPDF MCP 的核心原因，不只是「讓 AI 能處理 PDF」，而是先將複雜、冗長、雜訊較多的原始文件處理成更適合模型理解的輸入，再交由 AI 完成分析、摘要、問答或自動化任務。

原始 PDF、掃描件與圖片檔案通常體積更大、上下文更雜、結構也較不穩定。先透過 ComPDF MCP 完成轉換、擷取與頁面處理，再將結果交給 AI，可以：

- 降低 AI Token 消耗
- 減少 AI 費用支出
- 縮短回應時間
- 提高結構化結果品質
- 減少複雜檔案直接進入模型所帶來的成本浪費
- 透過單一 MCP 服務完成 PDF 與圖片檔案處理
- 適用於文件密集型工作流程與多平台 Agent 情境

尤其在需要批次處理報告、合約、發票、表格、掃描件等文件的情境中，這種「先處理文件、再呼叫 AI」的方式，通常比直接將原始檔交給模型更節省成本，也更適合銜接後續工作流程。

## 功能支援

ComPDF MCP 聚焦三大能力方向：文件轉換、PDF 操作，以及智慧解析與資料擷取。

### 1. PDF 與圖片轉換

| 能力             | 說明                                                           |
| -------------- | ------------------------------------------------------------ |
| PDF 轉 Word     | 將 PDF 檔案轉換為可編輯的 Word 文件，並盡可能保留原始版式、文字、圖片與格式。                 |
| PDF 轉 Excel    | 將 PDF 檔案轉換為 Excel，支援表格、數字與結構化商務資料。                           |
| PDF 轉 PPT      | 將 PDF 頁面轉換為可編輯的 PowerPoint 投影片，並盡量保留原始版式與視覺結構。               |
| PDF 轉 HTML     | 將 PDF 檔案轉換為 HTML，用於網頁展示與內容再利用，同時保留文字、圖片、表格與版式。               |
| PDF 轉 RTF      | 將 PDF 檔案轉換為 RTF 文件，支援文字與圖片內容。                                |
| PDF 轉圖片        | 將 PDF 頁面轉換為 PNG 或 JPG 圖片，並支援解析度與 DPI 設定。                     |
| PDF 轉 CSV      | 從 PDF 檔案中擷取表格並匯出為 CSV，可依單表匯出，也可合併匯出。                         |
| PDF 轉 TXT      | 從 PDF 或掃描版 PDF 中擷取文字，並儲存為純文字檔。                               |
| PDF 轉 JSON     | 從 PDF 檔案中擷取文字、表格與圖片，並儲存為結構化 JSON。                            |
| PDF 轉 Markdown | 將 PDF 檔案轉換為 Markdown，方便在知識庫、開發文件、部落格系統與 AI 工作流程中持續編輯、檢索與再利用。 |
| PDF 轉可搜尋 PDF   | 對掃描版 PDF 執行 OCR 辨識，產生可搜尋、可複製、可標示重點文字的 PDF 文件，便於檢索、歸檔與後續處理。   |
| PDF 轉 OFD      | 將 PDF 檔案轉換為 OFD，便於在 OFD 歸檔、流轉與在地化辦公情境中使用。                    |
| Word 轉 PDF     | 將 Word 文件轉換為 PDF，盡量保留原始排版、字型、圖片與頁面結構，適合正式分享、歸檔與列印。           |
| PNG 轉 PDF      | 將 PNG 圖片轉換為 PDF，便於將截圖、設計圖或佐證圖片統一整理、傳輸與歸檔。                    |
| RTF 轉 PDF      | 將 RTF 文件轉換為 PDF，在保留基本文字樣式與版面的同時，方便跨裝置檢視與正式輸出。                |
| Excel 轉 PDF    | 將 Excel 活頁簿或試算表轉換為 PDF，便於報表分享、列印、歸檔與避免公式被誤改。                 |
| TXT 轉 PDF      | 將 TXT 純文字檔轉換為 PDF，適合將日誌、筆記、說明文件等內容整理為固定版式檔案。                 |
| CSV 轉 PDF      | 將 CSV 表格資料轉換為 PDF，便於資料快照分享、審閱、列印與業務歸檔。                       |
| PPT 轉 PDF      | 將 PowerPoint 簡報轉換為 PDF，便於簡報資料分發、跨裝置檢視與正式留存。                  |
| HTML 轉 PDF     | 將 HTML 網頁或內容片段轉換為 PDF，適合網頁留存、報告匯出、郵件內容封存與可列印輸出。              |
| 圖片轉 Word       | 將 JPG、JPEG、PNG、BMP 圖片檔轉換為可編輯的 Word 文件。                       |
| 圖片轉 Excel      | 將圖片檔案轉換為 Excel 活頁簿，支援表格、文字與數字內容。                             |
| 圖片轉 PPT        | 將圖片檔案轉換為可編輯的 PowerPoint 投影片，並盡量保留可見版式與內容結構。                  |
| 圖片轉 PDF        | 將 JPG、JPEG、PNG、BMP 等圖片檔案轉換為 PDF，便於多張圖片統一彙整、分享、列印與歸檔。         |
| 圖片轉 HTML       | 將圖片檔案轉換為 HTML，並盡量保留文字、版式、表格與主要視覺元素。                          |
| 圖片轉 RTF        | 將圖片檔案轉換為 RTF 文件，支援擷取文字與圖片內容。                                 |
| 圖片轉 CSV        | 從圖片檔案中擷取表格並匯出為 CSV。                                          |
| 圖片轉 TXT        | 從圖片檔案中擷取文字並儲存為純文字檔。                                          |
| 圖片轉 JSON       | 從圖片檔案中擷取文字、表格與圖片，並儲存為結構化 JSON。                               |

### 2. PDF 編輯、加密與比對

| 能力        | 說明                              |
| --------- | ------------------------------- |
| 合併 PDF 檔案 | 將多個 PDF 檔案合併為一份 PDF 文件。         |
| 拆分 PDF 檔案 | 將一份 PDF 檔案拆分成多個較小的 PDF 檔案。      |
| 旋轉 PDF 頁面 | 將選定的 PDF 頁面旋轉 90、180 或 270 度。   |
| 刪除 PDF 頁面 | 刪除 PDF 檔案中的一個或多個頁面。             |
| 插入 PDF 頁面 | 在現有 PDF 中插入來自其他 PDF 的頁面。        |
| 擷取 PDF 頁面 | 擷取選定頁面或頁碼範圍，並另存為新檔案。            |
| 轉換 PDF 標準 | 轉換 PDF 的一致性或歸檔標準。               |
| 新增浮水印     | 為 PDF 檔案新增文字或圖片浮水印，用於品牌展示或使用控制。 |
| 刪除浮水印     | 從支援的 PDF 檔案中刪除文字或圖片浮水印。         |
| 壓縮 PDF    | 壓縮 PDF 檔案大小，便於儲存、上傳與分享。         |
| 加密 PDF    | 使用 AES 加密與權限控制保護 PDF 檔案。        |
| 解密 PDF    | 在授權前提下移除 PDF 檔案密碼，便於內部處理或再利用。   |
| 比對 PDF    | 比對兩份 PDF 的內容差異。                 |

### 3. 智慧解析與資料擷取

| 能力            | 說明                                         |
| ------------- | ------------------------------------------ |
| 智慧文件剖析        | 將 PDF 與圖片剖析為結構化文件輸出，便於 Agent、自動化流程與下游系統使用。 |
| PDF 與圖片智慧資料擷取 | 從 PDF 與圖片中擷取文字、表格、內容欄位等有價值的商務資料。           |

## 技術架構

本專案是基於 Python、FastMCP 與 Starlette 建構的 **MCP Streamable HTTP** 服務。工具的參數模式由隨套件發佈的官方 OpenAPI 參數快照產生，未知參數會在伺服器端遭到拒絕。

用戶端可透過統一入口存取所有工具：

```text
http://127.0.0.1:8000/mcp
```

如只需要使用 ComPDF MCP 的部分功能，可依下列模組端點進行使用：

| 模組           | MCP Endpoint          | 業務工具數 | 主要工具                                                            |
| ------------ | --------------------- | -----:| --------------------------------------------------------------- |
| PDF 與圖片轉換    | `/mcp/conversion/mcp` | 28    | `pdf_to_word`、`pdf_to_markdown`、`image_to_json`、`word_to_pdf` 等 |
| 智慧解析與資料擷取    | `/mcp/ai/mcp`         | 2     | `document_parse`、`document_extract`                             |
| PDF 編輯、加密與比對 | `/mcp/pdf/mcp`        | 13    | `merge_pdf`、`add_watermark`、`encrypt_pdf`、`compare_pdf` 等       |
| 全部功能         | `/mcp`                | 44    | 上述全部工具                                                          |

所有業務工具皆使用統一的檔案輸入結構。`options` 必須使用 ComPDF 官方文件定義的 camelCase 參數名稱；只有 `htmlFile`、`templateFile`、`dataFile`、`imageFile` 與 `iccFile` 可以透過 `special_files` 上傳。

```json
{
  "files": [
    {
      "filename": "report.pdf",
      "content_base64": "JVBERi0xLjc...",
      "content_type": "application/pdf"
    }
  ],
  "options": {
    "pageRanges": "1-3,6",
    "enableOcr": 1
  },
  "special_files": {
    "imageFile": {
      "filename": "watermark.png",
      "content_base64": "iVBORw0..."
    }
  }
}
```

單一檔案的 Base64 解碼後大小上限為 100 MB。同步工具的結果中包含 ComPDF 回傳資料、對應的官方文件連結，以及預設 24 小時有效的下載網址說明。

## 快速開始

### 1. 安裝並執行服務

前置需求：Python 3.10+。在儲存庫根目錄建立虛擬環境並以可編輯模式安裝：

Windows：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
Copy-Item .env.example .env
compdf-streaming-mcp
```

Linux / macOS：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
compdf-streaming-mcp
```

服務預設監聽 `0.0.0.0:8000`。可透過以下端點檢查執行狀態：

- `GET /healthz`：服務狀態與已掛載的 MCP 路由。
- `GET /readyz`：服務就緒狀態，不呼叫上游 ComPDF API。
- `GET /metrics`：Prometheus 文字格式的請求計數指標。

### 2. 設定服務

將 `.env.example` 複製為 `.env` 後，再依部署環境調整設定。服務端**不會儲存也不會設定**使用者的 ComPDF API Key；每個 MCP 請求都由用戶端透過 `X-ComPDF-API-Key` 請求標頭傳入自己的 Key。您可先[註冊 ComPDF Portal](https://www.compdf.com/compdf-portal/signin?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_tw&ref_platform_id=github_compdf_mcp_tw)，並於下列位置複製免費的 API Key。

![b0a118c5-b3f5-4bc7-bae7-3d0adfc634b2](assets/api_key.png)

```dotenv
COMPDF_API_BASE_URL=https://api-server.compdf.com/server
COMPDF_API_TIMEOUT_SECONDS=180
MCP_HOST=0.0.0.0
MCP_PORT=8000
MCP_ALLOWED_HOSTS=localhost,localhost:*,127.0.0.1,127.0.0.1:*,mcp.example.com
MCP_RATE_LIMIT_PER_MINUTE=120
```

中國大陸帳戶請使用 `COMPDF_API_BASE_URL=https://api-server.compdf.cn/server`。在正式環境中，應將反向代理網域加入 `MCP_ALLOWED_HOSTS`；若連接埠不是預設值，請明確寫出連接埠，或使用 `mcp.example.com:*`。

### 3. 設定 MCP 用戶端

以下範例使用統一 MCP URL `http://127.0.0.1:8000/mcp`。遠端部署時，請替換為公開的 HTTPS 位址，例如 `https://your-domain.example/mcp`。

請先取得個人的 ComPDF API Key（[註冊即可取得免費 API Key](https://www.compdf.com/compdf-portal/signin?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_tw&ref_platform_id=github_compdf_mcp_tw)）。使用環境變數的用戶端，可先在用戶端機器中設定：

```powershell
$env:COMPDF_API_KEY = "your-own-compdf-api-key"
```

#### Codex

在 `~/.codex/config.toml` 中加入遠端 MCP 服務：

```toml
[mcp_servers.compdf]
url = "http://127.0.0.1:8000/mcp"
env_http_headers = { "X-ComPDF-API-Key" = "COMPDF_API_KEY" }
tool_timeout_sec = 180
```

#### Claude（Claude Code）

在使用者層級設定檔 `~/.claude.json` 中加入以下 MCP 服務。`COMPDF_API_KEY` 必須可供啟動 Claude Code 的終端機工作階段使用：

```json
{
  "mcpServers": {
    "compdf": {
      "type": "http",
      "url": "http://127.0.0.1:8000/mcp",
      "headers": {
        "X-ComPDF-API-Key": "${COMPDF_API_KEY}"
      }
    }
  }
}
```

若 `~/.claude.json` 已有其他設定，請將 `compdf` 合併至現有的 `mcpServers` 物件中，不要覆寫整個檔案。

#### GitHub Copilot（VS Code）

在 VS Code 中執行命令面板的 **MCP: Open User Configuration**，或在工作區建立 `.vscode/mcp.json`，然後加入以下設定。首次使用時，VS Code 會以密碼輸入欄位要求填寫 API Key：

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "compdf-api-key",
      "description": "ComPDF API Key",
      "password": true
    }
  ],
  "servers": {
    "compdf": {
      "type": "http",
      "url": "http://127.0.0.1:8000/mcp",
      "headers": {
        "X-ComPDF-API-Key": "${input:compdf-api-key}"
      }
    }
  }
}
```

#### Cursor

開啟 **Cursor Settings > Tools & MCP**，選擇 **New MCP Server**，或編輯 `~/.cursor/mcp.json`，並加入：

```json
{
  "mcpServers": {
    "compdf": {
      "url": "http://127.0.0.1:8000/mcp",
      "headers": {
        "X-ComPDF-API-Key": "your-own-compdf-api-key"
      }
    }
  }
}
```

此 Cursor 設定會將 Key 儲存在本機設定檔中。請勿提交 `~/.cursor/mcp.json` 或包含該 Key 的專案層級設定檔。

所有用戶端都應在每個 MCP 請求中送出 `X-ComPDF-API-Key`。該 Key 不應作為工具參數、URL 參數或聊天訊息傳遞。

### 4. 非同步與預簽名上傳

除了 44 個同步業務工具外，每個模組還提供 `list_operations` 與以下任務工具：

- `start_async_operation`：呼叫對應的 `/v2/processAsync/...`，適用於耗時或多檔案任務。
- `get_task_status`：查詢 `/v2/task/taskInfo` 中的任務狀態。
- `create_presigned_upload`、`upload_presigned_file`、`start_presigned_operation`：依序建立預簽名任務、上傳檔案並啟動任務。

預簽名上傳僅支援單一一般檔案的操作；PDF 合併、比對、頁面插入等請改用非同步模式。預簽名 URL 僅保存在建立任務的模組服務記憶體中，不會作為工具參數或回應欄位對外暴露。

## 部署與維運

可使用 Docker Compose 建構並執行服務：

```powershell
docker compose up --build
```

正式環境應透過 HTTPS 反向代理公開統一入口 `https://your-domain.example/mcp`，並設定 `MCP_ENV=production`、`MCP_PUBLIC_URL`、`MCP_OAUTH_ISSUER_URL` 與 `MCP_STATIC_TOKENS_JSON`。啟用後，用戶端還需傳送 `Authorization: Bearer <token>`；此服務權杖與使用者的 ComPDF API Key 相互獨立。完整的映像傳輸、HTTPS 代理、更新與回滾步驟，請參閱 [DEPLOYMENT.md](DEPLOYMENT.md)。

## License 與免費使用

ComPDF MCP 可免費使用，無須事先採購或聯繫業務。

- [註冊](https://www.compdf.com/compdf-portal/signin?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_tw&ref_platform_id=github_compdf_mcp_tw) 取得免費 API Key 並完成設定
  ![b0a118c5-b3f5-4bc7-bae7-3d0adfc634b2](assets/api_key.png)
- 適合個人體驗、功能驗證與工作流程測試
- 如需更高 API 呼叫額度、企業部署或商務合作，可[聯繫業務團隊](https://www.compdf.com/contact-sales?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_tw&ref_platform_id=github_compdf_mcp_tw)

這有助於使用者以更低門檻完成接入與試用，也更適合先驗證 AI 文件工作流程的實際成效，再決定是否進入更深層的商業使用。

## 適用情境與範例提問

上傳 PDF、圖片或其他來源檔案後，輸入任務指令，例如擷取表格、轉換格式、合併 PDF、加入浮水印。Agent 會呼叫對應的 ComPDF MCP 工具並回傳結果。如需進一步分析，再將處理結果交給 AI。

範例情境：

* 使用者在 Claude、Cursor、Cline 等 MCP 用戶端中上傳報告、手冊或提案 PDF，先轉成 Markdown／Word，再讓 AI 進行摘要、知識問答或內容重組
* 使用者在 MCP 工作流程中處理發票、報表、掃描表格與圖片附件時，先擷取表格與結構化資料，再進入財務審核、資料輸入或自動化流轉
* 使用者在 Agent 中整理合約、標案文件、報價單與歸檔檔案時，先完成 PDF 合併、拆分、加浮水印與格式轉換，再交給 AI 進行整理、命名或對外發送準備
* 使用者在多步驟自動化流程中，先將 PDF 或圖片轉換成 CSV、JSON、TXT 等輕量結果，再交由後續 Agent 進行欄位整理、審批流程處理、知識庫寫入或腳本編排

**範例提問：**

* 把這份 PDF 轉成 Word，並盡量保留排版。
* 擷取這份 PDF 中的所有表格並匯出為 CSV。
* 把這張圖片轉成 JSON，輸出結構化內容。
* 合併這些 PDF、加入浮水印，然後回傳最終檔案。
* 先把這份報告轉成 Markdown，再幫我整理重點。

---

<p align="center">
  <b>由 ComPDF 團隊打造。</b><br>
  <a href="https://www.compdf.com?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_tw&ref_platform_id=github_compdf_mcp_tw">官網</a> ·
  <a href="https://www.compdf.com/contact-sales?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_tw&ref_platform_id=github_compdf_mcp_tw">聯繫業務</a> ·
  <a href="https://www.compdf.com/support?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_tw&ref_platform_id=github_compdf_mcp_tw">技術支援</a>
</p>
