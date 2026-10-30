from pathlib import Path
from html import escape
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).parent
ASSETS = ROOT / 'assets'
PALETTES = {
    'dark': dict(bg='#161513', panel='#1F1D1A', text='#ECE7DD', muted='#A39D91', accent='#D4895F'),
    'light': dict(bg='#F7F4EE', panel='#EFE9DF', text='#1F1D1A', muted='#5C574E', accent='#9C4B26'),
}
MARQUEE = 'FULL STACK DEVELOPER IN OPLEIDING • WEBDESIGN • WEBSITES • WEBAPPLICATIES • SOFTWARE OP MAAT • AI AUTOMATISERING • '
MARQUEE_PERIOD = 1440

def text(x, y, content, size=20, color='text', weight='400', mono=False, extra=''):
    family = 'IBM Plex Mono, Consolas, monospace' if mono else 'Schibsted Grotesk, Arial, sans-serif'
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{{{color}}}" {extra}>{escape(content)}</text>'

def svg(theme, name, height, body, description):
    colors = PALETTES[theme]
    # Only named palette tokens are replaced, leaving CSS braces intact.
    for k, v in colors.items():
        body = body.replace('{'+k+'}', v)
    result = f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc"><title id="title">{escape(description)}</title><desc id="desc">Original Wesley Dev &amp; Tech artwork in warm copper. Animation is disabled when reduced motion is requested.</desc>{body}</svg>\n'
    ET.fromstring(result)
    (ASSETS / f'{name}-{theme}.svg').write_text(result)

