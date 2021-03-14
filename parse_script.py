from parse_git_log import parse_log, select_subset_commits

shas_and_dates = [('ed114e15106192b22ebb78ef5bf5bce72b419d13', 'Wed Jul 13 01:25:57 2005 +0000'),
('07ffc7d605cc96557db28a9e35da69bc0719611b', 'Wed Jul 13 01:25:57 2005 +0000'),
('d6ded0e91bcdd2a8f7a221f6a5552a33fe545359', 'Wed Jul 13 16:56:05 2005 +0000')]
shas_and_dates = parse_log('django_git_log.md')
select_subset_commits(shas_and_dates, 3)