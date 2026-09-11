# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/about.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_section = '''   <!-- PIPELINE EXPLANATION -->
   <section class="py-5 position-relative" style="background-color: #ffffff; padding-top: 120px !important; padding-bottom: 120px !important; overflow: hidden;">
        <!-- Dot Pattern Background -->
        <div style="position: absolute; inset: 0; background-image: radial-gradient(#e5e7eb 1px, transparent 1px); background-size: 24px 24px; z-index: 0; opacity: 0.6;"></div>
        
        <div class="container position-relative" style="z-index: 1;">
            <div class="row align-items-center">
                <!-- IMAGE ON LEFT -->
                <div class="col-lg-6 mb-5 mb-lg-0 wow fadeInLeft">
                    <img src="img/minimal_workspace.webp" alt="Flow Vello Pipeline" class="img-fluid" style="border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); width: 100%; object-fit: cover; aspect-ratio: 4/3; border: 1px solid #e5e7eb; background: #f8fafc;">
                </div>
                
                <!-- TEXT ON RIGHT -->
                <div class="col-lg-5 offset-lg-1 wow fadeInRight">
                    <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #111827; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 500; font-family: 'Rubik', sans-serif; letter-spacing: 0.5px; margin-bottom: 24px;">
                        Pipeline
                    </div>
                    <h2 style="font-family:'Rubik', sans-serif; font-size: 48px; font-weight: 500; color: #111827; letter-spacing: -2px; margin-bottom: 24px; line-height: 1.05;">
                        Stop hiring disconnected teams.
                    </h2>
                    <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; line-height: 1.6; margin-bottom: 16px;">
                        Most companies scale by hiring a design agency for their brand, a dev shop for their app, a marketing firm for their traffic, and a consultant for their operations. The result is bloated costs, broken communication, and systems that refuse to talk to each other.
                    </p>
                    <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; line-height: 1.6; margin: 0;">
                        We built Flow Vello to be the single source of truth for your digital growth. A specialized pipeline where Creative, Development, Marketing, and Automation departments operate under one roof.
                    </p>
                </div>
            </div>
        </div>
   </section>'''

# Regex to find the current PIPELINE EXPLANATION section
new_html = re.sub(r'(?s)<!-- PIPELINE EXPLANATION -->.*?</section>', new_section, html)

with open('c:/Users/my/Desktop/chatgpt/about.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated section successfully.")
