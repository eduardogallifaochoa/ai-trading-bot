# build.spec
# PyInstaller build configuration for AI Trading Bot
# This file defines how to package the bot into a standalone executable.

# --- MAIN CONFIGURATION ---
main_script = 'bot.py'  # Entry point script

# Include these folders in the final build (services, analytics, database, etc.)
extra_data = [
    ('services', 'services'),
    ('analytics', 'analytics'),
    ('database', 'database'),
    ('utils', 'utils'),
]

block_cipher = None  # Encryption cipher (optional, usually None)

# --- IMPORTS ---
from PyInstaller.utils.hooks import collect_submodules

# Automatically detect hidden imports (e.g., OpenAI, dotenv)
hiddenimports = (
    collect_submodules('openai') +
    collect_submodules('dotenv')
)

# --- ANALYSIS ---
a = Analysis(
    [main_script],
    pathex=['.'],          # Project root
    binaries=[],           # No custom binaries
    datas=extra_data,      # Include additional data folders
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# --- PYZ (Python archive) ---
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# --- EXE BUILD ---
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AI_Trading_Bot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,        # Use UPX to compress the executable
    console=True,    # Set to False for GUI-only mode (no console window)
)

# --- FINAL BUNDLE ---
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AI_Trading_Bot',
)
