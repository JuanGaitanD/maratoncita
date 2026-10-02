#!/usr/bin/env python3
"""Genera el PDF de impresión (tamaño carta, blanco y negro) con todos los ejercicios del repo.

Uso: python tools/build_pdf.py [salida.pdf]
Recorre cada carpeta que tenga problems.json, arma una portada con índice
(número, letra, problema, evento, tema, complejidad, página) y luego una
sección por problema: resumen, explicación, código Python y código C++.
Las tablas de valores precalculados se sustituyen por una referencia al archivo.
"""
import glob, json, os, re, sys
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, Preformatted,
                                SimpleDocTemplate, Spacer, Table, TableStyle)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "Ejercicios-maraton.pdf")

ss = getSampleStyleSheet()
BLACK = colors.black
H1 = ParagraphStyle("h1", parent=ss["Title"], fontSize=22, spaceAfter=6, textColor=BLACK)
H2 = ParagraphStyle("h2", parent=ss["Heading2"], fontSize=13, spaceBefore=4, spaceAfter=2, textColor=BLACK)
H3 = ParagraphStyle("h3", parent=ss["Heading3"], fontSize=10, spaceBefore=6, spaceAfter=2, textColor=BLACK)
BODY = ParagraphStyle("body", parent=ss["BodyText"], fontSize=9, leading=11.5, textColor=BLACK)
SMALL = ParagraphStyle("small", parent=BODY, fontSize=7.5, leading=9)
CELL = ParagraphStyle("cell", parent=BODY, fontSize=7, leading=8.5)
CODE = ParagraphStyle("code", fontName="Courier", fontSize=7, leading=8.2, leftIndent=2, textColor=BLACK)
CENTER = ParagraphStyle("c", parent=BODY, alignment=TA_CENTER)


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def event_title(folder):
    p = os.path.join(folder, "README.md")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            if line.startswith("# "):
                return line[2:].strip()
    return os.path.basename(folder)


def load():
    items = []
    for pj in sorted(glob.glob(os.path.join(ROOT, "*", "problems.json"))):
        folder = os.path.dirname(pj)
        title = event_title(folder)
        for p in json.load(open(pj, encoding="utf-8")):
            p["folder"] = folder
            p["event"] = title
            p["short_event"] = os.path.basename(folder)
            items.append(p)
    return items


class Doc(SimpleDocTemplate):
    """Registra en self.pages la página real donde se dibuja el título de cada problema."""

    def __init__(self, *a, **k):
        self.pages = k.pop("pages")
        super().__init__(*a, **k)

    def afterFlowable(self, fl):
        key = getattr(fl, "prob_key", None)
        if key is not None:
            self.pages[key] = self.page


NUMS = re.compile(r"^[\s\[\]\{\}]*-?\d[\d,\s\-\.\[\]\{\}]*$")
LONG = re.compile(r"^(.*?[=\{\[]\s*)([\[\{]?\s*-?\d[\d,\s\-\.]{200,})(.*)$")


def collapse_tables(src, fname):
    """Sustituye literales largos de números precalculados por una referencia al archivo del repo."""
    out, lines, i = [], src.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        m = LONG.match(ln)
        if m:
            cnt = len(re.findall(r"-?\d+", m.group(2)))
            out.append(f"{m.group(1)}[... {cnt} valores precalculados: ver {fname} en el repositorio ...]{m.group(3)}")
            i += 1
            continue
        j = i
        while j < len(lines) and lines[j].strip() and NUMS.match(lines[j]):
            j += 1
        cnt = sum(len(re.findall(r"-?\d+", l)) for l in lines[i:j])
        if j - i >= 4 and cnt >= 20:
            out.append(f"    [... {cnt} valores precalculados: ver {fname} en el repositorio ...]")
            i = j
            continue
        out.append(ln)
        i += 1
    return "\n".join(out)


