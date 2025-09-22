# widgets.py

from PyQt5 import QtCore, QtWidgets

class TocItemWidget(QtWidgets.QTreeWidgetItem):
    def __init__(self, title, page):
        super().__init__([title, str(page)])
        self.setFlags(
            self.flags()
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsDragEnabled
            | QtCore.Qt.ItemIsDropEnabled
        )

    def title(self):
        return self.text(0)

    def page(self):
        text = self.text(1).strip()
        try:
            return int(text)
        except Exception:
            return 1

    def setData(self, column, role, value):
        if column == 1 and role == QtCore.Qt.EditRole:
            try:
                int(str(value).strip())
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Invalid Page", "Page must be an integer.")
                return
        super().setData(column, role, value)
