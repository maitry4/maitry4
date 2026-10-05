BG='#FAFAF8'; INK='#111111'; GR='#6B6B66'; LN='#D6D6D0'; SF='#EFEFEB'; AC='#C2410C'
SANS="'Helvetica Neue',Helvetica,Arial,sans-serif"
MONO="ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
def esc(s): return s.replace('&','&amp;').replace('<','&lt;')
def T(x,y,s,size=12,w=400,fill=INK,mono=False,anchor='start',ls=0):
    f=MONO if mono else SANS
    return f'<text x="{x}" y="{y}" font-family="{f}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{esc(s)}</text>'
def R(x,y,w,h,fill='none',stroke=LN,dash=None,sw=1):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def L(x1,y1,x2,y2,stroke=LN,dash=None,sw=1):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def A(x1,y1,x2,y2,c='ink'):
    col={'ink':INK,'ac':AC,'gr':GR}[c]
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="1.25" marker-end="url(#a{c})"/>'
def P(d,stroke=INK,dash=None,marker=None,sw=1.25):
    dd=f' stroke-dasharray="{dash}"' if dash else ''
    m=f' marker-end="url(#a{marker})"' if marker else ''
    return f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}"{dd}{m}/>'
def wrap(name,w,h,title,body):
    mk=''.join(f'<marker id="a{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1 L9 5 L0 9 z" fill="{c}"/></marker>' for k,c in [('ink',INK),('ac',AC),('gr',GR)])
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}"><title>{esc(title)}</title><defs>{mk}</defs><rect x=".5" y=".5" width="{w-1}" height="{h-1}" fill="{BG}" stroke="{INK}" stroke-opacity=".9"/>'+''.join(body)+'</svg>'
    open(f'assets/{name}.svg','w').write(s)
def header(left,right,w=880):
    return [T(40,42,left,12,700,INK,True,ls=2.5),T(w-40,42,right,10.5,400,GR,True,'end',1.2),L(40,60,w-40,60)]

# ---------- HERO ----------
b=header('MAITRY PARIKH','FIG. 00 / PRODUCT BLUEPRINT')
b+=[T(40,102,'SOFTWARE ENGINEER / PRODUCT BUILDER',11,700,AC,True,ls=2),
 T(40,156,'I turn messy product problems',44,700,INK,ls=-1.2),
 f'<text x="40" y="208" font-family="{SANS}" font-size="44" font-weight="700" fill="{INK}" letter-spacing="-1.2">into simple, reliable software<tspan fill="{AC}">.</tspan></text>',
 T(40,242,'Backend · Mobile · AI Systems',16,400,GR),
 T(40,288,'FIG. 00 — FROM PROBLEM TO PRODUCT',10,400,GR,True,ls=1.5)]
y=302; h=92; bw=176; gp=32
items=[('A / INPUT','Messy problem','unclear, conflicting, costly'),('B / DECISION','Product decision','decide what not to build'),('C / SYSTEM','System','constraints shape it'),('D / OUTPUT','User experience','fast, simple, private')]
for i,(tg,ti,su) in enumerate(items):
    x=40+i*(bw+gp)
    if i==0: b.append(R(x,y,bw,h,'none',GR,'4 3'))
    elif i==1: b.append(R(x,y,bw,h,SF,LN))
    elif i==2: b.append(R(x,y,bw,h,'#FFFFFF',INK))
    else: b.append(R(x,y,bw,h,INK,INK))
    dark=i==3
    b+=[T(x+14,y+24,tg,9.5,400,'#BDBDB6' if dark else GR,True,ls=1.2),
        T(x+14,y+52,ti,14.5,700,'#FFFFFF' if dark else INK),
        T(x+14,y+72,su,10.5,400,'#D6D6D0' if dark else GR)]
    if i<3: b.append(A(x+bw+5,y+46,x+bw+gp-5,y+46))
b.append(P(f'M{40+120} {y+24} l8 -9 l6 13 l-14 2 l13 9 l8 -11 l6 7',GR,sw=1))
b+=[L(40,y+h+24,840,y+h+24,LN,'2 3'),T(40,y+h+44,'Messy in. Simple out. The complexity lives underneath.',10.5,400,GR,True)]
wrap('hero',880,y+h+62,'Maitry Parikh — Software Engineer and Product Builder. I turn messy product problems into simple, reliable software.',b)

# ---------- NOODLE ----------
b=header('01 / NOODLE','PRIVACY-FIRST · VOICE · MOBILE + BACKEND')
b+=[T(40,102,'A sarcastic voice companion',32,700,INK,ls=-0.8),
 f'<text x="40" y="142" font-family="{SANS}" font-size="32" font-weight="700" fill="{INK}" letter-spacing="-0.8">that forgets you on purpose<tspan fill="{AC}">.</tspan></text>',
 T(40,176,'Privacy was not a settings toggle. It was the first architectural constraint.',14.5,400,GR),
 T(40,214,'FIG. 01 — ONE TURN OF CONVERSATION',10,400,GR,True,ls=1.5)]
