# build.spec
# PyInstaller build configuration for AI Trading Bot
# This file defines how to create a standalone executable for the project.

from PyInstaller.utils.hooks import collect_submodules, Tree

# --- MAIN CONFIGURATION ---
main_script = 'bot.py'  # Entry point of your app
block_cipher = None

# Include full directories (services, analytics, database, utils)
extra_data = [
    Tree('services', prefix='services'),
    Tree('analytics', prefix='analytics'),
    Tree('database', prefix='database'),
    Tree('utils', prefix='utils'),
]

# Automatically detect hidden imports (OpenAI, dotenv, etc.)
hiddenimports = collect_submodules('openai') + collect_submodules('dotenv')

# --- ANALYSIS ---
a = Analysis(
    [main_script],
    pathex=['.'],
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

# --- BUILD PYZ ---
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# --- BUILD EXE ---
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
    upx=True,  # Compress executable
    console=True,  # Change to False for GUI-only app
)

# --- COLLECT FILES ---
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