for theme in PALETTES:
    hero = '''
<style>
 .pulse{animation:pulse 2.4s ease-in-out infinite}.cursor{animation:cursor 1.3s steps(1) infinite}.packet{stroke-dasharray:12 160;animation:flow 9s linear infinite}.ticker{animation:ticker 30s linear infinite}
 .scene-a{animation:scene-a 18s infinite}.scene-b{opacity:0;animation:scene-b 18s infinite}.scene-c{opacity:0;animation:scene-c 18s infinite}.meter{transform-origin:22px 228px;animation:meter 6s ease-in-out infinite}
 @keyframes pulse{50%{opacity:.35}} @keyframes cursor{50%{opacity:0}} @keyframes flow{to{stroke-dashoffset:-688}} @keyframes ticker{to{transform:translateX(-1440px)}}
 @keyframes scene-a{0%,28%,100%{opacity:1}33%,94%{opacity:0}}@keyframes scene-b{0%,28%,66%,100%{opacity:0}34%,60%{opacity:1}}@keyframes scene-c{0%,60%,100%{opacity:0}67%,94%{opacity:1}}
 @keyframes meter{0%,100%{transform:scaleX(.2)}80%{transform:scaleX(1)}}
 @media(prefers-reduced-motion:reduce){.pulse,.cursor,.packet,.ticker,.scene-a,.scene-b,.scene-c,.meter{animation:none}.scene-a{opacity:1}.scene-b,.scene-c{opacity:0}}
</style>
<defs><clipPath id="ticker-clip"><rect x="40" y="382" width="1120" height="52" rx="4"/></clipPath></defs>
<rect width="1200" height="570" rx="18" fill="{bg}"/>
<rect x="1" y="1" width="1198" height="568" rx="18" fill="none" stroke="{muted}" stroke-opacity=".25"/>
<path d="M40 68H1160" stroke="{muted}" stroke-opacity=".3"/>
<rect x="40" y="24" width="32" height="28" rx="4" fill="{accent}"/>
'''+text(44,44,'WB',16,'bg','700',True)+text(86,44,'WESLEY DEV & TECH',16,'muted','400',True)+text(900,44,'BELGIUM / LEARNING BY BUILDING',12,'muted','400',True)+'''
<circle cx="52" cy="107" r="4" fill="{accent}" class="pulse"/>
'''+text(66,112,'FULL STACK & AI AUTOMATION / IN TRAINING',15,'accent','400',True)+text(40,208,'WESLEY',94,'text','700',False,'letter-spacing="-5"')+text(40,302,'DEV & TECH.',94,'accent','700',False,'letter-spacing="-5"')+text(44,347,'Business understanding. Built into code.',24,'muted')+'''
<g transform="translate(752 100)">
 <rect width="408" height="251" rx="12" fill="{panel}" stroke="{muted}" stroke-opacity=".28"/>
 <path d="M0 42H408" stroke="{muted}" stroke-opacity=".25"/>
 <circle cx="22" cy="21" r="4" fill="{accent}"/><circle cx="38" cy="21" r="4" fill="{muted}" opacity=".5"/><circle cx="54" cy="21" r="4" fill="{muted}" opacity=".3"/>
'''+text(80,26,'wesley / learning lab',13,'muted','400',True)+'''
<g class="scene-a">
'''+text(22,78,'// 01 / WEB DEVELOPMENT',15,'accent','400',True)+text(22,112,'const developer = {',17,'text','400',True)+text(40,144,'name: "Wesley",',17,'text','400',True)+text(40,176,'mindset: "keep learning"',17,'text','400',True)+text(22,211,'};',18,'accent','400',True)+'''
</g><g class="scene-b">
'''+text(22,78,'-- 02 / MYSQL & DATA',15,'accent','400',True)+text(22,112,'SELECT project, skills',17,'text','400',True)+text(22,144,'FROM learning_projects',17,'text','400',True)+text(22,176,'WHERE curiosity = TRUE;',17,'text','400',True)+text(22,211,'-- learning by querying',14,'muted','400',True)+'''
</g><g class="scene-c">
'''+text(22,78,'// 03 / AI AUTOMATION',15,'accent','400',True)+text(22,112,'understand(process);',17,'text','400',True)+text(22,144,'explore(automation);',17,'text','400',True)+text(22,176,'build(test(improve()));',17,'text','400',True)+text(22,211,'// one useful step at a time',14,'muted','400',True)+'''
</g><rect x="22" y="228" width="360" height="2" rx="1" fill="{accent}" class="meter"/>
<rect x="377" y="20" width="7" height="13" fill="{accent}" class="cursor"/>
</g>
<rect x="40" y="382" width="1120" height="52" rx="4" fill="{panel}"/>
<g clip-path="url(#ticker-clip)"><g class="ticker">
'''+''.join(text(64+i*MARQUEE_PERIOD,414,MARQUEE,18,'accent','400',True,'textLength="1416" lengthAdjust="spacingAndGlyphs"') for i in range(3))+'''
</g></g>
<path d="M190 505H1010" fill="none" stroke="{muted}" stroke-opacity=".3" stroke-width="2"/>
<path d="M190 505H1010" fill="none" stroke="{accent}" stroke-width="3" class="packet"/>
'''
    for x, n, label, sub in [(64,'01','FINANCE','Where I started'),(466,'02','DEVELOPMENT','What I am learning'),(868,'03','USEFUL SOFTWARE','What I want to build')]:
        hero += f'<rect x="{x}" y="471" width="268" height="74" rx="6" fill="{{bg}}" stroke="{{muted}}" stroke-opacity=".3"/>'
        hero += text(x+14,498,n,13,'accent','400',True)+text(x+49,498,label,15,'text','700',True)+text(x+49,523,sub,14,'muted')
    svg(theme,'header',570,hero,'Wesley Dev & Tech. Full Stack & AI Automation Developer in training. From finance to useful software.')

    divider='''<style>.signal{animation:signal 8s linear infinite;stroke-dasharray:50 1150}@keyframes signal{to{stroke-dashoffset:-1200}}@media(prefers-reduced-motion:reduce){.signal{animation:none}}</style><path d="M0 17H1200" stroke="{muted}" stroke-opacity=".25"/><path d="M0 17H1200" stroke="{accent}" stroke-width="2" class="signal"/><rect x="562" y="0" width="76" height="34" rx="4" fill="{bg}"/>'''+text(577,24,'</>',22,'accent','400',True)
    svg(theme,'divider',34,divider,'Wesley Dev & Tech animated code divider')

    footer='''<style>.arrow{animation:nudge 3s ease-in-out infinite}@keyframes nudge{50%{transform:translateX(8px)}}@media(prefers-reduced-motion:reduce){.arrow{animation:none}}</style><rect width="1200" height="194" rx="12" fill="{panel}"/><path d="M1 20V174" stroke="{accent}" stroke-width="4"/>'''+text(38,42,'NEXT CHAPTER / JUNIOR DEVELOPMENT',15,'accent','400',True)+text(36,104,"Let's build something useful.",47,'text','700')+text(40,151,'Explore my portfolio. See my work. Start a conversation.',22,'muted')+'''<g class="arrow"><path d="M1070 99H1138m-21-21 21 21-21 21" stroke="{accent}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>'''
    svg(theme,'footer',194,footer,"Let's build something useful. Explore my portfolio and get in touch.")

    strengths='''<rect width="1200" height="220" rx="10" fill="{bg}"/>'''
    for x, number, title, lines in [
        (0,'01','BUSINESS CONTEXT',['Invoices. Reporting. Real workflows.','Experience I bring into development.']),
        (410,'02','DATA THINKING',['MySQL. Relationships. Normalization.','Making sense of how data fits together.']),
        (820,'03','PRACTICAL OUTPUT',['A website. A calculation. A PDF.','Projects with something you can try.'])]:
        strengths += f'<rect x="{x+1}" y="1" width="378" height="218" rx="8" fill="{{panel}}" stroke="{{muted}}" stroke-opacity=".2"/>'
        strengths += text(x+22,45,number,15,'accent','400',True)+text(x+22,91,title,20,'text','700')+text(x+22,137,lines[0],16,'muted')+text(x+22,169,lines[1],16,'muted')
    svg(theme,'strengths',220,strengths,'Business context, data thinking and practical output. The strengths I am bringing to development.')

    stack = '<rect width="1200" height="204" rx="10" fill="{bg}"/>'
    for i,(glyph,label) in enumerate([('&lt;/&gt;','HTML'),('{ }','CSS'),('JS','JavaScript'),('SQL','MySQL'),('git','Git & GitHub')]):
        x = i * 244
        stack += f'<rect x="{x+1}" y="1" width="222" height="144" rx="8" fill="{{panel}}" stroke="{{muted}}" stroke-opacity=".25"/>'
        stack += text(x+22,63,glyph.replace('&lt;','<').replace('&gt;','>'),32,'accent','700',True)
        stack += text(x+22,117,label,23,'text','700')
    stack += text(12,188,'ALSO EXPLORING',14,'accent','400',True)+text(204,188,'TypeScript  /  Bootstrap  /  Tailwind  /  APIs  /  AI automation',19,'muted')
    svg(theme,'toolbox',204,stack,'My learning toolbox: HTML, CSS, JavaScript, MySQL, Git and GitHub. Also exploring TypeScript, Bootstrap, Tailwind, APIs and AI automation.')

    # An original animated lab panel, inspired by the portfolio's focus areas.
    lab='''<style>.trace{stroke-dasharray:16 124;animation:trace 6s linear infinite}.typing{animation:blink 1.5s steps(1) infinite}.float{animation:float 5s ease-in-out infinite}@keyframes trace{to{stroke-dashoffset:-560}}@keyframes blink{50%{opacity:0}}@keyframes float{50%{transform:translateY(-5px)}}@media(prefers-reduced-motion:reduce){.trace,.typing,.float{animation:none}}</style><rect width="1200" height="300" rx="12" fill="{panel}"/><path d="M40 55H1160" stroke="{muted}" stroke-opacity=".25"/>'''+text(24,34,'THE LEARNING LAB',16,'accent','400',True)+text(850,34,'EXPERIMENT / BUILD / REPEAT',14,'muted','400',True)
    lab+='''<path d="M110 166H1090" stroke="{muted}" stroke-opacity=".3" stroke-width="2"/><path d="M110 166H1090" stroke="{accent}" stroke-width="3" class="trace"/>'''
    for x,label,subtitle,icon in [
        (40,'WEB INTERFACES','Structure meets interaction.','<rect x="24" y="22" width="82" height="56" rx="5"/><path d="M24 36H106M49 50l-9 9 9 9M81 50l9 9-9 9M70 48l-9 22"/>'),
        (440,'DATA & LOGIC','Relationships before queries.','<ellipse cx="65" cy="30" rx="36" ry="11"/><path d="M29 30v44c0 15 72 15 72 0V30M29 52c0 15 72 15 72 0"/>'),
        (840,'AI AUTOMATION','Exploring smarter workflows.','<rect x="45" y="15" width="40" height="28" rx="4"/><rect x="14" y="66" width="40" height="28" rx="4"/><rect x="76" y="66" width="40" height="28" rx="4"/><path d="M65 43v12H34v11M65 55h31v11"/>')]:
        lab+=f'<rect x="{x}" y="77" width="320" height="197" rx="8" fill="{{bg}}" stroke="{{muted}}" stroke-opacity=".28"/><g transform="translate({x+94} 88)" class="float"><g fill="none" stroke="{{accent}}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">{icon}</g></g>'
        lab+=text(x+160,225,label,20,'text','700',False,'text-anchor="middle"')+text(x+160,253,subtitle,16,'muted','400',False,'text-anchor="middle"')
    svg(theme,'learning-lab',300,lab,'My learning lab: web interfaces, data and logic, and AI automation. Illustrated development interests, not a production system.')

