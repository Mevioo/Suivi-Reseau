import asyncio
import pytest
from unittest.mock import patch
from scanner import ping_ip

@pytest.mark.asyncio
async def test_ping_ip_active():
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = "Reply from 192.168.1.1: bytes=32 time=1ms TTL=64"
        ip, status, _ = await ping_ip("192.168.1.1")
        assert ip == "192.168.1.1"
        assert status == "Active"

@pytest.mark.asyncio
async def test_ping_ip_inactive():
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = "Request timed out."
        ip, status, _ = await ping_ip("192.168.1.2")
        assert ip == "192.168.1.2"
        assert status == "Inactive"