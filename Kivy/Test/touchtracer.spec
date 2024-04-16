# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['E:\\Project\\Python Project\\Kivy\\kivy_venv\\share\\kivy-examples\\demo\\touchtracer\\main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
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
    [],
    exclude_binaries=True,
    name='touchtracer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(Tree('E:\\Project\\Python Project\\Kivy\\kivy_venv\\share\\kivy-examples\\demo\\touchtracer'),
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='touchtracer',
)
