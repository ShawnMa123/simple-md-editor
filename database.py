import sqlite3
from contextlib import closing

DATABASE = 'documents.db'
SCHEMA = """
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL DEFAULT 'Untitled',
    content TEXT NOT NULL DEFAULT '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

def init_db():
    with closing(connect()) as conn:
        with conn:
            conn.execute(SCHEMA)

def connect():
    return sqlite3.connect(DATABASE)

def get_documents(limit=10):
    """获取最近编辑的文档列表"""
    with closing(connect()) as conn:
        cursor = conn.execute('''
            SELECT id, title, created_at, updated_at
            FROM documents
            ORDER BY updated_at DESC
            LIMIT ?
        ''', (limit,))
        return [
            {'id': row[0], 'title': row[1],
             'created_at': row[2], 'updated_at': row[3]}
            for row in cursor.fetchall()
        ]

def get_document(doc_id):
    with closing(connect()) as conn:
        cursor = conn.execute('''
            SELECT id, title, content, created_at, updated_at 
            FROM documents WHERE id = ?
        ''', (doc_id,))
        row = cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'title': row[1],
                'content': row[2],
                'created_at': row[3],
                'updated_at': row[4]
            }
        return None

def create_document(title, content):
    with closing(connect()) as conn:
        with conn:
            cursor = conn.execute(
                'INSERT INTO documents (title, content) VALUES (?, ?)',
                (title, content)
            )
            return cursor.lastrowid

def update_document(doc_id, title, content):
    with closing(connect()) as conn:
        with conn:
            cursor = conn.execute('''
                UPDATE documents 
                SET title = ?, content = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (title, content, doc_id))
            return cursor.rowcount > 0
