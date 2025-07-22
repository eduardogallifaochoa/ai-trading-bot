# build.spec
# PyInstaller build configuration for AI Trading Bot
# This file builds a standalone executable for the project.

# --- CONFIGURATION ---
# Entry point of the application
main_script = 'bot.py'

# Folders to include (copy all files inside each folder)
extra_data = [
    ('services/*', 'services'),
    ('analytics/*', 'analytics'),
    ('database/*', 'database'),
    ('utils/*', 'utils'),
]

# Cipher for encrypting Python bytecode (usually None)
block_cipher = None

# --- IMPORTS ---
from PyInstaller.utils.hooks import collect_submodules

# Automatically detect hidden imports for these libraries
hiddenimports = (
    collect_submodules('openai') +
    collect_submodules('dotenv')
)

# --- ANALYSIS STEP ---
a = Analysis(
    [main_script],
    pathex=['.'],  # Current project directory
    binaries=[],
    datas=extra_data,  # Additional folders/files
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
    upx=True,  # Use UPX compression
    console=True,  # Set False to hide console (GUI-only)
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
