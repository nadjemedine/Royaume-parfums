import re
import os

file_path = 'parfum-store.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update <main> class
content = content.replace('<main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">', '<main class="flex-grow w-full pb-6">')

# 2. Update Hero to be full width without margins
hero_old = '''            <div class="relative w-full h-[60vh] sm:h-[70vh] rounded-2xl overflow-hidden mb-10 border border-brand-accent flex items-center justify-center">
                <!-- Using an elegant perfume image from Unsplash -->
                <img src="https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=1200&q=80" alt="Parfums" class="absolute inset-0 w-full h-full object-cover">'''

hero_new = '''            <div class="relative w-full h-[60vh] sm:h-[70vh] lg:h-[80vh] flex items-center justify-center">
                <img src="video-hero.png" alt="Parfums" class="absolute inset-0 w-full h-full object-cover shadow-sm">'''
if hero_old in content:
    content = content.replace(hero_old, hero_new)

# Add container internally in tab-home after hero
# Find <!-- مقدمة ترحيبية راقية -->
intro_text = '''            <!-- مقدمة ترحيبية راقية -->'''
intro_text_new = '''            <div class="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 pt-10">
            <!-- مقدمة ترحيبية راقية -->'''
if intro_text in content:
    content = content.replace(intro_text, intro_text_new)

# Close the new container div after season cards
season_end = '''        </section>

        <!-- ================= الجزء الأول: المتجر (SHOP) ================= -->'''
season_end_new = '''            </div>
        </section>

        <!-- ================= الجزء الأول: المتجر (SHOP) ================= -->'''
if season_end in content:
    content = content.replace(season_end, season_end_new)


# 3. Wrapping other tabs in the max-w-7xl wrapper
# They are sections, so we can just add classes to the sections
content = content.replace('<section id="tab-shop" class="tab-content hidden">', '<section id="tab-shop" class="tab-content hidden max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8">')
content = content.replace('<section id="tab-favorites" class="tab-content hidden">', '<section id="tab-favorites" class="tab-content hidden max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8">')
content = content.replace('<section id="tab-cart" class="tab-content hidden">', '<section id="tab-cart" class="tab-content hidden max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8">')

# 4. Images update
content = content.replace("'https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=600&q=80'", "'image1.jpg'")
content = content.replace("'https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?auto=format&fit=crop&w=600&q=80'", "'image11.jpg'")
content = content.replace("'https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80'", "'image2.jpg'") # Autumn image is here twice (in season card and database). No, wait. My previous script made season card use the same! So the season card and product will both be updated.
content = content.replace("'https://images.unsplash.com/photo-1588405748373-122b2321bc31?auto=format&fit=crop&w=600&q=80'", "'image22.jpg'")
content = content.replace("'https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=600&q=80'", "'image3.jpg'")
content = content.replace("'https://images.unsplash.com/photo-1592945409244-b3fbafd7f539?auto=format&fit=crop&w=600&q=80'", "'image33.jpg'")
content = content.replace("'https://images.unsplash.com/photo-1547887537-6158d64c35b3?auto=format&fit=crop&w=600&q=80'", "'image4.jpg'")
content = content.replace("'https://images.unsplash.com/photo-1595425970377-c9703cf48b6d?auto=format&fit=crop&w=600&q=80'", "'image44.jpg'")


# 5. Footer addition
footer_code = """
    <!-- ================= الفوتر الاحترافي ================= -->
    <footer class="bg-brand-dark text-white pt-16 pb-24 px-4 sm:px-6 lg:px-8 border-t border-brand-accent">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-10">
            <div>
                <h3 class="text-xl font-serif tracking-[0.2em] mb-4">LUXYA PARFUM</h3>
                <p class="text-xs text-brand-gray leading-relaxed max-w-sm">Découvrez l'art de la parfumerie française à travers nos collections saisonnières. Des fragrances uniques qui racontent votre histoire.</p>
            </div>
            <div>
                <h4 class="text-xs tracking-widest uppercase font-semibold mb-4 text-brand-gold">Service Client</h4>
                <ul class="space-y-2 text-xs text-brand-gray">
                    <li><a href="#" class="hover:text-white transition-colors">Livraison 58 Wilayas</a></li>
                    <li><a href="#" class="hover:text-white transition-colors">Paiement à la livraison</a></li>
                    <li><a href="#" class="hover:text-white transition-colors">Contactez-nous</a></li>
                    <li><a href="#" class="hover:text-white transition-colors">FAQ</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-xs tracking-widest uppercase font-semibold mb-4 text-brand-gold">Nous Suivre</h4>
                <div class="flex gap-4">
                    <a href="#" class="w-8 h-8 rounded-full border border-brand-gray flex items-center justify-center hover:bg-white hover:text-brand-dark transition-colors"><span class="text-xs">IG</span></a>
                    <a href="#" class="w-8 h-8 rounded-full border border-brand-gray flex items-center justify-center hover:bg-white hover:text-brand-dark transition-colors"><span class="text-xs">FB</span></a>
                    <a href="#" class="w-8 h-8 rounded-full border border-brand-gray flex items-center justify-center hover:bg-white hover:text-brand-dark transition-colors"><span class="text-xs">TT</span></a>
                </div>
            </div>
        </div>
        <div class="max-w-7xl mx-auto mt-12 pt-6 border-t border-brand-gray/30 text-center text-[10px] text-brand-gray uppercase tracking-widest">
            &copy; 2026 LUXYA PARFUM. TOUS DROITS RÉSERVÉS.
        </div>
    </footer>
"""

content = content.replace("    </main>", "    </main>\n" + footer_code)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates to parfum-store.html complete.")
