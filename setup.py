from setuptools import find_packages, setup

setup(name="BuLaScripte",
      version="1.0",
      packages=find_packages(),
      install_requires=["python_decouple",
                        "atlassian-python-api",
                        "pandas",
                        "openpyxl",
                        "Pretix_API@git+ssh://git@github.com/nds-pfadfinden/pretix_api_package.git",
                        "bdp_mv_api_package@git+ssh://git@github.com/magisterNocte/bdp_mv_ica_api.git"
                        ],
      extras_require={
          'opt1': ['autopep8'],
      }
      )
