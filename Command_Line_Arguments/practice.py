from argparse import ArgumentParser as ap

ap.add_argument('-i', '--input', required=True,
                            help='path to the input')
ap.add_argument('-0', '--output', required=True,
                            help='path to the output')
arg = vars(ap.parse_args())



