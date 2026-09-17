from pathlib import Path

from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "output" / "pdf" / "CampusRide_Written_Submission.pdf"

FONT_DIR = Path("/System/Library/Fonts/Supplemental")
pdfmetrics.registerFont(TTFont("TimesNR", str(FONT_DIR / "Times New Roman.ttf")))
pdfmetrics.registerFont(TTFont("TimesNR-Bold", str(FONT_DIR / "Times New Roman Bold.ttf")))
pdfmetrics.registerFontFamily(
    "TimesNR",
    normal="TimesNR",
    bold="TimesNR-Bold",
)


def page_setup(canvas, doc):
    canvas.saveState()
    canvas.setTitle("CampusRide Written Submission")
    canvas.setAuthor("Arnav Jain")
    canvas.setSubject("Pitch to Prototype Written Submission")
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=letter,
    leftMargin=1.0 * inch,
    rightMargin=1.0 * inch,
    topMargin=0.38 * inch,
    bottomMargin=0.45 * inch,
    title="CampusRide Written Submission",
    author="Arnav Jain",
)

normal = ParagraphStyle(
    "Normal",
    fontName="TimesNR",
    fontSize=11.75,
    leading=15.0,
    textColor="#000000",
    alignment=TA_LEFT,
    spaceAfter=0,
    splitLongWords=False,
)

name_style = ParagraphStyle(
    "Name",
    parent=normal,
    fontSize=11.85,
    leading=15,
)

heading = ParagraphStyle(
    "Heading",
    parent=normal,
    fontName="TimesNR-Bold",
    fontSize=12.0,
    leading=15.0,
    spaceBefore=11,
    spaceAfter=7,
    keepWithNext=True,
)

bullet = ParagraphStyle(
    "Bullet",
    parent=normal,
    leftIndent=36,
    firstLineIndent=0,
    bulletIndent=18,
    bulletFontName="TimesNR",
    bulletFontSize=11.4,
    spaceAfter=1.5,
)

iteration_title = ParagraphStyle(
    "IterationTitle",
    parent=normal,
    leftIndent=36,
    bulletIndent=18,
    bulletFontName="TimesNR",
    bulletFontSize=11.4,
    spaceBefore=2,
    spaceAfter=1.5,
    keepWithNext=True,
)

nested = ParagraphStyle(
    "Nested",
    parent=normal,
    leftIndent=72,
    firstLineIndent=0,
    bulletIndent=54,
    bulletFontName="TimesNR",
    bulletFontSize=10.8,
    spaceAfter=1.3,
)

paragraph = ParagraphStyle(
    "Paragraph",
    parent=normal,
    fontSize=11.75,
    leading=15.1,
    spaceAfter=6,
)


def h(text):
    return Paragraph(text, heading)


def b(text):
    return Paragraph(text, bullet, bulletText="•")


def it(text):
    return Paragraph(text, iteration_title, bulletText="•")


def sub(text):
    return Paragraph(text, nested, bulletText="○")


story = [
    Paragraph("Arnav Jain", name_style),
    Spacer(1, 25),
    h("A. MVP Goal &amp; Results"),
    b("<b>Driver trip publishing:</b> Met. A student can enter trip details and publish a new ride card in under two minutes."),
    b("<b>Ride discovery and contact:</b> Partially Met. Filters and trip details work, but request and message actions do not reach a real driver."),
    b("<b>Three coordinated weekend trips:</b> Not Met. Three routes are displayed, but no real trips have been scheduled through a persistent backend."),
    h("B. Current Product"),
    b("<b>Interactive Route Map:</b> Pan, zoom, and view road routes from UT Austin to three Texas metros."),
    b("<b>Ride Discovery:</b> Filter listings through search, destination chips, map markers, or cards."),
    b("<b>Ride Details:</b> Review pickup area, time, seats, arrival estimate, and driver information."),
    b("<b>Post a Ride:</b> Enter trip details and add a new listing to the current session."),
    b("<b>Responsive Experience:</b> The map, dialogs, filters, and confirmations adapt to desktop and mobile."),
    h("C. Technical &amp; Product Docs"),
    b("<b>Tools:</b> HTML, CSS, JavaScript, MapLibre, CARTO tiles, OSRM routing, and OpenAI Sites."),
    b("<b>Implemented:</b> Responsive UI, map controls, destination markers, road routes, filtering, trip details, and session-local ride creation."),
    b("<b>Mocked:</b> Student profiles, .edu verification, ride history, seats, sponsor content, and listing data."),
    b("<b>Incomplete:</b> There is no database, authentication, notification delivery, real messaging, or booking state."),
    b("<b>Key Decisions:</b> Keep the product free and map-first, use a dark gold visual system, and exclude payments and navigation."),
    b("<b>Limitations:</b> New rides reset on refresh, only three metros are mapped, and map data requires network access."),
    h("D. Requirements"),
    Paragraph(
        "The rider workflow starts at UT Austin: choose Dallas, Houston, or San Antonio; inspect the route and matching trip; open the details; then request a seat or message the driver. The driver workflow collects destination, date, time, pickup area, and open seats, then adds the listing to the feed. The MVP is only for verified university students and remains free to use.",
        paragraph,
    ),
    PageBreak(),
    Paragraph(
        "Significant prompts emphasized building the product instead of a marketing page, matching the clarity of the Robotaxi app, replacing the static map with a movable map API, accurately pinning locations, and changing the accent from green to gold. Pitch constraints include a web-only MVP, no payments, no native navigation, and no public accounts. The prototype assumes UT Austin as the origin, three known metro destinations, available map services, and no production user data.",
        paragraph,
    ),
    h("E. Iteration &amp; Learning"),
    it("<b>Map Accuracy:</b>"),
    sub("<b>Before:</b> The first version used a fixed illustrated map with approximate markers."),
    sub("<b>Learning:</b> A rideshare interface needs accurate locations and direct map control."),
    sub("<b>Change:</b> I added MapLibre, CARTO tiles, OSRM routes, and synchronized map/list selection."),
    sub("<b>Result:</b> Users can drag, zoom, compare destinations, and see the road path."),
    it("<b>Visual Direction:</b>"),
    sub("<b>Before:</b> The main accent was a bright greenish color."),
    sub("<b>Learning:</b> The reference uses restrained charcoal surfaces and warm metallic gold."),
    sub("<b>Change:</b> I remapped buttons, markers, routes, and selected states to one gold system."),
    sub("<b>Result:</b> The interface feels more cohesive and closer to the Robotaxi direction."),
    h("F. Reflection"),
    b("<b>Biggest Remaining Risk:</b> Verified identity may not create punctual drivers, and there is no real behavioral data yet."),
    b("<b>What I Would Change Next:</b> Add persistence, .edu authentication, real messaging and booking states, then test five routes with 25 students."),
    b("<b>What I Learned:</b> Visual polish helps, but trust only becomes real when map data, listings, and contact actions work together end to end."),
]

doc.build(story, onFirstPage=page_setup, onLaterPages=page_setup)
print(OUTPUT)
