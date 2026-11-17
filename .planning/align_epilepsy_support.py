import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    pattern = re.compile(
        r'<div class="reminders-grid">\s*<div class="reminder-card">\s*<h3>Medication Reminder</h3>\s*<p>Supports awareness of scheduled medication\.</p>\s*</div>\s*<div class="reminder-card">\s*<h3>Appointment Reminder</h3>\s*<p>Helps patients keep track of scheduled clinical appointments\.</p>\s*</div>\s*</div>\s*<!-- Strict Safety & Responsible Wording -->\s*<div class="safety-disclaimer-box">\s*<p><b>Responsible wording\.</b> Neuro Mates monitors for abnormal EEG signals that may indicate a seizure\. It does not diagnose, predict or prevent seizures, and detection cannot be guaranteed\.</p>\s*</div>',
        re.DOTALL
    )

    new_block = '''<div class="reminders-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
          <div class="reminder-card">
            <span style="display:inline-block;font-size:0.7rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#0B7A7C;background:#EAF6F5;padding:4px 10px;border-radius:99px;margin-bottom:12px;">Routine Care</span>
            <h3>Medication Reminder</h3>
            <p>Supports awareness of scheduled medication.</p>
          </div>
          <div class="reminder-card">
            <span style="display:inline-block;font-size:0.7rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#0B7A7C;background:#EAF6F5;padding:4px 10px;border-radius:99px;margin-bottom:12px;">Clinical Follow-up</span>
            <h3>Appointment Reminder</h3>
            <p>Helps patients keep track of scheduled clinical appointments.</p>
          </div>
          <div class="reminder-card" style="border-color:rgba(43,181,138,0.35);background:linear-gradient(160deg,#ffffff,#F0FAF7);">
            <span style="display:inline-block;font-size:0.7rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#0E7A5A;background:#E8F8F2;padding:4px 10px;border-radius:99px;margin-bottom:12px;">Clinical Protocol</span>
            <h3>Responsible Wording</h3>
            <p>Neuro Mates monitors for abnormal EEG signals that may indicate a seizure. It does not diagnose, predict or prevent seizures, and detection cannot be guaranteed.</p>
          </div>
        </div>'''

    if pattern.search(c):
        c = pattern.sub(new_block, c)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {filepath}")
    else:
        print(f"Pattern not found in {filepath}")

update_file('epilepsy-care.html')
update_file('products/epilepsy-care.html')
