from PyQt5.QtWidgets import QToolBar, QWidget, QHBoxLayout, QSizePolicy, QAction, QWidgetAction
from PyQt5.QtCore import Qt, QPropertyAnimation, QAbstractAnimation
from pyqt_svg_icon_pushbutton import SvgIconPushButton


class FoldableToolBar(QToolBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initUi()

    def __initUi(self):
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

        self.__menuAnimation = QPropertyAnimation(self, b"height")
        self.__menuAnimation.valueChanged.connect(self.setFixedHeight)

        self.__menuAnimation.setStartValue(self.sizeHint().height())
        self.__menuAnimation.setDuration(200)  # default duration
        self.__menuAnimation.setEndValue(self.__foldBtn.sizeHint().height())  # default end value

    def __fold(self, f):
        if f:
            self.__menuAnimation.setDirection(QAbstractAnimation.Forward)
            self.__menuAnimation.start()
            self.__foldBtn.setIcon('ico/unfold.svg')
            self.setFixedHeight(self.__foldBtn.sizeHint().height())
        else:
            self.__menuAnimation.setDirection(QAbstractAnimation.Backward)
            self.__menuAnimation.start()
            self.__foldBtn.setIcon('ico/fold.svg')
            self.setFixedHeight(self.sizeHint().height())

    def addWidget(self, widget: QWidget) -> QAction:
        self.insertWidget(self.__foldAction, widget)
        self.__menuAnimation.setStartValue(self.sizeHint().height())