import argparse
import subprocess
import sys

from playwright.sync_api import sync_playwright


def extract_stream_info(page_url: str) -> dict:
    """Extract m3u8 URL and headers from page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()

        stream_data = {}

        def handle_request(request):
            if ".m3u8" in request.url:
                stream_data["url"] = request.url
                stream_data["headers"] = dict(request.headers)

        page.on("request", handle_request)
        page.goto(page_url)
        page.wait_for_load_state("networkidle", timeout=30000)
        page.wait_for_timeout(5000)
        browser.close()

        return stream_data


def launch_player(stream_url: str, headers: dict, user_agent: str) -> None:
    """Launch mpv with stream URL and headers."""
    # Build header fields string (comma-separated key: value pairs)
    header_fields = []
    if headers.get("referer"):
        header_fields.append(f"Referer: {headers['referer']}")
    if headers.get("origin"):
        header_fields.append(f"Origin: {headers['origin']}")

    cmd = ["mpv", stream_url]

    if header_fields:
        cmd.extend(["--http-header-fields", ", ".join(header_fields)])

    if user_agent:
        cmd.extend(["--user-agent", user_agent])

    subprocess.run(cmd)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract m3u8 streams from URLs and play in mpv"
    )
    parser.add_argument("url", help="The webpage URL to extract stream from")
    parser.add_argument(
        "--no-play",
        action="store_true",
        help="Only extract and print stream info, don't launch mpv",
    )

    args = parser.parse_args()

    print(f"Extracting stream from: {args.url}")
    stream_data = extract_stream_info(args.url)

    if not stream_data.get("url"):
        print("Error: No m3u8 URL found", file=sys.stderr)
        sys.exit(1)

    print(f"Stream URL: {stream_data['url']}")
    headers = stream_data.get("headers", {})
    print(f"Headers: {headers}")
    referer = headers.get("referer", "")
    user_agent = headers.get("user-agent", "")

    print(f"Referer: {referer}")
    print(f"User-Agent: {user_agent}")

    if args.no_play:
        print("\nStream info extracted (--no-play specified)")
        return

    print("\nLaunching mpv...")
    launch_player(
        stream_data["url"],
        headers,
        user_agent,
    )


if __name__ == "__main__":
    main()
