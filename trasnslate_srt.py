#!/usr/bin/env python3
# translate_srt.py
# Usage: python translate_srt.py input.srt output.srt

import re
import sys
import time
from deep_translator import GoogleTranslator
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration 
SRC_LANG = 'id'   # Source language (ISO 639-1 code)
DEST_LANG = 'ja'  # Target language (ISO 639-1 code)
WORKERS = 6       # Number of parallel translation threads
DELAY = 0.5       # Delay between requests per thread (seconds)

def translate_block(index, block):
    lines = block.splitlines()
    if len(lines) >= 3 and '-->' in lines[1]:
        index_line = lines[0]
        timestamp = lines[1]
        text_lines = lines[2:]
        original_text = ' '.join(text_lines)
        try:
            translated_text = GoogleTranslator(source=SRC_LANG, target=DEST_LANG).translate(original_text)
        except Exception as e:
            translated_text = original_text
            print(f"⚠️ Block {index_line} failed: {e}")
        parts = re.split(r'(?<=[.?!])\s+', translated_text)
        result = '\n'.join([index_line, timestamp] + parts)
    else:
        result = block
    time.sleep(DELAY)
    return (index, result)

def translate_srt_parallel(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = content.strip().split('\n\n')
    translated_blocks = [None] * len(blocks)

    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        futures = [executor.submit(translate_block, i, block) for i, block in enumerate(blocks)]
        for future in tqdm(as_completed(futures), total=len(futures), desc="Translating", unit="block"):
            i, translated = future.result()
            translated_blocks[i] = translated

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(translated_blocks))

    print(f"\n✅ Translation complete → {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python translate_srt.py input.srt output.srt")
        sys.exit(1)

    translate_srt_parallel(sys.argv[1], sys.argv[2])
