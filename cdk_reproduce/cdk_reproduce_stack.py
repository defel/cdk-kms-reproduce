from aws_cdk import core
from aws_cdk.aws_iam import PolicyStatement, Effect, AnyPrincipal
from aws_cdk.aws_kms import Key
from aws_cdk.core import Construct


class KmsConstruct(Construct):

    @property
    def key(self):
        return self._key

    def __init__(self, scope: Construct, id: str, name: str) -> None:
        super().__init__(scope, id)

        self._key = Key(self, f"kms_key_{name}")
        self._key.add_alias(f"alias/kms-{name}")
        self._key.add_to_resource_policy(PolicyStatement(
            effect=Effect.ALLOW,
            actions=["kms:*"],
            principals=[AnyPrincipal()],
            resources=["*"]
        ))


class CdkReproduceStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        name = "test"

        kms = KmsConstruct(self, f"cdk-test-{name}", name)
