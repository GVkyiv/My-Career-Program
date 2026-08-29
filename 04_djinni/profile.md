# Djinni — профиль (английский)

Ревизия 23.08.2026. Предыдущая версия — 19.08.2026, до неё — 31.07.2026
(`https://djinni.co/q/1a1b009b63/`) — сломана: markdown-экранирование
(`\~30`) протекло в текст, всё саммари одним абзацем, поля Highlights,
Looking for и Domain experience не заполнены.

Правка 23.08.2026 (1): пользователь указал, что широта ERP-доменов
(финансы, продажи, закупки, основные средства, заработная плата и
т.д.) не отражена — поле Domain experience на Джинні этого не вмещает
(закрытый список, см. раздел ниже), значит компенсировать нужно
текстом. Добавлен явный перечень внедрённых ERP-модулей в Досвід
роботи и Highlights. Новые факты (основные средства, заработная
плата) подтверждены пользователем за периодом Intellect-Service /
ІС-Про (2004-2010) и внесены в `00_profile/candidate.md`.

Правка 23.08.2026 (2), по замечанию пользователя на реальную
опубликованную страницу (`https://djinni.co/q/1a1b009b63/`): из
Досвід роботи убраны Certifications и MSc-строка — они дублировали
отдельные поля (Сертифікації; освіта — стандартное поле Джинні, в
этом файле не описано, но существует на платформе). Убран
уточняющий довесок «(GAAP and management accounting)» после payroll
accounting — оставлено только payroll accounting.

**Важно при вставке:** поля Джинні — plain text. Не вставлять markdown
(`**`, `-`, `~`). Тильду писать как обычный символ или заменять словом
`about`. Переносы строк Джинні сохраняет — использовать их.

Дисциплина verified-facts-only: все цифры ниже взяты из
`00_profile/candidate.md`. Непроверенное помечено
`[НУЖНЫ ДАННЫЕ: ...]` и в профиль не вставляется до подтверждения.

---

## Поле: Заголовок

```
Head of PMO / Delivery Director / Deputy IT Director / Delivery Manager / Portfolio Manager
```

Расширен с трёх ролей до пяти. Причина: оба конкурента с максимальными
просмотрами держат 5-7 ролей в заголовке — это попадание в большее
число поисковых выдач рекрутеров, а не размывание позиционирования.

---

## Поле: Досвід роботи (Work experience)

```
Delivery and PMO leader with 24+ years in IT and enterprise ERP systems — 16 of them at ERC Distribution, an international distributor with 1,000+ employees and offices in 10 countries.

WHAT I OWN
The company's full IT project portfolio: up to 10 projects running concurrently, 100-150 delivered per year. I decide portfolio composition, prioritize with business stakeholders, build project teams, and stay accountable for delivery end to end.

Team: 3 direct-report project managers, plus cross-functional teams of up to 30 specialists — developers, business analysts, QA. I hire, assess and mentor the project managers I work with.

KEY DOMAINS
ERP • Distribution and retail • B2B integration (EDI) • BI and analytics

Across two ERP implementations, as vendor and as customer, I covered the full transactional core: finance and banking, sales, procurement, cash management, order management, B2B, production, warehouse, fixed assets, and payroll accounting.

HOW I DELIVER
Predictive, agile and hybrid approaches; Scrum and Kanban; in-house teams and vendor engagement models.

I have worked both sides of the ERP table — as a vendor (Intellect-Service; Softline, Oracle E-Business Suite) and as the customer (ERC). That shapes how I scope and de-risk delivery from day one: I know where the estimates bend and where the integrations break.

AI IN DELIVERY
Hands-on, not in conversation. I initiated and shipped an internal AI meeting-summarization tool (Webex + LLM) that the company adopted in full. I use AI coding agents (Claude Code, Codex) in daily work.
```

Живой текст 23.08.2026 взят как основа (структура с капс-подзаголовками
WHAT I OWN / KEY DOMAINS / HOW I DELIVER / AI IN DELIVERY —
предпочтение пользователя, не переделывать без причины). В KEY DOMAINS
добавлена строка с перечнем ERP-модулей (правка от того же дня, см.
чейнджлог выше). Из живого текста убрана хвостовая строка про MSc —
переносится в отдельное поле образования на платформе, не дублируется
здесь. Tools-строки в живом тексте нет — не восстанавливать, инструменты
частично закрыты через `Jira & Confluence` в Досвід навичок.

---

## Поле: Highlights

```
Led migration of the core ERP (about 1,000 users; finance, banking, sales, procurement) from a legacy DOS platform to a proprietary web+SQL system, with a team of up to 20.

Implemented ERP modules across ten functional domains over my career, as both vendor and customer: finance and banking, sales, procurement, cash management, order management, B2B, production, warehouse, fixed assets, and payroll accounting.

Implemented EDI with partners and customers — cut document processing time by 70%.

Redesigned order management — reduced data errors by 30% and order processing time by 50%.

Built company-wide Power BI reporting — cut data analysis time by 50% and supported a 25% increase in the customer assortment portfolio.

Initiated and shipped an internal AI meeting-summarization tool (Webex + LLM), adopted company-wide — saves 30-60 minutes of protocol writing per meeting, across 4-5 meetings a day.

Contributed to a 5x revenue growth of the company over about 10 years through automation of core business processes.

Built the IT portfolio process end to end: intake, prioritization with business owners, team composition, delivery accountability.

Hired, assessed and mentored project managers — recruitment, performance assessment, and one-on-one coaching.
```

Каждая строка — отдельный буллет с цифрой. Это ровно тот формат, в
котором работают оба конкурента с максимальными просмотрами.

Формулировка про 5x выручки намеренно осторожная («contributed …
through automation»), а не «drove» — принцип осторожной атрибуции
причинности из `00_profile/candidate.md`.

