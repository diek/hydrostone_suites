#!/bin/bash
cd /derrick/app/digital-ocean-github-actions-ci/scripts/deploy.sh
git pull origin master
sudo systemctl restart digital-ocean-github-actions-ci
