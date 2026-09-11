# -*- coding: utf-8 -*-
import json

content = {
    "Web Applications": {
        "images": [
            "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=800&q=80"
        ],
        "features": [
            {"icon": "layer-group", "title": "Full-Stack Architecture", "desc": "Custom frontend and backend infrastructure designed for high traffic and maximum security without template bloat."},
            {"icon": "database", "title": "Database Optimization", "desc": "Scalable cloud database modeling ensuring lightning-fast query times and structural integrity for large datasets."},
            {"icon": "plug", "title": "Custom API Endpoints", "desc": "Bespoke REST or GraphQL APIs to connect your new web application seamlessly with your existing enterprise tools."},
            {"icon": "shield-check", "title": "Role-Based Authentication", "desc": "Enterprise-grade security protocols with JWT auth, SSO integration, and strict permission levels."},
            {"icon": "rocket", "title": "Sub-Second Rendering", "desc": "Advanced server-side rendering (SSR) and edge caching to guarantee flawless Lighthouse performance scores."},
            {"icon": "box-open", "title": "Complete Code Handover", "desc": "You retain 100% IP ownership. We provide full GitHub repository access, deployment pipelines, and documentation."}
        ]
    },
    "Graphic Design": {
        "images": [
            "https://images.unsplash.com/photo-1626785774573-4b799315345d?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=800&q=80"
        ],
        "features": [
            {"icon": "paint-brush", "title": "Brand Identity Systems", "desc": "Complete visual guidelines including primary logos, secondary marks, typography hierarchies, and color palettes."},
            {"icon": "vector-square", "title": "Vector Asset Creation", "desc": "High-resolution, infinitely scalable SVG assets for web, print, and physical merchandise."},
            {"icon": "share-alt", "title": "Social Media Kits", "desc": "Customized template libraries for Instagram, LinkedIn, and Twitter designed to maximize platform engagement."},
            {"icon": "file-pdf", "title": "Corporate Collateral", "desc": "Professional pitch decks, whitepapers, letterheads, and business cards aligned with your brand identity."},
            {"icon": "eye", "title": "Visual Hierarchy Audits", "desc": "Strategic analysis of your existing assets to ensure consistent messaging and aesthetic dominance."},
            {"icon": "folder-open", "title": "Raw Source Files", "desc": "Delivery of all native .AI, .PSD, and .FIG files so your internal teams can iterate without restrictions."}
        ]
    },
    "Ai Agents": {
        "images": [
            "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80"
        ],
        "features": [
            {"icon": "robot", "title": "Autonomous Task Execution", "desc": "Custom LLM-powered agents capable of handling complex multi-step workflows without human intervention."},
            {"icon": "brain", "title": "Custom Knowledge Bases (RAG)", "desc": "Agents trained directly on your proprietary company data, docs, and FAQs to guarantee accurate responses."},
            {"icon": "network-wired", "title": "Multi-Platform Integration", "desc": "Deploy agents natively into Slack, Discord, Zendesk, or custom dashboards via secure API hooks."},
            {"icon": "comment-alt-lines", "title": "Conversational UI", "desc": "Natural language processing interfaces that allow your team or clients to interact with data organically."},
            {"icon": "user-shield", "title": "Human-in-the-Loop Triggers", "desc": "Smart escalation protocols that instantly route complex or high-risk queries to a human supervisor."},
            {"icon": "chart-line", "title": "Analytics & Logging", "desc": "Comprehensive dashboards tracking agent success rates, token usage, and conversation histories."}
        ]
    }
}

with open('c:/Users/my/Desktop/chatgpt/scripts/data.json', 'w') as f:
    json.dump(content, f)

print("Created data.json")
