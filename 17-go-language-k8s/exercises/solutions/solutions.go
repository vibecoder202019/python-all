// Đáp án tham khảo Module 17 — chỉ xem sau khi tự làm
package solutions

// TaskWithPriority — Bài 1
type TaskWithPriority struct {
	ID       int
	Title    string
	Done     bool
	Priority int
}

func (t TaskWithPriority) IsHighPriority() bool {
	return t.Priority >= 8
}

// FilterDone — Bài 2: lọc tasks theo done status
func FilterDone(tasks []TaskWithPriority, done bool) []TaskWithPriority {
	var out []TaskWithPriority
	for _, t := range tasks {
		if t.Done == done {
			out = append(out, t)
		}
	}
	return out
}
