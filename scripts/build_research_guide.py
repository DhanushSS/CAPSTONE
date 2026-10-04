from pathlib import Path
from html import escape
import json, re
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/research/VerdictTrace_Research_Gap_Evidence.pdf'
META = json.loads((ROOT/'research/paper-index.json').read_text())
EXTRA = json.loads((ROOT/'research/expanded-context.json').read_text())
META.append(dict(
    id='P13', short='PES evidence-integrity paper',
    title='Validity of Forensic Evidence using Hash Function',
    authors='Pradeep K C, Rajashree Soman and Prasad Honnavalli',
    venue='IEEE ICCES 2020, pp. 823-826. DOI: 10.1109/ICCES48766.2020.9138061.',
    kind='PES C-ISFCR / author-posted abstract only',
    quote='They are used to verify whether the evidence has been subject to some unauthorized manipulation.',
    location='Author-posted abstract on Rajashree Soman\'s Academia.edu profile, under this paper title; middle sentences. Full paper not reviewed.',
    links=[('IEEE paper record','https://ieeexplore.ieee.org/document/9138061'),
           ('Author-posted abstract','https://jainuniversity.academia.edu/RajashreeSoman'),
           ('PES C-ISFCR listing','https://www.isfcr.pes.edu/research')]))

extra = {p['id']:p for p in EXTRA}
papers = [{**p, **extra[p['id']]} for p in META]
assert len(papers)==13
for p in papers:
    assert len(p['quote'].split()) <= 25, p['id']
    assert p['context'].count('[[')==p['context'].count(']]')==1

NAVY='#20345A'; BLUE='#0033CC'; TEAL='#087E8B'; GRAY='#53627A'
GOLD='#FFF0A8'; PALE='#EDF4FC'; LINE='#CAD7E6'; LIGHT='#F6F8FB'
W,H=A4; M=47; CW=W-2*M
c=canvas.Canvas(str(OUT),pagesize=A4)
c.setTitle('VerdictTrace - Research Context, Gaps and Proposed Contributions')
c.setAuthor('Prepared for Batch 51, PES University')
c.setSubject('Paragraph-length source summaries, short verified excerpts, research gaps, proposed implementation and validation')
page=0
layout=[]

def para(text,y,size=10.6,leading=14.4,color=NAVY,bold=False,width=CW,x=M):
    style=ParagraphStyle('body',fontName='Helvetica-Bold' if bold else 'Helvetica',fontSize=size,leading=leading,textColor=HexColor(color))
    p=Paragraph(text,style);_,h=p.wrap(width,1000)
    p.drawOn(c,x,y-h)
    return y-h

def highlight(text):
    return escape(text).replace('[[',f'<font backColor="{GOLD}"><b>').replace(']]','</b></font>')

def linked(label,url):
    return f'<link href="{escape(url,quote=True)}" color="{BLUE}"><u>{escape(label)}</u></link>'

def line(y):
    c.setStrokeColor(HexColor(LINE));c.setLineWidth(.7);c.line(M,y,W-M,y)

def newpage(label):
    global page
    if page:c.showPage()
    page+=1
    c.setFillColor(HexColor(TEAL));c.rect(0,H-9,W,9,fill=1,stroke=0)
    para('VERDICTTRACE / BATCH 51',H-28,8.7,10.5,TEAL,True)
    para(escape(label),H-28,8.6,10.5,GRAY,width=260,x=W-M-260)
    line(48)
    para('Research evidence guide - expanded edition | 3 October 2026',35,8.1,10.5,GRAY)
    c.setFillColor(HexColor(GRAY));c.setFont('Helvetica',8.6);c.drawRightString(W-M,25,str(page))
    return H-65

def section(label,body,y,color=TEAL):
    y=para(escape(label),y,10.6,14,color,True)-5
    return para(escape(body),y)-11

def box(text,y,bg=PALE,size=10.8,leading=14.8,bold=False):
    style=ParagraphStyle('box',fontName='Helvetica-Bold' if bold else 'Helvetica',fontSize=size,leading=leading,textColor=HexColor(NAVY))
    p=Paragraph(text,style);_,h=p.wrap(CW-26,1000)
    c.setFillColor(HexColor(bg));c.rect(M,y-h-20,CW,h+20,fill=1,stroke=0)
    p.drawOn(c,M+13,y-h-10)
    return y-h-30

