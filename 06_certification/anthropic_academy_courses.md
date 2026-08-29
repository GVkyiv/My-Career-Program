# Anthropic Academy — бесплатные курсы с сертификатом

Проверено 25.08.2026. Это **отдельный, более лёгкий слой** от
проктored-экзаменов ($99-175, партнёрский шлюз, разбор — в
`claude_certified_architect.md` и `partner_access_paths.md`).

## Чем это отличается от CCA/Associate/Developer

Anthropic Academy (`anthropic.skilljar.com`) —self-paced курсы, не
экзамены. Регистрация — только email, **партнёрский статус не
требуется**, доступно уже сейчас. По завершении — PDF-сертификат с
верификационной ссылкой, годится для LinkedIn/Upwork. Это не то же
самое по весу, что проктored-сертификат — ближе к «подтверждённому
прохождению курса», чем к экзамену. Но бесплатно, без блокеров, и
можно начинать сегодня.

**Подтверждено 25.08.2026 напрямую по курсам из приоритетного
списка** (Introduction to Model Context Protocol, Introduction to
subagents, Claude Code in Action, Introduction to Agent Skills):
партнёрский доступ не нужен ни одному из них — механизм тот же, что
уже сработал для AI Fluency: Framework & Foundations. Skilljar
генерирует сертификат по завершении (имя, курс, дата, credential URL).

**Предупреждение из первоисточника** (реальный автор, прошедший все
курсы): в интернете продаются платные курсы с названиями вроде «Claude
certification» (Udemy и похожие площадки) — Anthropic их не
одобряет и не имеет к ним отношения. Настоящий, официальный сертификат
даёт только `anthropic.skilljar.com`. Платные Udemy-курсы, упомянутые в
`learning_plan.md` как подготовка к экзамену CCA-F — по-прежнему
годный учебный материал, но не путать с официальным сертификатом.

## Уточнение по вашему «Клод 101»

В `00_profile/candidate.md` зафиксирован **AI Fluency: Framework &
Foundations (Anthropic, 03.2026)** — это отдельный курс от **Claude
101**, который тоже существует в каталоге (основы работы с Claude:
Chat, Cowork, Code, Projects, Artifacts, Skills, Connectors). Возможно,
вы имеете в виду один из них, возможно — прошли оба. `[НУЖНЫ ДАННЫЕ]`
уточните, что именно у вас на руках, прежде чем добавлять что-то новое
в `candidate.md` — по дисциплине verified-facts-only ничего не
добавляется без вашего подтверждения.

## Полный каталог (22 курса на 25.08.2026)

### Прямо готовят к экзамену CCA-F — приоритет

Экзамен CCA-F (см. `claude_certified_architect.md`) взвешен по пяти
доменам. Эти курсы покрывают ровно их содержание — время на них не
альтернатива подготовке к экзамену, а сама подготовка:

| Курс | Домен CCA-F, который закрывает |
|---|---|
| **Introduction to Model Context Protocol** | Tool Design & MCP Integration (18%) |
| **MCP: Advanced Topics** | Tool Design & MCP Integration (18%) — продвинутый уровень, после Introduction |
| **Introduction to subagents** | Agentic Architecture & Orchestration (27%, самый тяжёлый домен) |
| **Claude Code in Action** | Claude Code Configuration & Workflows (20%) |
| **Introduction to Agent Skills** | Claude Code Configuration & Workflows (20%) / Tool Design |
| **Building with the Claude API** | Prompt Engineering & Structured Output (20%) — фундамент |

### Общая база (если ещё не пройдено)

- **Claude 101** — основы использования Claude, без кода
- **Claude Code 101** — введение в Claude Code
- **Claude Platform 101** — основы работы с API-платформой
- **Introduction to Claude Cowork** — совместная работа с файлами/проектами

### Позиционирование под нишу Upwork

Из `01_markets/upwork.md` — ниша «AI-augmented delivery consultant»:

- **AI Fluency for Builders** — полный путь «проблема → решение», близко к тому, что кандидат продаёт на Upwork
- **AI Fluency for Small Businesses** — прямое попадание в типичного Upwork-клиента (SMB)

### Облачные деплойменты (низкий приоритет, только под конкретного клиента)

- Claude with Amazon Bedrock
- Claude on Google Cloud / Claude with Google Vertex AI

Кандидат не заявляет AWS/GCP как домен — брать только если появится
клиент именно на этой инфраструктуре.

### Не релевантно профилю (аудитория не совпадает)

AI Fluency for Students / Educators / pK-12 / Nonprofits / Creative
Work, Teaching AI Fluency — под другие аудитории (образование,
некоммерческий сектор, творческие профессии). Пропустить.

## Рекомендация

Это ровно тот «не простаивать», о котором шла речь в
`partner_access_paths.md` (план Б, пока решается доступ к CCA-F через
Partner Network) — но лучше, чем Google Gen AI Leader как заполнитель
паузы: **знания здесь не тратятся впустую**, они прямой конспект
экзамена CCA-F. Разумный порядок:

1. Introduction to Model Context Protocol
2. Introduction to subagents
3. Claude Code in Action
4. Introduction to Agent Skills
5. Building with the Claude API (если основы ещё не закрыты)
6. MCP: Advanced Topics — после 1

Каждый курс бесплатный и самостоятельный по темпу — можно проходить
параллельно с ожиданием ответа от ERC/партнёра, без потери времени.

## Источники (проверено 25.08.2026)

- [Anthropic Academy, anthropic.skilljar.com](https://anthropic.skilljar.com/) — официальный, полный каталог курсов
- [Claude 101, Anthropic Academy](https://anthropic.skilljar.com/claude-101) — официальный
- [Anthropic Academy Guide: All 13 Free Claude Courses, Termdock](https://www.termdock.com/en/blog/anthropic-academy-claude-courses-guide) — вторичный, для кросс-проверки формата сертификатов
