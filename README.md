# pyqt-foldable-toolbar
PyQt foldable/hidable toolbar. You can add widget with `addWidget(widget)`. You can see how to use it in the example below.

There is fold/unfold animation to make it look better.

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-foldable-toolbar`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-svg-button.git">pyqt-svg-button</a>

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

Here's another example with `SettingsDialog` in <a href="https://github.com/yjg30737/pyqt-timer.git">pyqt-timer</a>.

Unfold

![image](https://user-images.githubusercontent.com/55078043/168452297-8bdce2f0-3126-4a83-8dee-c4ffd932ac4d.png)

Fold

![image](https://user-images.githubusercontent.com/55078043/168452302-aae84399-aa3b-4e5d-bcef-1b8cbf682ba8.png)

