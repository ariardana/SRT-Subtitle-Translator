# 🎬 SRT Subtitle Translator

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-orange.svg)](https://github.com/yourusername/srt-translator)

A powerful and efficient command-line tool for translating SRT subtitle files using Google Translator with multi-threading support for faster processing.

## ✨ Features

- 🚀 **Parallel Processing**: 3-5x faster translation with configurable worker threads
- 🌍 **Multi-Language Support**: 100+ languages via Google Translate API
- 📊 **Real-time Progress**: Progress bar with translation status and ETA
- 🎯 **Smart Text Processing**: Automatic sentence splitting for better subtitle readability
- 🛡️ **Robust Error Handling**: Continues translation even if individual blocks fail
- ⚡ **Rate Limiting**: Built-in delays to avoid API restrictions
- 📝 **UTF-8 Support**: Proper handling of international characters
- 🔧 **Production Ready**: Comprehensive logging and error recovery

## 📦 Installation

### Requirements

- Python 3.7 or higher
- Internet connection for Google Translate API

### Install Dependencies

```bash
pip install deep-translator tqdm
```

### Download the Script

```bash
# Clone the repository
git clone https://github.com/ariardana/SRT-Subtitle-Translator
cd SRT-Subtitle-Translator
```

## 🚀 Quick Start

### Basic Usage

```bash
# Translate from Indonesian to Japanese (default)
python translate_srt.py input.srt output.srt

# Translate English subtitles to Japanese
python translate_srt.py english_movie.srt japanese_movie.srt --src en --dest ja
```

### Advanced Usage

```bash
# High-speed translation (use with caution)
python translate_srt.py input.srt output.srt --workers 10 --delay 0.2

# Conservative translation (more reliable)
python translate_srt.py input.srt output.srt --workers 4 --delay 1.0

# Batch processing with different target languages
python translate_srt.py anime.srt anime_en.srt --src ja --dest en --workers 8
python translate_srt.py drama.srt drama_ko.srt --src ja --dest ko --workers 6
```

## 📖 Command Line Options

### Required Arguments
- `input_file` - Path to input SRT subtitle file (must be UTF-8 encoded)
- `output_file` - Path where translated SRT file will be saved

### Optional Arguments

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--src` | | Source language code | `id` (Indonesian) |
| `--dest` | | Target language code | `ja` (Japanese) |
| `--workers` | `-w` | Number of parallel threads (1-30) | `6` |
| `--delay` | `-d` | Delay between requests in seconds | `0.5` |
| `--list-langs` | | Show all supported language codes | |
| `--verbose` | `-v` | Enable detailed output | |
| `--version` | | Show version information | |
| `--help` | `-h` | Show help message | |

### Examples with Options

```bash
# Show all supported languages
python translate_srt.py --list-langs

# Verbose output with custom settings
python translate_srt.py movie.srt movie_translated.srt --src en --dest ko --workers 8 --delay 0.3 --verbose

# Help and version
python translate_srt.py --help
python translate_srt.py --version
```

## 🌍 Supported Languages

The tool supports 100+ languages through Google Translate. Here are the most commonly used:

### Major Languages
| Code | Language | Code | Language |
|------|----------|------|----------|
| `en` | English | `es` | Spanish |
| `fr` | French | `de` | German |
| `it` | Italian | `pt` | Portuguese |
| `ru` | Russian | `ar` | Arabic |

### Asian Languages
| Code | Language | Code | Language |
|------|----------|------|----------|
| `ja` | Japanese | `ko` | Korean |
| `zh` | Chinese (Simplified) | `zh-tw` | Chinese (Traditional) |
| `th` | Thai | `vi` | Vietnamese |
| `hi` | Hindi | `id` | Indonesian |
| `ms` | Malay | `tl` | Filipino |

> 💡 Use `--list-langs` to see all available language codes or see [Google Translate supported languages](https://cloud.google.com/translate/docs/languages)

## ⚙️ Performance Tuning

### Recommended Settings

| File Size | Blocks | Workers | Delay | Est. Time |
|-----------|--------|---------|-------|-----------|
| Small | < 100 | 4 | 0.5s | ~30 seconds |
| Medium | 100-500 | 6 | 0.3s | 1-3 minutes |
| Large | 500-1000 | 8 | 0.2s | 3-8 minutes |
| Very Large | 1000+ | 10 | 0.1s | 5-15 minutes |

### Performance Tips

- **More workers** = faster translation but higher risk of rate limiting
- **Higher delay** = more stable but slower translation
- **Sweet spot**: 6-8 workers with 0.3-0.5s delay for balanced performance
- **Production use**: 4-6 workers with 0.5-1.0s delay for maximum reliability

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Rate Limit Errors
```
⚠️ Block 45 failed: Too Many Requests
```
**Solution**: Increase delay or reduce workers
```bash
python translate_srt.py input.srt output.srt --workers 4 --delay 1.0
```

#### File Encoding Errors
```
❌ Error: Cannot decode 'input.srt'. Please ensure it's UTF-8 encoded
```
**Solution**: Convert file to UTF-8 encoding
```bash
# On Linux/Mac
iconv -f ISO-8859-1 -t UTF-8 input.srt > input_utf8.srt

# On Windows (using PowerShell)
Get-Content input.srt -Encoding Default | Set-Content input_utf8.srt -Encoding UTF8
```

#### Network Timeout
```
❌ Error: Network timeout
```
**Solution**: Check internet connection and retry with higher delay
```bash
python translate_srt.py input.srt output.srt --delay 2.0
```

#### Memory Issues (Large Files)
**Solution**: Reduce workers
```bash
python translate_srt.py input.srt output.srt --workers 2
```

### Recovery from Interruption

If translation is interrupted, the script handles partial completion gracefully:

1. **Keyboard Interrupt (Ctrl+C)**: Saves progress and shows partial results location
2. **Network Issues**: Continues with remaining blocks, marks failed ones
3. **System Crash**: Re-run the same command to continue from where it left off

## 📊 Usage Examples

### Movie/TV Show Subtitles
```bash
# Translate anime subtitles from Japanese to English
python translate_srt.py anime_episode01.srt anime_episode01_en.srt --src ja --dest en --workers 6

# Translate Korean drama to multiple languages
python translate_srt.py kdrama.srt kdrama_en.srt --src ko --dest en --workers 8
python translate_srt.py kdrama.srt kdrama_ja.srt --src ko --dest ja --workers 8
```

### Educational Content
```bash
# Translate lecture subtitles
python translate_srt.py lecture.srt lecture_zh.srt --src en --dest zh --workers 4 --delay 0.8

# Language learning materials
python translate_srt.py spanish_lesson.srt spanish_lesson_en.srt --src es --dest en
```

### Batch Processing Script
```bash
#!/bin/bash
# batch_translate.sh - Translate multiple files

for file in *.srt; do
    echo "Translating $file..."
    python translate_srt.py "$file" "${file%.srt}_en.srt" --src ja --dest en --workers 6
done
```

## 🏗️ Technical Details

### Architecture
- **Multi-threading**: Uses ThreadPoolExecutor for parallel translation
- **Rate Limiting**: Configurable delays prevent API abuse
- **Error Recovery**: Failed blocks don't stop the entire process
- **Memory Efficient**: Processes blocks individually without loading entire file

### SRT Format Handling
- Preserves original timing information
- Maintains subtitle block structure
- Handles multi-line subtitles correctly
- Splits long translated sentences automatically

### Translation Quality
- Uses Google Translate API for high-quality results
- Maintains context for better translation accuracy
- Handles special characters and Unicode properly
- Preserves formatting and line breaks where appropriate

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
```bash
git clone https://github.com/yourusername/srt-translator.git
cd srt-translator
pip install -r requirements.txt
```

### Running Tests
```bash
python -m pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [deep-translator](https://pypi.org/project/deep-translator/) - Translation API wrapper
- [tqdm](https://pypi.org/project/tqdm/) - Progress bar library
- Google Translate - Translation service
---

⭐ **Star this repository if you find it helpful!**

Made with ❤️ by [Ari Ardana](https://github.com/ariardana)