Цифры по AI-инструменту (30-60 минут на встречу, 4-5 встреч в день) и
работа с PM (найм, оценка, менторинг) подтверждены пользователем
19.08.2026, перенесены в `00_profile/candidate.md`.

---

## Поле: Looking for

```
Head of PMO, Delivery Director, or Deputy IT Director (Projects and Programs) — at international companies operating in Ukraine, or at large Ukrainian corporations.

I am looking for a role where delivery is built as a system rather than followed as a process: a transparent portfolio, prioritization the business actually trusts, and teams that grow. I am ready either to build a PMO from the ground up or to scale an existing one.
```

---

## Поле: Досвід у доменах (Domain experience) — СЕЙЧАС ПУСТОЕ

Главный структурный пробел против конкурентов: рекрутеры фильтруют по
домену, а профиль в этих фильтрах отсутствует.

**Фактически проставлено на 19.08.2026** (список доменов на Джинні
закрытый, часть подтверждённых доменов там просто отсутствует):

- Logistics / Supply Chain — більше 10 років
- Manufacturing — більше 10 років

Хотели поставить, но пунктов нет в списке платформы:
Distribution / Retail (16 лет — основной домен кандидата), ERP (24
года). Компенсируются текстом в «Досвід роботи».

Не закрыто: `E-commerce / Marketplace` (кандидат подтвердил 16 лет).
Пункт в списке Джинні **есть** — стоит в профиле конкурента с той же
специализацией Delivery Manager. Проверить выпадашку ещё раз.

**Finance / Fintech — НЕ ставить.** Пользователь явно подтвердил
19.08.2026, что финансами не занимался. См. принцип в
`00_profile/candidate.md`.

Убраны 19.08.2026 после проверки: `SaaS` (оснований в профиле нет),
`GovTech` (основание было — Softline / Oracle EBS для Держмитслужби, —
но срок не подтверждён).

Риски, о которых пользователь предупреждён:
- Logistics 10+ років при том, что Manhattan SCALE WMS фреймится только
  как общий надзор — быть готовым к вопросу о глубине вовлечённости.
- `[НУЖНЫ ДАННЫЕ: Manufacturing — больше 10 лет? Основание есть
  (Intellect-Service делал ERP для производственных компаний, Київська
  меблева фабрика), но это период до ERC. Единственная цифра в профиле,
  не сводимая с candidate.md.]`

Охват: 2 домена против 5 у обоих конкурентов с максимальными
просмотрами. Каждый домен — отдельный фильтр рекрутера.

Компенсация 23.08.2026: закрытый список доменов Джинні не вмещает
ERP-модули (финансы, продажи, закупки, основные средства, заработная
плата и т.д.) как отдельные пункты — их некуда проставить. Вместо
этого явный перечень из десяти функциональных доменов ERP добавлен
текстом в Досвід роботи и Highlights (см. выше), где рекрутер это
прочитает даже без фильтра.

---

## Поле: Досвід навичок (Skills experience)

Сейчас годы проставлены почти нигде, кроме Product ownership. У
конкурентов — у каждого навыка. Черновик:

- Project Management — більше 10 років
- Team Management — більше 10 років
- Delivery Management — `[НУЖНЫ ДАННЫЕ]`
- Portfolio Management — `[НУЖНЫ ДАННЫЕ: в версии 31.07 стояло 4 года]`
- PMO — `[НУЖНЫ ДАННЫЕ: в версии 31.07 стояло 5 лет]`
- Product ownership — більше 10 років (уже стоит)
- Jira & Confluence — більше 10 років
- Agile / Scrum, Waterfall, Kanban — `[НУЖНЫ ДАННЫЕ]`
- AI Integration — `[НУЖНЫ ДАННЫЕ: в версии 31.07 стояло 2 года]`

Блок «Досвід з AI-агентами: Claude Code, Codex» — оставить. Ни у
одного из двух конкурентов этого нет, это реальный дифференциатор.

---

## Поле: Додаткові навички (Additional skills)

Убрать: `PSM1`, `PSPO`, `Google Project Management Certificate` —
дублируют секцию Certifications и занимают слоты.
Исправить опечатку: `Busines Analysis` → `Business Analysis`.

Добавить (все — из подтверждённого профиля, кроме помеченных):
`stakeholder management`, `risk management`, `SDLC`, `process
development`, `capacity management`, `vendor management`, `roadmapping`,
`ITIL`, `data-driven decision making`, `C-level communication`,
`hiring`, `mentoring`, `coaching`.

**Не добавлять `budgeting` / `financial management`** — прямого
владения бюджетом нет, это структурный гэп. Оба конкурента его
заявляют; закрывать его нужно масштабом портфеля (что и сделано в
«Scale of ownership»), а не ложным claim.

---

## Поле: Сертифікації

Добавить отсутствующий **ITIL v4 Foundation** (есть в
`00_profile/candidate.md`, в профиле не указан).

---

## Ставка

Сейчас $4500, диапазон $4000-6000. Оба топовых по просмотрам
конкурента просят $6000.

Рекомендация: поднять отображаемую цифру до $5000-5500. Обоснование —
не «у них больше», а то, что $4500 при 24 годах опыта и портфеле
100-150 проектов/год якорит ниже людей с сопоставимым или меньшим
объёмом ответственности, и рекрутер читает цифру как прокси
seniority. Решение за пользователем, не менять без подтверждения.

Важная оговорка: причинно-следственной связи «выше ставка → больше
просмотров» здесь нет. Более вероятно, что и высокая ставка, и высокие
просмотры у конкурентов — следствие более полного и структурированного
профиля. Поднимать ставку имеет смысл после того, как заполнены
Highlights, Looking for и Domain experience, а не вместо этого.
