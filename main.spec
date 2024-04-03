# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/Users/ijiyeong/Desktop/save/1_program/proTool/main.py'],
    pathex=[],
    binaries=[("/opt/homebrew/bin/ffmpeg", 'ffmpeg')],
    datas=[],
    hiddenimports=['PIL', 'PySide6', 'PIL.Image', 'workalendar', 'OpenEXR', 'Imath', 'xlsxwriter', 'pandas', 'openpyxl'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='main.app',
    icon=None,
    bundle_identifier=None,
)
