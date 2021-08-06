# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['time_tracker_v_4.py'],
             pathex=['/Users/tejal/Documents/Tracker/time_tracker_mac-main'],
             binaries=[],
             datas=[('/usr/local/lib/python3.9/site-packages/eel/eel.js', 'eel'), ('web', 'web')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='time_tracker_v_4',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
app = BUNDLE(exe,
             name='time_tracker_v_4.app',
             icon=None,
             bundle_identifier=None)