import unittest

from unittest.mock import patch, MagicMock, mock_open
from src import scanner


class TestScanner(unittest.IsolatedAsyncioTestCase):

    async def test_ping_ip_active(self):
        mock_result = MagicMock()
        mock_result.stdout = "Reply from 192.168.1.1: bytes=32 time<1ms TTL=64"
        with patch("subprocess.run", return_value=mock_result):
            result = await scanner.ping_ip("192.168.1.1")
            self.assertEqual(result, ("192.168.1.1", "Active", None))

    async def test_ping_ip_inactive(self):
        mock_result = MagicMock()
        mock_result.stdout = "Request timed out."
        with patch("subprocess.run", return_value=mock_result):
            result = await scanner.ping_ip("192.168.1.2")
            self.assertEqual(result, ("192.168.1.2", "Inactive", None))

    async def test_scan_range(self):
        async def mock_ping_ip(ip):
            if ip.endswith(".1"):
                return ip, "Active", None
            return ip, "Inactive", None

        with patch("src.scanner.ping_ip", side_effect=mock_ping_ip):
            result = await scanner.scan_range("192.168.1.0/30")
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0][1], "Active")
            self.assertEqual(result[1][1], "Inactive")

    async def test_scan_file(self):
        ip_list = ["192.168.1.1", "192.168.1.2"]
        content = "\n".join(ip_list)

        async def mock_ping_ip(ip):
            if ip.endswith(".1"):
                return ip, "Active", None
            return ip, "Inactive", None

        with patch("builtins.open", new_callable=mock_open, read_data=content):
            with patch("src.scanner.ping_ip", side_effect=mock_ping_ip):
                result = await scanner.scan_file("dummy_file.txt")
                self.assertEqual(len(result), 2)
                self.assertEqual(result[0][0], ip_list[0])
                self.assertEqual(result[1][0], ip_list[1])

    async def test_run_scanner_with_range(self):
        mock_result = [
            ("192.168.1.1", "Active", None),
            ("192.168.1.2", "Inactive", None),
        ]

        with (
            patch("src.scanner.scan_range", return_value=mock_result),
            patch("src.scanner.os.makedirs"),
            patch("builtins.open", new_callable=mock_open),
        ):
            await scanner.run_scanner(['--range', '192.168.1.0/30'])

    async def test_run_scanner_with_file(self):
        mock_result = [("192.168.1.3", "Active", None)]

        with (
            patch("src.scanner.scan_file", return_value=mock_result),
            patch("src.scanner.os.makedirs"),
            patch("builtins.open", new_callable=mock_open),
        ):
            await scanner.run_scanner(['--file', 'ips.txt'])

    async def test_run_scanner_no_args(self):
        with patch("builtins.print") as mocked_print:
            await scanner.run_scanner([])
            mocked_print.assert_called_with(
                "Please specify either --range or --file."
            )

    async def test_run_scanner_prints(self):
        mock_result = [
            ("192.168.1.1", "Active", None),
            ("192.168.1.2", "Inactive", None),
        ]

        with (
            patch("src.scanner.scan_range", return_value=mock_result),
            patch("src.scanner.os.makedirs"),
            patch("builtins.open", new_callable=mock_open),
            patch("builtins.print") as mock_print,
        ):

            await scanner.run_scanner(['--range', '192.168.1.0/30'])

            mock_print.assert_any_call("192.168.1.1 Active")
            mock_print.assert_any_call("192.168.1.2 Inactive")
            mock_print.assert_any_call(
                "Résultats sauvegardés dans data/results/resultat.csv"
            )


if __name__ == '__main__':
    unittest.main()
