<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

<h1>🔒 Outlook Encryption Plugin</h1>

<blockquote>
  <em>A Microsoft Outlook plugin that encrypts email contents using 4096-bit RSA encryption and AES-256 hybrid encryption, ensuring only trusted recipients with the plugin can read secured emails.</em>
</blockquote>

<hr>

<h2>🚀 Project Overview</h2>

<p>The Outlook Encryption Plugin allows users to optionally encrypt outgoing emails with strong 4096-bit RSA encryption combined with AES-256 hybrid encryption for larger messages. Recipients must have the same plugin installed with their private key to decrypt and read the secured message.</p>

<p>The plugin offers:</p>
<ul>
  <li>Optional encryption toggle per email</li>
  <li>User-supplied public/private key management</li>
  <li>Secure AES-256 hybrid encryption for efficient large-message encryption</li>
  <li>RSA encryption for AES key exchange</li>
  <li>Custom Outlook Ribbon UI</li>
  <li>Fully containerized COM add-in using PyInstaller</li>
</ul>

<hr>

<h2>🛡️ How It Works</h2>

<ul>
  <li>When sending an email, the user can choose to encrypt it.</li>
  <li>The email body is encrypted using AES-256 (symmetric key encryption).</li>
  <li>The AES key itself is encrypted with the recipient's RSA-4096 public key (asymmetric encryption).</li>
  <li>The plugin automatically assembles the encrypted message and transmits it securely.</li>
  <li>Recipients use the plugin to decrypt both the AES key and the message body transparently.</li>
</ul>

<hr>

<h2>📂 Folder Structure</h2>

<pre><code>
outlook_encryption_plugin/
├── README.md
├── setup.py
├── requirements.txt
├── plugin/
│   ├── __init__.py
│   ├── addin.py
│   ├── ribbon_ui.xml
│   ├── encryption.py
│   ├── config.py
│   └── ui.py
├── keys/
│   ├── private_key.pem
│   └── public_key.pem
└── installer/
    ├── create_addin.bat
    └── outlook_encryption_plugin.spec
</code></pre>

<hr>

<h2>⚙️ Installation</h2>

<ol>
  <li>Clone the repository:</li>
  <pre><code>git clone https://github.com/yourusername/outlook_encryption_plugin.git
cd outlook_encryption_plugin
</code></pre>

  <li>Install dependencies:</li>
  <pre><code>pip install -r requirements.txt
</code></pre>

  <li>Generate RSA keys (if needed):</li>
  <pre><code>
openssl genrsa -out keys/private_key.pem 4096
openssl rsa -in keys/private_key.pem -pubout -out keys/public_key.pem
</code></pre>

</ol>

<hr>

<h2>🐳 Build COM Add-in (DLL) with PyInstaller</h2>

<p>Run the following command to build the plugin as a COM-compatible executable:</p>

<pre><code>
pyinstaller --onefile --hidden-import=win32com --hidden-import=pythoncom --com-server=plugin.addin plugin/addin.py
</code></pre>

<p>Then register it with Windows:</p>

<pre><code>
regsvr32 dist/outlook_encryption_plugin.dll
</code></pre>

<hr>

<h2>📬 Using the Plugin</h2>

<ul>
  <li>Compose an email in Outlook.</li>
  <li>Use the "Secure Email" tab on the Ribbon.</li>
  <li>Select whether to encrypt the message.</li>
  <li>Send the email securely!</li>
  <li>Recipients with the plugin and private key installed can decrypt and read the message.</li>
</ul>

<hr>

<h2>📝 Example Encrypted Message</h2>

<pre><code>
{
  "encrypted_aes_key": "Base64-encoded string",
  "nonce": "Base64-encoded string",
  "tag": "Base64-encoded string",
  "ciphertext": "Base64-encoded string"
}
</code></pre>

<p>Decryption happens automatically on the recipient side using their private key.</p>

<hr>

<h2>📈 Future Improvements</h2>

<ul>
  <li>Key Management UI for easier import/export of keys</li>
  <li>Automatic detection of encrypted messages for auto-decryption</li>
  <li>Support for multiple recipients with key exchange</li>
  <li>Cloud-based key vault integration</li>
  <li>Cross-device plugin synchronization using Microsoft Graph API</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<ul>
  <li><a href="https://github.com/joshuanmoses">Joshua Moses</a> — AI Engineer & Cybersecurity SME</li>
   <li>All rights reserved © 2004, Joshua Moses</li>
</ul>

</body>
</html>