def finish(y,identifier):
    layout.append({'page':page,'id':identifier,'last_content_y':round(y,2)})
    assert y>=64,(identifier,y)

y=newpage('Purpose and reading guide')
c.bookmarkPage('INTRO');c.addOutlineEntry('How to use this guide','INTRO',level=0)
y=para('Research context,<br/>gaps and proposed contributions',y,27,32,BLUE,True)-18
y=para('VerdictTrace',y,19,24,NAVY,True)-9
y=para('Thirteen papers connected to the project through highlighted evidence, explicit research questions and testable implementation plans.',y,12.3,18)-24
y=box('<b>Proposal-stage language throughout.</b> Every VerdictTrace mechanism and benefit described here is planned. An identified gap becomes a contribution only after implementation and comparative evaluation.',y)
y=section('How each paper is presented',
    'Each entry contains a paragraph-length summary of the relevant source context, a short exact excerpt, its page or section, the proposed research gap, how VerdictTrace plans to address it, and the evidence needed to support that claim.',y)
y=section('What the highlighting means',
    'Yellow text within a context paragraph marks the key point in our own wording. The separate yellow quotation box contains a short verbatim excerpt. The context paragraphs are summaries, not reproduced source paragraphs. Source links let you read the surrounding original text.',y)
y=section('How to interpret the gaps',
    'The gap label separates an explicit author-stated limitation from a proposed extension or new evaluation question. A paper being outside our project scope does not establish a weakness in that paper, and this curated set is not an exhaustive proof of novelty.',y)
y=section('Evidence access',
    'P01-P12 use inspected source passages from PDFs or primary publisher/conference text. P13 uses an author-posted abstract, with its publication and PES C-ISFCR connection independently checked. Its complete method and limitations still require full-text review.',y)
y=para('SOURCE CONTEXT  >  RESEARCH QUESTION  >  PROPOSED METHOD  >  TEST',y,9.7,14,BLUE,True)
finish(y,'INTRO')

y=newpage('Paper map and reading order')
c.bookmarkPage('MAP');c.addOutlineEntry('Paper map and reading order','MAP',level=0)
y=para('Find the evidence for each claim',y,23,28,BLUE,True)-16
rows=[['Paper / page','Primary role','Use in the proposal'],
 ['P01 / 3','Adversarial drift','Problem motivation + existing robust defense'],
 ['P02 / 4','CADE','Drift explanations already exist'],
 ['P03 / 5','CND-IDS - IEEE/ACM','Continual detection comparison'],
 ['P04 / 6','Block4Forensic - IEEE','Explicit evidence-availability limitation'],
 ['P05 / 7','ICTC language agent - IEEE','Close architecture + future collaboration'],
 ['P06 / 8','APCC distributed consensus','Closest overlap; discuss directly'],
 ['P07 / 9','Robust federated learning','Attack-dependent collaboration trade-offs'],
 ['P08 / 10','DYNOTEARS','Model assumptions + ablation design'],
 ['P09 / 11','Targeted forgetting','Model degradation versus evidence corruption'],
 ['P10 / 12','ROAD dataset','Realism, provenance and reproducibility'],
 ['P11 / 13','Secure audit logs','Tamper-evidence foundation and its limits'],
 ['P12 / 14','PBFT','Protocol assumptions and quorum discipline'],
 ['P13 / 15','PES C-ISFCR / IEEE ICCES','Integrity background; abstract only']]
