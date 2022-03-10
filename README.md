# pyqt-foldable-toolbar
PyQt foldable toolbar

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-foldable-toolbar.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a>

## Example
### Code Sample
```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from pyqt_foldable_toolbar import FoldableToolBar

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    toolBar = FoldableToolBar()
    toolBar.addWidget(QTextEdit())
    mainWindow.addToolBar(toolBar)
    mainWindow.show()
    sys.exit(app.exec_())
```

### Result

Unfold

![image](https://user-images.githubusercontent.com/55078043/157591512-9654f7c5-b852-48f9-95bf-2ac22baa182b.png)

Fold

![image](https://user-images.githubusercontent.com/55078043/157591529-2b1ccbb9-5f9b-4342-a52b-d4d48e7e15c5.png)
