# Учебная программа — черновик

Зависит от решений в `roadmap.md`, которые ещё не приняты пользователем
— это не финальный план, а структура, которую можно наполнить датами
после обсуждения. Заполняется по факту (тот же принцип, что в
`gaps.md`), не наперёд.

## Claude Certified Architect — Foundations (если выбран первым)

Порядок шагов, из `claude_certified_architect.md`:

1. **Предусловие: партнёрский доступ.** Закрыть открытый вопрос —
   юрлицо/домен, заявка в Claude Partner Network, уровень Registered.
   Без этого шага 2-4 не имеют смысла планировать по датам.
2. **Подготовка (можно начинать параллельно с шагом 1, экзамен не
   привязан к моменту получения партнёрского статуса).** Домены
   экзамена и их вес — в `claude_certified_architect.md`:
   - Agentic Architecture & Orchestration (27%)
   - Claude Code Configuration & Workflows (20%)
   - Prompt Engineering & Structured Output (20%)
   - Tool Design & MCP Integration (18%)
   - Context Management & Reliability (15%)
   Материалы для подготовки (не проверены на актуальность/качество,
   `[НУЖНЫ ДАННЫЕ]` — оценить перед покупкой):
   - Официальные prep-курсы внутри Anthropic Partner Academy (доступны
     после регистрации партнёром).
   - [Community study guide, GitHub](https://github.com/daronyondem/claude-architect-exam-guide) — бесплатный.
   - Платные курсы на Udemy/Pluralsight — найдены поиском 25.08.2026,
     не оценивались по качеству.
3. **Регистрация и сдача.** Через Pearson VUE (онлайн-прокторинг или
   тест-центр), $125 до партнёрской скидки. Closed-book, 120 минут,
   проходной балл 720/1000.
4. **Поддержание.** Сертификат действует 12 месяцев — пересдача или
   обновление входит в регулярный цикл, не разовое действие.

## Google Cloud Generative AI Leader — что учить

Официальный exam guide зафетчен напрямую 25.08.2026
([PDF](https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf))
— это первичный источник, не пересказ блогов. Четыре секции с
официальным весом:

| Секция | Вес | Что внутри |
|---|---|---|
| 1. Fundamentals of gen AI | ~30% | базовые понятия (AI/ML/gen AI/foundation models/LLM), ML lifecycle, как выбрать foundation model под задачу, структурированные/неструктурированные и labeled/unlabeled данные, слои gen AI-стека (infrastructure/models/platforms/agents/applications), модели Google — Gemini, Gemma, Imagen, Veo |
| 2. Google Cloud's gen AI offerings | ~35% | **самая тяжёлая секция.** Продуктовая линейка Google: Gemini app/Advanced, Gemini Enterprise, Gemini для Workspace, Customer Engagement Suite (Conversational Agents, Agent Assist), Agent Platform (Model Garden, Agent Search, AutoML), RAG-предложения Google, инструментарий агентов (API-каталог: Speech-to-Text, Document AI, Vision и т.д.), Agent Studio vs Google AI Studio |
| 3. Techniques to improve gen AI model output | ~20% | ограничения foundation-моделей (галлюцинации, bias, knowledge cutoff), способы борьбы (grounding, RAG, fine-tuning, HITL), техники промптинга (zero/one/few-shot, role prompting, chain-of-thought, ReAct), параметры сэмплинга (temperature, top-p, safety settings) |
| 4. Business strategies for a successful gen AI solution | ~15% | как выбрать и внедрить gen AI-решение в организации, измерение эффекта, Secure AI Framework (SAIF), responsible AI — приватность, bias, fairness, accountability |

### Что уже частично закрыто, а что учить с нуля

Оценка по фактам из `00_profile/candidate.md` (не проверялась
экзаменом, ориентир для расстановки приоритетов при подготовке):

- **Секции 1, 3 и часть 4 — вероятно частичное пересечение** с уже
  пройденным AI Fluency: Framework & Foundations (Anthropic, 03.2026)
  и общим PM/delivery-бэкграундом: базовые понятия gen AI, техники
  промптинга, ограничения моделей, responsible AI на концептуальном
  уровне — знакомая территория, но термины и фреймворки
  Google-специфичные (SAIF, конкретные названия техник) требуют
  освежения, не изучения с нуля.
- **Секция 2 — учить с нуля.** Это чистая продуктовая номенклатура
  Google Cloud (Gemini Enterprise, Agent Platform, Customer Engagement
  Suite, RAG APIs, TPU-инфраструктура) — нулевое пересечение с Claude
  или другим опытом кандидата. Самая тяжёлая секция (35% экзамена) и
  самая незнакомая — приоритет подготовки.

### Материалы

- Официальный бесплатный learning path "Generative AI Leader" —
  [skills.google/paths/1951](https://www.skills.google/paths/1951).
  `[НУЖНЫ ДАННЫЕ]` — страница отдаёт контент только залогиненным
  пользователям через JS, автоматический фетч не показал список
  модулей и время прохождения. Открыть вручную под своим Google-
  аккаунтом перед планированием дат.
- [Study guide (PDF), Google Cloud](https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf) — официальный, не читался в эту сессию.
- [Sample questions, Google Cloud](https://forms.gle/soztS7Q74AXBncATA) — официальные пробные вопросы, неограниченное число попыток.

### Формат экзамена

$99, 50-60 вопросов, 90 минут, онлайн- или очный прокторинг, без
пререквизитов, валидность 3 года.

## Остальные сертификаты из roadmap.md

Не расписаны — программа под них появится после того, как
приоритизация в `roadmap.md` будет подтверждена пользователем (AWS AI
Practitioner, IIBA vs PMI-PBA для Ирландии, PMP/ICAgile для Украины,
AI Fluency доп-модули).
