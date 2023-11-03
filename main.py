
def count_batteries_by_health(present_capacities):
  ex=f=h=0
  for i in present_capacities:
    #calculating soh for each battery in the list
    soh=100*(i/120)
    #checking for soh range
    if soh>80:
      h+=1
    elif soh>=62:
      ex+=1
    else:
      f+=1
  return {
    "healthy": h,
    "exchange": ex,
    "failed": f
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")

  #test with minimum battery capacity
  present_capacities = [0]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 1)

  #test with empty input
  present_capacities = []
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)

  #test with maximumm battery capacity
  present_capacities = [120]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 1)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)

  #test with similar battery capacity
  present_capacities = [100,100,100]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 3)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)

  #test with all least battery capacity
  present_capacities = [10,20,30]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 3)

  #test with mixed capacity
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)

  #test with large input
  present_capacities = [110]*1000
  counts = count_batteries_by_health(present_capacities)
  
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
