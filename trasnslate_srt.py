#!/usr/bin/env python3
# translate_srt_progress_parallel.py
# Usage: python translate_srt_progress_parallel.py input.srt output.srt [options]

import re
import sys
import time
import argparse
from deep_translator import GoogleTranslator
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def translate_block(index, block, src_lang, dest_lang, delay):
    """Translate a single SRT block"""
    lines = block.splitlines()
    if len(lines) >= 3 and '-->' in lines[1]:
        index_line = lines[0]
        timestamp = lines[1]
        text_lines = lines[2:]
        original_text = ' '.join(text_lines)
        try:
            translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(original_text)
        except Exception as e:
            translated_text = original_text
            print(f"⚠️ Block {index_line} failed: {e}")
        
        # Split long sentences for better readability
        parts = re.split(r'(?<=[.?!])\s+', translated_text)
        result = '\n'.join([index_line, timestamp] + parts)
    else:
        result = block
    
    time.sleep(delay)
    return (index, result)

def translate_srt_parallel(input_file, output_file, src_lang='id', dest_lang='ja', workers=6, delay=0.5):
    """Translate SRT file using parallel processing"""
    print(f"🔄 Translating from {src_lang.upper()} to {dest_lang.upper()}")
    print(f"📊 Using {workers} workers with {delay}s delay")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found")
        return False
    except UnicodeDecodeError:
        print(f"❌ Error: Cannot decode '{input_file}'. Please ensure it's UTF-8 encoded")
        return False

    blocks = content.strip().split('\n\n')
    translated_blocks = [None] * len(blocks)

    print(f"📝 Found {len(blocks)} subtitle blocks")

    try:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [
                executor.submit(translate_block, i, block, src_lang, dest_lang, delay) 
                for i, block in enumerate(blocks)
            ]
            
            for future in tqdm(as_completed(futures), total=len(futures), desc="Translating", unit="block"):
                i, translated = future.result()
                translated_blocks[i] = translated

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(translated_blocks))

        print(f"\n✅ Translation complete → {output_file}")
        return True
        
    except KeyboardInterrupt:
        print(f"\n❌ Translation interrupted by user")
        return False
    except Exception as e:
        print(f"❌ Error during translation: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description='Translate SRT subtitle files using Google Translator with parallel processing',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.srt output.srt
  %(prog)s input.srt output.srt --src en --dest ja
  %(prog)s input.srt output.srt --workers 10 --delay 0.3
  %(prog)s input.srt output.srt --src id --dest en --workers 8 --delay 1.0

Common language codes:
  en (English), ja (Japanese), id (Indonesian), zh (Chinese),
  ko (Korean), es (Spanish), fr (French), de (German), ru (Russian)
        """)
    
    parser.add_argument('input_file', help='Input SRT file path')
    parser.add_argument('output_file', help='Output SRT file path')
    
    parser.add_argument('--src', '--source', dest='src_lang', default='id',
                       help='Source language code (default: id)')
    parser.add_argument('--dest', '--target', dest='dest_lang', default='ja',
                       help='Target language code (default: ja)')
    parser.add_argument('--workers', '-w', type=int, default=6,
                       help='Number of parallel workers (default: 6)')
    parser.add_argument('--delay', '-d', type=float, default=0.5,
                       help='Delay between requests in seconds (default: 0.5)')
    parser.add_argument('--list-langs', action='store_true',
                       help='List available language codes')
    parser.add_argument('--version', action='version', version='%(prog)s 1.1.0')

    args = parser.parse_args()

    if args.list_langs:
        print("Common language codes:")
        langs = {
            'en': 'English', 'ja': 'Japanese', 'id': 'Indonesian', 'zh': 'Chinese',
            'ko': 'Korean', 'es': 'Spanish', 'fr': 'French', 'de': 'German',
            'ru': 'Russian', 'ar': 'Arabic', 'hi': 'Hindi', 'th': 'Thai',
            'vi': 'Vietnamese', 'ms': 'Malay', 'pt': 'Portuguese', 'it': 'Italian'
        }
        for code, name in sorted(langs.items()):
            print(f"  {code:3} - {name}")
        return

    # Validate arguments
    if args.workers < 1:
        print("❌ Error: Number of workers must be at least 1")
        return
    
    if args.delay < 0:
        print("❌ Error: Delay must be non-negative")
        return
    
    if args.workers > 20:
        print("⚠️ Warning: Using more than 20 workers may trigger rate limits")
    
    if args.delay < 0.1:
        print("⚠️ Warning: Very low delay may trigger rate limits")

    # Start translation
    success = translate_srt_parallel(
        args.input_file,
        args.output_file,
        args.src_lang,
        args.dest_lang,
        args.workers,
        args.delay
    )
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