def code_block(path):
    if not os.path.exists(path):
        return [Paragraph("<i>(no disponible)</i>", SMALL)]
    src = open(path, encoding="utf-8", errors="replace").read().rstrip("\n")
    src = collapse_tables(src, os.path.basename(path))
    return [Preformatted(src, CODE, maxLineLength=118)]


def build(items, pages, out, shown):
    doc = Doc(out, pages=pages, pagesize=letter, leftMargin=1.5 * cm, rightMargin=1.5 * cm,
              topMargin=1.5 * cm, bottomMargin=1.5 * cm,
              title="Ejercicios de maratón de programación", author="JuanGaitanD")
    story = [Paragraph("Ejercicios de maratón de programación", H1),
             Paragraph("Soluciones en Python 3 y C++11 con explicación breve. Material de apoyo para competencia.", CENTER),
             Spacer(1, 8)]
    rows = [["#", "L", "Problema", "Evento", "Tema", "Tiempo", "Pág."]]
    for i, p in enumerate(items, 1):
        rows.append([str(i), p.get("letter", "-"), Paragraph(esc(p["name"]), CELL),
                     Paragraph(esc(p["short_event"]), CELL), Paragraph(esc(p.get("topic", "")), CELL),
                     Paragraph(esc(p.get("time_complexity", "")), CELL), str(shown.get(i, ""))])
    t = Table(rows, colWidths=[0.8 * cm, 0.7 * cm, 5.0 * cm, 3.6 * cm, 4.2 * cm, 2.6 * cm, 1.0 * cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 7.5), ("FONT", (0, 1), (-1, -1), "Helvetica", 7),
        ("TEXTCOLOR", (0, 0), (-1, -1), BLACK),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dddddd")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f2f2f2")]),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (1, -1), "CENTER"), ("ALIGN", (-1, 0), (-1, -1), "RIGHT"),
        ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5)]))
    story += [t, PageBreak()]
    for i, p in enumerate(items, 1):
        hdr = f"{i}. {p.get('letter', '-')}. {esc(p['name'])}"
        meta = (f"<b>Evento:</b> {esc(p['event'])} &nbsp;&nbsp; <b>Tema:</b> {esc(p.get('topic', ''))} &nbsp;&nbsp; "
                f"<b>Tiempo:</b> {esc(p.get('time_complexity', ''))} &nbsp;&nbsp; <b>Memoria:</b> {esc(p.get('memory', ''))} &nbsp;&nbsp; "
                f"<b>Archivo:</b> {esc(p['file'])}.py / .cpp &nbsp;&nbsp; <b>Estado:</b> {esc(p.get('status', ''))}")
        title = Paragraph(hdr, H2)
        title.prob_key = i
        head = [title, Paragraph(meta, SMALL)]
        if p.get("summary"):
            head += [Paragraph("<b>Enunciado:</b> " + esc(p["summary"]), BODY)]
        head += [Paragraph("<b>Solución:</b> " + esc(p.get("explanation", "")), BODY)]
        story += [KeepTogether(head)]
        story += [Paragraph("Python 3", H3)] + code_block(os.path.join(p["folder"], p["file"] + ".py"))
        story += [Paragraph("C++11", H3)] + code_block(os.path.join(p["folder"], p["file"] + ".cpp"))
        story += [Spacer(1, 10)]

    def footer(canv, d):
        canv.saveState()
        canv.setFont("Helvetica", 7)
        canv.setFillColor(BLACK)
        canv.drawRightString(letter[0] - 1.5 * cm, 0.9 * cm, str(canv.getPageNumber()))
        canv.drawString(1.5 * cm, 0.9 * cm, "github.com/JuanGaitanD/maratoncita")
        canv.restoreState()

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    items = load()
    pages = {}
    for _ in range(6):  # repetir hasta que el índice y las páginas reales coincidan
        shown = dict(pages)
        pages = {}
        build(items, pages, OUT, shown)
        if pages == shown:
            break
    else:
        print("AVISO: la numeración del índice no convergió")
    print(f"{len(items)} problemas -> {OUT}")
