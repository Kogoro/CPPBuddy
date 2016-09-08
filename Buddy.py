import argparse
import os
import shutil
from string import Template
from BuddyAnalyzer import *


class Buddy:
    def __init__(self):
        print "init"

    def execute(self, task):
        print "execute {}".format(task)


def main():
    parser = argparse.ArgumentParser(description="Buddy: the small build tool for CPP")
    parser.add_argument("-r", "--reload", action='store_true', help="reloads the dependencies")  # TODO
    parser.add_argument("-d", "--debug", action="store_true", help="enables debug mode")  # TODO
    parser.add_argument("-v", "--version", action="store_true", help="prints version info")
    parser.add_argument("-s", default="buddy.txt", help="build script location")
    parser.add_argument("-q", "--quiet", action="store_true", help="shows no output")  # TODO

    parser.add_argument("task", default="run", help="specifies task (e.g. init,run,clean,show)")
    parser.add_argument("arg", nargs="?", default="all", help="argument for the task")


    args = parser.parse_args()

    if args.task == "init":
        filein = open('buddyTemplate.txt')
        src = Template(filein.read())
        d = {'name': args.arg}
        result = src.substitute(d)
        cwd = os.getcwd()
        if os.name == 'nt':
            fileout = open(cwd + "\\buddy.txt", "w")
        else:
            fileout = open(cwd + "/buddy.txt", "w")
        fileout.write(result)
        fileout.close()
        if os.name == 'nt':
            print "File written successfully to {}\\buddy.txt".format(cwd)
        else:
            print "File written successfully to {}/buddy.txt".format(cwd)
        return

    buddyProj = BuddyAnalyzer(args.s).analyze()

    if args.task == "show":
        if args.arg == "script" or args.arg == "project":
            print buddyProj

    if args.task == "clean":
        cwd = os.getcwd()
        outputDir = buddyProj.parameter("bin")
        if os.name == 'nt':
            shutil.rmtree(cwd + "\\" + outputDir)
        else:
            shutil.rmtree(cwd + "/" + outputDir)
        print "Clean finished through removing {} folder".format(outputDir)

    if args.task == "run":
        if args.arg == "all":
            print "Build all variants"
            print buddyProj.variants
        else:
            print "Build variant {}".format(args.arg)
            for task in buddyProj.variant(args.arg).command('before_run').values:
                Buddy().execute(task)
            for task in buddyProj.variant(args.arg).command('run').values:
                Buddy().execute(task)
            for task in buddyProj.variant(args.arg).command('after_run').values:
                Buddy().execute(task)


if __name__ == "__main__":
    main()
