"""Runtime configuration: constants plus settings from .env locally or GitHub Secrets in CI."""
import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import dotenv_values, load_dotenv

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"
# This repository is private. Publishing runs in a public one (free GitHub Actions and Pages) that holds the queue,
# publisher/, shared/ and the media; PUBLIC_DIR is its local clone (generator/public_repo.py).
PUBLIC_REMOTE = "https://github.com/Falamarcante/falamarcante.github.io.git"
PUBLIC_DIR = ROOT / "public"
TIMEZONE = "America/Sao_Paulo"
VOICE_RATE = "+0%"  # inside sentences only; the pauses between sentences keep their length
# edge-tts multilingual male voices reading pt-BR, picked by the owner on 2026-10-28 from samples.
# The kind of work quoted picks the voice, so each kind keeps its own sound.
VOICES_BY_KIND = {
    "livro": "fr-FR-RemyMultilingualNeural",
    "filme": "en-US-BrianMultilingualNeural",
    "serie": "en-US-BrianMultilingualNeural",
}
VOICE = VOICES_BY_KIND["livro"]
# Keys shared by every profile on this PC (owner's choice, 2026-10-28); the project's own .env wins when it has a value.
SHARED_ENV_FILE = Path.home() / "Downloads" / "chaves-compartilhadas.env"


@dataclass(frozen=True)
class Settings:
    pixabay_api_key: str | None
    ig_user_id: str | None
    ig_access_token: str | None
    pages_base_url: str | None
    handle: str


def load_settings(env_file: Path | None = ROOT / ".env", shared_env_file: Path | None = SHARED_ENV_FILE) -> Settings:
    if env_file is not None and Path(env_file).exists():
        load_dotenv(env_file, override=False)
    shared = dotenv_values(shared_env_file) if shared_env_file is not None and Path(shared_env_file).exists() else {}
    return Settings(
        pixabay_api_key=os.getenv("PIXABAY_API_KEY") or shared.get("PIXABAY_API_KEY") or None,
        ig_user_id=os.getenv("IG_USER_ID") or None,
        ig_access_token=os.getenv("IG_ACCESS_TOKEN") or None,
        pages_base_url=(os.getenv("PAGES_BASE_URL") or "").rstrip("/") or None,
        handle=os.getenv("IG_HANDLE", ""),
    )


def require(value: str | None, name: str) -> str:
    if not value:
        raise RuntimeError(f"Missing required setting {name}; set it in .env or GitHub Secrets")
    return value
