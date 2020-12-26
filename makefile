# pipの管理makefileで自動化できないかな
.PHONY: cleanup

cleanup:
	yes | pip uninstall DBAccessLib > /dev/null
	pip install -e . > /dev/null
