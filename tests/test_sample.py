import json
import subprocess
import sys
import unittest

from services.sample.core.quantities import total_quantity
from services.sample.shell.main import parse_request


class QuantityTests(unittest.TestCase):
    def test_total_does_not_mutate_input(self):
        quantities = (1, 2, 3)
        self.assertEqual(total_quantity(quantities), 6)
        self.assertEqual(quantities, (1, 2, 3))

    def test_empty_input(self):
        self.assertEqual(total_quantity(()), 0)

    def test_negative_quantity_fails(self):
        with self.assertRaises(ValueError):
            total_quantity((1, -1))

    def test_boundary_rejects_invalid_requests(self):
        for payload in ([], {}, {"quantities": True}, {"quantities": [True]}, {"quantities": [1.0]}, {"quantities": [1], "extra": 2}):
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                parse_request(payload)

    def test_boundary_creates_immutable_input(self):
        payload = {"quantities": [1, 2]}
        parsed = parse_request(payload)
        payload["quantities"].append(3)
        self.assertEqual(parsed, (1, 2))

    def test_json_cli_success(self):
        result = subprocess.run(
            [sys.executable, "-B", "-m", "services.sample.shell.main"],
            input='{"quantities": [1, 2, 3]}',
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {"total": 6})
        self.assertEqual(result.stderr, "")

    def test_json_cli_failure_does_not_echo_payload(self):
        for payload in ('invalid input', '{"quantities": [-1]}', '{"quantities": [true]}'):
            with self.subTest(payload=payload):
                result = subprocess.run(
                    [sys.executable, "-B", "-m", "services.sample.shell.main"],
                    input=payload, text=True, capture_output=True, check=False,
                )
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertEqual(result.stderr, "Invalid quantity request.\n")
