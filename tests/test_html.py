
from pathlib import Path
import unittest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
HTML_FILE = PROJECT_ROOT / "index.html"


class TestHTMLPage(unittest.TestCase):

    def test_html_file_exists(self):
        self.assertTrue(
            HTML_FILE.is_file(),
            "index.html file is missing"
        )

    def test_main_heading_exists(self):
        content = HTML_FILE.read_text(encoding="utf-8")
        self.assertIn(
            "<h1>My First CI Project</h1>",
            content
        )

    def test_required_paragraph_exists(self):
        content = HTML_FILE.read_text(encoding="utf-8")
        self.assertIn(
            "This project uses GitHub Actions.",
            content
        )


if __name__ == "__main__":
    unittest.main()
