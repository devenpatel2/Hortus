#!/usr/bin/env python
#! -*- coding:utf-8

from parser import Parser
from logger import Logger
from hortus import Hortus
from exceptions import InfluxException, MQTTException
import argparse

def hortus():

    """ Entry point for the command line tool. """
    parser = argparse.ArgumentParser(
        description='Run Hortus application.')
    parser.add_argument(
        "-c", "--config", type=str, help='Location of the configuration file.')

    parser.add_argument("--logfile", help="set log file")

    verb = parser.add_mutually_exclusive_group()
    verb.add_argument(
        "-v", "--verbose", help="print more", action='store_true')
    verb.add_argument("-q", "--quiet", help="print less", action='store_true')

    class Cmdline(object):
        pass
    
    cmdline = Cmdline()
    parser.parse_args(namespace=cmdline)

    if cmdline.logfile:
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    if cmdline.verbose:
        level = logging.DEBUG
    elif cmdline.quiet:
        level = logging.WARN
    else:
        level = logging.INFO

    log_file = cmdline.logfile
    
    log = Logger(level, log_file)

    config_filename = os.path.expanduser(cmdline.config)
    log.info("Using config file: {}".format(config_filename))

    shutdownhandler = util.ShutdownHandler()

    config = util.open_config(config_filename)

    with Hortus(config) as hortus:

        try:
            hortus.init_mqtt()
        except MQTTException as e:
            log.fatal("Failed to itialize mqtt : {}".format(str(e)))
            log.info("Exiting...")
            sys.exit(0)

        try
            hortus.init_influxDB()

        except InfluxException as e:

            log.warn("Failed to connect to database. {}"format(str(e)))
            log.info("Attempt reconnect afer 30 min")

        while True:
            if shutdownhandler.shutdown:
                break
            
            hortus.run()

            sleep(1)

    log.info("shutting down Hortus")

if __name__ == "__main__"

    hortus()
    
