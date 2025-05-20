import sys
import os
import tempfile
import shutil
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QHBoxLayout, QPushButton
)
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap, QPainter

from main import main as cloneDetection

from PyQt5.QtGui import QPixmap, QPainter, QFont, QCursor  

from PyQt5.QtGui import QPixmap, QPainter, QFont, QColor  

class DropZone(QLabel):
    def __init__(self, on_file_dropped):
        super().__init__()
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("border: 2px dashed #888; padding: 40px;")
        self.on_file_dropped = on_file_dropped

        if getattr(sys, 'frozen', False):
            self.base_dir = sys._MEIPASS
        else:
            self.base_dir = os.path.dirname(os.path.abspath(__file__))

        image_path = os.path.join(self.base_dir, 'images/background.png')
        self.original_pixmap = QPixmap(image_path)

        if self.original_pixmap.isNull():
            print(f"Error: Could not load image from {image_path}")
            self.show_fallback_text = True
        else:
            self.show_fallback_text = False

        self.set_top_image("addDocument.png")

        self.filename = None 

    def set_top_image(self, image_filename):
        top_image_path = os.path.join(self.base_dir, 'images', image_filename)
        new_pixmap = QPixmap(top_image_path)
        if not new_pixmap.isNull():
            self.top_pixmap = new_pixmap
            self.update()
        else:
            print(f"Warning: Could not load image from {top_image_path}")
            self.top_pixmap = QPixmap() 

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)

        if self.show_fallback_text:
            painter.drawText(self.rect(), Qt.AlignCenter, "Drag a Python (.py) file here")
        else:
            scaled_bg = self.original_pixmap.scaled(
                self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            pix_x = (self.width() - scaled_bg.width()) // 2
            pix_y = (self.height() - scaled_bg.height()) // 2
            painter.drawPixmap(pix_x, pix_y, scaled_bg)

            if not self.top_pixmap.isNull():
                top_scaled = self.top_pixmap.scaledToWidth(self.width() // 6, Qt.SmoothTransformation)
                top_x = (self.width() - top_scaled.width()) // 2
                top_y = (self.height() - top_scaled.height()) // 2
                painter.drawPixmap(top_x, top_y, top_scaled)

                if self.filename:
                    font = QFont()
                    font.setPointSize(20)
                    font.setWeight(QFont.Bold)
                    font.setUnderline(True)
                    painter.setFont(font)
                    painter.setPen(QColor('#f7efdf'))

                    # Measure text width and height for proper centering
                    text_rect = painter.boundingRect(0, 0, self.width(), 0, Qt.AlignCenter, self.filename)
                    text_x = (self.width() - text_rect.width()) // 2
                    text_y = top_y + top_scaled.height() + 12  # 12px below the image

                    # Draw the text manually at calculated position
                    painter.drawText(text_x, text_y + text_rect.height(), self.filename)


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.toLocalFile().endswith(".py"):
                    event.acceptProposedAction()
                    return
        event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.endswith(".py"):
                self.set_top_image("document.png")
                self.filename = os.path.basename(file_path) 
                self.on_file_dropped(file_path)
                self.update() 
                break

class CodeComparerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Code Comparison Tool")
        self.setStyleSheet("background-color: #f7efdf;")
        self.resize(900, 600)

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # DropZone
        self.drop_zone = DropZone(self.process_python_file)

        # Results container (VBox inside a QWidget)
        self.result_boxes_layout = QVBoxLayout()
        self.result_container = QWidget()
        self.result_container.setLayout(self.result_boxes_layout)
        self.result_container.setVisible(False)  # Initially hidden
        self.run_ast_button = QPushButton("Run Higher Depth Scanner")
        self.run_ast_button.clicked.connect(lambda: self.process_python_file(self.last_file_path, algorithm_type='ast'))
        self.run_ast_button.setStyleSheet("""
            QPushButton {
                background-color: #a1887f;
                color: white;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #8d6e63;
            }
        """)
        self.run_ast_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.run_ast_button.setVisible(False)

        self.layout.addWidget(self.drop_zone)
        self.layout.addWidget(self.result_container)

        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 0)


    def process_python_file(self, file_path, algorithm_type='difflib'):
        try:
            temp_dir = tempfile.mkdtemp()
            safe_file_path = os.path.join(temp_dir, os.path.basename(file_path))
            shutil.copy(file_path, safe_file_path)

            result = cloneDetection(safe_file_path, algorithm_type)
            
            self.last_file_path = file_path

            restructuredResult = []
            for i, item in enumerate(result):
                if i >= 5:
                    break
                if algorithm_type == 'difflib':
                    for path, values in item.items():
                        restructuredResult.append({
                            "path": path,
                            "code": values[0],
                            "comments": values[1]
                        })
                elif algorithm_type == 'ast':
                    for path, similarity in item.items():
                        restructuredResult.append({
                            "path": path,
                            "code": similarity,
                        })

            while self.result_boxes_layout.count():
                item = self.result_boxes_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            for entry in restructuredResult:
                if algorithm_type == 'difflib':
                    box = QLabel(f" {os.path.basename(entry['path'])}\n Code Similarity: {entry['code']}%\n Comments Similarity: {entry['comments']}%")
                else:
                    box = QLabel(f" {os.path.basename(entry['path'])}\n Code Similarity: {entry['code']}%")
                box.setStyleSheet("""
                    background-color: #e7e1d6;
                    border-radius: 8px;
                    padding: 10px;
                    font-size: 14px;
                    color: black;
                    max-height: 60px;
                """)
                box.setAlignment(Qt.AlignLeft)
                self.result_boxes_layout.addWidget(box)
                
            self.result_boxes_layout.addWidget(self.run_ast_button)
            
            self.result_container.setVisible(True)
            self.run_ast_button.setVisible(True)
            self.layout.setStretch(0, 2) 
            self.layout.setStretch(1, 1)

        except Exception as e:
            print('❌ Error during file processing:', e)

def run_cli_mode(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_cli_mode(sys.argv[1])
    else:
        app = QApplication(sys.argv)
        window = CodeComparerApp()
        window.show()
        sys.exit(app.exec_())
