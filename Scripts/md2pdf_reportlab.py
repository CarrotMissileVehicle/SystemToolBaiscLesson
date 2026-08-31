#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import re
import sys

def parse_markdown(md_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    elements = []
    lines = content.split('\n')
    in_code_block = False
    code_lines = []
    in_table = False
    table_rows = []
    
    for line in lines:
        if line.startswith('```'):
            if in_code_block:
                elements.append(('code', '\n'.join(code_lines)))
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            continue
        
        if in_code_block:
            code_lines.append(line)
            continue
        
        if line.startswith('|'):
            if not in_table:
                in_table = True
                table_rows = []
            if '---' in line:
                continue
            cells = [c.strip() for c in line.split('|')[1:-1]]
            table_rows.append(cells)
            if line.rstrip().endswith('|'):
                elements.append(('table', table_rows[:]))
                table_rows = []
                in_table = False
        else:
            if in_table and table_rows:
                elements.append(('table', table_rows))
                table_rows = []
                in_table = False
        
        if line.startswith('# ') and not line.startswith('## '):
            elements.append(('h1', line[2:].strip()))
        elif line.startswith('## ') and not line.startswith('### '):
            elements.append(('h2', line[3:].strip()))
        elif line.startswith('### '):
            elements.append(('h3', line[4:].strip()))
        elif line.startswith('---'):
            elements.append(('hr', ''))
        elif line.strip():
            elements.append(('text', line))
        else:
            elements.append(('empty', ''))
    
    if in_table and table_rows:
        elements.append(('table', table_rows))
    
    return elements

def md_to_pdf(md_file, pdf_file):
    doc = SimpleDocTemplate(pdf_file, pagesize=A4)
    styles = getSampleStyleSheet()
    
    custom_styles = {
        'h1': ParagraphStyle('CustomH1', parent=styles['Heading1'], fontSize=18, spaceAfter=12),
        'h2': ParagraphStyle('CustomH2', parent=styles['Heading2'], fontSize=14, spaceAfter=10),
        'h3': ParagraphStyle('CustomH3', parent=styles['Heading3'], fontSize=12, spaceAfter=8),
        'text': ParagraphStyle('CustomText', parent=styles['Normal'], fontSize=11, spaceAfter=6),
        'code': ParagraphStyle('CustomCode', parent=styles['Code'], fontSize=9, backColor=colors.grey),
    }
    
    story = []
    
    for elem_type, content in parse_markdown(md_file):
        if elem_type == 'h1':
            story.append(Paragraph(content, custom_styles['h1']))
        elif elem_type == 'h2':
            story.append(Paragraph(content, custom_styles['h2']))
        elif elem_type == 'h3':
            story.append(Paragraph(content, custom_styles['h3']))
        elif elem_type == 'text':
            clean = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', content)
            clean = re.sub(r'`(.*?)`', r'<font face="Courier">\1</font>', clean)
            story.append(Paragraph(clean, custom_styles['text']))
        elif elem_type == 'code':
            code_html = content.replace('\n', '<br/>')
            story.append(Paragraph(code_html, custom_styles['code']))
        elif elem_type == 'table':
            if content:
                table = Table(content)
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 9),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ]))
                story.append(table)
                story.append(Spacer(1, 12))
        elif elem_type == 'empty':
            story.append(Spacer(1, 6))
    
    doc.build(story)
    print(f"转换成功: {pdf_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python md2pdf_reportlab.py input.md output.pdf")
        sys.exit(1)
    
    md_to_pdf(sys.argv[1], sys.argv[2])