nodes=['USER','FLUTTER','WEBSOCKET','FASTAPI','GEMINI + TTS','RESPONSE','DISCARD']
nw=94; g=(800-7*nw)/6; ny=228; nh=52
xs=[40+i*(nw+g) for i in range(7)]
for i,n in enumerate(nodes):
    x=xs[i]
    if n=='DISCARD': b.append(R(x,ny,nw,nh,'none',AC,'4 3'))
    elif n=='FLUTTER': b.append(R(x,ny,nw,nh,SF,INK))
    else: b.append(R(x,ny,nw,nh,'#FFFFFF',INK))
    b.append(T(x+nw/2,ny+31,n,10,700,AC if n=='DISCARD' else INK,True,'middle',0.4))
    if i<6: b.append(A(x+nw+3,ny+26,xs[i+1]-3,ny+26,'ac' if i==5 else 'ink'))
def br(i,j,label,c=GR):
    x1=xs[i]; x2=xs[j]+nw
    return [P(f'M{x1} {ny+nh+8} v6 H{x2} v-6',c,sw=1),T((x1+x2)/2,ny+nh+32,label,9,400,c,True,'middle',0.8)]
b+=br(1,1,'ON DEVICE')+br(2,2,'LIVE STREAM')+br(3,4,'STATELESS SERVER')+br(6,6,'NOT STORED',AC)
b+=[L(40,ny+nh+54,840,ny+nh+54,LN,'2 3'),T(40,ny+nh+74,'Nothing outlives the turn: audio and text exist only while a response is in flight.',10.5,400,GR,True)]
wrap('noodle',880,ny+nh+92,'Noodle architecture: User, Flutter, WebSocket, FastAPI, Gemini and TTS, Response, then Discard.',b)

# ---------- RUNBAIT ----------
b=header('02 / RUNBAIT','AI QA AGENT · BACKEND ORCHESTRATION')
b+=[T(40,104,"Don't ask an LLM whether a PR looks okay.",32,700,INK,ls=-0.8),
 f'<text x="40" y="144" font-family="{SANS}" font-size="32" font-weight="700" fill="{INK}" letter-spacing="-0.8">Make the browser prove it<tspan fill="{AC}">.</tspan></text>',
 T(40,186,'FIG. 02 — FROM PULL REQUEST TO STRUCTURED VERDICT',10,400,GR,True,ls=1.5)]
st=[('PR diff','Actions trigger on PR','GITHUB'),('Understand repo','routes, components, flows','AI'),('Affected journeys','which paths did it touch?','AI'),('Generate flows','targeted browser steps','AI'),
    ('Run in Playwright','real browser, real run','BROWSER'),('Capture evidence','screenshots + console logs','BROWSER'),('Evaluate evidence','reasons over what happened','AI'),('Structured verdict','pass / fail + reasons','PYDANTIC')]
bh=84; ys=[204,334]
def chip(x,y,k):
    w=int(6*len(k)+14)
    if k=='AI': return R(x-w,y,w,15,'none',AC)+T(x-w/2,y+11,k,8.5,700,AC,True,'middle',1)
    if k=='BROWSER': return R(x-w,y,w,15,INK,INK)+T(x-w/2,y+11,k,8.5,700,'#FFFFFF',True,'middle',1)
    return R(x-w,y,w,15,'none',GR)+T(x-w/2,y+11,k,8.5,700,GR,True,'middle',1)
for i,(ti,su,k) in enumerate(st):
    r=i//4; c=i%4; x=40+c*(bw+gp); y=ys[r]
    fill=SF if k=='BROWSER' else '#FFFFFF'
    b+=[R(x,y,bw,bh,fill,INK),T(x+14,y+25,f'{i+1:02d}',9.5,400,GR,True),chip(x+bw-12,y+13,k),
        T(x+14,y+54,ti,13,700,INK),T(x+14,y+72,su,10,400,GR)]
    if c<3: b.append(A(x+bw+5,y+bh/2,x+bw+gp-5,y+bh/2))
xa=40+3*(bw+gp)+bw/2; xb=40+bw/2; ym=(ys[0]+bh+ys[1])/2
b.append(P(f'M{xa} {ys[0]+bh+2} V{ym} H{xb} V{ys[1]-5}',INK,marker='ink'))
py=ys[1]+bh+34
cols=[('AI decides what to test.','01 · PLAN'),('The browser determines what happened.','02 · OBSERVE'),('Evidence determines the verdict.','03 · DECIDE')]
for i,(t,s) in enumerate(cols):
    x=[40,270,600][i]; wd=[210,310,240][i]
    b+=[L(x,py,x+wd,py,AC if i==2 else INK,sw=2),T(x,py+24,t,12,700,INK),T(x,py+42,s,9.5,400,GR,True,ls=1.2)]
