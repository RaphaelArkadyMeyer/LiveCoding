import argparse
import testcl_packager

args = argparse.ArgumentParser(
    description='Prepare a testcl package for students\' exams.')
args.add_argument('config file', type=str,
                  help='The config file associated with the exam.')
config_file = vars(args.parse_args())['config file']

print(testcl_packager.make_testcl_package(config_file))
