# Claude-сертификация Anthropic — разбор

Проверено 25.08.2026 через веб-поиск (список источников — в конце
файла). Официальный источник — `claude.com/partners` и
`anthropic-partners.skilljar.com` — частично не отдаёт детали через
автоматический фетч, часть фактов — из сторонних блогов, которые
местами расходятся. Отмечено явно где именно.

## Что это такое

Anthropic с марта 2026 ведёt проктored-программу сертификации
(экзамены через Pearson VUE, онлайн-прокторинг или тест-центр).
Три роли, четыре экзамена:

| Сертификат | Цена (до партнёрской скидки) | Что проверяет |
|---|---|---|
| Claude Certified Associate | $99 | базовый уровень, не даёт зачёта в Partner Network |
| Claude Certified Developer — Foundations | $125 | сборка приложений/интеграций с Claude |
| Claude Certified Architect — Foundations (CCA-F) | $125 | архитектура agentic-систем на Claude |
| Claude Certified Architect — Professional (CCAR-P) | $175 | дизайн и governance Claude-решений на enterprise-масштабе |

Формат: closed-book, multiple-choice + сценарные вопросы, 120 минут
(~135 минут с check-in). Проходной балл — 720 из 1000 (шкала
100–1000). Сертификат действует **12 месяцев** с даты получения —
это не разовое достижение, а то, что придётся периодически
пересдавать.

Foundations и Professional по Architect-треку — **независимые
экзамены**, Foundations не конвертируется в Professional и не
обязателен как пререквизит для него. Формально можно сдавать Professional
напрямую, но рекомендуемый бэкграунд для Professional — 3+ года в
архитектуре систем и от 6 месяцев практической работы с Claude или
аналогичными моделями в проде.

Содержание Architect — Foundations (по вторичным источникам, вес в
экзамене, 60 вопросов / 5 доменов):
- Agentic Architecture & Orchestration — 27%
- Tool Design & MCP Integration — 18%
- Claude Code Configuration & Workflows — 20%
- Prompt Engineering & Structured Output — 20%
- Context Management & Reliability — 15%

Это прямое попадание в позиционирование Upwork-ниши №1 (AI-внедрение и
автоматизация, см. `01_markets/upwork.md`) — экзамен буквально проверяет
то, что предлагается продавать как услугу.

## Foundations vs Professional — сравнение (проверено 25.08.2026)

Формально независимые экзамены, пререквизита нет — можно сдавать
Professional напрямую, минуя Foundations. Но по содержанию они разные,
не «тот же экзамен сложнее»:

| | Foundations | Professional |
|---|---|---|
| Вопросов / доменов | 60 / 5 | 63 / 7 |
| Формат | сценарные (4 сценария из банка 6) | standalone-items |
| Домены | те же 5, что выше — вся техническая сборка | те же принципы дизайна **+ governance/risk, stakeholder communication & lifecycle, developer enablement** (вместе ~35% экзамена) |
| Целевой профиль | ~6 месяцев практики с Claude | 3+ года архитектуры систем/платформ + 6 мес. практики с Claude + реальные end-to-end внедрения |

Professional не «сложнее технически» (тот же формат 120 минут, тот же
порог 720/1000) — он шире по охвату: добавляет три домена про
governance, работу со стейкхолдерами и владение жизненным циклом
решения, которых в Foundations нет вовсе.

**Вывод для этого кандидата**: домены, которые отличают Professional
(governance, stakeholder communication, lifecycle ownership) —
совпадают с 24-летним PMO/Delivery-бэкграундом кандидата, здесь он
сильнее среднего claimanta. А домены Foundations (agentic architecture,
MCP, Claude Code workflows) — зона, где подтверждённого трек-рекорда
меньше (один курс AI Fluency Foundations + два pet-проекта, не
продакшн-опыт). Рекомендация — **начать с Foundations**: дешевле,
быстрее, закрывает более слабое место. Professional добирать после
накопления практики на реальных Claude-проектах (Upwork-контракты).

## Ключевое препятствие: партнёрский шлюз

**Официальный источник (`anthropic-partners.skilljar.com/page/faq-certifications`,
зафетчено 25.08.2026) говорит прямо**: экзамены доступны только для
организаций, состоящих в Claude Partner Network. Регистрация требует
"partner email address on a recognized company domain — personal email
addresses will not work". Личная почта (gmail и т.п.) не пройдёт.

Это значит: прежде чем сдавать экзамен, нужно:
1. Иметь юрлицо/бизнес с собственным доменом (не обязательно большая
   компания — но нужен домен, не `@gmail.com`).
2. Подать заявку в Claude Partner Network через
   `claude.com/form/cpn-partner-application`.
3. Получить допуск на уровень **Registered** — по описанию это
   бесплатный входной уровень, дающий доступ к Partner Hub, Partner
   Academy и допуску к экзаменам по партнёрским ценам.

**Уточнено 25.08.2026** — детальный разбор всех путей получения допуска
(через ERC, свой ФОП, чужого партнёра) вынесен в
`partner_access_paths.md`. Там же снят вопрос о «круговой зависимости»
(CCA до вступления не требуется) и подтверждён статус Украины как
поддерживаемой страны.

