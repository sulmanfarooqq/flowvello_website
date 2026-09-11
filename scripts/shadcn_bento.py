# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

new_bento = '''
     <!-- ECOSYSTEM FLYWHEEL (SHADCN BENTO UI) -->
     <section class="py-5" style="background-color: #ffffff; position: relative; overflow: hidden;">
        <!-- Dotted pattern background -->
        <div style="position: absolute; inset: 0; background-image: radial-gradient(#e5e7eb 1.5px, transparent 1.5px); background-size: 24px 24px; opacity: 0.5; z-index: 0;"></div>
        
        <div class="container py-5" style="position: relative; z-index: 1; max-width: 1200px;">
           
           <!-- Header Section -->
           <div class="mb-5 d-flex flex-column align-items-start" style="gap: 16px;">
              <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #111827; color: #ffffff; padding: 4px 12px; font-size: 12px; font-weight: 600; font-family: 'Rubik', sans-serif;">
                 Platform
              </div>
              <div class="d-flex flex-column" style="gap: 8px;">
                 <h2 style="font-family:'Rubik', sans-serif; font-size: 48px; font-weight: 400; color: #111827; letter-spacing: -2px; margin: 0; line-height: 1.1;">
                    One Unified Growth Engine.
                 </h2>
                 <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; margin: 0; max-width: 600px; line-height: 1.6; letter-spacing: -0.2px;">
                    Managing enterprise scale today is already tough. We engineer a compounding ecosystem where your software, operations, and marketing feed each other.
                 </p>
              </div>
           </div>

           <!-- CSS for Shadcn Grid -->
           <style>
               .shadcn-grid { display: grid; grid-template-columns: 1fr; gap: 32px; }
               .shadcn-box { background-color: #f4f4f5; border-radius: 6px; padding: 32px; display: flex; flex-direction: column; justify-content: space-between; transition: background-color 0.2s ease; aspect-ratio: 1/1; }
               .shadcn-box:hover { background-color: #e4e4e7; }
               .shadcn-icon { font-size: 28px; color: #111827; margin-bottom: 20px; font-weight: 300; }
               .shadcn-title { font-family: 'Rubik', sans-serif; font-size: 20px; font-weight: 400; color: #111827; margin-bottom: 8px; letter-spacing: -0.5px; }
               .shadcn-desc { font-family: 'Rubik', sans-serif; color: #6b7280; font-size: 15px; line-height: 1.6; margin: 0; max-width: 280px; }
               
               @media (min-width: 768px) {
                   .shadcn-grid { grid-template-columns: repeat(2, 1fr); }
               }
               @media (min-width: 1024px) {
                   .shadcn-grid { grid-template-columns: repeat(3, 1fr); }
                   .shadcn-span-2 { grid-column: span 2; aspect-ratio: auto; }
               }
           </style>

           <!-- Grid Section -->
           <div class="shadcn-grid">
               <!-- Development (Span 2) -->
               <div class="shadcn-box shadcn-span-2 wow fadeInUp" data-wow-delay="0.1s">
                   <div class="shadcn-icon"><i class="fal fa-browser"></i></div>
                   <div class="mt-auto">
                       <h3 class="shadcn-title">Foundation & Development</h3>
                       <p class="shadcn-desc">We architect scalable custom software, e-commerce platforms, and robust web applications. This is the indestructible bedrock of your digital business.</p>
                   </div>
               </div>
               
               <!-- Creative (Span 1) -->
               <div class="shadcn-box wow fadeInUp" data-wow-delay="0.2s">
                   <div class="shadcn-icon"><i class="fal fa-pen-nib"></i></div>
                   <div class="mt-auto">
                       <h3 class="shadcn-title">Brand & UI/UX</h3>
                       <p class="shadcn-desc">Elite UI/UX prototyping and digital branding to establish absolute market authority.</p>
                   </div>
               </div>

               <!-- Marketing (Span 1) -->
               <div class="shadcn-box wow fadeInUp" data-wow-delay="0.3s">
                   <div class="shadcn-icon"><i class="fal fa-bullhorn"></i></div>
                   <div class="mt-auto">
                       <h3 class="shadcn-title">Traffic & Scaling</h3>
                       <p class="shadcn-desc">Relentless growth marketing, SEO, and LinkedIn pipeline scaling to drive qualified leads.</p>
                   </div>
               </div>

               <!-- Automation (Span 2) -->
               <div class="shadcn-box shadcn-span-2 wow fadeInUp" data-wow-delay="0.4s">
                   <div class="shadcn-icon"><i class="fal fa-robot"></i></div>
                   <div class="mt-auto">
                       <h3 class="shadcn-title">Autonomous Operations</h3>
                       <p class="shadcn-desc">We layer autonomous AI agents and API workflows over your foundation to eliminate manual labor and accelerate data processing exponentially.</p>
                   </div>
               </div>
           </div>
        </div>
     </section>
'''

match = re.search(r'(?s)(<!-- ECOSYSTEM FLYWHEEL \(BENTO BOX\) -->.*?)(<!-- WHY FLOW VELLO \(FEATURE GRID\))', html)
if match:
    new_html = html[:match.start(1)] + new_bento + '\n     ' + html[match.end(1):]
    with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Injected Shadcn-style Bento Grid using pure HTML/CSS.")
else:
    print("Regex failed to find ecosystem block.")
