## Introduction

AKLite is a lite version of AKShare, which will be used in the future to support the AKShare project.

## Installation

```shell
pip install aklite
```

## Usage



## Contributing

## Translate

```shell
cd docs
sphinx-build -b gettext ./source build/gettext
sphinx-intl update -p ./build/gettext -l zh_CN
```

## Publish

```shell
hatch build
hatch publish
```


