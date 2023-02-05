@echo off
rem pytest -v -s -m "sanity or regression" --browser chrome --html=reports/reports.html
rem pytest -v -s -m "regression" --browser chrome --html=reports/reports.html
pytest -v -s -m "sanity" --browser chrome --html=reports/reports.html
rem pytest -v -s -m "sanity and regression" --browser chrome --html=reports/reports.html
