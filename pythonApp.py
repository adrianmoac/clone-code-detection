import sys
import os
import tempfile
import shutil
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QHBoxLayout, QTextEdit
)
from PyQt5.QtCore import Qt, QMimeData
from main import main as cloneDetection

class DropZone(QLabel):
    def __init__(self, on_file_dropped):
        super().__init__("⬇️ Drag a Python (.py) file here ⬇️")
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("border: 2px dashed #888; padding: 40px; font-size: 16px;")
        self.on_file_dropped = on_file_dropped

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
                self.on_file_dropped(file_path)
                break


class CodeComparerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Code Comparison Tool")
        self.resize(900, 600)

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # Left Panel
        self.info_panel = QTextEdit()
        self.info_panel.setReadOnly(True)
        self.info_panel.setStyleSheet("background-color: #f4f4f4; padding: 10px;")
        self.info_panel.setText("📝 Waiting for a Python file to be dropped...")
        self.layout.addWidget(self.info_panel, 2)

        # Right Panel
        self.right_panel = QVBoxLayout()
        self.drop_zone = DropZone(self.process_python_file)
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)

        self.right_panel.addWidget(self.drop_zone)
        self.right_panel.addWidget(self.result_display)

        container = QWidget()
        container.setLayout(self.right_panel)
        self.layout.addWidget(container, 3)

    def process_python_file(self, file_path):
        self.info_panel.setText(f"Processing file: {file_path}")
        self.result_display.setText("🔄 Running the script...")

        try:
            # Create a temp copy of the file to avoid _MEI temp issues
            temp_dir = tempfile.mkdtemp()
            safe_file_path = os.path.join(temp_dir, os.path.basename(file_path))
            shutil.copy(file_path, safe_file_path)

            result = cloneDetection(safe_file_path)
            self.result_display.setText(f"✅ Output:\n\n{result}")

            self.info_panel.setText("✅ File processed successfully.")
        except Exception as e:
            self.result_display.setText(f"❌ Error:\n{e}")
            self.info_panel.setText("❌ Error during execution.")

def run_cli_mode(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_cli_mode(sys.argv[1])
    else:
        # Run the GUI app
        app = QApplication(sys.argv)
        window = CodeComparerApp()
        window.show()
        sys.exit(app.exec_())
