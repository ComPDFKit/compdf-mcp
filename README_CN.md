![compdf-github-banner 1](assets/ComPDF-Comprehensive%20PDF%20Solutions.png)
[English](README.md) | [繁體中文](README_繁中.md) | [日本語](README_JA.md) | [简体中文](README_CN.md)

# ComPDF MCP

ComPDF MCP 面向 MCP 客户端与 AI Agent 平台，提供 PDF /图片解析与数据提取、PDF 格式转换、PDF 编辑、图片格式转换等能力。它帮助用户先处理原始文档，再把更轻量、更干净、更结构化的结果交给 AI，从而降低 AI Token 消耗，减少 AI 费用支出，并提升整体处理效率。

> * 如果你觉得 ComPDF MCP 有帮助，欢迎在 GitHub 给我们一个 ⭐ **Star**，这会帮助我们持续迭代和完善产品。
> * 如果你有问题或想法，欢迎参与我们的 [Discussions](https://github.com/ComPDFKit/compdf-mcp/discussions) 讨论。

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/docker-supported-blue" alt="Docker"></a>
  <a href="#"><img src="https://img.shields.io/github/stars/ComPDFKit/compdf-mcp" alt="GitHub Stars"></a>
  <a href="#"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs Welcome"></a>
</p>

<p align="center">
  <a href="#为什么选择-compdf-mcp"><b>为什么选择 ComPDF MCP</b></a> •
  <a href="#功能支持"><b>功能支持</b></a> •
  <a href="#技术架构"><b>技术架构</b></a> •
  <a href="#快速开始"><b>快速开始</b></a> •
  <a href="#部署与运维"><b>部署与运维</b></a> •
  <a href="#license-与免费使用"><b>License 与免费使用</b></a> •
  <a href="#适用场景与示例提问"><b>适用场景与示例提问</b></a> •
  <a href="#支持"><b>支持</b></a>
</p>

## 为什么选择 ComPDF MCP

用户使用 ComPDF MCP 的核心原因，不只是“让 AI 能处理 PDF”，而是先把复杂、冗长、噪声较多的原始文档处理成更适合模型理解的输入，再交给 AI 完成分析、总结、问答或自动化任务。

原始 PDF、扫描件和图片文件通常体积更大、上下文更杂、结构也更不稳定。先通过 ComPDF MCP 完成转换、提取和页面处理，再将结果交给 AI，可以：

- 降低 AI Token 消耗
- 减少 AI 费用支出
- 缩短响应时间
- 提高结构化结果质量
- 减少复杂文件直接进入模型带来的成本浪费
- 通过一个 MCP 服务完成 PDF 和图片文件处理
- 适合文档密集型工作流和多平台 Agent 场景

尤其在需要批量处理报告、合同、发票、表格、扫描件等文档的场景中，这种“先处理文档、再调用 AI”的方式，通常比直接把原文件交给模型更省成本，也更适合进入后续工作流。

## 功能支持

ComPDF MCP 聚焦三大能力方向：文档转换、PDF 操作，以及智能解析与数据提取。

### 1. PDF 与图片转换

| 能力             | 说明                                                        |
| -------------- | --------------------------------------------------------- |
| PDF 转 Word     | 将 PDF 文件转换为可编辑的 Word 文档，并尽可能保留原始版式、文本、图片和格式。              |
| PDF 转 Excel    | 将 PDF 文件转换为 Excel，支持表格、数字和结构化业务数据。                        |
| PDF 转 PPT      | 将 PDF 页面转换为可编辑的 PowerPoint 幻灯片，并尽量保留原始版式和视觉结构。            |
| PDF 转 HTML     | 将 PDF 文件转换为 HTML，用于网页展示与内容复用，同时保留文本、图片、表格和版式。             |
| PDF 转 RTF      | 将 PDF 文件转换为 RTF 文档，支持文本和图片内容。                             |
| PDF 转图片        | 将 PDF 页面转换为 PNG 或 JPG 图片，并支持分辨率与 DPI 配置。                  |
| PDF 转 CSV      | 从 PDF 文件中提取表格并导出为 CSV，可按单表导出，也可合并导出。                      |
| PDF 转 TXT      | 从 PDF 或扫描版 PDF 中提取文本，并保存为纯文本文件。                           |
| PDF 转 JSON     | 从 PDF 文件中提取文本、表格和图片，并保存为结构化 JSON。                         |
| PDF 转 Markdown | 将 PDF 文件转换为 Markdown，便于在知识库、开发文档、博客系统和 AI 工作流中继续编辑、检索与复用。 |
| PDF 转可搜索 PDF   | 对扫描版 PDF 执行 OCR 识别，生成可搜索、可复制、可高亮文本的 PDF 文档，便于检索、归档与后续处理。  |
| PDF 转 OFD      | 将 PDF 文件转换为 OFD，便于在 OFD 归档、流转与本地化办公场景中使用。                 |
| Word 转 PDF     | 将 Word 文档转换为 PDF，尽量保留原始排版、字体、图片和页面结构，适合正式分享、归档和打印。        |
| PNG 转 PDF      | 将 PNG 图片转换为 PDF，便于将截图、设计图或证据图片统一整理、传输和归档。                 |
| RTF 转 PDF      | 将 RTF 文档转换为 PDF，在保留基础文本样式和版面的同时，便于跨设备查看与正式输出。             |
| Excel 转 PDF    | 将 Excel 工作簿或表格转换为 PDF，便于报表共享、打印、归档和防止公式被误改。               |
| TXT 转 PDF      | 将 TXT 纯文本文件转换为 PDF，适合将日志、笔记、说明文档等内容整理为固定版式文件。             |
| CSV 转 PDF      | 将 CSV 表格数据转换为 PDF，便于数据快照分享、审阅、打印和业务归档。                    |
| PPT 转 PDF      | 将 PowerPoint 演示文稿转换为 PDF，便于演示材料分发、跨设备查看和正式留档。             |
| HTML 转 PDF     | 将 HTML 网页或内容片段转换为 PDF，适合网页留存、报告导出、邮件内容存档和可打印输出。           |
| 图片转 Word       | 将 JPG、JPEG、PNG、BMP 图片文件转换为可编辑的 Word 文档。                   |
| 图片转 Excel      | 将图片文件转换为 Excel 工作簿，支持表格、文本和数字内容。                          |
| 图片转 PPT        | 将图片文件转换为可编辑的 PowerPoint 幻灯片，并尽量保留可见版式和内容结构。               |
| 图片转 PDF        | 将 JPG、JPEG、PNG、BMP 等图片文件转换为 PDF，便于多张图片统一汇总、分享、打印和归档。      |
| 图片转 HTML       | 将图片文件转换为 HTML，并尽量保留文本、版式、表格和主要视觉元素。                       |
| 图片转 RTF        | 将图片文件转换为 RTF 文档，支持提取文本和图片内容。                              |
| 图片转 CSV        | 从图片文件中提取表格并导出为 CSV。                                       |
| 图片转 TXT        | 从图片文件中提取文本并保存为纯文本文件。                                      |
| 图片转 JSON       | 从图片文件中提取文本、表格和图片，并保存为结构化 JSON。                            |

### 2. PDF 编辑、加密与对比

| 能力        | 说明                             |
| --------- | ------------------------------ |
| 合并 PDF 文件 | 将多个 PDF 文件合并为一个 PDF 文档。        |
| 拆分 PDF 文件 | 将一个 PDF 文件拆分成多个更小的 PDF 文件。     |
| 旋转 PDF 页面 | 将选定的 PDF 页面旋转 90、180 或 270 度。  |
| 删除 PDF 页面 | 删除 PDF 文件中的一个或多个页面。            |
| 插入 PDF 页面 | 在现有 PDF 中插入来自其他 PDF 的页面。       |
| 提取 PDF 页面 | 提取选定页面或页码范围，并另存为新文件。           |
| 转换 PDF 标准 | 转换 PDF 的一致性或归档标准。              |
| 添加水印      | 为 PDF 文件添加文字或图片水印，用于品牌展示或使用控制。 |
| 删除水印      | 从支持的 PDF 文件中删除文字或图片水印。         |
| 压缩 PDF    | 压缩 PDF 文件体积，便于存储、上传和分享。        |
| 加密 PDF    | 使用 AES 加密和权限控制保护 PDF 文件。       |
| 解密 PDF    | 在授权前提下移除 PDF 文件密码，便于内部处理或复用。   |
| 对比 PDF    | 对比两份 PDF 的内容差异。                |

### 3. 智能解析与数据提取

| 能力            | 说明                                         |
| ------------- | ------------------------------------------ |
| 智能文档解析        | 将 PDF 和图片解析为结构化文档输出，便于 Agent、自动化流程和下游系统使用。 |
| PDF 与图片智能数据提取 | 从 PDF 和图片中提取文本、表格、内容字段等有价值的业务数据。           |

## 技术架构

本项目是基于 Python、FastMCP 和 Starlette 构建的 **MCP Streamable HTTP** 服务。工具的参数模式由随包发布的官方 OpenAPI 参数快照生成，未知参数会在服务端被拒绝。

客户端通过统一入口接入即可使用所有工具：

```text
http://127.0.0.1:8000/mcp
```

如只需要使用 ComPDF MCP 的部分功能，可根据以下模块端点进行使用：

| 模块           | MCP Endpoint          | 业务工具数 | 主要工具                                                            |
| ------------ | --------------------- | -----:| --------------------------------------------------------------- |
| PDF 与图片转换    | `/mcp/conversion/mcp` | 28    | `pdf_to_word`、`pdf_to_markdown`、`image_to_json`、`word_to_pdf` 等 |
| 智能解析与数据提取    | `/mcp/ai/mcp`         | 2     | `document_parse`、`document_extract`                             |
| PDF 编辑、加密与对比 | `/mcp/pdf/mcp`        | 13    | `merge_pdf`、`add_watermark`、`encrypt_pdf`、`compare_pdf` 等       |
| 全部功能         | `/mcp`                | 44    | 上述全部工具                                                          |

所有业务工具使用统一的文件输入结构。`options` 必须使用 ComPDF 官方文档定义的 camelCase 参数名；只有 `htmlFile`、`templateFile`、`dataFile`、`imageFile` 和 `iccFile` 可以通过 `special_files` 上传。

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

单个文件的 Base64 解码后大小上限为 100 MB。同步工具的结果中包含 ComPDF 返回数据、对应官方文档链接，以及默认 24 小时有效的下载地址说明。

## 快速开始

### 1. 安装并运行服务

前置要求：Python 3.10+。在仓库根目录创建虚拟环境并以可编辑模式安装：

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

服务默认监听 `0.0.0.0:8000`。可通过以下端点检查运行状态：

- `GET /healthz`：服务状态和已挂载的 MCP 路由。
- `GET /readyz`：服务就绪状态，不调用上游 ComPDF API。
- `GET /metrics`：Prometheus 文本格式的请求计数指标。

### 2. 配置服务

将 `.env.example` 复制为 `.env` 后，根据部署环境调整配置。服务端**不保存也不配置**用户的 ComPDF API Key；每个 MCP 请求由客户端在 `X-ComPDF-API-Key` 请求头中传入自己的 Key。您可以[注册 ComPDF Portal](https://www.compdf.com/compdf-portal/signin?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_cn&ref_platform_id=github_compdf_mcp_cn)，并在以下位置复制免费的 API Key。

![b0a118c5-b3f5-4bc7-bae7-3d0adfc634b2](assets/api_key.png)

```dotenv
COMPDF_API_BASE_URL=https://api-server.compdf.com/server
COMPDF_API_TIMEOUT_SECONDS=180
MCP_HOST=0.0.0.0
MCP_PORT=8000
MCP_ALLOWED_HOSTS=localhost,localhost:*,127.0.0.1,127.0.0.1:*,mcp.example.com
MCP_RATE_LIMIT_PER_MINUTE=120
```

中国大陆账户使用 `COMPDF_API_BASE_URL=https://api-server.compdf.cn/server`。生产环境应将反向代理域名加入 `MCP_ALLOWED_HOSTS`；若端口不是默认端口，请写明端口或使用 `mcp.example.com:*`。

### 3. 配置 MCP 客户端

以下示例使用统一 MCP URL `http://127.0.0.1:8000/mcp`。远程部署时，请替换为公开的 HTTPS 地址，例如 `https://your-domain.example/mcp`。

先获取个人 ComPDF API Key（[注册立即获得您的免费 API Key](https://www.compdf.com/compdf-portal/signin?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_cn&ref_platform_id=github_compdf_mcp_cn)）。使用环境变量的客户端，可先在客户端机器中设置：

```powershell
$env:COMPDF_API_KEY = "your-own-compdf-api-key"
```

#### Codex

在 `~/.codex/config.toml` 中添加远程 MCP 服务：

```toml
[mcp_servers.compdf]
url = "http://127.0.0.1:8000/mcp"
env_http_headers = { "X-ComPDF-API-Key" = "COMPDF_API_KEY" }
tool_timeout_sec = 180
```

#### Claude（Claude Code）

在用户级配置文件 `~/.claude.json` 中添加以下 MCP 服务。`COMPDF_API_KEY` 需要在启动 Claude Code 的终端会话中可用：

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

若 `~/.claude.json` 已有其他配置，请将 `compdf` 合并到现有的 `mcpServers` 对象中，而不要覆盖原文件。

#### GitHub Copilot（VS Code）

在 VS Code 中运行命令面板的 **MCP: Open User Configuration**，或在工作区创建 `.vscode/mcp.json`，然后添加以下配置。首次使用时，VS Code 会以密码输入框要求填写 API Key：

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

打开 **Cursor Settings > Tools & MCP**，选择 **New MCP Server**，或编辑 `~/.cursor/mcp.json`，添加：

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

Cursor 的此配置会将 Key 保存在本地配置文件中。请勿提交 `~/.cursor/mcp.json` 或包含该 Key 的项目级配置文件。

所有客户端均应在每个 MCP 请求中发送 `X-ComPDF-API-Key`。该 Key 不应作为工具参数、URL 参数或聊天文本传递。

### 4. 异步与预签名上传

除 44 个同步业务工具外，每个模块还提供 `list_operations` 与以下任务工具：

- `start_async_operation`：调用对应的 `/v2/processAsync/...`，适用于耗时或多文件任务。
- `get_task_status`：查询 `/v2/task/taskInfo` 中的任务状态。
- `create_presigned_upload`、`upload_presigned_file`、`start_presigned_operation`：依次创建预签名任务、上传文件并启动任务。

预签名上传仅支持单个普通文件的操作；PDF 合并、对比、页面插入等请使用异步模式。预签名 URL 仅保存在创建任务的模块服务内存中，不会作为工具参数或响应字段暴露。

## 部署与运维

可使用 Docker Compose 构建并运行服务：

```powershell
docker compose up --build
```

生产环境应通过 HTTPS 反向代理公开统一入口 `https://your-domain.example/mcp`，并设置 `MCP_ENV=production`、`MCP_PUBLIC_URL`、`MCP_OAUTH_ISSUER_URL` 和 `MCP_STATIC_TOKENS_JSON`。启用后，客户端还需要发送 `Authorization: Bearer <token>`；该服务令牌与用户的 ComPDF API Key 相互独立。完整的镜像传输、HTTPS 代理、更新和回滚步骤见 [DEPLOYMENT.md](DEPLOYMENT.md)。

## License 与免费使用

ComPDF MCP 可免费使用，无需先采购或联系销售。

* [注册](https://www.compdf.com/compdf-portal/signin?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_cn&ref_platform_id=github_compdf_mcp_cn)获取免费 API Key 并配置
  ![b0a118c5-b3f5-4bc7-bae7-3d0adfc634b2](assets/api_key.png)
- 适合个人体验、功能验证与工作流测试

- 如有更高 API 调用资产、企业部署或商务合作需求，可[联系商务团队](https://www.compdf.com/contact-sales?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_cn&ref_platform_id=github_compdf_mcp_cn)

这能帮助用户更低门槛地完成接入和试用，也更适合先验证 AI 文档工作流的实际效果，再决定是否进入更深层的业务使用。

## 适用场景与示例提问

上传 PDF、图片或其他源文件。输入任务指令，例如提取表格、转换格式、合并 PDF、添加水印。Agent 调用ComPDF MCP 对应工具并返回结果。如需进一步分析，再将处理结果交给 AI。

示例场景：

* 用户在 Claude、Cursor、Cline 等 MCP 客户端中上传报告、手册或方案 PDF，先转成 Markdown / Word，再让 AI 做总结、知识问答或内容重组
* 用户在 MCP 工作流中处理发票、报表、扫描表格和图片附件时，先提取表格与结构化数据，再进入财务审核、数据录入或自动化流转
* 用户在 Agent 中整理合同、标书、报价单、归档文件时，先完成 PDF 合并、拆分、加水印、格式转换，再交给 AI 做整理、命名或对外发送准备
* 用户在多步骤自动化流程中，先把 PDF 或图片转换成 CSV、JSON、TXT 等轻量结果，再交给后续 Agent 做字段归纳、审批流处理、知识库写入或脚本编排

**示例提问：**

* 把这份 PDF 转成 Word，并尽量保留排版。
* 提取这份 PDF 中的所有表格并导出为 CSV。
* 把这张图片转成 JSON，输出结构化内容。
* 合并这些 PDF，添加水印，然后返回最终文件。
* 先把这份报告转成 Markdown，再帮我总结重点。

---

<p align="center">
  <b>由 ComPDF 团队打造。</b><br>
  <a href="https://www.compdf.com?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_cn&ref_platform_id=github_compdf_mcp_cn">官网</a> ·
  <a href="https://www.compdf.com/contact-sales?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_cn&ref_platform_id=github_compdf_mcp_cn">联系销售</a> ·
  <a href="https://www.compdf.com/support?utm_source=github&utm_medium=referral&utm_campaign=compdf_mcp_repo_cn&ref_platform_id=github_compdf_mcp_cn">技术支持</a>
</p>