wrap('runbait',880,py+66,'RunBait pipeline: PR diff, understand repository, affected journeys, generate flows, run in Playwright, capture evidence, AI evaluates, structured verdict.',b)

# ---------- LAYERED ----------
b=header('03 / LAYERED','FLUTTER · OFFLINE · 100 LEVELS')
b+=[T(40,104,'Skip the expensive solver.',32,700,INK,ls=-0.8),
 f'<text x="40" y="144" font-family="{SANS}" font-size="32" font-weight="700" fill="{INK}" letter-spacing="-0.8">Constrain the generator instead<tspan fill="{AC}">.</tspan></text>',
 T(40,186,'FIG. 03A — ARCHITECTURE',10,400,GR,True,ls=1.5),T(440,186,'FIG. 03B — LEVEL GENERATOR',10,400,GR,True,ls=1.5)]
lay=[('PRESENTATION','Screens · Cubits · Widgets'),('DOMAIN','Level model · Move rules · Generator'),('DATA','Hive · Firebase Analytics')]
for i,(t,s) in enumerate(lay):
    y=202+i*92
    b+=[R(40,y,340,70,SF if i==1 else '#FFFFFF',INK),T(56,y+30,t,12,700,INK,True,ls=1.5),T(56,y+52,s,11,400,GR)]
    if i<2: b.append(A(210,y+73,210,y+89))
gen=[('CONTROLLED SCRAMBLING','randomness with a leash'),('VALID-MOVE CONSTRAINTS','only legal transitions'),('DEADLOCK DETECTION','reject dead ends'),('HOMOGENEITY SCORING','measure quality, not just validity')]
for i,(t,s) in enumerate(gen):
    y=202+i*54
    b+=[R(440,y,400,46,'#FFFFFF',INK),T(456,y+28,str(i+1),11,700,AC,True),T(480,y+20,t,11.5,700,INK,True,ls=0.6),T(480,y+36,s,10.5,400,GR)]
    if i<3: b.append(A(460,y+47,460,y+53,'gr'))
oy=202+4*54
b+=[R(440,oy,400,38,INK,INK),T(456,oy+24,'→ LEVEL N / 100 · fully offline',11,700,'#FFFFFF',True,ls=0.5)]
b+=[L(40,oy+62,840,oy+62,LN,'2 3'),T(40,oy+82,'TRADEOFF  Heuristic checks instead of a full solver: cheaper generation, no optimality proof.',10.5,400,GR,True)]
wrap('layered',880,oy+100,'Layered: Presentation, Domain, Data architecture and a four-step level generator that avoids an expensive solver.',b)

# ---------- THINKING ----------
b=[T(40,40,'ENGINEERING LOOP',10.5,700,INK,True,ls=2.5),T(840,40,'FIG. 04',10.5,400,GR,True,'end',1.2),L(40,56,840,56)]
steps=[('PROBLEM',''),('SIMPLIFY',''),('FIND THE|CONSTRAINT',''),('DESIGN THE|SYSTEM',''),('SHIP',''),('OBSERVE',''),('ITERATE','')]
nw=96; g=(800-7*nw)/6; ny=84; nh=60
xs=[40+i*(nw+g) for i in range(7)]
for i,(t,_) in enumerate(steps):
    x=xs[i]
    fill=INK if t=='SHIP' else ('#FFFFFF')
    stroke=AC if t.startswith('FIND') else INK
    b+=[R(x,ny,nw,nh,fill,stroke),T(x,ny-8,f'{i+1:02d}',9.5,400,GR,True)]
    tc='#FFFFFF' if t=='SHIP' else (AC if t.startswith('FIND') else INK)
    ls=t.split('|')
    if len(ls)==1: b.append(T(x+nw/2,ny+35,ls[0],10,700,tc,True,'middle',0.4))
    else: b+=[T(x+nw/2,ny+28,ls[0],10,700,tc,True,'middle',0.4),T(x+nw/2,ny+43,ls[1],10,700,tc,True,'middle',0.4)]
    if i<6: b.append(A(x+nw+3,ny+nh/2,xs[i+1]-3,ny+nh/2))
b.append(P(f'M{xs[6]+nw/2} {ny+nh+3} V{ny+nh+30} H{xs[0]+nw/2} V{ny+nh+5}',GR,'3 3',marker='gr'))
b.append(T(440,ny+nh+46,'repeat',9.5,400,GR,True,'middle',1.2))
wrap('thinking',880,ny+nh+66,'How I work: problem, simplify, find the constraint, design the system, ship, observe, iterate.',b)
