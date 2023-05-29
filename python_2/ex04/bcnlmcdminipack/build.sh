#!/bin/bash


version=$(grep version pyproject.toml | cut -d '=' -f2 | sed 's/"//g' |sed 's/ //g')

echo "--------------------------  Checking  package --------------------------"
pip-compile --resolver=backtracking 



echo "--------------------------  Building  package --------------------------"
python3 -m build
test2=$(python3 -m twine check "dist/bcnlmcdminipack-${version}-py3-none-any.whl" | cut -d ' ' -f3)

# i get int test2 last word of twin check. i chek if ti contains "PASSED"
result="PASSED"

  if [ -z "${test2##*$result*}" ] ;then
    echo "--------------------------  uploading  package --------------------------"
    python3 -m twine upload --verbose  -r testpypi "dist/bcnlmcdminipack-${version}-py3-none-any.whl"
else
    echo "I got a problem building de package"
fi
echo "--------------------------  Installing  package --------------------------"
python3 -m pip install -i https://test.pypi.org/simple/ "bcnlmcdminipack==${version}"
echo "--------------------------  Listing  packages    --------------------------"
python3 -m pip list 