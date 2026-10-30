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
 .pulse{animation:pulse 2.4s ease-in-out infinite}.cursor{animation:cursor 1.3s steps(1) infinite}.packet{stroke-dasharray:12 160;animation:flow 9s linear infinite}.ticker{animation:ticker 26s linear infinite}
 @keyframes pulse{50%{opacity:.35}} @keyframes cursor{50%{opacity:0}} @keyframes flow{to{stroke-dashoffset:-688}} @keyframes ticker{to{transform:translateX(-1110px)}}
 @media(prefers-reduced-motion:reduce){.pulse,.cursor,.packet,.ticker{animation:none}}
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
'''+text(80,26,'developer.config.ts',13,'muted','400',True)+text(22,78,'const wesley = {',18,'accent','400',True)+text(40,112,'background: "finance",',17,'text','400',True)+text(40,144,'direction: "development",',17,'text','400',True)+text(40,176,'mindset: "keep learning"',17,'text','400',True)+text(22,211,'};',18,'accent','400',True)+'''
<rect x="46" y="194" width="9" height="21" fill="{accent}" class="cursor"/>
</g>
<rect x="40" y="382" width="1120" height="52" rx="4" fill="{panel}"/>
<g clip-path="url(#ticker-clip)"><g class="ticker">
'''+''.join(text(64+i*1110,414,'WEB DEVELOPMENT  /  DATABASES  /  AI AUTOMATION  /  BUSINESS LOGIC  /  KEEP BUILDING  /',18,'accent','400',True) for i in range(3))+'''
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

print('Generated 10 theme-aware SVG assets.')
