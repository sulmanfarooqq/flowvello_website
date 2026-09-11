# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

subtle_bento = '''
     <!-- ECOSYSTEM FLYWHEEL (ULTRA-SUBTLE MINIMALIST) -->
     <section class="py-5" style="background-color: #ffffff; position: relative; overflow: hidden;">
        <!-- Dotted pattern background -->
        <div style="position: absolute; inset: 0; background-image: radial-gradient(#f3f4f6 1px, transparent 1px); background-size: 24px 24px; opacity: 0.8; z-index: 0;"></div>
        
        <div class="container py-5" style="position: relative; z-index: 1; max-width: 1200px;">
           
           <!-- Header Section -->
           <div class="mb-5 d-flex flex-column align-items-start" style="gap: 16px;">
              <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #f3f4f6; color: #111827; padding: 4px 12px; font-size: 13px; font-weight: 500; font-family: 'Rubik', sans-serif;">
                 The Platform
              </div>
              <div class="d-flex flex-column" style="gap: 8px;">
                 <h2 style="font-family:'Rubik', sans-serif; font-size: 48px; font-weight: 400; color: #111827; letter-spacing: -2px; margin: 0; line-height: 1.1;">
                    One Unified Growth Engine.
                 </h2>
                 <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; margin: 0; max-width: 600px; line-height: 1.6; letter-spacing: -0.2px;">
                    Managing enterprise scale is tough. We engineer a compounding ecosystem where your software, operations, and marketing naturally feed each other.
                 </p>
              </div>
           </div>

           <!-- Ultra-Subtle CSS -->
           <style>
               .subtle-grid { display: grid; grid-template-columns: 1fr; gap: 24px; }
               .subtle-box { 
                   background-color: #fdfdfd; 
                   border: 1px solid #f3f4f6;
                   border-radius: 12px; 
                   padding: 40px; 
                   display: flex; 
                   flex-direction: column; 
                   justify-content: space-between; 
                   transition: transform 0.4s ease, box-shadow 0.4s ease; 
                   aspect-ratio: 1/1; 
               }
               .subtle-box:hover { 
                   transform: translateY(-4px);
                   box-shadow: 0 12px 30px rgba(0,0,0,0.04); 
               }
               .subtle-icon { font-size: 28px; color: #111827; margin-bottom: 24px; font-weight: 300; opacity: 0.8; }
               .subtle-title { font-family: 'Rubik', sans-serif; font-size: 20px; font-weight: 500; color: #111827; margin-bottom: 8px; letter-spacing: -0.5px; }
               .subtle-desc { font-family: 'Rubik', sans-serif; color: #6b7280; font-size: 15px; line-height: 1.6; margin: 0; max-width: 300px; }
               
               @media (min-width: 768px) {
                   .subtle-grid { grid-template-columns: repeat(2, 1fr); }
               }
               @media (min-width: 1024px) {
                   .subtle-grid { grid-template-columns: repeat(3, 1fr); }
                   .subtle-span-2 { grid-column: span 2; aspect-ratio: auto; }
               }
           </style>

           <!-- Grid Section -->
           <div class="subtle-grid">
               <!-- Development (Span 2) -->
               <div class="subtle-box subtle-span-2 wow fadeInUp" data-wow-delay="0.1s">
                   <div class="subtle-icon"><i class="fal fa-browser"></i></div>
                   <div class="mt-auto">
                       <h3 class="subtle-title">Foundation & Development</h3>
                       <p class="subtle-desc">We architect scalable custom software, e-commerce platforms, and robust web applications. This is the indestructible bedrock of your digital business.</p>
                   </div>
               </div>
               
               <!-- Creative (Span 1) -->
               <div class="subtle-box wow fadeInUp" data-wow-delay="0.2s">
                   <div class="subtle-icon"><i class="fal fa-pen-nib"></i></div>
                   <div class="mt-auto">
                       <h3 class="subtle-title">Brand & UI/UX</h3>
                       <p class="subtle-desc">Elite UI/UX prototyping and digital branding to establish absolute market authority.</p>
                   </div>
               </div>

               <!-- Marketing (Span 1) -->
               <div class="subtle-box wow fadeInUp" data-wow-delay="0.3s">
                   <div class="subtle-icon"><i class="fal fa-bullhorn"></i></div>
                   <div class="mt-auto">
                       <h3 class="subtle-title">Traffic & Scaling</h3>
                       <p class="subtle-desc">Relentless growth marketing, SEO, and LinkedIn scaling to drive qualified enterprise leads.</p>
                   </div>
               </div>

               <!-- Automation (Span 2) -->
               <div class="subtle-box subtle-span-2 wow fadeInUp" data-wow-delay="0.4s">
                   <div class="subtle-icon"><i class="fal fa-robot"></i></div>
                   <div class="mt-auto">
                       <h3 class="subtle-title">Autonomous Operations</h3>
                       <p class="subtle-desc">We layer autonomous AI agents and API workflows over your foundation to eliminate manual labor and accelerate data processing exponentially.</p>
                   </div>
               </div>
           </div>
        </div>
     </section>
'''

match = re.search(r'(?s)(<!-- ECOSYSTEM FLYWHEEL \(PREMIUM AGENCY BENTO\) -->.*?)(<section class="fv-why-grid)', html)
if match:
    new_html = html[:match.start(1)] + subtle_bento + '\n     ' + html[match.end(1):]
    with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Reverted to ultra-subtle minimalist shadcn style.")
else:
    print("Regex failed to find dark mode block.")
