package models

import "time"

// Now — helper testable thay vì time.Now() trực tiếp
func Now() time.Time {
	return time.Now().UTC()
}
