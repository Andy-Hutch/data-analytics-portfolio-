from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import os

# Ensure reports folder exists
os.makedirs("reports", exist_ok=True)

def generate_pdf_report():
    report_file = "reports/chapter_growth_report.pdf"
    doc = SimpleDocTemplate(report_file, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("Chapter Growth & Expansion Report", styles['Title']))
    elements.append(Spacer(1, 0.2*inch))

    # Summary text
    summary_text = """
    This report provides an analysis of chapter growth and expansion across different regions.
    The charts below highlight student recruitment trends, the impact of events on growth, 
    and chapter-level performance month by month. These insights can guide future outreach,
    resource allocation, and recruitment strategies.
    """
    elements.append(Paragraph(summary_text, styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))

    # Insert charts into the PDF
    charts_to_include = [
        "reports/student_growth_over_time.png",
        "reports/chapter_distribution.png",
        "reports/charts/events_vs_students.png",
        "reports/charts/students_distribution.png",
        "reports/charts/monthly_growth_heatmap.png",
    ]

    for chart in charts_to_include:
        if os.path.exists(chart):
            elements.append(Image(chart, width=6*inch, height=4*inch))
            elements.append(Spacer(1, 0.2*inch))

    # Closing note
    closing_text = """
    Recommendation: Focus recruitment efforts on high-performing chapters while 
    providing additional support to underperforming ones. Events have shown a strong 
    correlation with new student growth, so continued investment in event-driven outreach 
    is recommended.
    """
    elements.append(Paragraph(closing_text, styles['Normal']))

    # Build PDF
    doc.build(elements)
    print(f"PDF report generated: {report_file}")

if __name__ == "__main__":
    generate_pdf_report()
