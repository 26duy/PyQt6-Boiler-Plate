from PyQt6.QtCore import QLibraryInfo
print(f"Path: {QLibraryInfo.path(QLibraryInfo.LibraryPath.PluginsPath)}")