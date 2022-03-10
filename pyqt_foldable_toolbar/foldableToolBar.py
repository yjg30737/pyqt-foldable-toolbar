from PyQt5.QtWidgets import QToolBar, QWidget, QHBoxLayout, QSizePolicy, QAction, QWidgetAction
from PyQt5.QtCore import Qt
from pyqt_svg_icon_pushbutton import SvgIconPushButton


class FoldableToolBar(QToolBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMovable(False)

        self.__foldBtn = SvgIconPushButton()
        self.__foldBtn.setIcon('ico/fold.svg')
        self.__foldBtn.setCheckable(True)
        self.__foldBtn.toggled.connect(self.__fold)
        self.__foldBtn.setMaximumWidth(12)

        cornerWidget = QWidget()
        lay = QHBoxLayout()
        lay.addWidget(self.__foldBtn)
        lay.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        lay.setContentsMargins(0, 0, 0, 0)
        cornerWidget.setLayout(lay)
        cornerWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.__foldAction = QWidgetAction(self)
        self.__foldAction.setDefaultWidget(cornerWidget)

        self.addAction(self.__foldAction)

    def __fold(self, f):
        if f:
            self.__foldBtn.setIcon('ico/unfold.svg')
            self.setFixedHeight(self.__foldBtn.sizeHint().height())
        else:
            self.__foldBtn.setIcon('ico/fold.svg')
            self.setFixedHeight(self.sizeHint().height())

    def addWidget(self, widget: QWidget) -> QAction:
        self.insertWidget(self.__foldAction, widget)