#!/usr/bin/env node
// index.html の問題データが参照する画像と images/ の実在ファイルを突き合わせる。
//   node check_images.js
// 画像が無い問題はゲーム内で写真の枠ごと非表示になる（エラーにはならない）。
const fs = require('fs');
const path = require('path');
const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
const dir = path.join(__dirname, 'images');
const isImg = f => /\.(jpe?g|png|webp|gif|svg)$/i.test(f);
const files = fs.existsSync(dir) ? fs.readdirSync(dir).filter(isImg) : [];
const refs = [];
const re = /\{no:'([^']+)'[^}]*?img:'([^']*)'/g;
let m;
while ((m = re.exec(html))) refs.push({ no: m[1], img: m[2] });

const missing = refs.filter(r => !files.includes(r.img));
const used = new Set(refs.map(r => r.img));
const unused = files.filter(f => !used.has(f));
const dup = {};
refs.forEach(r => { (dup[r.img] = dup[r.img] || []).push(r.no); });
const shared = Object.entries(dup).filter(([, v]) => v.length > 1);

console.log(`問題数: ${refs.length} / images/ の画像ファイル: ${files.length}`);
console.log(`画像あり: ${refs.length - missing.length} 問 / 画像なし: ${missing.length} 問`);
if (missing.length) console.log('画像なしの問題:\n' + missing.map(r => `  ${r.no} -> images/${r.img}`).join('\n'));
if (unused.length) console.log('どの問題からも参照されていない画像:\n' + unused.map(f => '  ' + f).join('\n'));
if (shared.length) console.log('複数の問題が共有している画像:\n' + shared.map(([f, v]) => `  ${f}: ${v.join(', ')}`).join('\n'));
