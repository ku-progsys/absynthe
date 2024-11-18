class SortedList
  def initialize
    @arr = []
  end

  def insort_left(elem, weight)
    idx = bisect_left(weight)
    @arr.insert(idx, [elem, weight])
  end

  def insort_right(elem, weight)
    idx = bisect_right(weight)
    @arr.insert(idx, [elem, weight])
  end

  def top
    @arr[0][0]
  end

  def pop
    @arr.shift[0]
  end

  def empty?
    @arr.empty?
  end

  private
  def bisect_left(weight)
    lo = 0
    hi = @arr.size
    while lo < hi
      mid = lo + (hi - lo) / 2
      if @arr[mid][1] < weight
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  def bisect_right(weight)
    lo = 0
    hi = @arr.size
    while lo < hi
      mid = lo + (hi - lo) / 2
      if weight < @arr[mid][1]
        hi = mid
      else
        lo = mid + 1
      end
    end
    lo
  end
end
