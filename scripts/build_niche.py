import os

niches = [
    "Real Estate Agencies", "Law Firms & Attorneys", "Dental Practices", "E-Commerce Brands (6-7 Fig)", 
    "B2B SaaS Companies", "Medical Practices & Clinics", "Med Spas & Cosmetic Clinics", 
    "Financial Advisors & Wealth Managers", "Insurance Agencies", "Home Services (HVAC/Plumbing/Electrical)", 
    "High-Ticket Coaches & Course Creators", "Property Developers & Construction", "Property Management Companies", 
    "Private Schools & Colleges", "Travel Agencies & Tour Operators", "E-Commerce Brands (Local Pakistan)", 
    "Staffing & Recruitment Agencies", "Hospitality (Hotels & Restaurants)", "Healthcare Staffing Agencies", 
    "Solar Energy Companies", "Auto Dealerships & Car Sales", "Gyms & Fitness Centers", "Salons & Beauty Studios", 
    "Photographers & Videographers", "Wedding & Event Planners", "Online Course Platforms & EdTech", 
    "CPA & Accounting Firms", "Dental Labs & Veterinary Clinics", "Logistics & Freight Companies", 
    "Pharmacies & Drug Stores", "IELTS / Test Prep Institutes", "Diagnostic Laboratories", "Interior Design Firms", 
    "IT & Software Development Agencies", "Manufacturing Companies", "Coworking Spaces & Business Centers", 
    "Dermatology & Skincare Clinics", "Physical Therapy & Chiropractic", "Non-Profits & NGOs", 
    "Optometry & Eye Care Clinics", "Car Wash & Detailing Services", "Bakeries & Cafes", "Jewelry Stores", 
    "Furniture & Home Decor Stores", "Laundry & Dry Cleaning Services", "Tutoring & Home Tuition Services", 
    "Marble & Tiles / Construction Materials", "Clothing Boutiques & Fashion Brands", 
    "Pharmacies (Compounding / Specialized)", "Mobile Phone & Electronics Repair"
]

output_file = 'c:/Users/my/Desktop/strategy/6_Niche_Systems.txt'
os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("THE 50 NICHE ILLUSION - READ THIS FIRST\n")
    f.write("If you try to execute all 50 of these, your agency will die within 6 months.\n")
    f.write("Pick ONE or TWO to start. Become the undisputed king of that niche.\n")
    f.write("You cannot sell B2B SaaS architectures while building SMS bots for Car Washes.\n")
    f.write("=================================================================================\n\n")

    for niche in niches:
        f.write(f"[{niche.upper()}]\n")
        # Generic but highly targeted 5-line system formula
        if "Real Estate" in niche or "Property" in niche:
            f.write("1. Core Problem: Wasting hours qualifying dead leads and missing fast inbound web queries.\n")
            f.write("2. Frontend Setup: AI WhatsApp Agent that instantly qualifies leads (budget, timeframe) 24/7.\n")
            f.write("3. Backend Retainer: Full GoHighLevel CRM mapping property inventory to automated drip campaigns.\n")
            f.write("4. Client Result: Agents only talk to pre-qualified buyers ready to tour properties.\n")
            f.write("5. Retainer Value: They pay /mo because a single closed deal covers your fee for the year.\n\n")
        elif "E-Commerce" in niche or "Clothing" in niche or "Jewelry" in niche:
            f.write("1. Core Problem: High cart abandonment and terrible post-purchase customer support.\n")
            f.write("2. Frontend Setup: Shopify-integrated AI chatbot to handle 'Where is my order?' and sizing queries.\n")
            f.write("3. Backend Retainer: Klaviyo/Omnisend predictive flow automation based on user browsing behavior.\n")
            f.write("4. Client Result: Automated recovery of 15%+ of abandoned carts without human support staff.\n")
            f.write("5. Retainer Value: They pay /mo because your system directly scales their top-line revenue.\n\n")
        elif "B2B" in niche or "Software" in niche or "IT" in niche:
            f.write("1. Core Problem: High customer churn and sales reps wasting time doing manual data entry.\n")
            f.write("2. Frontend Setup: HubSpot/Salesforce bi-directional sync to eliminate manual CRM updating.\n")
            f.write("3. Backend Retainer: Executive Dashboard tracking product usage to predict and prevent churn.\n")
            f.write("4. Client Result: Sales reps double their call volume; founders get real-time MRR visibility.\n")
            f.write("5. Retainer Value: They pay /mo because reducing churn by 2% saves them hundreds of thousands.\n\n")
        elif "Medical" in niche or "Dental" in niche or "Health" in niche or "Clinic" in niche:
            f.write("1. Core Problem: No-shows cost them thousands, and front desk staff are overwhelmed by calls.\n")
            f.write("2. Frontend Setup: Missed-call text-back AI that instantly books appointments via Calendly/EHR.\n")
            f.write("3. Backend Retainer: Automated patient reactivation campaigns (check-ups, cleanings, botox refills).\n")
            f.write("4. Client Result: Zero missed leads from unanswered phones and an extra 10 bookings/week.\n")
            f.write("5. Retainer Value: They pay .5k/mo because a single new patient LTV covers your monthly cost.\n\n")
        elif "Home Services" in niche or "Solar" in niche or "Construction" in niche:
            f.write("1. Core Problem: Paying for expensive Google Ads but missing calls when on a job site.\n")
            f.write("2. Frontend Setup: AI voice/text agent that quotes basic jobs and schedules dispatch instantly.\n")
            f.write("3. Backend Retainer: Automated review generation requests the second a job is marked 'Complete'.\n")
            f.write("4. Client Result: They outcompete rivals simply by being the first to reply within 10 seconds.\n")
            f.write("5. Retainer Value: They pay /mo because local SEO dominance and instant lead capture doubles their ROI.\n\n")
        elif "Coaches" in niche or "Tutor" in niche or "EdTech" in niche:
            f.write("1. Core Problem: Manual onboarding of students and chaotic lead tracking from webinars.\n")
            f.write("2. Frontend Setup: Zapier automations linking Stripe payments to immediate course/Slack access.\n")
            f.write("3. Backend Retainer: AI Setter agent qualifying DMs and pushing them to a VSL or booking link.\n")
            f.write("4. Client Result: A completely hands-free funnel from Instagram ad to enrolled student.\n")
            f.write("5. Retainer Value: They pay /mo because they can scale ad spend without breaking their ops.\n\n")
        elif "Car Wash" in niche or "Laundry" in niche or "Bakeries" in niche:
            f.write("1. Core Problem: Low customer loyalty and relying entirely on random walk-in traffic.\n")
            f.write("2. Frontend Setup: QR code loyalty program capturing phone numbers at the point of sale.\n")
            f.write("3. Backend Retainer: Automated SMS blasts on slow days (e.g., '50% off Wash this Tuesday').\n")
            f.write("4. Client Result: The ability to instantly generate foot traffic on demand via a text button.\n")
            f.write("5. Retainer Value: They pay /mo because the tech is simple but the revenue spike is immediate.\n\n")
        else:
            f.write("1. Core Problem: Chaotic internal operations, data silos, and manual repetitive reporting.\n")
            f.write("2. Frontend Setup: Custom AI agent trained on their company SOPs to act as internal support.\n")
            f.write("3. Backend Retainer: Monday.com/Airtable workspace replacing 10 disjointed Google Sheets.\n")
            f.write("4. Client Result: Leadership can finally see project status without scheduling a 2-hour meeting.\n")
            f.write("5. Retainer Value: They pay /mo for operational clarity and hundreds of saved payroll hours.\n\n")

print("Generated 50 niche systems.")
