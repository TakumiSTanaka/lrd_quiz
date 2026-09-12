#!/usr/bin/env python3
from pathlib import Path
import csv, sys
root=Path(__file__).resolve().parents[1]
def read(name):
    with (root/'data'/name).open(encoding='utf-8-sig', newline='') as f:return list(csv.DictReader(f))
papers=read('papers.csv'); figs=read('figures.csv')
errors=[]; warnings=[]
ids=[p['paper_id'].strip() for p in papers]
if len(ids)!=len(set(ids)): errors.append('papers.csv: duplicate paper_id')
fids=[f['figure_id'].strip() for f in figs]
if len(fids)!=len(set(fids)): errors.append('figures.csv: duplicate figure_id')
ps=set(ids)
for i,f in enumerate(figs, start=2):
    if f['paper_id'].strip() not in ps: errors.append(f'figures.csv line {i}: unknown paper_id {f["paper_id"]!r}')
    local=f.get('image_path','').strip(); remote=f.get('remote_image_url','').strip(); enabled=f.get('enabled','1').strip().lower() not in {'0','false','no'}
    if enabled and not (local or remote): errors.append(f'figures.csv line {i}: enabled figure has no image_path or remote_image_url')
    if local and not (root/local).exists(): warnings.append(f'figures.csv line {i}: local image not found: {local}')
for msg in warnings: print('WARNING:',msg)
for msg in errors: print('ERROR:',msg)
print(f'papers={len(papers)} figures={len(figs)} errors={len(errors)} warnings={len(warnings)}')
sys.exit(1 if errors else 0)
