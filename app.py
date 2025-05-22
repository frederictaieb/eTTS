from dotenv import load_dotenv
import os
from hume import AsyncHumeClient
import asyncio
from contextlib import contextmanager
from typing import Generator, Protocol
import time
import base64
import tempfile
from pathlib import Path
import aiofiles
from hume.tts import ReturnGeneration

load_dotenv()
api_key = os.getenv("HUME_API_KEY")
if not api_key:
    raise EnvironmentError("HUME_API_KEY not found in environment variables")

hume = AsyncHumeClient(api_key=api_key)

# Create an output directory in the temporary folder.
timestamp = int(time.time() * 1000)  # similar to Date.now() in JavaScript
output_dir = Path(tempfile.gettempdir()) / f"hume-audio-{timestamp}"

async def write_result_to_file(base64_encoded_audio: str, filename: str) -> None:
    file_path = output_dir / f"{filename}.wav"
    audio_data = base64.b64decode(base64_encoded_audio)
    async with aiofiles.open(file_path, "wb") as f:
        await f.write(audio_data)
    print("Wrote", file_path)

async def main() -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    print("Results will be written to", output_dir)

        
    # All the code examples in the remainder of the guide
    # belong within this main function.

if __name__ == "__main__":
    asyncio.run(main())
    print("Done")