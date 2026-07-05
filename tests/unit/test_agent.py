"""Medical Coding Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_assign_codes():
    """Test Assign diagnosis and procedure codes from clinical documentation."""
    tools = AgentTools()
    result = await tools.assign_codes(clinical_note="test", code_types="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_validate_codes():
    """Test Validate assigned codes against documentation evidence."""
    tools = AgentTools()
    result = await tools.validate_codes(codes="test", clinical_note="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_coding_patterns():
    """Test Detect under-coding or over-coding patterns."""
    tools = AgentTools()
    result = await tools.detect_coding_patterns(provider_id="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_calculate_drg():
    """Test Calculate DRG assignment and expected reimbursement."""
    tools = AgentTools()
    result = await tools.calculate_drg(diagnosis_codes="test", procedure_codes="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.medical_coding_agent_agent import MedicalCodingAgentAgent
    agent = MedicalCodingAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
