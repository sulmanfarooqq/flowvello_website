# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

new_bento = '''
     <!-- ECOSYSTEM FLYWHEEL (PREMIUM AGENCY BENTO) -->
     <section class="py-5" style="background-color: #ffffff; position: relative; overflow: hidden;">
        <!-- Dotted pattern background -->
        <div style="position: absolute; inset: 0; background-image: radial-gradient(#e5e7eb 1.5px, transparent 1.5px); background-size: 24px 24px; opacity: 0.5; z-index: 0;"></div>
        
        <div class="container py-5" style="position: relative; z-index: 1; max-width: 1200px;">
           
           <!-- Header Section -->
           <div class="mb-5 d-flex flex-column align-items-start" style="gap: 16px;">
              <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #fb383b; color: #ffffff; padding: 4px 12px; font-size: 12px; font-weight: 700; font-family: 'Rubik', sans-serif; letter-spacing: 1px; text-transform: uppercase;">
                 The Flow Vello Pipeline
              </div>
              <div class="d-flex flex-column" style="gap: 8px;">
                 <h2 style="font-family:'Rubik', sans-serif; font-size: 48px; font-weight: 600; color: #111827; letter-spacing: -1.5px; margin: 0; line-height: 1.1;">
                    One Unified Growth Engine.
                 </h2>
                 <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; margin: 0; max-width: 600px; line-height: 1.6;">
                    We don't sell isolated services. We deploy a 4-stage compounding pipeline where your brand, software, traffic, and operations feed into each other.
                 </p>
              </div>
           </div>

           <!-- Premium Bento CSS -->
           <style>
               .pipeline-grid { display: grid; grid-template-columns: 1fr; gap: 24px; }
               .pipeline-box { 
                   background: #111827; /* Deep dark agency background */
                   border-radius: 12px; 
                   padding: 40px; 
                   display: flex; 
                   flex-direction: column; 
                   justify-content: space-between; 
                   transition: transform 0.3s ease, box-shadow 0.3s ease; 
                   aspect-ratio: 1/1; 
                   position: relative;
                   overflow: hidden;
                   border: 1px solid rgba(255,255,255,0.05);
               }
               .pipeline-box::before {
                   content: '';
                   position: absolute;
                   top: 0; left: 0; right: 0;
                   height: 4px;
                   background: transparent;
                   transition: background 0.3s ease;
               }
               .pipeline-box:hover { 
                   transform: translateY(-5px); 
                   box-shadow: 0 20px 40px rgba(0,0,0,0.15); 
               }
               .pipeline-box:hover::before {
                   background: #fb383b; /* Red top border on hover */
               }
               .pipeline-step {
                   font-family: 'Rubik', sans-serif;
                   font-size: 13px;
                   font-weight: 700;
                   color: #fb383b;
                   text-transform: uppercase;
                   letter-spacing: 2px;
                   margin-bottom: 20px;
                   display: flex;
                   align-items: center;
               }
               .pipeline-icon { font-size: 32px; color: #ffffff; opacity: 0.9; margin-bottom: 20px; font-weight: 300; }
               .pipeline-title { font-family: 'Rubik', sans-serif; font-size: 24px; font-weight: 400; color: #ffffff; margin-bottom: 12px; letter-spacing: -0.5px; }
               .pipeline-desc { font-family: 'Rubik', sans-serif; color: #9ca3af; font-size: 15px; line-height: 1.6; margin: 0; max-width: 320px; }
               
               @media (min-width: 768px) {
                   .pipeline-grid { grid-template-columns: repeat(2, 1fr); }
               }
               @media (min-width: 1024px) {
                   .pipeline-grid { grid-template-columns: repeat(3, 1fr); }
                   .pipeline-span-2 { grid-column: span 2; aspect-ratio: auto; }
               }
           </style>

           <!-- Pipeline Grid Section -->
           <div class="pipeline-grid">
               <!-- Phase 1: Creative (Span 2) -->
               <div class="pipeline-box pipeline-span-2 wow fadeInUp" data-wow-delay="0.1s">
                   <div>
                       <div class="pipeline-step">Phase 01</div>
                       <div class="pipeline-icon"><i class="fal fa-pen-nib"></i></div>
                   </div>
                   <div class="mt-auto">
                       <h3 class="pipeline-title">Strategy & Brand</h3>
                       <p class="pipeline-desc">Before we write a single line of code, our Creative department prototypes your entire UI/UX flow and visual identity to establish absolute market authority.</p>
                   </div>
               </div>
               
               <!-- Phase 2: Development (Span 1) -->
               <div class="pipeline-box wow fadeInUp" data-wow-delay="0.2s">
                   <div>
                       <div class="pipeline-step">Phase 02</div>
                       <div class="pipeline-icon"><i class="fal fa-browser"></i></div>
                   </div>
                   <div class="mt-auto">
                       <h3 class="pipeline-title">Architecture</h3>
                       <p class="pipeline-desc">We build the scalable web applications and e-commerce bedrock required to handle enterprise volume.</p>
                   </div>
               </div>

               <!-- Phase 3: Marketing (Span 1) -->
               <div class="pipeline-box wow fadeInUp" data-wow-delay="0.3s">
                   <div>
                       <div class="pipeline-step">Phase 03</div>
                       <div class="pipeline-icon"><i class="fal fa-bullhorn"></i></div>
                   </div>
                   <div class="mt-auto">
                       <h3 class="pipeline-title">Traffic & Growth</h3>
                       <p class="pipeline-desc">We deploy aggressive LinkedIn and SEO campaigns to flood your new platform with qualified leads.</p>
                   </div>
               </div>

               <!-- Phase 4: Automation (Span 2) -->
               <div class="pipeline-box pipeline-span-2 wow fadeInUp" data-wow-delay="0.4s">
                   <div>
                       <div class="pipeline-step">Phase 04</div>
                       <div class="pipeline-icon"><i class="fal fa-robot"></i></div>
                   </div>
                   <div class="mt-auto">
                       <h3 class="pipeline-title">Autonomous Scale</h3>
                       <p class="pipeline-desc">Once the traffic hits, we layer AI agents and API workflows over your foundation to automate fulfillment, support, and sales triage—allowing you to scale without hiring.</p>
                   </div>
               </div>
           </div>
        </div>
     </section>
'''

match = re.search(r'(?s)(<!-- ECOSYSTEM FLYWHEEL \(SHADCN BENTO UI\) -->.*?)(<!-- WHY FLOW VELLO \(FEATURE GRID\))', html)
if match:
    new_html = html[:match.start(1)] + new_bento + '\n     ' + html[match.end(2):]
    with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Injected Premium Dark-Mode Pipeline Grid.")
else:
    print("Regex failed to find shadcn block.")
