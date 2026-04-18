from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QComboBox, QFrame, QGridLayout,
    QColorDialog, QMenu, QToolButton
)
from PySide6.QtCore import Qt, QTimer, QPoint, QSize
from PySide6.QtGui import QColor, QPainter, QPalette


PRESET_COLORS = [
    "#E74C3C", "#E67E22", "#F1C40F", "#2ECC71",
    "#1ABC9C", "#3498DB", "#9B59B6", "#34495E"
]


class ColorButton(QPushButton):
    def __init__(self, color="#888888", parent=None):
        super().__init__(parent)
        self._color = QColor(color)
        self.setFixedSize(28, 28)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border: 2px solid #cccccc;
                border-radius: 4px;
            }}
            QPushButton:hover {{
                border: 2px solid #888888;
            }}
        """)
    
    def get_color(self):
        return self._color.name()
    
    def set_color(self, color):
        self._color = QColor(color)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border: 2px solid #cccccc;
                border-radius: 4px;
            }}
            QPushButton:hover {{
                border: 2px solid #888888;
            }}
        """)


class MainWindow(QWidget):
    def __init__(self, storage):
        super().__init__()
        self.storage = storage
        self.running = False
        self.start_time = None
        self.current_activity_name = ""
        self.current_activity_color = "#888888"
        self.elapsed_seconds = 0
        self.drag_position = None
        
        self._init_ui()
        self._load_previous_activities()
        self._restore_window_state()
    
    def _init_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMinimumSize(280, 180)
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(6)
        
        title_bar = self._create_title_bar()
        main_layout.addWidget(title_bar)
        
        content = QFrame()
        content.setStyleSheet("""
            QFrame {
                background-color: #f5f5f5;
                border-radius: 8px;
            }
        """)
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(12, 12, 12, 12)
        content_layout.setSpacing(10)
        
        activity_layout = QHBoxLayout()
        activity_layout.setSpacing(8)
        
        self.activity_combo = QComboBox()
        self.activity_combo.setEditable(True)
        self.activity_combo.setMinimumWidth(180)
        self.activity_combo.setStyleSheet("""
            QComboBox {
                padding: 6px;
                border: 1px solid #cccccc;
                border-radius: 4px;
                background-color: white;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 6px solid #666666;
                margin-right: 5px;
            }
        """)
        self.activity_combo.currentTextChanged.connect(self._on_activity_changed)
        
        activity_layout.addWidget(self.activity_combo)
        
        self.color_btn = ColorButton("#888888")
        self.color_btn.clicked.connect(self._pick_color)
        
        activity_layout.addWidget(self.color_btn)
        
        content_layout.addLayout(activity_layout)
        
        timer_layout = QHBoxLayout()
        timer_layout.addStretch()
        
        self.timer_label = QLabel("00:00:00")
        self.timer_label.setStyleSheet("""
            QLabel {
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 28px;
                font-weight: bold;
                color: #333333;
                padding: 8px 16px;
            }
        """)
        timer_layout.addWidget(self.timer_label)
        
        timer_layout.addStretch()
        content_layout.addLayout(timer_layout)
        
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        self.toggle_btn = QPushButton("▶")
        self.toggle_btn.setFixedSize(60, 40)
        self.toggle_btn.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                background-color: #27ae60;
                color: white;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
            QPushButton:pressed {
                background-color: #1e8449;
            }
        """)
        self.toggle_btn.clicked.connect(self._toggle_timer)
        
        button_layout.addWidget(self.toggle_btn)
        
        button_layout.addStretch()
        content_layout.addLayout(button_layout)
        
        main_layout.addWidget(content)
        
        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
            }
        """)
    
    def _create_title_bar(self):
        title_bar = QFrame()
        title_bar.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
                border-radius: 8px 8px 0 0;
            }
        """)
        title_layout = QHBoxLayout(title_bar)
        title_layout.setContentsMargins(10, 4, 10, 4)
        
        title_label = QLabel("Time Logger")
        title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 12px;
                font-weight: bold;
            }
        """)
        title_layout.addWidget(title_label)
        
        title_layout.addStretch()
        
        self.menu_btn = QToolButton()
        self.menu_btn.setText("...")
        self.menu_btn.setFixedSize(24, 20)
        self.menu_btn.setStyleSheet("""
            QToolButton {
                background-color: transparent;
                color: white;
                border: none;
                font-size: 12px;
                font-weight: bold;
            }
            QToolButton:hover {
                background-color: #34495e;
            }
        """)
        
        menu = QMenu(self)
        always_on_top = self.windowFlags() & Qt.WindowStaysOnTopHint
        if always_on_top:
            action = menu.addAction("Disable Always on Top")
        else:
            action = menu.addAction("Enable Always on Top")
        action.triggered.connect(self._toggle_always_on_top)
        
        self.menu_btn.setMenu(menu)
        
        title_layout.addWidget(self.menu_btn)
        
        self.min_btn = QPushButton("─")
        self.min_btn.setFixedSize(24, 20)
        self.min_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                border: none;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
        """)
        self.min_btn.clicked.connect(self.showMinimized)
        
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(24, 20)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                border: none;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #e74c3c;
            }
        """)
        close_btn.clicked.connect(self._close_app)
        
        title_layout.addWidget(self.min_btn)
        title_layout.addWidget(close_btn)
        
        return title_bar
    
    def _load_previous_activities(self):
        activities = self.storage.get_activities()
        for activity in activities:
            self.activity_combo.addItem(activity["name"])
    
    def _restore_window_state(self):
        always_on_top = self.storage.get_always_on_top()
        if not always_on_top:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        
        position = self.storage.get_window_position()
        if position:
            self.move(position["x"], position["y"])
        else:
            self._center_on_screen()
    
    def _center_on_screen(self):
        screen = self.screen()
        geom = screen.geometry()
        x = (geom.width() - self.width()) // 2
        y = (geom.height() - self.height()) // 2
        self.move(x, y)
    
    def _on_activity_changed(self, text):
        self.current_activity_name = text
        color = self.storage.get_activity_color(text)
        self.current_activity_color = color
        self.color_btn.set_color(color)
    
    def _pick_color(self):
        dialog = QColorDialog(self)
        dialog.setWindowTitle("Select Color")
        dialog.setCurrentColor(QColor(self.current_activity_color))
        dialog.setOption(QColorDialog.DontUseNativeDialog)
        
        if dialog.exec():
            self.current_activity_color = dialog.currentColor().name()
            self.color_btn.set_color(self.current_activity_color)
    
    def _toggle_timer(self):
        if not self.running:
            if not self.current_activity_name.strip():
                self.activity_combo.setStyleSheet("""
                    QComboBox {
                        padding: 6px;
                        border: 2px solid #e74c3c;
                        border-radius: 4px;
                        background-color: white;
                    }
                """)
                return
            
            self.activity_combo.setStyleSheet("""
                QComboBox {
                    padding: 6px;
                    border: 1px solid #cccccc;
                    border-radius: 4px;
                    background-color: white;
                }
            """)
            
            self.running = True
            self.start_time = QTimer()
            self.start_time.timeout.connect(self._update_timer)
            self.start_time.start(1000)
            
            self.toggle_btn.setText("■")
            self.toggle_btn.setStyleSheet("""
                QPushButton {
                    font-size: 20px;
                    background-color: #e74c3c;
                    color: white;
                    border: none;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: #c0392b;
                }
                QPushButton:pressed {
                    background-color: #a93226;
                }
            """)
            
            if self.activity_combo.currentText():
                if self.activity_combo.findText(self.activity_combo.currentText()) == -1:
                    self.activity_combo.addItem(self.activity_combo.currentText())
                    self.storage.add_activity(
                        self.activity_combo.currentText(), 
                        self.current_activity_color
                    )
        else:
            self.running = False
            self.start_time.stop()
            
            if self.current_activity_name and self.elapsed_seconds > 0:
                self.storage.add_time(self.current_activity_name, self.elapsed_seconds)
            
            self.toggle_btn.setText("▶")
            self.toggle_btn.setStyleSheet("""
                QPushButton {
                    font-size: 20px;
                    background-color: #27ae60;
                    color: white;
                    border: none;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: #2ecc71;
                }
                QPushButton:pressed {
                    background-color: #1e8449;
                }
            """)
            
            self.elapsed_seconds = 0
            self._update_display()
    
    def _update_timer(self):
        self.elapsed_seconds += 1
        self._update_display()
    
    def _update_display(self):
        hours = self.elapsed_seconds // 3600
        minutes = (self.elapsed_seconds % 3600) // 60
        seconds = self.elapsed_seconds % 60
        self.timer_label.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    
    def _close_app(self):
        if self.running and self.elapsed_seconds > 0:
            self.storage.add_time(self.current_activity_name, self.elapsed_seconds)
        
        pos = self.pos()
        self.storage.set_window_position(pos.x(), pos.y())
        
        self.close()
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
        elif event.button() == Qt.RightButton:
            self._show_context_menu(event.globalPosition())
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_position:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()
    
    def mouseReleaseEvent(self, event):
        self.drag_position = None
    
    def _show_context_menu(self, pos):
        menu = QMenu(self)
        
        always_on_top = self.windowFlags() & Qt.WindowStaysOnTopHint
        if always_on_top:
            action = menu.addAction("Disable Always on Top")
        else:
            action = menu.addAction("Enable Always on Top")
        
        action.triggered.connect(self._toggle_always_on_top)
        
        menu.exec(pos.x(), pos.y())
    
    def _toggle_always_on_top(self):
        if self.windowFlags() & Qt.WindowStaysOnTopHint:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.storage.set_always_on_top(False)
        else:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.storage.set_always_on_top(True)
        
        self.show()