import pythoncom
import win32com.client
from plugin import encryption, config
from plugin.ui import ask_user_encryption_choice

class OutlookAddin:
    _reg_clsid_ = "{B1A53DFA-A65C-4E11-99EF-338F42D5323C}"
    _reg_progid_ = "Outlook.EncryptionPlugin"
    _public_methods_ = ["OnConnection", "OnDisconnection", "OnSend"]
    _com_interfaces_ = [pythoncom.IID_IDispatch]

    def OnConnection(self, application, connect_mode, addin_inst, custom):
        self.outlook = application

    def OnDisconnection(self, disconnect_mode, custom):
        pass

    def OnSend(self, mail_item):
        encrypt = config.CONFIG["encrypt_by_default"] or ask_user_encryption_choice()

        if encrypt:
            body = mail_item.Body
            encrypted = encryption.encrypt_message(body, config.CONFIG["public_key_path"])
            mail_item.Body = encrypted.hex()  # convert bytes to hex for transport

        return True

