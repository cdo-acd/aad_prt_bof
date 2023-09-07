from typing import List, Tuple

from outflank_stage1.task.base_bof_task import BaseBOFTask
from outflank_stage1.task.enums import BOFArgumentEncoding


class AzureADPRTBOF(BaseBOFTask):
    def __init__(self):
        super().__init__("aadprt")

        self.parser.description = (
            "Extract Azure AD PRT tokens from the machine."
        )
        self.parser.epilog = "Synopsis: aadprt <NONCE>"

        self.parser.add_argument(
            "nonce",
            help=f"Nonce from roadrecon auth."
        )

    def _encode_arguments_bof(
        self, arguments: List[str]
    ) -> List[Tuple[BOFArgumentEncoding, str]]:
        parser_arguments = self.parser.parse_args(arguments)

        return [
            (BOFArgumentEncoding.WSTR, parser_arguments.nonce)
        ]
