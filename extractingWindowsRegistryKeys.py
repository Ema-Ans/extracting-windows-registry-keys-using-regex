import re

#Things to match on:
#ensure the root keys are always the same and case sensitive
#Each subkey has a mandatory name, which is a non-empty string
# that cannot contain any backslash or null character
# and whose letter case is insignificant.

text = '''HKEY_CURRENT The Windows Registry is a hierarchical database that stores configuration settings and options for the Microsoft Windows operating system. It contains numerous keys and subkeys that control various aspects of the system. Here are some examples of Windows Registry keys:

1. HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced
2. HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
3. HKEY_CLASSES_ROOT\.exe
4. HKEY_USERS\.DEFAULT\Control Panel\Keyboard
5. HKEY_CURRENT_CONFIG\System\CurrentControlSet\Control\FileSystem
6. HKEY_CURRENT_USER\Software

These are just a few examples, and there are many more registry keys available. The keys are organized in a hierarchical structure, similar to folders and files in a file system. Each key may contain subkeys and values that store specific configuration information.

When working with the Windows Registry, it's essential to handle the keys carefully, as modifying or deleting the wrong key can potentially disrupt the system's functionality. Therefore, it's always recommended to create backups and exercise caution while making any changes to the registry.
'''

text2 = '''The Windows registry is a hierarchical database that stores configuration settings and options for the Microsoft Windows operating system. It contains numerous keys and subkeys that control various aspects of the system. Here are some examples of Windows Registry keys:

1. hkey_current_user\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced
2. HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\run
3. hkey_classes_root\.EXE
4. HKEY_USERS\default\Control Panel\Keyboard
5. HKEY_CURRENT_CONFIG\System\CurrentControlSet\Control\FileSystem

These examples demonstrate different variations in case and formatting of the Windows Registry keys. Your code should be able to handle these variations and extract the correct keys regardless of case sensitivity or incorrect formatting.
'''
    
    
import re

result = re.findall(r'(\bHKEY)([A-Z_\.]+)(\\[a-zA-z0-9_\-\.]*)', text)


paths = []

for tuple in result:
    paths.append(''.join(tuple))

print(paths)
