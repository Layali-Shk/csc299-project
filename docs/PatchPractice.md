## Git Diff / Patch Practice Log

This file documents my practice with the git diff, patch, and related Git workflow experiments as required in the project timeline.

### Commands Practiced

-git diff

  * Used to view differences between working directory and last commit.
- git diff > changes.patch

  * Exported the differences into a patch file.
-git apply changes.patch

  * Applied the patch back to a file.
-git checkout -- <file>

  * Reverted file back to the last committed state.
-git add <file> and git commit

  * Confirmed changes after applying patch.

### Summary of What I Learned

* git diff shows what has changed before committing.
* A patch is basically a saved diff that can be reapplied later.
* You can share or reapply patches across different machines or repos.
* This is useful for testing, debugging, or reviewing code before merging.

### Example Terminal Session

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents (master)
$ cd csc299-project

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project (main)
$ mkdir csc299-project

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project (main)
$ cd csc299-project

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project/csc299-project (main)
$ git init
Initialized empty Git repository in C:/Users/layal/Documents/csc299-project/csc299-project/.git/

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project/csc299-project (master)
$ echo "Hello World" >text.txt

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project/csc299-project (master)
$ git add text.txt
warning: in the working copy of 'text.txt', LF will be replaced by CRLF the next time Git touches it

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project/csc299-project (master)
$ git commit -m "add text.txt for patch practice"
[master (root-commit) 15dbca8] add text.txt for patch practice
 1 file changed, 1 insertion(+)
 create mode 100644 text.txt

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project/csc299-project (master)
$ echo "This is a change" >> text.txt

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project/csc299-project (master)
$ git diff
warning: in the working copy of 'text.txt', LF will be replaced by CRLF the next time Git touches it
diff --git a/text.txt b/text.txt
index 557db03..10e5e7f 100644
--- a/text.txt
+++ b/text.txt
@@ -1 +1,2 @@
 Hello World
+This is a change

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project/csc299-project (master)
$ git diff > change.patch
warning: in the working copy of 'text.txt', LF will be replaced by CRLF the next time Git touches it

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project/csc299-project (master)
$ git checkout -- text.txt

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project/csc299-project (master)
$ git apply change.patch

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project/csc299-project (master)
$ cat text.txt
Hello World
This is a change

layal@LAPTOP-T0LCNKQ0 MINGW64 ~/Documents/csc299-project/csc299-project (master)
$ git add text.txt
git commit -m "Apply patch to text.txt"
[master 3c603ff] Apply patch to text.txt
 1 file changed, 1 insertion(+)


### Notes

This practice step ensures I am comfortable editing, reviewing, and restoring changes before working on larger codebases for the final project.
