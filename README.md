# Simple Markdown Editor

A lightweight, feature-rich Markdown editor with real-time preview, file management, and export capabilities.

## Features

- **Real-time Editing**: Write Markdown with live preview
- **File Management**: 
  - Create, save, and manage multiple documents
  - Recent files sidebar for quick access
- **Export Options**:
  - Export to HTML (with embedded images)
  - Export to PDF (rendered output only)
- **Image Handling**:
  - Paste images directly from clipboard
  - Automatic image upload and embedding
- **Responsive Design**: Collapsible sidebar for more editing space
- **Auto-save**: Documents are automatically saved to local database

## Tech Stack

- **Frontend**: 
  - Editor.md (Markdown editor)
  - HTML5/CSS3
  - JavaScript (with jQuery)
  - jsPDF (PDF export)
  - html2canvas (HTML to image conversion)
- **Backend**:
  - Python Flask
  - SQLite database
- **Python**: 3.9+
- **Flask**: 2.0.2
- **Dependencies**: See requirements.txt

## Installation & Running

1. Clone the repository:
```bash
git clone https://github.com/yourusername/simple-md-editor.git
cd simple-md-editor
```

2. Create virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
source venv/bin/activate  # Windows (if using Git Bash)
venv\Scripts\activate.bat  # Windows Command Prompt
venv\Scripts\Activate.ps1  # Windows PowerShell
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and visit:
```
http://localhost:5000
```

### Docker Deployment
```bash
docker build -t markdown-editor .
docker run -d -p 5000:5000 markdown-editor
```

## Usage Guide

1. **Creating New Document**:
   - Click "+ New Document" in sidebar
   - Start typing in the editor

2. **Saving Documents**:
   - Documents auto-save when switching or closing
   - Manual save: Click "Save" button

3. **Exporting**:
   - HTML: Click "Export HTML" to download formatted HTML
   - PDF: Click "Export PDF" to download rendered PDF

4. **Image Handling**:
   - Copy an image to clipboard
   - Paste directly into the editor
   - Images will be uploaded and embedded automatically

5. **Sidebar Management**:
   - Click "◀" button to collapse/expand sidebar
   - Recent documents appear in the sidebar

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## Reporting Issues
Please use the [GitHub Issue Tracker](https://github.com/ShawnMa123/simple-md-editor/issues) to report any problems or suggest enhancements.

## License
This project is licensed under the [MIT License](LICENSE)

