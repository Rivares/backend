# -*- mode: python ; coding: utf-8 -*-

import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)

block_cipher = None


a = Analysis(['Global_main.py', 'win.spec'],
             pathex=['E:\\Python\\Proj\\backend'],
             binaries=[],
             datas=[ ('data\\hash_market.json', '.'),
             		 ('data\\hash_print_graph.json', '.'),
             		 ('data\\list_current_assets.json', '.'),
             		 ('data\\list_operations_assets.json', '.'),
             		 ('data\\market.json', '.'),
             		 ('data\\money_movement.json', '.'),
             		 ('data\\print_graph_NVTK.json', '.'),
             		 ('data\\print_graph_TATN.json', '.'),
             		 ('data\\result_ta_TATN_MACD_RSI_ATR_EMA.json', '.'),
             		 ('data\\target_ticker_NVTK.csv', '.'),
             		 ('data\\target_ticker_TATN.csv', '.'),
             		 
             		 ('gui\\button.kv', '.'),
             		 ('command.bat', '.'),
             		],
             hiddenimports=[],
             hookspath=[],
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
          name='Investment analysis',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
