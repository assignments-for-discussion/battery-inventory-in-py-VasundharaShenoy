
def count_batteries_by_usage(cycles):
  if cycles<310:
    count_batteries_by_usage["lowCount"]=count_batteries_by_usage["lowCount"]+1
  elif cycles>=310 and cycles<=929:
    count_batteries_by_usage["mediumCount"]=count_batteries_by_usage["mediumCount"]+1
  else:
    count_batteries_by_usage["highCount"]=count_batteries_by_usage["highCount"]+1
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
