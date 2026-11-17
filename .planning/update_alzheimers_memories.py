import os
import re

product_files = ['neuromates-products.html', 'products.html', 'Products _ Neuro Mates.html']

old_ppl_pattern = re.compile(
    r'<div class="ppl"[^>]*>.*?</div>',
    re.DOTALL
)

new_ppl_html = '''<div class="ppl-cluster" aria-label="Personalised memory contacts">
  <div class="ppl-item">
    <div class="ppl-avatar-wrap">
      <img src="assets/images/avatar-1.png" alt="Daughter Ananya" class="ppl-avatar">
      <span class="ppl-role-dot" style="background:#2BB58A" title="Primary Caretaker"></span>
    </div>
    <span class="ppl-name">Ananya</span>
    <span class="ppl-relation">Daughter</span>
  </div>
  <div class="ppl-item">
    <div class="ppl-avatar-wrap">
      <img src="assets/images/avatar-2.png" alt="Grandson Aarav" class="ppl-avatar">
      <span class="ppl-role-dot" style="background:#4F9CF9" title="Family Member"></span>
    </div>
    <span class="ppl-name">Aarav</span>
    <span class="ppl-relation">Grandson</span>
  </div>
  <div class="ppl-item">
    <div class="ppl-avatar-wrap">
      <img src="assets/images/avatar-3.png" alt="Dr. Mehta" class="ppl-avatar">
      <span class="ppl-role-dot" style="background:#7C6CFF" title="Care Specialist"></span>
    </div>
    <span class="ppl-name">Dr. Mehta</span>
    <span class="ppl-relation">Care Specialist</span>
  </div>
  <div class="ppl-item ppl-upload">
    <div class="ppl-upload-circle" title="Upload photo of family member">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12h14"/></svg>
    </div>
    <span class="ppl-name">Add Photo</span>
    <span class="ppl-relation">Upload</span>
  </div>
</div>
<div class="mem-preview-box">
  <div class="mem-preview-head">
    <span class="mem-tag">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
      AI RECALL PROMPT PREVIEW
    </span>
    <span class="mem-badge-live">Active Care Sync</span>
  </div>
  <div class="mem-prompt-body">
    <p class="mem-q">"Who visited you yesterday afternoon with fresh flowers?"</p>
    <div class="mem-choices">
      <div class="mem-chip mem-correct"><span class="mem-tick">✓</span> Daughter Ananya</div>
      <div class="mem-chip">Neighbor Mrs. Patel</div>
    </div>
  </div>
  <div class="mem-preview-foot">
    <span>Auto-generated from uploaded family album</span>
    <span class="mem-stats">94% recall rate</span>
  </div>
</div>'''

css_to_add = '''
/* Alzheimer's Personalised Memories Enriched Styling */
.ppl-cluster { display: flex; align-items: center; gap: 16px; margin: 22px 0 16px; flex-wrap: wrap; }
.ppl-item { display: flex; flex-direction: column; align-items: center; text-align: center; gap: 4px; }
.ppl-avatar-wrap { position: relative; width: 66px; height: 66px; }
.ppl-avatar { width: 66px; height: 66px; border-radius: 50%; object-fit: cover; border: 3px solid #fff; box-shadow: 0 8px 20px rgba(14,59,67,.14); background: #fff; transition: transform .3s var(--sp), box-shadow .3s; animation: bob 4s ease-in-out infinite; }
.ppl-item:nth-child(2) .ppl-avatar { animation-delay: -1.3s; }
.ppl-item:nth-child(3) .ppl-avatar { animation-delay: -2.6s; }
.ppl-item:hover .ppl-avatar { transform: translateY(-4px) scale(1.05); box-shadow: 0 12px 26px rgba(14,59,67,.2); }
.ppl-role-dot { position: absolute; right: 2px; bottom: 2px; width: 14px; height: 14px; border-radius: 50%; border: 2px solid #fff; }
.ppl-name { font-family: var(--font-heading, sans-serif); font-weight: 700; font-size: .82rem; color: var(--ink, #0E3B43); margin-top: 2px; }
.ppl-relation { font-family: var(--font-body, sans-serif); font-size: .72rem; color: var(--mu, #4F6F73); font-weight: 500; }
.ppl-upload { cursor: pointer; }
.ppl-upload-circle { width: 66px; height: 66px; border-radius: 50%; border: 2px dashed #7FD6D0; background: rgba(127,214,208,.12); display: flex; align-items: center; justify-content: center; color: #0B7A7C; transition: transform .3s var(--sp), background .3s; }
.ppl-upload:hover .ppl-upload-circle { transform: translateY(-4px) scale(1.05); background: rgba(127,214,208,.25); }
.mem-preview-box { background: #fff; border: 1px solid rgba(14,59,67,.08); border-radius: 20px; padding: 16px 18px; margin-top: 14px; box-shadow: 0 10px 28px rgba(14,59,67,.06); }
.mem-preview-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
.mem-tag { display: inline-flex; align-items: center; gap: 6px; font-family: var(--font-heading, sans-serif); font-size: .68rem; font-weight: 700; letter-spacing: .08em; color: #0B7A7C; text-transform: uppercase; }
.mem-badge-live { font-size: .66rem; font-weight: 700; padding: 3px 9px; border-radius: 99px; background: rgba(43,181,138,.15); color: #0E7A5A; }
.mem-q { font-family: var(--font-heading, sans-serif); font-weight: 600; font-size: .92rem; line-height: 1.4; color: var(--ink, #0E3B43); margin: 0 0 10px !important; }
.mem-choices { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 10px; }
.mem-chip { padding: 6px 12px; border-radius: 99px; font-size: .8rem; font-weight: 600; background: #F4F7F6; color: var(--mu, #4F6F73); border: 1px solid rgba(14,59,67,.08); display: inline-flex; align-items: center; gap: 6px; }
.mem-chip.mem-correct { background: #E8F8F2; color: #0E7A5A; border-color: #2BB58A; }
.mem-tick { font-weight: 800; color: #2BB58A; }
.mem-preview-foot { display: flex; justify-content: space-between; font-size: .72rem; color: var(--mu, #4F6F73); border-top: 1px solid rgba(14,59,67,.06); padding-top: 8px; margin-top: 4px; }
.mem-stats { font-weight: 700; color: #0B7A7C; }
'''

for fn in product_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace ppl section
    if '<div class="ppl"' in content:
        content = old_ppl_pattern.sub(new_ppl_html, content)
        print('Updated ppl HTML in', fn)
    elif '<div class="ppl-cluster"' in content:
        print('Already updated ppl in', fn)
    else:
        print('ppl not found in', fn)

    if '.ppl-cluster' not in content:
        content = content.replace('</style>', css_to_add + '\n</style>', 1)
        print('Added CSS in', fn)

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done updating products files.')
