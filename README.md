# SRT Subtitle Translator

A fast, parallel SRT subtitle translator that uses Google Translate to convert subtitle files between languages with real-time progress tracking.

## ✨ Features

- 🚀 **Parallel Processing** - Translates multiple subtitle blocks simultaneously
- 📊 **Progress Tracking** - Real-time progress bar with completion status
- 🌐 **Multi-language Support** - Supports all Google Translate languages
- ⚡ **Fast Translation** - Optimized with configurable thread workers
- 🛡️ **Error Handling** - Gracefully handles translation failures
- 📝 **Smart Text Splitting** - Intelligently splits long sentences for better readability

## 🔧 Requirements

```bash
pip install deep-translator tqdm
```

## 📖 Usage

### Basic Usage
```bash
python translate_srt.py input.srt output.srt
```

### Examples
```bash
# Translate Indonesian subtitles to Japanese
python translate_srt.py movie_id.srt movie_ja.srt

# Translate English subtitles to Spanish
python translate_srt.py series_en.srt series_es.srt
```

## ⚙️ Configuration

Edit the configuration variables at the top of the script:

```python
SRC_LANG = 'id'   # Source language (ISO 639-1 code)
DEST_LANG = 'ja'  # Target language (ISO 639-1 code)
WORKERS = 6       # Number of parallel translation threads
DELAY = 0.5       # Delay between requests per thread (seconds)
```

### Supported Language Codes

| Language | Code | Language | Code |
|----------|------|----------|------|
| English | `en` | Spanish | `es` |
| Indonesian | `id` | Japanese | `ja` |
| French | `fr` | German | `de` |
| Chinese | `zh` | Korean | `ko` |
| Portuguese | `pt` | Russian | `ru` |

*For complete list, see [Google Translate supported languages](https://cloud.google.com/translate/docs/languages)*

## 🎯 How It Works

1. **Parse SRT File** - Reads and splits subtitle file into blocks
2. **Parallel Translation** - Distributes blocks across multiple threads
3. **Smart Text Processing** - Splits long sentences at natural breakpoints
4. **Progress Tracking** - Shows real-time translation progress
5. **Output Generation** - Assembles translated blocks into final SRT file

## 📁 Input/Output Format

### Input SRT Format
```
1
00:00:01,500 --> 00:00:04,000
Hello, how are you today?

2
00:00:05,000 --> 00:00:08,500
I'm doing great, thanks for asking!
```

### Output SRT Format
```
1
00:00:01,500 --> 00:00:04,000
こんにちは、今日はいかがですか？

2
00:00:05,000 --> 00:00:08,500
元気です、聞いてくれてありがとう！
```

## 🛠️ Performance Tuning

### Adjust Workers
- **More workers** = Faster translation but higher API load
- **Fewer workers** = Slower but more stable
- **Recommended**: 4-8 workers for optimal balance

### Adjust Delay
- **Lower delay** = Faster translation but risk of rate limiting
- **Higher delay** = Slower but more reliable
- **Recommended**: 0.3-0.8 seconds

## ⚠️ Error Handling

The script handles common errors gracefully:

- **Translation API failures** - Falls back to original text
- **Network timeouts** - Retries automatically
- **Malformed SRT blocks** - Preserves original formatting
- **Rate limiting** - Uses configurable delays

## 🚨 Limitations

- Depends on Google Translate availability
- May hit rate limits with very large files
- Translation quality depends on Google Translate accuracy
- Some formatting may be lost in complex subtitles

## 💡 Tips

1. **Test with small files first** to find optimal settings
2. **Backup original files** before translation
3. **Use appropriate delays** to avoid rate limiting
4. **Check output quality** and adjust settings if needed
5. **Consider splitting very large SRT files** (>1000 blocks)

## 🐛 Troubleshooting

### Common Issues

**"ModuleNotFoundError"**
```bash
pip install deep-translator tqdm
```

**"Rate limit exceeded"**
- Increase `DELAY` value
- Reduce `WORKERS` count

**"Translation failed"**
- Check internet connection
- Verify language codes are correct
- Try with smaller files

**"Malformed output"**
- Check input SRT format
- Ensure proper encoding (UTF-8)

## 📄 License

This project is open source. Feel free to modify and distribute.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📧 Support

If you encounter issues or have questions, please check the troubleshooting section first or create an issue in the repository.

---

**Made with ❤️ for subtitle translation enthusiasts**
