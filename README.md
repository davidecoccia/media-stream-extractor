# Stream Extractor

CLI tool to extract m3u8 stream URLs from webpages and play them in VLC with the correct headers.

## Prerequisites

- [VLC](https://www.videolan.org/) installed on your system
- [uv](https://github.com/astral-sh/uv) package manager

## Installation

### macOS

```bash
# Install uv if not present
brew install astral-sh/uv/uv

# Clone and setup
git clone https://github.com/davidecoccia/media-stream-extractor.git
cd media-stream-extractor
uv sync --extra dev
playwright install chromium
```

### Linux

```bash
# Install uv if not present
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc  # or ~/.zshrc

# Clone and setup
git clone https://github.com/davidecoccia/media-stream-extractor.git
cd media-stream-extractor
uv sync --extra dev
playwright install chromium
```

### Windows

```powershell
# Install uv if not present
winget install astral-sh.uv

# Clone and setup
git clone https://github.com/davidecoccia/media-stream-extractor.git
cd media-stream-extractor
uv sync --extra dev
playwright install chromium
```

## Usage

```bash
# Extract stream and play in VLC
uv run stream-extractor <url>

# Extract stream info only (don't launch VLC)
uv run stream-extractor <url> --no-play
```

## Example

```bash
uv run stream-extractor "https://shd247.live/live-go-streaming-29.html"
```

## Development

```bash
# Install dependencies
uv sync --extra dev

# Install Playwright browsers
playwright install chromium

# Run tests
uv run pytest

# Run CLI
uv run stream-extractor <url>
```