style=ParagraphStyle('table',fontName='Helvetica',fontSize=9.6,leading=12.6,textColor=HexColor(NAVY))
cells=[[Paragraph(escape(v),style) for v in row] for row in rows]
t=Table(cells,colWidths=[73,161,CW-234]);t.setStyle(TableStyle([
 ('BACKGROUND',(0,0),(-1,0),HexColor(PALE)),('VALIGN',(0,0),(-1,-1),'TOP'),
 ('GRID',(0,0),(-1,-1),.5,HexColor(LINE)),
 ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
 ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
_,th=t.wrap(CW,1000);t.drawOn(c,M,y-th);y-=th+20
y=section('Suggested Review 1 reading order',
    'Read P01, P02 and P04 first, then P06 to understand the closest overlap. P03 and P04 provide two IEEE-related references; P05 and P13 add further IEEE-proceedings context. Paper IDs are local to this guide.',y)
finish(y,'MAP')

for p in papers:
    y=newpage(p['id']+' / '+p['kind'])
    c.bookmarkPage(p['id']);c.addOutlineEntry(p['id']+' - '+p['short'],p['id'],level=0)
    y=para(escape(p['title']),y,19,23,BLUE,True)-9
    y=para(escape(p['authors']),y,9.4,12.5,GRAY)-4
    y=para(escape(p['venue']),y,9.4,12.5,GRAY)-13
    y=para('Relevant paragraph context - paraphrased',y,10.6,14,TEAL,True)-5
    y=para(highlight(p['context']),y)-11
    y=para('Short exact excerpt to locate in the original',y,10.1,13,TEAL,True)-5
    y=box('&quot;'+escape(p['quote'])+'&quot;',y,GOLD,10.6,14.1,True)
    y=para(escape(p['location']),y,9,12.1,GRAY)-12
    y=para('Research gap / '+escape(p['gap_type']),y,10.1,13.2,TEAL,True)-5
    y=para(escape(p['gap']),y)-11
    y=section('How VerdictTrace proposes to fill it',p['fill'],y)
    y=section('What must be demonstrated',p['validation'],y)
    y=para('<b>Claim boundary:</b> '+escape(p['boundary']),y,9.6,13,GRAY)-11
    y=para('  |  '.join(linked(*link) for link in p['links']),y,9.7,13.2,BLUE)
    if p.get('extra'):
        y-=8
        y=para(escape(p['extra']),y,8.8,11.6,GRAY)
    finish(y,p['id'])

y=newpage('Cross-paper contribution and evaluation')
c.bookmarkPage('SYNTHESIS');c.addOutlineEntry('Cross-paper contribution and evaluation','SYNTHESIS',level=0)
y=para('What the proposed paper must establish',y,24,29,BLUE,True)-17
y=box('VerdictTrace will test whether independent CAN and V2X judgments, event-matched fleet corroboration and witnessed evidence improve attribution and forensic reliability under controlled drift, outages and compromised participation. A downstream agent will explain evidence without modifying canonical verdicts.',y,PALE,11.5,16)
items=[
 ('1. Attribution adds measurable value',
  'Compare independent detectors, bounded timing correlation and DYNOTEARS on matched benign and malicious changes. Include single-layer attacks, clock offsets and unrelated-event controls. Report false alarms, attack recall, cause accuracy, delay and calibrated uncertainty. [P01-P03, P08]'),
 ('2. Fleet corroboration has a precise guarantee',
  'Define membership, event matching, fault bounds and non-equivocation. Test false votes, replay, partitions, honest disagreement and insufficient quorum. Separate agreement safety, progress and semantic detection accuracy. [P07, P12]'),
 ('3. Evidence survives the declared failure conditions',
  'Compare local hashes, external receipts and independent encrypted copies. Measure recoverability and detectable manipulation separately; assess genuine outages and deletion before or after witnessing. State key and witness assumptions. [P04, P11, P13]'),
 ('4. The agent improves investigation without gaining authority',
  'Compare fixed reports with evidence-grounded agent reports. Score supported statements, citation validity, timeline accuracy, latency and human usefulness. Verify read-only permissions even when retrieved text attempts to redirect the agent. [P02, P05, P06]'),
 ('5. Datasets and measurements support reproduction',
  'Release cause manifests, data provenance, synchronization rules, scenario-disjoint splits and repeatable scripts. Include ordinary forgetting controls. Measure CPU, RAM, storage and latency on the machines assigned each role. [P09, P10]')]
for label,body in items:
    y=section(label,body,y)
y=para('<b>Publication claim:</b> demonstrate a reproducible improvement under stated conditions. The architecture, datasets and ablations should support that claim; the number of combined technologies is not the result.',y,10.6,14.4,BLUE)
finish(y,'SYNTHESIS')
c.save()
(ROOT/'build').mkdir(exist_ok=True)
(ROOT/'build/expanded-paper-index.json').write_text(json.dumps(papers,indent=2))
(ROOT/'build/expanded-layout.json').write_text(json.dumps(layout,indent=2))
print(json.dumps({'output':str(OUT),'pages':page,'papers':len(papers),'min_bottom_margin':min(i['last_content_y'] for i in layout)}))
