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
venv\Scripts\activate    # Windows
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

## License

