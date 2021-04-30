from typing import Callable, Dict

import pytest
from nornir.core.filter import F
from nornir.core.task import MultiResult, AggregatedResult
from nornir_netmiko import netmiko_send_command

from nuts.context import NornirNutsContext
from nuts.helpers.result import nuts_result_wrapper, NutsResult


class NtpStatusContext(NornirNutsContext):
    
    def nuts_task(self) -> Callable:
        return netmiko_send_command

    def nuts_arguments(self) -> dict:
        return {"command_string": "show ntp status", "use_genie": True}

    def nornir_filter(self) -> F:
        hosts = {entry["host"] for entry in self.nuts_parameters["test_data"]}
        return F(name__any=hosts)

    def _transform_host_results(self, single_result: MultiResult) -> dict:
        assert single_result[0].result is not None
        return single_result[0].result

    def transform_result(self, general_result: AggregatedResult) -> Dict[str, NutsResult]:
        return {
            host: nuts_result_wrapper(result, self._transform_host_results) for host, result in general_result.items()
        }


CONTEXT = NtpStatusContext


@pytest.mark.usefixtures("check_nuts_result")
class TestNtpStatus:

    @pytest.mark.nuts("host,ntp_status")
    def test_ntp_status(self, single_result, ntp_status):
        assert single_result.result["clock_state"]["system_status"]["status"] == ntp_status