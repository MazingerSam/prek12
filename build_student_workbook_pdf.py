import sys
sys.stdout.reconfigure(encoding='utf-8')
import os, json
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

font_path = 'C:\\Windows\\Fonts\\msjh.ttc'
pdfmetrics.registerFont(TTFont('MSJH', font_path))

pdf_filename = 'Elementary_Math_Student_Workbook_20Units_Master.pdf'
doc = SimpleDocTemplate(pdf_filename, pagesize=A4, rightMargin=28, leftMargin=28, topMargin=28, bottomMargin=28)

styles = getSampleStyleSheet()

PRIMARY_COLOR = colors.HexColor('#FF6B6B')
SECONDARY_COLOR = colors.HexColor('#4ECDC4')
ACCENT_COLOR = colors.HexColor('#FFE66D')
BG_LIGHT_GREEN = colors.HexColor('#E8F8F5')
BG_LIGHT_YELLOW = colors.HexColor('#FFFDE7')
DARK_TEXT = colors.HexColor('#2D3436')

title_style = ParagraphStyle('T1', fontName='MSJH', fontSize=14, leading=18, textColor=colors.white, alignment=1)
subtitle_style = ParagraphStyle('T2', fontName='MSJH', fontSize=11, leading=15, textColor=colors.HexColor('#2C3E50'), spaceAfter=3)
body_style = ParagraphStyle('B1', fontName='MSJH', fontSize=8.5, leading=12, textColor=DARK_TEXT, spaceAfter=2)
story_box_style = ParagraphStyle('S1', fontName='MSJH', fontSize=8.5, leading=12, textColor=colors.HexColor('#7D6608'))
prob_title_style = ParagraphStyle('P1', fontName='MSJH', fontSize=9, leading=13, textColor=colors.HexColor('#2563EB'), spaceAfter=2)

with open('units_curriculum_master.json', 'r', encoding='utf-8') as f:
    master_units = json.load(f)

with open('student_workbooks_data/all_20_units_workbook_questions.json', 'r', encoding='utf-8') as f:
    exercises_data = json.load(f)

img_map = {
    1: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u1_kids_cubes_1785564305661.jpg',
        'tool': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u1_math_tools_1785564317842.jpg'
    },
    2: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u2_story_image_1785566040323.jpg',
        'tool': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u2_tool_image_1785566053183.jpg'
    },
    3: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u3_story_img_1785566232221.jpg',
        'tool': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u3_tool_img_1785566245503.jpg'
    },
    4: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u4_story_img_1785566257369.jpg',
        'tool': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u4_tool_img_1785566269869.jpg'
    },
    5: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u5_story_img_1785566282253.jpg',
        'tool': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u5_tool_img_1785566292438.jpg'
    },
    6: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u6_story_img_1785627561669.jpg',
        'tool': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u6_tool_img_1785627570880.jpg'
    },
    7: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u7_story_img_1785627580711.jpg',
        'tool': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u7_tool_img_1785627589340.jpg'
    },
    8: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u8_story_img_1785566306130.jpg',
        'tool': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u8_tool_img_1785566320532.jpg'
    },
    9: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u9_story_img_1785627598616.jpg',
        'tool': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u9_tool_img_1785627607953.jpg'
    },
    10: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u10_story_img_1785627619176.jpg',
        'tool': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u10_tool_img_1785627628065.jpg'
    },
    11: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u11_story_img_1785627638402.jpg',
        'tool': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u11_tool_img_1785627648465.jpg'
    },
    12: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u12_story_img_1785627657624.jpg',
        'tool': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u12_tool_img_1785627668217.jpg'
    },
    13: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u13_storybook_art_1785674582489.jpg',
        'tool': r'generated_art\u13_tool_img.jpg'
    },
    14: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u14_storybook_art_1785674597616.jpg',
        'tool': r'generated_art\u14_tool_img.jpg'
    },
    15: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u15_storybook_art_1785674613394.jpg',
        'tool': r'generated_art\u15_tool_img.jpg'
    },
    16: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u16_storybook_art_1785674627076.jpg',
        'tool': r'generated_art\u16_tool_img.jpg'
    },
    17: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u17_storybook_art_1785674638220.jpg',
        'tool': r'generated_art\u17_tool_img.jpg'
    },
    18: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u18_storybook_art_1785674651424.jpg',
        'tool': r'generated_art\u18_tool_img.jpg'
    },
    19: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u19_storybook_art_1785674663872.jpg',
        'tool': r'generated_art\u19_tool_img.jpg'
    },
    20: {
        'story': r'C:\Users\sam09\.gemini\antigravity\brain\5ae608de-07be-4df4-a7cf-be16204fca3b\u20_storybook_art_1785674675411.jpg',
        'tool': r'generated_art\u20_tool_img.jpg'
    }
}

