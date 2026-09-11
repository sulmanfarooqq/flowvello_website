# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

new_why = '''
     <!-- WHY FLOW VELLO (SHADCN DARK GRID UI) -->
     <section class="py-5" style="background-color: #0a0a0a; position: relative; overflow: hidden; border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
        
        <div class="container py-5" style="position: relative; z-index: 1; max-width: 1000px;">
           
           <!-- Header Section -->
           <div class="text-center mb-5 pb-4 mx-auto" style="max-width: 700px;">
              <span class="wow fadeInUp" style="color: #fb383b; font-family: 'Rubik', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; display: inline-block;">WHY FLOW VELLO</span>
              <h2 class="wow fadeInUp" data-wow-delay="0.1s" style="font-family:'Rubik', sans-serif; font-size: 42px; font-weight: 500; color: #ffffff; letter-spacing: -1px; margin-bottom: 20px; line-height: 1.15;">
                 The foundation for enterprise scaling
              </h2>
              <p class="wow fadeInUp" data-wow-delay="0.2s" style="color: #a1a1aa; font-size: 16px; font-family:'Rubik', sans-serif; margin: 0; line-height: 1.6;">
                 No templates. No busywork. We build custom architecture that supports your entire growth ecosystem—helping developers, marketers, and operations innovate.
              </p>
           </div>

           <!-- Ultra-Clean Dark Grid CSS -->
           <style>
               .shadcn-dark-grid {
                   display: grid;
                   grid-template-columns: 1fr;
                   border: 1px solid rgba(255,255,255,0.1);
                   border-radius: 8px;
                   overflow: hidden;
               }
               .shadcn-dark-cell {
                   padding: 48px;
                   border-bottom: 1px solid rgba(255,255,255,0.1);
                   background-color: transparent;
                   transition: background-color 0.2s ease;
               }
               .shadcn-dark-cell:hover {
                   background-color: rgba(255,255,255,0.02);
               }
               .shadcn-dark-cell:last-child {
                   border-bottom: none;
               }
               
               .shadcn-dark-icon {
                   font-size: 18px;
                   color: #ffffff;
                   margin-right: 12px;
               }
               .shadcn-dark-title {
                   font-family: 'Rubik', sans-serif;
                   font-size: 15px;
                   font-weight: 500;
                   color: #ffffff;
                   margin: 0;
               }
               .shadcn-dark-desc {
                   font-family: 'Rubik', sans-serif;
                   color: #a1a1aa;
                   font-size: 14px;
                   line-height: 1.6;
                   margin: 16px 0 0 0;
               }

               /* Tablet & Desktop Layout */
               @media (min-width: 768px) {
                   .shadcn-dark-grid { grid-template-columns: repeat(2, 1fr); }
                   .shadcn-dark-cell { border-right: 1px solid rgba(255,255,255,0.1); }
                   .shadcn-dark-cell:nth-child(2n) { border-right: none; }
                   .shadcn-dark-cell:nth-last-child(-n+2) { border-bottom: none; }
               }
               @media (min-width: 1024px) {
                   .shadcn-dark-grid { grid-template-columns: repeat(3, 1fr); }
                   .shadcn-dark-cell { border-right: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); }
                   .shadcn-dark-cell:nth-child(2n) { border-right: 1px solid rgba(255,255,255,0.1); } /* reset tablet */
                   .shadcn-dark-cell:nth-child(3n) { border-right: none; }
                   .shadcn-dark-cell:nth-last-child(-n+3) { border-bottom: none; }
               }
           </style>

           <!-- Grid Section -->
           <div class="shadcn-dark-grid wow fadeInUp" data-wow-delay="0.3s">
               
               <!-- Cell 1 -->
               <div class="shadcn-dark-cell">
                   <div class="d-flex align-items-center">
                       <div class="shadcn-dark-icon"><i class="fal fa-bolt"></i></div>
                       <h3 class="shadcn-dark-title">Faaast Execution</h3>
                   </div>
                   <p class="shadcn-dark-desc">We ship production-ready systems without the bloat, helping your enterprise move faster than the competition.</p>
               </div>
               
               <!-- Cell 2 -->
               <div class="shadcn-dark-cell">
                   <div class="d-flex align-items-center">
                       <div class="shadcn-dark-icon"><i class="fal fa-microchip"></i></div>
                       <h3 class="shadcn-dark-title">Powerful Infrastructure</h3>
                   </div>
                   <p class="shadcn-dark-desc">Built on top-tier cloud architecture like AWS and Supabase to guarantee 99.99% uptime and unrestricted scaling.</p>
               </div>

               <!-- Cell 3 -->
               <div class="shadcn-dark-cell">
                   <div class="d-flex align-items-center">
                       <div class="shadcn-dark-icon"><i class="fal fa-fingerprint"></i></div>
                       <h3 class="shadcn-dark-title">Enterprise Security</h3>
                   </div>
                   <p class="shadcn-dark-desc">Your data stays yours. We implement rigorous security protocols and custom auth flows for absolute protection.</p>
               </div>

               <!-- Cell 4 -->
               <div class="shadcn-dark-cell">
                   <div class="d-flex align-items-center">
                       <div class="shadcn-dark-icon"><i class="fal fa-pen-ruler"></i></div>
                       <h3 class="shadcn-dark-title">True Customization</h3>
                   </div>
                   <p class="shadcn-dark-desc">Your workflows are designed entirely around your business instead of forcing you into a rigid SaaS template.</p>
               </div>

               <!-- Cell 5 -->
               <div class="shadcn-dark-cell">
                   <div class="d-flex align-items-center">
                       <div class="shadcn-dark-icon"><i class="fal fa-sliders-h-square"></i></div>
                       <h3 class="shadcn-dark-title">Absolute Control</h3>
                   </div>
                   <p class="shadcn-dark-desc">We build human-fallback protocols. AI and automation should know when to stop and escalate to your team.</p>
               </div>

               <!-- Cell 6 -->
               <div class="shadcn-dark-cell">
                   <div class="d-flex align-items-center">
                       <div class="shadcn-dark-icon"><i class="fal fa-sparkles"></i></div>
                       <h3 class="shadcn-dark-title">Built for AI</h3>
                   </div>
                   <p class="shadcn-dark-desc">Every platform we deploy is natively wired to integrate seamlessly with autonomous AI agents and LLMs.</p>
               </div>
               
           </div>
        </div>
     </section>
'''

match = re.search(r'(?s)(<section class="fv-why-grid py-5">.*?)(<!-- HOW WE WORK -->|<section class="fv-process-dark)', html)
if match:
    new_html = html[:match.start(1)] + new_why + '\n     ' + html[match.start(2):]
    with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Replaced Why Flow Vello grid with the dark-mode Shadcn grid.")
else:
    print("Regex failed to find fv-why-grid block.")
