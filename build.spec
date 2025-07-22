# build.spec
# PyInstaller build configuration for AI Trading Bot
# This spec file is used to create a standalone executable of the bot.

# --- CONFIGURATION ---
# Main script entry point
main_script = 'bot.py'

# Data folders to include in the build (copy entire directories)
extra_data = [
    ('services', 'services'),
    ('analytics', 'analytics'),
    ('database', 'database'),
    ('utils', 'utils'),
]

# Optional cipher for encryption (usually None)
block_cipher = None

# --- IMPORTS ---
from PyInstaller.utils.hooks import collect_submodules

# Collect hidden imports (required by libraries like openai or dotenv)
hiddenimports = (
    collect_submodules('openai') +
    collect_submodules('dotenv')
)

# --- ANALYSIS STEP ---
a = Analysis(
    [main_script],
    pathex=['.'],  # Current directory
    binaries=[],
    datas=extra_data,
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

# --- BUILD PYZ (Python archive) ---
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# --- CREATE EXE ---
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
    upx=True,  # Use UPX to compress the executable
    console=True,  # Set to False if you want to hide the console (GUI-only mode)
)

# --- FINAL COLLECTION ---
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
