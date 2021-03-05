git log > ../monolith_quality_history/git_log.md
grep ^commit git_log.md > shas.md
grep ^Date git_log.md > dates.md
grep -rl 'Date:  ' dates.md | xargs sed -i '' 's/Date:  //g'
grep -rl 'commit ' shas.md | xargs sed -i '' 's/commit //g'
paste dates.md shas.md | column -s $'\t' -t > commits.md