# Theme-neutral, copper buttons replace all plain-text links in the README.
BUTTONS = {
    'portfolio': ('PORTFOLIO', '<rect x="18" y="13" width="24" height="20" rx="3"/><path d="M18 19H42M23 16h1m3 0h1M25 25l-3 3 3 3m10-6 3 3-3 3"/>'),
    'linkedin': ('LINKEDIN', '<rect x="19" y="12" width="22" height="22" rx="3"/><path d="M25 22v8m0-13v1m6 12v-8m0 3c0-5 6-5 6 0v5"/>'),
    'about': ('ABOUT ME', '<circle cx="30" cy="17" r="5"/><path d="M19 34c0-14 22-14 22 0"/>'),
    'projects': ('PROJECTS', '<rect x="19" y="12" width="22" height="23" rx="3"/><path d="M25 12v23M29 18h7m-7 6h7m-7 6h4"/>'),
    'toolbox': ('TOOLBOX', '<rect x="17" y="19" width="26" height="16" rx="3"/><path d="M24 19v-6h12v6M17 25h26m-13-3v6"/>'),
    'contact': ('CONTACT', '<rect x="17" y="14" width="26" height="19" rx="3"/><path d="M18 16l12 10 12-10"/>'),
    'demo': ('LIVE DEMO', '<circle cx="29" cy="23" r="11"/><path d="M18 23h22M29 12c-8 7-8 15 0 22m0-22c8 7 8 15 0 22"/>'),
    'code': ('SOURCE CODE', '<path d="M25 14l-9 9 9 9m11-18 9 9-9 9m-3-21-5 24"/>'),
    'all-projects': ('ALL REPOSITORIES', '<path d="M18 16h11l3 4h20v17H18zM22 11h24v9"/>'),
    'top': ('BACK TO TOP', '<path d="M20 15h22M31 36V21m-9 8 9-9 9 9"/>'),
}
for key,(label,icon) in BUTTONS.items():
    width=222 if key=='all-projects' else 190
    button=f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="46" viewBox="0 0 {width} 46" role="img" aria-label="{label}"><rect x="1" y="1" width="{width-2}" height="44" rx="7" fill="#D4895F"/><g fill="none" stroke="#161513" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{icon}</g><text x="59" y="28" font-family="Arial, sans-serif" font-size="13" font-weight="700" letter-spacing=".6" fill="#161513">{label}</text></svg>\n'
    ET.fromstring(button)
    (ASSETS/f'button-{key}.svg').write_text(button)

print('Generated 12 theme-aware SVG assets and 10 original icon buttons.')
