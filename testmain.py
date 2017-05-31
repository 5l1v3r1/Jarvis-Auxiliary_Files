from testlib import testlib
plugin = 'discover_people'
exec('from unospace.tasks import ' + plugin)
discover_people.just_a_test()