story = []

# Front cover
cover_title = ParagraphStyle('CT', fontName='MSJH', fontSize=22, leading=26, textColor=PRIMARY_COLOR, alignment=1)
cover_sub = ParagraphStyle('CS', fontName='MSJH', fontSize=12, leading=16, textColor=colors.HexColor('#2C3E50'), alignment=1)

story.append(Spacer(1, 40))
story.append(Paragraph('<b>🌈 兒童數學皮克斯美工繪本與學生練習作業本</b>', cover_title))
story.append(Spacer(1, 10))
story.append(Paragraph('<b>全套 20 單元 — 每單元 10 題課堂練習 + 2 題作業 (充足計算留白空間)</b>', cover_sub))
story.append(Spacer(1, 30))

for m_u, e_u in zip(master_units, exercises_data):
    u = m_u['unit']
    unit_title = m_u['title']
    target = m_u['target']
    math_check = m_u['math_check']
    story_text = m_u['story'].replace('\n', '<br/>')
    
    # 1. Header Banner
    header_str = f'<b>第 {u} 單元：{unit_title}</b>'
    header_table = Table([[Paragraph(header_str, title_style)]], colWidths=[538])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), PRIMARY_COLOR if u%2!=0 else SECONDARY_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 6))
    
    # 2. Cover Storybook Artwork
    if u in img_map and os.path.exists(img_map[u]['story']):
        story.append(Image(img_map[u]['story'], width=340, height=210))
        story.append(Spacer(1, 6))
        
    # 3. Story Card
    story_card_str = f'<b>📖 【童話繪本故事引導】</b><br/>{story_text}'
    story_table = Table([[Paragraph(story_card_str, story_box_style)]], colWidths=[538])
    story_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT_YELLOW),
        ('BOX', (0,0), (-1,-1), 1.2, ACCENT_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(story_table)
    story.append(Spacer(1, 6))
    
    # 4. Tool Diagram Image
    if u in img_map and os.path.exists(img_map[u]['tool']):
        story.append(Image(img_map[u]['tool'], width=320, height=150))
        story.append(Spacer(1, 6))
        
    # 5. Practice Problems (10 Problems with Workspace)
    story.append(Paragraph('<b>📝 【課堂學生練習題（共 10 題，請在留白處畫圖或計算）】</b>', subtitle_style))
    story.append(Spacer(1, 4))
    
    for p in e_u['practice_problems']:
        p_num = p['id']
        q_text = p['question']
        eq_text = p['equation']
        
        p_cell_text = '<b>' + q_text + '</b><br/>算式：<b>' + eq_text + '</b><br/><font color="#888888">【學生計算與思考畫圖空間】：</font>'
        p_table = Table([[Paragraph(p_cell_text, prob_title_style)]], colWidths=[538], rowHeights=[75])
        p_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#93C5FD')),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(p_table)
        story.append(Spacer(1, 5))
        
    story.append(Spacer(1, 4))
    
    # 6. Homework Problems (2 Problems with Large Workspace)
    story.append(Paragraph('<b>🏠 【課後回家作業（共 2 題，請詳細記錄思考與畫圖過程）】</b>', subtitle_style))
    story.append(Spacer(1, 4))
    
    for h in e_u['homework_problems']:
        h_num = h['id']
        hq_text = h['question']
        
        h_cell_text = '<b>' + hq_text + '</b><br/><font color="#888888">算式：_____________________</font><br/><font color="#888888">【完整作業答題與計算/畫圖解題空間】：</font><br/><br/><br/><font color="#888888">答：_____________________</font>'
        h_table = Table([[Paragraph(h_cell_text, prob_title_style)]], colWidths=[538], rowHeights=[120])
        h_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F9FAFB')),
            ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#10B981')),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(h_table)
        story.append(Spacer(1, 6))
        
    if u < 20:
        story.append(PageBreak())

doc.build(story)
print('Master Student Workbook PDF Generated Successfully:', pdf_filename)
