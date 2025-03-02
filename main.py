from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QComboBox, QProgressBar, QTextEdit, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("音階練習アプリ")
    self.setGeometry(100, 100, 400, 500)
    self.setStyleSheet("background-color: #1E1E2E; color: white;")

    layout = QVBoxLayout()

    # タイトル
    self.title = QLabel("音階練習アプリ")
    self.title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
    self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.title)

    # 音階選択
    self.combo_box = QComboBox()
    self.combo_box.addItems(
        ["ド↓レ↓ド↓", "レミレ", "ミファミ", "ファソファ", "ソラソ", "ラシラ", "シドシ", "ド↑レ↑ド↑"]
    )
    self.combo_box.setStyleSheet(
        "background-color: #2E2E3E; color: white; padding: 7px;")
    layout.addWidget(self.combo_box)

    # 再生ボタン
    self.play_button = QPushButton("再生")
    self.play_button.setStyleSheet(
        "background-color: #4A90E2; color: white; padding: 10px; border-radius: 5px;")
    layout.addWidget(self.play_button)

    # 録音ボタン
    self.record_button = QPushButton("録音")
    self.record_button.setStyleSheet(
        "background-color: #E94E77; color: white; padding: 10px; border-radius: 5px;")
    layout.addWidget(self.record_button)

    # 判定結果
    self.result = QLabel("結果: ")
    self.result.setFont(QFont("Arial", 12))
    layout.addWidget(self.result)

    # 一致率バーと数値
    progress_layout = QHBoxLayout()
    self.match_bar = QProgressBar()
    self.match_bar.setRange(0, 100)
    self.match_bar.setValue(0)
    self.match_bar.setTextVisible(False)
    self.match_bar.setStyleSheet("""
      QProgressBar {
        background-color: #2E2E3E; 
        color: white; 
        border-radius: 10px;
      }
      QProgressBar::chunk { 
        background-color: #4A90E2;
        border-radius: 10px;
        }
    """)
    self.percent_label = QLabel("0%")
    self.percent_label.setFont(QFont("Arial", 10))
    self.match_bar.valueChanged.connect(self.update_percent_label)
    progress_layout.addWidget(self.match_bar)
    progress_layout.addWidget(self.percent_label)
    layout.addLayout(progress_layout)

    # 詳細結果
    self.detail_result = QTextEdit()
    self.detail_result.setReadOnly(True)
    self.detail_result.setStyleSheet(
        "background-color: #2E2E3E; color: white; padding: 5px;")
    layout.addWidget(self.detail_result)

    self.setLayout(layout)

  def update_percent_label(self, value):
    self.percent_label.setText(f"{value}%")

if __name__ == "__main__":
  app = QApplication([])
  window = MainWindow()
  window.show()
  app.exec()
