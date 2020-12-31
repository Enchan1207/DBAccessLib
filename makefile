# pipの管理makefileで自動化できないかな
.PHONY: cleanup

cleanup:
	yes | pip uninstall DBAccessLib > /dev/null
	pip install git+https://github.com/Enchan1207/DBAccessLib
