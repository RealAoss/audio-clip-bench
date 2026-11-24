from pathlib import Path

import os
from tempfile import TemporaryDirectory
from playwright.sync_api import sync_playwright

import io
import struct
import wave

ROOT = Path(__file__).resolve().parents[1]

with sync_playwright() as p, TemporaryDirectory() as temp:
    browser = p.chromium.launch(executable_path=os.environ.get("CHROME_PATH"))
    page = browser.new_page()
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto((ROOT / "index.html").as_uri())
    audio = io.BytesIO()
    with wave.open(audio, "wb") as f:
        f.setparams((2, 2, 48000, 0, "NONE", "not compressed"))
        f.writeframes(struct.pack("<hh", 1000, -1000) * 48000)
    page.locator("#file").set_input_files(
        dict(name="test.wav", mimeType="audio/wav", buffer=audio.getvalue())
    )
    page.locator("#start").fill("0.25")
    page.locator("#end").fill("0.75")
    with page.expect_download() as download:
        page.locator("#save").click()
    dest = Path(temp) / "clip.wav"
    download.value.save_as(dest)
    with wave.open(str(dest), "rb") as clip:
        assert clip.getnchannels() == 2 and clip.getsampwidth() == 2
        assert abs(clip.getnframes() / clip.getframerate() - 0.5) < 0.0001
        clip.setpos(clip.getnframes() // 2)
        a, b = struct.unpack("<hh", clip.readframes(1))
        assert abs(a - 1000) < 5 and abs(b + 1000) < 5
    page.locator("#end").fill("0.1")
    page.locator("#save").click()
    assert "end after the start" in page.locator("#status").inner_text()
    assert not errors, errors
    browser.close()
