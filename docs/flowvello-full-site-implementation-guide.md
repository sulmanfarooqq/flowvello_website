# Flow Vello — Full Site Build Guide (mapped from protogroup.co)

You have 3 template files right now: `index.html`, `service.html`, `contact.html`. Every new page below is one of these three, cloned and re-worded — never build a page from scratch, or your styling drifts between pages. `about`, `case-studies`, `digital-transformations` etc. don't exist on protogroup.co as unique templates either — they're all the same inner-page shell as their service pages, just different content blocks.

---

## 1. URL cleanup first (before you build anything)

Your list has duplicates and junk from how the crawler dumped it — fix these in your own mental model before assigning pages:

- `/contact-us/` and `/contact-us` → same page, trailing slash is not a separate page.
- `/about/` and `/about` → same page.
- `mailto:` and `tel:` links → these aren't pages, they're footer/header links (email + phone), not routes to build.
- `/ambiance-hotels/` → this is a **case study client page**, not a top-level nav item. It nests under `/case-studies/`.
- `/business-process-outsource-bpo/` → your own strategy doc already told you to **skip this pillar** unless you're actually staffing VAs. Don't build it just because Proto has it.

Real, unique pages to build: **Home (done), Software Development, Digital Operations, Business Applications, About, Blog, Case Studies (hub), 2 case study detail pages, Contact, Privacy Policy, Terms of Use, Disclosure.**

---

## 2. Page → Template → Content source map

| Flow Vello page | File to create | Clone from | Content source |
|---|---|---|---|
| `/services.html` (hub) | new | `service.html` | Services Hub intro in `flowvello_agency_information.md` |
| `/software-development.html` | new | `service.html` | "Software Development" section in the doc |
| `/digital-operations.html` | new | `service.html` | "Digital Operations Page" section — monday.com/Pipedrive/HubSpot/Odoo |
| `/business-applications.html` | new | `service.html` | Map to your "Executive Dashboards" + "Workflow & AI Automation" pillars — Proto uses this term for CRM/ERP tooling, decide if it's a real distinct page for you or folds into Digital Operations |
| `/about.html` | new | `index.html` (its layout is closer to a mixed content page than `service.html`) | "About Page" section in the doc |
| `/case-studies.html` (hub) | new | `service.html` | "Case Studies Page" section — **leave empty of fabricated entries, per your own doc's rule** |
| `/case-studies/[client-slug].html` | new, one per real client | `service.html` | Only build this once you have a real client — the template in the doc under "Case Studies Page" |
| `/blog.html` (index) | new | `service.html` | "Blog Page" — categories only for now, no fake posts |
| `/blog/[post-slug].html` | new, per post | `service.html` | Write real posts before creating the file — an empty blog index is fine, a blog with 1 real post and a linked file structure is better than 9 fake titles |
| `/contact.html` | already exists | — | Update copy to match `flowvello_agency_information.md` "Contact Page" section — form fields, no fake phone number |
| `/privacy-policy.html` | new | `service.html` (strip hero/CTA, keep text body sections only) | Write yourself — do not copy Proto's legal text, it's their company's data-handling terms, not yours |
| `/terms-of-use.html` | new | same | Same — original text, based on your actual engagement terms |
| `/disclosure.html` | new | same | Only include if you have an actual disclosure to make (affiliate links, AI-generated content notice, etc.) — otherwise skip it, don't invent a page to match Proto's count |

---

## 3. Nav + footer wiring (do this once, not per-page)

Since every page shares the same `<nav>` and `<section id="footerSection">` markup, update these **once** and copy the updated header/footer block into every new file you create — don't hand-edit nav links 12 separate times and let them drift out of sync.

Target nav structure (from your own sitemap doc):
```
Home · Services (dropdown: Workflow Automation, AI Agents & Automation, Executive Dashboards)
· Digital Operations (dropdown: monday.com, Pipedrive, HubSpot, Odoo)
· Software Development (dropdown: Mobile App Dev, Web App Dev)
· About · Blog · Case Studies · Contact          [CTA: Let's Connect → contact.html]
```
Your current `index.html` nav already has the dropdown markup pattern (`#menu1`–`#menu4`) — reuse that exact structure, just repoint `href` values from `#` to the real filenames once they exist, and remove dropdowns from pages where they'd be redundant (e.g. don't repeat the Services dropdown items as a page section AND a nav dropdown pointing to itself).

Footer: identical on every page. Build it once on `index.html` (already done), then paste it verbatim into every new file.

---

## 4. Build order (do NOT build all 12 pages at once)

1. **Contact page** — you already have it, just update the copy. This is your money page; get it right first.
2. **Services hub + its 2-3 real sub-pages** — this is what a cold visitor clicks after the homepage.
3. **About page** — but stop at the "Meet the Team" section until you have real names/photos. A missing team section reads better than a placeholder with generic stock photos.
4. **Digital Operations page** — only list the platforms (monday.com/Pipedrive/HubSpot/Odoo) you can actually demo or have real experience with. Don't list all 4 to look bigger.
5. **Legal pages** (privacy/terms) — needed before you run any real ad traffic or take a client's data via the contact form. Do these before case studies/blog, not after.
6. **Case studies + blog** — last, and only populate as real work/posts exist. An empty hub page with "Coming Soon" (like your homepage portfolio section now shows) is fine; a padded fake one isn't.

---

## 5. One thing to decide before you build any of this

Your source, protogroup.co, sells **BPO/staffing** as a full pillar — you're explicitly not doing that per your own doc. That means roughly 20% of their site structure (an entire outsourcing sales funnel) doesn't map to you at all. Don't try to force-fit `business-process-outsource-bpo` into your build just because it was on the list you pasted — cut it now, the same way your own strategy doc told you to cut fabricated stats. Copying a competitor's full sitemap when a third of it is a different business model is how you end up promising services you can't deliver on your first real client call.
