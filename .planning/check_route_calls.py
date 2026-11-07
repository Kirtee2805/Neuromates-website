with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect line 211
# <div class="pv" id="v-epilepsy-care">
# Does it have .on? By default:
# <div class="pv on" id="v-overview">
# <div class="pv" id="v-parkinsons-care">
# <div class="pv" id="v-alzheimers-care">
# <div class="pv" id="v-epilepsy-care">
# <div class="pv" id="v-paralysis-care">

# In CSS:
# .pv { display: none; }
# .pv.on { display: block; }

# What if JavaScript has an error before route() runs?
# Let's check what runs before route() is called!
idx = html.find('<script')
idx_end = html.rfind('</script>')
js_code = html[idx:idx_end]
print("JS length:", len(js_code))

# Check where route() is called
calls = [l for l in js_code.split('\n') if 'route()' in l or 'addEventListener' in l]
for c in calls[:10]:
    print("Call:", c[:100])

