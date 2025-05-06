
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog
)
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from encode_decode import file_to_square_image, square_image_to_file

class DragDropWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Перетащите файл сюда или нажмите для выбора")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                border: 2px dashed #aaa;
                border-radius: 10px;
                padding: 20px;
                font-size: 14px;
                color: #555;
            }
        """)

        self.file_path = None
        self.layout.addWidget(self.label)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls and urls[0].isLocalFile():
            self.set_file_path(urls[0].toLocalFile())

    def mousePressEvent(self, event):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл")
        if file_path:
            self.set_file_path(file_path)

    def set_file_path(self, path):
        self.file_path = path
        self.label.setText(f"Выбран файл:\n{os.path.basename(path)}")
        self.label.setStyleSheet("""
            QLabel {
                border: 2px dashed #4CAF50;
                border-radius: 10px;
                padding: 20px;
                font-size: 14px;
                color: #333;
            }
        """)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bit-to-Pixel Encoder")
        self.setFixedSize(500, 400)
        self.initUI()

    def initUI(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        self.drag_drop = DragDropWidget()
        layout.addWidget(self.drag_drop)

        buttons_layout = QHBoxLayout()

        self.encode_btn = QPushButton("Кодировать в PNG")
        self.encode_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.encode_btn.clicked.connect(self.encode_file)

        self.decode_btn = QPushButton("Декодировать из PNG")
        self.decode_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        """)
        self.decode_btn.clicked.connect(self.decode_file)

        buttons_layout.addWidget(self.encode_btn)
        buttons_layout.addWidget(self.decode_btn)
        layout.addLayout(buttons_layout)

        self.status_label = QLabel()
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

    def encode_file(self):
        if not self.drag_drop.file_path:
            self.show_error("Файл не выбран")
            return

        output_file, _ = QFileDialog.getSaveFileName(
            self, "Сохранить PNG", "", "PNG Files (*.png)"
        )

        if output_file:
            try:
                file_to_square_image(self.drag_drop.file_path, output_file)
                self.show_success(f"Файл закодирован:\n{output_file}")
            except Exception as e:
                self.show_error(f"Ошибка кодирования: {str(e)}")

    def decode_file(self):
        if not self.drag_drop.file_path:
            self.show_error("Файл не выбран")
            return

        output_file, _ = QFileDialog.getSaveFileName(
            self, "Сохранить восстановленный файл", "", "All Files (*)"
        )

        if output_file:
            try:
                square_image_to_file(self.drag_drop.file_path, output_file)
                self.show_success(f"Файл восстановлен:\n{output_file}")
            except Exception as e:
                self.show_error(f"Ошибка декодирования: {str(e)}")

    def show_error(self, message):
        self.status_label.setText(f"<font color='red'>{message}</font>")

    def show_success(self, message):
        self.status_label.setText(f"<font color='green'>{message}</font>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
