from flask import Flask, render_template, request, jsonify, send_from_directory
import database as db
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

# 初始化数据库
db.init_db()


@app.route('/')
def index():
    return render_template('editor.html')


# 获取文档列表
@app.route('/api/documents', methods=['GET'])
def list_documents():
    # 获取最近编辑的10个文档
    return jsonify(db.get_documents(limit=10))


# 获取单篇文档
@app.route('/api/documents/<int:doc_id>', methods=['GET'])
def get_document(doc_id):
    doc = db.get_document(doc_id)
    if doc:
        return jsonify(doc)
    return jsonify({'error': 'Document not found'}), 404


import re

# 清理文件名函数
def clean_filename(filename):
    # 移除非法字符
    cleaned = re.sub(r'[\\/*?:"<>|]', '', filename)
    # 替换空格为下划线
    cleaned = cleaned.replace(' ', '_')
    # 限制文件名长度
    return cleaned[:50] if len(cleaned) > 50 else cleaned

# 保存文档
@app.route('/api/documents/<int:doc_id>', methods=['POST'])
def save_document(doc_id):
    data = request.get_json()
    title = data.get('title') or "Untitled"
    content = data.get('content')

    # 确保documents目录存在
    documents_dir = os.path.join(app.root_path, 'documents')
    if not os.path.exists(documents_dir):
        os.makedirs(documents_dir)

    if doc_id == 0:  # 新建文档
        doc_id = db.create_document(title, content)
        # 清理文件名
        safe_filename = clean_filename(title)
        # 保存到文件系统
        file_path = os.path.join(documents_dir, f'{safe_filename}_{doc_id}.md')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return jsonify({'id': doc_id}), 201
    else:  # 更新文档
        if db.update_document(doc_id, title, content):
            # 清理文件名
            safe_filename = clean_filename(title)
            # 保存到文件系统
            file_path = os.path.join(documents_dir, f'{safe_filename}_{doc_id}.md')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return jsonify({'success': True}), 200
        return jsonify({'error': 'Save failed'}), 500


# 图片上传
@app.route('/api/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'success': 0, 'message': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': 0, 'message': 'No selected file'})

    if file:
        filename = file.filename
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        return jsonify({
            'success': 1,
            'message': 'Uploaded successfully',
            'url': f'/static/images/{filename}'
        })


# 获取图片
@app.route('/static/images/<filename>')
def get_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
