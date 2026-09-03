# Flow Vello — Agent Operating Contract

## Project
Flow Vello is a production marketing website for an AI automation and software agency. Preserve the existing visual identity and improve structure, accessibility, SEO, performance, and maintainability.

## Source of truth
- Existing HTML/CSS/JS is the current implementation.
- `docs/` contains product, content, architecture, and implementation decisions.
- `.agents/skills/` contains reusable design/engineering skills.
- Do not invent clients, testimonials, awards, certifications, revenue, employee counts, performance percentages, case studies, addresses, phone numbers, or integrations that Flow Vello cannot substantiate.

## Architecture rules
- Keep the site static-first and dependency-light.
- Reuse the existing visual system: Teko display typography, Rubik body typography, Flow Vello red `#fb383b`, dark `#222429`, generous spacing, sharp editorial hierarchy, subtle borders, and restrained motion.
- Existing pages should retain their visual language. New pages must use the same shell, navigation, footer, buttons, animations, spacing, and responsive behavior.
- Use semantic HTML5 landmarks and exactly one meaningful H1 per page.
- Use descriptive, human-readable URLs and page-specific metadata.
- Keep navigation and footer consistent across every page.
- Do not introduce React/Next/Vue or a build system unless the architecture is deliberately migrated and documented.

## SEO contract
Every indexable page must have:
- unique `<title>`
- unique meta description
- canonical URL
- Open Graph metadata
- Twitter metadata where useful
- meaningful H1/H2 hierarchy
- descriptive image `alt` text
- internal links to relevant pages
- JSON-LD appropriate to the page type

Use Organization/WebSite/WebPage/Service/BreadcrumbList/Article schemas only where they are truthful. Never use fake review/rating schema or fabricated claims.

## Accessibility contract
- Keyboard-accessible navigation and controls.
- Visible focus states.
- Sufficient color contrast.
- Decorative images use empty alt; informative images use useful alt text.
- Do not communicate essential information through color alone.
- Respect `prefers-reduced-motion` for non-essential animation.

## Engineering contract
- Prefer small, reversible changes.
- Preserve existing working plugins and IDs unless there is a documented reason to change them.
- Do not duplicate CSS systems unnecessarily.
- Avoid inline JavaScript for page behavior when a shared module can handle it.
- Validate links, asset paths, metadata, and console errors before considering a page complete.
- Do not commit secrets, API keys, credentials, `.env` files, or generated build artifacts.

## Delivery checklist
Before finishing a task: inspect affected files, implement the smallest coherent change, check responsive behavior, check SEO/accessibility, verify internal links, update relevant docs, and report exactly what changed and any remaining risks.
