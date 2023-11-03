
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
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
