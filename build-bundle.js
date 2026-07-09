#!/usr/bin/env node
/**
 * Build index-standalone.html — embed manifest, .md files, and assets into one HTML.
 *
 * Usage: node build-bundle.js
 */

const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const INPUT_HTML = path.join(ROOT, 'index.html');
const OUTPUT_HTML = path.join(ROOT, 'index-standalone.html');
const MANIFEST_PATH = path.join(ROOT, 'manifest.json');
const BUNDLE_SCRIPT_ID = 'quiz-bundle';

function fail(message) {
  console.error(`ERROR: ${message}`);
  process.exit(1);
}

function toDataUrl(filePath) {
  const ext = path.extname(filePath).slice(1).toLowerCase();
  const mime = ext === 'jpg' ? 'jpeg' : ext;
  const b64 = fs.readFileSync(filePath).toString('base64');
  return `data:image/${mime};base64,${b64}`;
}

function collectAssetsForQuiz(quizPath, bundle) {
  const dir = path.dirname(quizPath);
  const assetsDir = path.join(ROOT, dir, 'assets');
  if (!fs.existsSync(assetsDir)) return;

  for (const file of fs.readdirSync(assetsDir)) {
    const abs = path.join(assetsDir, file);
    if (!fs.statSync(abs).isFile()) continue;
    const rel = `${dir}/assets/${file}`.replace(/\\/g, '/');
    bundle.assets[rel] = toDataUrl(abs);
  }
}

function loadManifest() {
  if (!fs.existsSync(MANIFEST_PATH)) {
    fail(`missing ${path.basename(MANIFEST_PATH)} — tạo file với danh sách quiz, ví dụ:\n  { "quizzes": ["os/4-5-6.md"] }`);
  }

  let manifest;
  try {
    manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
  } catch (err) {
    fail(`invalid ${path.basename(MANIFEST_PATH)}: ${err.message}`);
  }

  if (!Array.isArray(manifest.quizzes)) {
    fail(`${path.basename(MANIFEST_PATH)} phải có mảng "quizzes"`);
  }

  return manifest;
}

function main() {
  if (!fs.existsSync(INPUT_HTML)) {
    fail(`missing ${path.basename(INPUT_HTML)}`);
  }

  const manifest = loadManifest();
  const bundle = { quizzes: manifest.quizzes, md: {}, assets: {} };
  let missingCount = 0;

  for (const entry of manifest.quizzes) {
    const quizPath = typeof entry === 'string' ? entry : entry.path;
    if (!quizPath) continue;

    const absMd = path.join(ROOT, quizPath);
    if (!fs.existsSync(absMd)) {
      console.warn(`WARN: missing ${quizPath}`);
      missingCount += 1;
      continue;
    }

    bundle.md[quizPath] = fs.readFileSync(absMd, 'utf8');
    collectAssetsForQuiz(quizPath, bundle);
  }

  if (Object.keys(bundle.md).length === 0) {
    fail('không có quiz nào được bundle — kiểm tra manifest.json và các file .md');
  }

  let html = fs.readFileSync(INPUT_HTML, 'utf8');
  const inject = `<script id="${BUNDLE_SCRIPT_ID}">\nwindow.BUNDLE = ${JSON.stringify(bundle)};\n</script>`;

  html = html.replace(
    new RegExp(`<script id="${BUNDLE_SCRIPT_ID}">[\\s\\S]*?</script>\\s*`, 'i'),
    ''
  );
  html = html.replace('</head>', `  ${inject}\n</head>`);

  fs.writeFileSync(OUTPUT_HTML, html);

  const sizeMb = (fs.statSync(OUTPUT_HTML).size / 1024 / 1024).toFixed(1);
  console.log(`OK → ${path.basename(OUTPUT_HTML)} (${sizeMb} MB)`);
  console.log(`  ${Object.keys(bundle.md).length} quizzes, ${Object.keys(bundle.assets).length} assets`);
  if (missingCount > 0) {
    console.warn(`  ${missingCount} quiz trong manifest không tìm thấy file`);
  }
}

main();
