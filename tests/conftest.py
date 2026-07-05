"""Test configuration for Medical Coding Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "medical-coding-agent", "category": "Healthcare"}
