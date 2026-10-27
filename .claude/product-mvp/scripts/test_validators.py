import tempfile
import unittest
from pathlib import Path

from validate_feature_plan import validate as validate_markdown
from validate_package import validate as validate_package

ROOT = Path(__file__).resolve().parents[3]
SAMPLE = ROOT / '.claude/product-mvp/examples/feature-mvp-plan.example.md'


class PackageTests(unittest.TestCase):
    def test_package(self):
        self.assertEqual([], validate_package(ROOT))

    def test_valid_sample_markdown(self):
        self.assertEqual([], validate_markdown(SAMPLE))

    def validate_variant(self, content):
        with tempfile.TemporaryDirectory() as d:
            file = Path(d) / 'feature-mvp-plan.md'
            file.write_text(content, encoding='utf-8')
            return validate_markdown(file)

    def test_missing_market_evidence(self):
        s = SAMPLE.read_text()
        modified = s.replace('SIN_EVIDENCIA: validar con compradores', 'algo sin fuente')
        self.assertTrue(any('mercado sin enlace' in issue for issue in self.validate_variant(modified)))

    def test_verified_market_requires_url(self):
        s = SAMPLE.read_text().replace('SIN_EVIDENCIA: validar con compradores','FUENTE_VERIFICADA sin link')
        self.assertTrue(any('sin URL' in issue for issue in self.validate_variant(s)))

    def test_report_action_mismatch(self):
        s = SAMPLE.read_text().replace('### F-001 · Reportes · REDUCIR','### F-001 · Reportes · MANTENER')
        self.assertTrue(any('acción distinta' in issue for issue in self.validate_variant(s)))

    def test_missing_feature_details(self):
        s = SAMPLE.read_text().replace('### F-001 · Reportes · REDUCIR','### F-002 · Reportes · REDUCIR')
        issues = self.validate_variant(s)
        self.assertTrue(any('Falta ficha detallada: F-001' in issue for issue in issues))
        self.assertTrue(any('Ficha sin entrada en tabla: F-002' in issue for issue in issues))

    def test_duplicate_feature_table(self):
        s = SAMPLE.read_text()
        row = '| F-001 | Generación de reportes | Reportes con plantillas, filtros, envíos `[ejemplo/no verificable]` | Mantener reporte básico y posponer plantillas | REDUCIR | SIN_EVIDENCIA: validar con compradores | Menor complejidad operativa, HIPÓTESIS | P0 |'
        self.assertTrue(row in s)
        self.assertTrue(any('duplicado' in issue for issue in self.validate_variant(s.replace(row,row+'\n'+row))))

    def test_csv_reference_not_allowed(self):
        s = SAMPLE.read_text() + '\nTambién genera feature-actions.csv\n'
        self.assertTrue(any('CSV' in issue for issue in self.validate_variant(s)))


if __name__ == '__main__':
    unittest.main()
