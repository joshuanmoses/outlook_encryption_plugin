@echo off
python -m win32com.client.makepy "Microsoft Outlook 16.0 Object Library"
regsvr32 /s outlook_encryption_plugin.dll

