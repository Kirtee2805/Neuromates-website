const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const regex = /<script\b[^>]*>([\s\S]*?)<\/script>/gi;
let match;
let i = 0;
while ((match = regex.exec(html)) !== null) {
  i++;
  const src = match[0].includes('src=');
  if (src) continue;
  const code = match[1];
  try {
    new Function(code);
    console.log(`Script #${i}: Syntax OK (${code.length} chars)`);
  } catch (err) {
    console.error(`Script #${i} Syntax ERROR:`, err.message);
    process.exit(1);
  }
}
console.log('All inline scripts in index.html passed verification!');

