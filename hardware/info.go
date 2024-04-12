package main

type HardwareInfo struct {
	cpuUtil     float32
	memUtil     float32
	memUsage    float32
	diskUtil    float32 // disk io activity
	diskUsage   float32 // total allocated size on disk
	diskWritten float32
	diskRead    float32
	gpuUtil     float32
	gpuTemp     float32
}
