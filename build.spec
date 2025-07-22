# build.spec
# PyInstaller build configuration for AI Trading Bot
# This file defines how the executable is built and what data is included.

# --- CONFIGURATION ---
main_script = 'bot.py'

# Folders to include (services, analytics, database, utils)
extra_data = [
    ('services', 'services'),
    ('analytics', 'analytics'),
    ('database', 'database'),
    ('utils', 'utils'),
]

block_cipher = None

# --- IMPORTS ---
from PyInstaller.utils.hooks import collect_submodules

# Collect hidden imports for libraries like openai and dotenv
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

# --- PYZ (Python archive) ---
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# --- EXE ---
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
    upx=True,
    console=True,  # Set to False for GUI-only mode
)

# --- COLLECT ---
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
