import os
import shutil

PUSH_FN = """
function $$$1()
{
	make fclean
	echo "\\n"
	git status
	echo "\\n"
	git add .
	git commit -m "$1"
	git push
	echo "MMEEEEEOOOOOOWWWW 🐈🐈\\n\\n"
	cat ~/.cats/cat"$(($RANDOM % 26))"
	echo "\\n"
}
"""

CAT_FN = """
function $$$1()
{
	cat ~/.cats/cat"$(($RANDOM % 26))"
	echo "\\n"
}
"""

home = os.path.expanduser('~/')

push_fn = input("Enter the push function name :")
cat_fn = input("Enter the display cat function name :")

if (not os.path.isdir("{}.cats".format(home))):
	shutil.copytree("./cats", "{}.cats".format(home))

if (os.path.exists("{}.bashrc".format(home))):
	shutil.copy("{}.bashrc".format(home), "{}.bashrc_backup".format(home))
	with open("{}.bashrc".format(home), 'a') as file:
		file.write('\n\n# Addition by shell-cat\n')
		file.write(PUSH_FN.replace("$$$1", push_fn))
		file.write("\n")
		file.write(CAT_FN.replace("$$$1", cat_fn))

if (os.path.exists("{}.zshrc".format(home))):
	shutil.copy("{}.zshrc".format(home), "{}.zshrc_backup".format(home))
	with open("{}.zshrc".format(home), 'a') as file:
		file.write('\n\n# Addition by shell-cat\n')
		file.write(PUSH_FN.replace("$$$1", push_fn))
		file.write("\n")
		file.write(CAT_FN.replace("$$$1", cat_fn))
