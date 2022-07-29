import io
import pstats
import quickSort
import cProfile

pr = cProfile.Profile()
pr.enable()

result = quickSort.main()

pr.disable()

s = io.StringIO()

pstat = pstats.Stats(pr, stream = s).sort_stats('tottime')
pstat.print_stats()

with open('output.txt', 'w') as file:
    file.write(s.getvalue())