`[НУЖНЫ ДАННЫЕ]` Требования именно Registered-уровня расходятся между
источниками:
- Один источник (Enterprise DNA / anthropic.com news-страница) говорит,
  что уже на входе в Registered нужно **обязательство подготовить 10
  сертифицированных практиков** — это про партнёрство именно как про
  компанию/агентство, не про одиночку.
- Другой источник (сводные блоги про Claude Partner Network) говорит
  обратное: у Registered **нет минимума по числу практиков** — этот
  порог (10 практиков, 2 продакшн-клиента, 1 публичный кейс) начинается
  только с уровня **Select**, а Registered — это просто бесплатная
  регистрация, открытая соло-фрилансерам и малым командам, дающая
  доступ к обучению и экзаменам.

Официальная страница `claude.com/partners`, которую удалось зафетчить,
не подтверждает и не опровергает ни одну версию — отправляет к форме
заявки. **Это первое, что нужно проверить напрямую** — либо подачей
заявки и чтением полного текста формы/условий, либо вопросом в чат
поддержки Anthropic для партнёров, прежде чем планировать бюджет и
время под этот путь.

## Решения пользователя (25.08.2026)

- **Юрлицо/домен есть.** Партнёрская регистрация технически не
  заблокирована — есть домен, на который можно завести email для
  Claude Partner Network. Стоппер снят.
- **Начинаем с Claude Certified Architect напрямую**, не с AI Fluency
  доп-модулей. Это первый шаг Tier 1 в `roadmap.md`.
- **Foundations vs Professional — начинаем с Foundations** (обсуждено
  25.08.2026, см. сравнение доменов выше). Обоснование: домены
  Professional поверх Foundations (governance, stakeholder
  communication, lifecycle) совпадают с сильной стороной кандидата
  (PMO/Delivery), а домены Foundations (agentic architecture, MCP,
  Claude Code workflows) — со слабой (мало подтверждённой практики).
  Foundations закрывает более слабое место дешевле и быстрее.
  Professional — второй шаг, после накопления практики на реальных
  Claude-проектах.

## Следующие шаги (план действий)

1. Подать заявку в Claude Partner Network:
   [claude.com/form/cpn-partner-application](https://claude.com/form/cpn-partner-application)
   — с почтой на своём домене.
2. Дождаться допуска на уровень **Registered** (бесплатный, по
   вторичным источникам — без минимума практиков, но это
   `[НУЖНЫ ДАННЫЕ]`, см. раздел выше; подтвердится по факту подачи
   заявки).
3. Получить доступ к Anthropic Partner Academy и странице
   сертификации CCA-F.
4. Пройти официальные prep-курсы Partner Academy (плюс опционально
   community-guide и сторонние курсы — см. `learning_plan.md`).
5. Зарегистрироваться на экзамен через Pearson VUE, оплатить ($125 до
   партнёрской скидки), сдать.

Статус шага 1 — не выполнено на 25.08.2026, ждёт действия пользователя
(заявка подаётся вручную через форму, не автоматизируется агентом).

## Источники (проверено 25.08.2026)

- [FAQ - Certifications, anthropic-partners.skilljar.com](https://anthropic-partners.skilljar.com/page/faq-certifications) — официальный, зафетчен напрямую
- [Introducing the Services Track and Partner Hub of the Claude Partner Network, anthropic.com](https://www.anthropic.com/news/services-track-partner-hub) — официальный, зафетчен напрямую
- [claude.com/partners](https://claude.com/partners) — официальный, зафетчен напрямую, деталей по тирам не раскрыл
- [Claude Certified Architect (Professional): Exam Guide and Blueprint](https://claudecertificationguide.com/blog/claude-certified-architect-professional-exam-guide) — вторичный
- [The Complete Guide to Anthropic's Claude Certifications, Medium](https://medium.com/@roanmonteiro/the-complete-guide-to-anthropics-claude-certifications-the-4-exams-the-prerequisite-that-blocks-4d1f743bc5c4) — вторичный
- [Claude Partner Network 2026: How to Join, Tiers, Benefits & What It Means for Buyers](https://claudeimplementation.com/blog/claude-partner-network) — вторичный
- [Anthropic Formalises Its Claude Partner Services Tiers, Enterprise DNA](https://enterprisedna.co/resources/news/anthropic-claude-partner-network-services-track-june-2026/) — вторичный, версия «10 практиков уже на входе»
- [GitHub: daronyondem/claude-architect-exam-guide](https://github.com/daronyondem/claude-architect-exam-guide) — community-guide, не проверялся детально
- [Claude Certified Architect (Foundations): Exam Guide and Blueprint](https://claudecertificationguide.com/blog/claude-certified-architect-foundations-exam-guide) — вторичный, формат/домены Foundations
- [Claude Architect Professional Exam: Cost, Format, 7 Domains, FindSkill.ai](https://findskill.ai/blog/claude-certified-architect-professional-exam/) — вторичный, домены и вес Professional
