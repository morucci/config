#!/usr/bin/env python

import os
import sys
import yaml

if __name__ == "__main__":

    seed_path = sys.argv[1]
    path = sys.argv[2]
    repos = {}

    struct = {
        'project-templates': {
            'Fedora Distgits template': {
                'uri': 'file://' + seed_path + '/%(name)s',
                'branches': ['master'],
                'gitweb': 'https://src.fedoraproject.org/rpms/%(name)s/c/%%(sha)s',
                'index-tags': False
            }
        },
        'projects': {
            'Fedora Distgits': {
                'description': 'The Fedora project - Distgit repositories',
                'repos': repos
            }
        }
    }

    _repos = [i for i in os.listdir(seed_path)
              if os.path.isdir(os.path.join(seed_path, i))]
    for r in _repos:
        repos.update({r: {'template': 'Fedora Distgits template'}})

    with open(path, 'w') as fd:
        fd.write(yaml.safe_dump(struct,
                                default_flow_style=False))
