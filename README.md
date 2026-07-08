<h1 align="center">Advanced Telegram Uploader Bot</h1>

<p align="center">
  <a href="https://github.com/anishmusician/Advanced-Tg-Uploader/stargazers"><img src="https://img.shields.io/github/stars/anishmusician/Advanced-Tg-Uploader?color=blue&style=flat" alt="GitHub Repo stars"></a>
  <a href="https://github.com/anishmusician/Advanced-Tg-Uploader/issues"><img src="https://img.shields.io/github/issues/anishmusician/Advanced-Tg-Uploader" alt="GitHub issues"></a>
  <a href="https://github.com/anishmusician/Advanced-Tg-Uploader/pulls"><img src="https://img.shields.io/github/issues-pr/anishmusician/Advanced-Tg-Uploader" alt="GitHub pull requests"></a>
</p>

<p align="center">
  <em>An advanced Telegram bot script to download files from direct download URLs, check file sizes, rename files, and upload them with progress indicators directly to Telegram.</em>
</p>
<hr>

## ✨ Features

- 📥 Download files from direct download URLs and upload them to Telegram.
- 📊 Shows download and upload progress using custom handlers.
- ✏️ Rename Option: Allows renaming the file before uploading.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher.
- `pyrofork`, `tgcrypto`, `pyleaves` and `aiohttp` libraries.
- A Telegram bot token (you can get one from [@BotFather](https://t.me/BotFather) on Telegram).
- API ID and Hash: You can get these by creating an application on [my.telegram.org](https://my.telegram.org).
- To Get `SESSION_STRING` Open [@SmartUtilBot](https://t.me/SmartUtilBot) and use the `/pyro` command.

## Installation

To install the required libraries, run the following command:

```bash
pip install pyrofork tgcrypto pyleaves aiohttp
```

**Note: If you previously installed `pyrogram`, uninstall it before installing `pyrofork`.**

## Configuration

1. Open the `config.py` file in your favorite text editor.
2. Replace the placeholders for `API_ID`, `API_HASH`, `SESSION_STRING`, and `BOT_TOKEN` with your actual values:
   - **`API_ID`**: Your API ID from [my.telegram.org](https://my.telegram.org).
   - **`API_HASH`**: Your API Hash from [my.telegram.org](https://my.telegram.org).
   - **`SESSION_STRING`**: The session string you generated.
   - **`BOT_TOKEN`**: The token you obtained from BotFather.

## Deploy the Bot

```sh
git clone https://github.com/anishmusician/Advanced-Tg-Uploader
cd Advanced-Tg-Uploader
python uploder.py
```

## Usage

Send a URL to the bot in a private message. If the file is valid and within the size limit, the bot will present two options:

- **Default:** Download and upload the file with its original name.
- **Rename:** Allows you to specify a new filename before upload.
- **Download Progress:** While downloading and uploading, progress messages display current status.

## Author

- Name: Anish Kumar
- GitHub: [anishmusician](https://github.com/anishmusician)

Feel free to reach out if you have any questions or feedback.
