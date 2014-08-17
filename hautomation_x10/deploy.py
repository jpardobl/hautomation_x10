#!/usr/bin/env python

import os
import sys


def populate_db():
    pwd = os.getcwd()
    sys.path.append(pwd)

    try:
        if "DJANGO_SETTINGS_MODULE" not in os.environ:
            raise ImportError("No DJANGO_SETTINGS_MODULE env variable found")

        from hacore.models import Protocol
        if Protocol.objects.filter(name="X10").count() == 0:
            Protocol(
                name="X10",
                gobj_name="driver_X10",
                module="hautomation_x10",
                validate_address_module="hautomation_x10.utils",
                switch="hautomation_x10.cmds.pl_switch",
                bri="hautomation_x10.cmds.pl_bri",
                dim="hautomation_x10.cmds.pl_dim",
                all_lights_on="hautomation_x10.cmds.pl_all_lights_on",
                all_lights_off="hautomation_x10.cmds.pl_all_lights_off").save()

            sys.stdout.writelines("Protocoll successfully populated into db")
        else:
            sys.stdout.writelines("Protocol is already at the db. No changes made.")
        sys.path.remove(os.getcwd())
        sys.exit(0)
    except Exception, ex:
        sys.path.remove(os.getcwd())
        sys.stderr.writelines(ex.message)
        sys.exit(1)
