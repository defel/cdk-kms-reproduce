#!/usr/bin/env python3

from aws_cdk import core

from cdk_reproduce.cdk_reproduce_stack import CdkReproduceStack


app = core.App()
CdkReproduceStack(app, "cdk-reproduce")

app.synth()
